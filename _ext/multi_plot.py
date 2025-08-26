"""multi-plot directive: create a grid of function plots using plotmath.multiplot.

Features:
 - Accepts a list of function expressions and plots each in a grid (rows x cols)
 - Expressions compiled safely with sympy -> numpy (vectorized)
 - Caching via hashed parameters unless :nocache: set
 - Optional :debug: preserves original SVG (no stripping / id rewrite) and also saves PDF copy
 - Width control and safe ID rewriting for multiple instances on same page
 - YAML front matter (--- ... ---) or simple key: value lines before caption

Usage (MyST):

:::{multi-plot}
functions: [x**2 - 2*x, -x + 2, x - 3]
rows: 1
cols: 3
width: 100%
:::
"""

from __future__ import annotations

import os
import re
import uuid
import hashlib
import shutil
from typing import Callable, Dict, Any, Tuple, List

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _hash_key(*parts) -> str:
    h = hashlib.sha1()
    for p in parts:
        if p is None:
            p = "__NONE__"
        h.update(str(p).encode("utf-8"))
        h.update(b"||")
    return h.hexdigest()[:12]


def _compile_function(expr: str) -> Callable:
    import sympy, numpy as np  # local import

    expr = expr.strip()
    x = sympy.symbols("x")
    try:
        sym = sympy.sympify(expr)
    except Exception as e:  # pragma: no cover - user error path
        raise ValueError(f"Ugyldig funksjonsuttrykk '{expr}': {e}")
    fn_np = sympy.lambdify(x, sym, modules=["numpy"])

    def f(arr):
        return fn_np(np.asarray(arr, dtype=float))

    # simple vectorization test
    _ = f([0.0, 1.0])
    return f


# ---------------------------------------------------------------------------
# Directive
# ---------------------------------------------------------------------------


def _strip_root_svg_size(svg_text: str) -> str:
    """Remove width/height only on the root <svg> tag for responsiveness."""

    def repl(m):
        tag = m.group(0)
        tag = re.sub(r'\swidth="[^"]+"', "", tag)
        tag = re.sub(r'\sheight="[^"]+"', "", tag)
        return tag

    return re.sub(r"<svg\b[^>]*>", repl, svg_text, count=1)


def _parse_bool(val, default: bool | None = None) -> bool | None:
    if val is None:
        return default
    if isinstance(val, bool):
        return val
    s = str(val).strip().lower()
    if s == "":  # option present with no value => treat as True
        return True
    if s in {"true", "yes", "on", "1"}:
        return True
    if s in {"false", "no", "off", "0"}:
        return False
    return default


def _split_expr_list(val: str) -> List[str]:
    if not isinstance(val, str):
        return []
    s = val.strip()
    if not s:
        return []
    # allow [a,b,c] or a;b;c or a,b,c
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    s = s.replace(";", ",")
    parts = [p.strip() for p in s.split(",")]
    return [p for p in parts if p]


def _split_top_level(val: str) -> List[str]:
    """Split by commas at top level only (ignores commas inside (), [], {})."""
    if not isinstance(val, str):
        return []
    s = val.strip()
    if not s:
        return []
    # Strip surrounding brackets if present
    if (s.startswith("[") and s.endswith("]")) or (
        s.startswith("(") and s.endswith(")")
    ):
        s = s[1:-1].strip()
    out: List[str] = []
    cur = []
    depth = 0
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: List[str] = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in "([{":
            depth += 1
            stack.append(ch)
            cur.append(ch)
        elif ch in ")]}":
            depth = max(0, depth - 1)
            if stack:
                stack.pop()
            cur.append(ch)
        elif ch == "," and depth == 0:
            part = "".join(cur).strip()
            if part:
                out.append(part)
            cur = []
        else:
            cur.append(ch)
        i += 1
    tail = "".join(cur).strip()
    if tail:
        out.append(tail)
    return out


def _safe_literal(val: str):
    try:
        import ast as _ast

        return _ast.literal_eval(val)
    except Exception:
        return None


def _parse_values_list_or_none(s: str):
    """Parse a scalar number or a tuple/list of numbers; return list[float] or None."""
    if not isinstance(s, str):
        return None
    st = s.strip()
    if not st or st.lower() == "none":
        return None
    lit = _safe_literal(st)
    if isinstance(lit, (int, float)):
        try:
            return [float(lit)]
        except Exception:
            return None
    if isinstance(lit, (list, tuple)):
        out: List[float] = []
        for v in lit:
            try:
                out.append(float(v))
            except Exception:
                pass
        return out if out else None
    # fallback: split by commas
    parts = [p.strip() for p in st.split(",") if p.strip()]
    out2: List[float] = []
    for p in parts:
        try:
            out2.append(float(p))
        except Exception:
            return None
    return out2 if out2 else None


class MultiPlotDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    option_spec = {
        "functions": directives.unchanged_required,  # list of expressions
        "fn_labels": directives.unchanged,  # optional list of labels
        "function-names": directives.unchanged,  # alias for fn_labels in examples
        "domains": directives.unchanged,  # per-function domain (a,b) or (a,b) \ {..}
        "vlines": directives.unchanged,  # per-function vline x or None
        "hlines": directives.unchanged,  # per-function hline y or None
        "xlims": directives.unchanged,  # per-function xlim tuple or None
        "ylims": directives.unchanged,  # per-function ylim tuple or None
        "lines": directives.unchanged,  # per-axis line spec: (a,b) or (a,(x,y)) or None
        "xmin": directives.unchanged,
        "xmax": directives.unchanged,
        "ymin": directives.unchanged,
        "ymax": directives.unchanged,
        "xstep": directives.unchanged,
        "ystep": directives.unchanged,
        "fontsize": directives.unchanged,
        "lw": directives.unchanged,
        "alpha": directives.unchanged,
        "grid": directives.unchanged,
        "ticks": directives.unchanged,
        "rows": directives.unchanged,
        "cols": directives.unchanged,
        "align": lambda a: directives.choice(a, ["left", "center", "right"]),
        "class": directives.class_option,
        "name": directives.unchanged,
        "nocache": directives.flag,
        "alt": directives.unchanged,
        "width": directives.length_or_percentage_or_unitless,
        "debug": directives.flag,
    }

    # -----------------------------
    # Content key/value parsing
    # -----------------------------
    def _gather_kv_from_content(self) -> Tuple[Dict[str, str], int]:
        kv: Dict[str, str] = {}
        lines = list(self.content)
        idx = 0
        # YAML front matter style
        if lines and lines[0].strip() == "---":
            idx = 1
            while idx < len(lines) and lines[idx].strip() != "---":
                line = lines[idx].rstrip()
                m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
                if m:
                    kv[m.group(1)] = m.group(2)
                idx += 1
            if idx < len(lines) and lines[idx].strip() == "---":
                idx += 1
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            return kv, idx
        # flat key: value lines until first non-matching or blank separation
        caption_start = 0
        for i, line in enumerate(lines):
            if not line.strip():
                caption_start = i + 1
                continue
            m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
            if m:
                kv[m.group(1)] = m.group(2)
                caption_start = i + 1
            else:
                break
        return kv, caption_start

    # -----------------------------
    # Main run
    # -----------------------------
    def run(self):  # noqa: C901 (complexity OK for directive)
        env = self.state.document.settings.env
        app = env.app
        try:
            import plotmath  # type: ignore
        except Exception as e:  # pragma: no cover - dependency missing
            err = nodes.error()
            err += nodes.paragraph(text=f"Kunne ikke importere plotmath: {e}")
            return [err]

        kv, caption_idx = self._gather_kv_from_content()
        merged: Dict[str, Any] = {**kv, **self.options}
        if "functions" not in merged:
            return [
                self.state_machine.reporter.error(
                    "Directive 'multi-plot' krever 'functions:'", line=self.lineno
                )
            ]

        exprs = _split_expr_list(str(merged["functions"]))
        if not exprs:
            return [
                self.state_machine.reporter.error(
                    "'functions' var tomt eller ugyldig.", line=self.lineno
                )
            ]
        # compile all
        functions: List[Callable] = []
        for e in exprs:
            try:
                functions.append(_compile_function(e))
            except Exception as ex:
                return [
                    self.state_machine.reporter.error(
                        f"Ugyldig funksjon '{e}': {ex}", line=self.lineno
                    )
                ]

        def _f(name, default):
            v = merged.get(name)
            if v in (None, ""):
                return default
            try:
                return float(v)
            except Exception:
                return default

        xmin = _f("xmin", -6)
        xmax = _f("xmax", 6)
        ymin = _f("ymin", -6)
        ymax = _f("ymax", 6)
        xstep = _f("xstep", 1)
        ystep = _f("ystep", 1)
        fontsize = _f("fontsize", 20)
        lw = _f("lw", 2.5)
        alpha_raw = merged.get("alpha")
        grid_flag = _parse_bool(merged.get("grid"), default=True)
        ticks_flag = _parse_bool(merged.get("ticks"), default=True)

        try:
            alpha = float(alpha_raw) if alpha_raw not in (None, "") else None
        except Exception:
            alpha = None

        # Accept both fn_labels and function-names; function-names takes precedence if provided
        labels_list: List[str] = _split_expr_list(
            str(merged.get("function-names", merged.get("fn_labels", "")))
        )
        if labels_list and len(labels_list) == len(functions):
            labels_arg: Any = labels_list
        else:
            labels_arg = True

        # Per-function domains with optional exclusions, vlines, hlines, and axis limits
        # Helper to parse domain with optional set-difference exclusions
        def _parse_domain_with_exclusions(s: str):
            if not isinstance(s, str):
                return None, []
            s = s.strip()
            if not s or s.lower() == "none":
                return None, []
            num_re = r"[+-]?\d+(?:\.\d+)?"
            dom_ex_pat = re.compile(
                rf"\(\s*({num_re})\s*,\s*({num_re})\s*\)\s*(?:\\\s*\{{\s*([^}}]*)\s*\}})?"
            )
            m = dom_ex_pat.search(s)
            if not m:
                return None, []
            try:
                d0 = float(m.group(1))
                d1 = float(m.group(2))
                dom = (d0, d1)
            except Exception:
                dom = None
            excludes: List[float] = []
            excl_str = m.group(3) if m.lastindex and m.lastindex >= 3 else None
            if excl_str:
                for tok in [t.strip() for t in excl_str.split(",") if t.strip()]:
                    try:
                        excludes.append(float(tok))
                    except Exception:
                        pass
            return dom, excludes

        def _parse_tuple_or_none(s: str):
            if not isinstance(s, str):
                return None
            st = s.strip()
            if not st or st.lower() == "none":
                return None
            lit = _safe_literal(st)
            if isinstance(lit, (list, tuple)) and len(lit) == 2:
                try:
                    return (float(lit[0]), float(lit[1]))
                except Exception:
                    return None
            m = re.match(
                r"\(\s*([+-]?\d+(?:\.\d+)?)\s*,\s*([+-]?\d+(?:\.\d+)?)\s*\)", st
            )
            if m:
                try:
                    return (float(m.group(1)), float(m.group(2)))
                except Exception:
                    return None
            return None

        def _parse_scalar_or_none(s: str):
            if not isinstance(s, str):
                return None
            st = s.strip()
            if not st or st.lower() == "none":
                return None
            try:
                return float(st)
            except Exception:
                return None

        domains_raw = _split_top_level(str(merged.get("domains", "")))
        vlines_raw = _split_top_level(str(merged.get("vlines", "")))
        hlines_raw = _split_top_level(str(merged.get("hlines", "")))
        xlims_raw = _split_top_level(str(merged.get("xlims", "")))
        ylims_raw = _split_top_level(str(merged.get("ylims", "")))
        lines_raw = _split_top_level(str(merged.get("lines", "")))

        # Normalize sizes to match number of functions
        n = len(functions)

        def _pad(lst, fill="None"):
            return lst + [fill] * max(0, n - len(lst))

        domains_raw = _pad(domains_raw)
        vlines_raw = _pad(vlines_raw)
        hlines_raw = _pad(hlines_raw)
        xlims_raw = _pad(xlims_raw)
        ylims_raw = _pad(ylims_raw)
        lines_raw = _pad(lines_raw)

        dom_list: List[Tuple[float, float] | None] = []
        excl_list: List[List[float]] = []
        for s in domains_raw[:n]:
            dom, ex = _parse_domain_with_exclusions(s)
            dom_list.append(dom)
            excl_list.append(ex)

        vline_vals: List[List[float] | None] = [
            _parse_values_list_or_none(s) for s in vlines_raw[:n]
        ]
        hline_vals: List[List[float] | None] = [
            _parse_values_list_or_none(s) for s in hlines_raw[:n]
        ]
        xlim_vals: List[Tuple[float, float] | None] = [
            _parse_tuple_or_none(s) for s in xlims_raw[:n]
        ]
        ylim_vals: List[Tuple[float, float] | None] = [
            _parse_tuple_or_none(s) for s in ylims_raw[:n]
        ]

        # Parse per-axis line specs
        def _parse_line_spec(s: str):
            if not isinstance(s, str):
                return None
            st = s.strip()
            if not st or st.lower() == "none":
                return None
            lit = _safe_literal(st)
            a_val = None
            b_val = None
            if isinstance(lit, (list, tuple)) and len(lit) >= 2:
                try:
                    a_val = float(lit[0])
                except Exception:
                    a_val = None
                second = lit[1]
                if isinstance(second, (list, tuple)) and len(second) == 2:
                    try:
                        x0p = float(second[0])
                        y0p = float(second[1])
                        if a_val is not None:
                            b_val = y0p - a_val * x0p
                    except Exception:
                        b_val = None
                else:
                    try:
                        b_val = float(second)
                    except Exception:
                        b_val = None
                if a_val is not None and b_val is not None:
                    return (a_val, b_val)
            return None

        line_specs: List[Tuple[float, float] | None] = [
            _parse_line_spec(s) for s in lines_raw[:n]
        ]
        explicit_name = merged.get("name")
        debug_mode = "debug" in merged
        rows = int(float(merged.get("rows", 1)))
        # If cols not provided, default to enough columns to fit all functions over the given rows
        default_cols = max(1, (len(functions) + rows - 1) // max(1, rows))
        cols = int(float(merged.get("cols", default_cols)))

        # Include per-axis settings in the hash to prevent stale caches
        content_hash = _hash_key(
            "|".join(exprs),
            "|".join(labels_list),
            xmin,
            xmax,
            ymin,
            ymax,
            xstep,
            ystep,
            fontsize,
            lw,
            alpha,
            rows,
            cols,
            int(grid_flag),
            int(ticks_flag),
            "|".join(["" if d is None else f"{d[0]},{d[1]}" for d in dom_list]),
            "|".join(["|".join(map(str, exs)) if exs else "" for exs in excl_list]),
            "|".join(["|".join(map(str, vs)) if vs else "" for vs in vline_vals]),
            "|".join(["|".join(map(str, hs)) if hs else "" for hs in hline_vals]),
            "|".join(["" if xl is None else f"{xl[0]},{xl[1]}" for xl in xlim_vals]),
            "|".join(["" if yl is None else f"{yl[0]},{yl[1]}" for yl in ylim_vals]),
            "|".join(["" if ls is None else f"{ls[0]},{ls[1]}" for ls in line_specs]),
        )
        base_name = explicit_name or f"multi_plot_{content_hash}"

        rel_dir = os.path.join("_static", "multi_plot")
        abs_dir = os.path.join(app.srcdir, rel_dir)
        os.makedirs(abs_dir, exist_ok=True)
        svg_name = f"{base_name}.svg"
        abs_svg = os.path.join(abs_dir, svg_name)

        regenerate = ("nocache" in merged) or not os.path.exists(abs_svg)
        if regenerate:
            try:
                letters = [chr(i) for i in range(65, 65 + len(functions))]
                # Create axes grid without auto-plotting functions
                fig, axes = plotmath.multiplot(
                    functions=[],
                    fn_labels=False,
                    xmin=xmin,
                    xmax=xmax,
                    ymin=ymin,
                    ymax=ymax,
                    xstep=xstep,
                    ystep=ystep,
                    ticks=ticks_flag,
                    grid=grid_flag,
                    rows=rows,
                    cols=cols,
                    lw=lw,
                    alpha=alpha,
                    fontsize=fontsize,
                    figsize=(4.5 * cols, 3.5 * rows),
                )
                # Normalize axes to flat list
                try:
                    import numpy as _np

                    axes_list = (
                        list(axes.flatten())
                        if hasattr(axes, "flatten")
                        else list(_np.array(axes).flatten())
                    )
                except Exception:
                    axes_list = axes if isinstance(axes, (list, tuple)) else [axes]

                # Manual plotting per-axis
                import numpy as np

                for idx, (expr, fn) in enumerate(zip(exprs, functions)):
                    if idx >= len(axes_list):
                        break
                    ax = axes_list[idx]
                    # Per-axis domain
                    dom = dom_list[idx]
                    x0, x1 = dom if dom is not None else (xmin, xmax)
                    N = int(2**12)
                    x = np.linspace(x0, x1, N)
                    y = fn(x)
                    # Ensure float array and blank out non-finite values
                    y = np.asarray(y, dtype=float)
                    y[~np.isfinite(y)] = np.nan
                    # Robust exclusions: widen window and clear neighbors
                    exs = [e for e in excl_list[idx] if x0 < e < x1]
                    if exs and N > 1:
                        dx = (x1 - x0) / (N - 1)
                        w = max(4 * dx, 1e-6 * (1.0 + max(abs(e) for e in exs)))
                        for e in exs:
                            try:
                                mask = np.abs(x - e) <= w
                                if mask.any():
                                    y[mask] = np.nan
                                j = int(np.argmin(np.abs(x - e)))
                                for k in (j - 2, j - 1, j, j + 1, j + 2):
                                    if 0 <= k < y.size:
                                        y[k] = np.nan
                            except Exception:
                                try:
                                    j = int(np.argmin(np.abs(x - e)))
                                    if 0 <= j < y.size:
                                        y[j] = np.nan
                                except Exception:
                                    pass
                    # Also break across steep jumps or extreme magnitudes
                    # Determine per-axis y-span preference: use provided ylim for this axis if any
                    if ylim_vals[idx] is not None:
                        y0_lim, y1_lim = ylim_vals[idx]
                    else:
                        y0_lim, y1_lim = ymin, ymax
                    try:
                        y_span = abs(float(y1_lim) - float(y0_lim))
                    except Exception:
                        y_span = np.nan
                    if not (isinstance(y_span, (int, float)) and y_span > 0):
                        finite_y = y[np.isfinite(y)]
                        if finite_y.size > 0:
                            y_span = float(np.nanmax(finite_y) - np.nanmin(finite_y))
                    if not (isinstance(y_span, (int, float)) and y_span > 0):
                        y_span = 1.0
                    finite_pair = np.isfinite(y[:-1]) & np.isfinite(y[1:])
                    jump_factor = 0.5
                    big_jump = finite_pair & (
                        np.abs(y[1:] - y[:-1]) > (jump_factor * y_span)
                    )
                    if big_jump.any():
                        idx_break = np.where(big_jump)[0]
                        for i_b in idx_break:
                            if 0 <= i_b + 1 < y.size:
                                y[i_b + 1] = np.nan
                    mag_factor = 50.0
                    too_big = np.isfinite(y) & (np.abs(y) > (mag_factor * y_span))
                    if too_big.any():
                        y[too_big] = np.nan
                    lbl = (
                        labels_list[idx]
                        if (labels_list and idx < len(labels_list))
                        else None
                    )
                    if lbl:
                        ax.plot(x, y, lw=lw, alpha=alpha, label=f"${lbl}$")
                        ax.legend(fontsize=int(fontsize))
                    else:
                        ax.plot(x, y, lw=lw, alpha=alpha)
                    # Optional line y = a*x + b per axis
                    if line_specs[idx] is not None:
                        try:
                            a_l, b_l = line_specs[idx]  # type: ignore[misc]
                            # Use provided xlim for this axis if any; else global
                            if xlim_vals[idx] is not None:
                                x_min_line, x_max_line = xlim_vals[idx]
                            else:
                                x_min_line, x_max_line = xmin, xmax
                            x_line = np.array(
                                [float(x_min_line), float(x_max_line)], dtype=float
                            )
                            y_line = a_l * x_line + b_l
                            ax.plot(
                                x_line,
                                y_line,
                                linestyle="--",
                                color=plotmath.COLORS.get("red"),
                                lw=lw,
                                alpha=alpha,
                            )
                        except Exception:
                            pass
                    # vlines / hlines (support multiple values per axis)
                    for xv in vline_vals[idx] or []:
                        try:
                            ax.axvline(
                                x=float(xv),
                                color=plotmath.COLORS.get("red"),
                                linestyle="--",
                                lw=lw,
                            )
                        except Exception:
                            pass
                    for yh in hline_vals[idx] or []:
                        try:
                            ax.axhline(
                                y=float(yh),
                                color=plotmath.COLORS.get("red"),
                                linestyle="--",
                                lw=lw,
                            )
                        except Exception:
                            pass
                    # x/ylims
                    if xlim_vals[idx] is not None:
                        ax.set_xlim(*xlim_vals[idx])
                    if ylim_vals[idx] is not None:
                        ax.set_ylim(*ylim_vals[idx])
                # Save via the single Figure object
                fig.savefig(
                    abs_svg, format="svg", bbox_inches="tight", transparent=True
                )
                # Also save a PDF sidecar for debugging comparisons (optional)
                # try:
                #     fig.savefig(
                #         os.path.join(abs_dir, f"{base_name}.pdf"),
                #         format="pdf",
                #         bbox_inches="tight",
                #         transparent=True,
                #     )
                # except Exception:
                #     pass
                import matplotlib

                matplotlib.pyplot.close(fig)
            except Exception as e:
                return [
                    self.state_machine.reporter.error(
                        f"Feil under generering av graf: {e}", line=self.lineno
                    )
                ]

        if not os.path.exists(abs_svg):
            return [
                self.state_machine.reporter.error(
                    "multi-plot: SVG mangler.", line=self.lineno
                )
            ]

        env.note_dependency(abs_svg)
        try:  # copy to output _static
            out_static = os.path.join(app.outdir, "_static", "multi_plot")
            os.makedirs(out_static, exist_ok=True)
            shutil.copy2(abs_svg, os.path.join(out_static, svg_name))
        except Exception:
            pass

        try:
            raw_svg = open(abs_svg, "r", encoding="utf-8").read()
        except Exception as e:
            return [
                self.state_machine.reporter.error(
                    f"graph inline: kunne ikke lese SVG: {e}", line=self.lineno
                )
            ]

        if not debug_mode and "viewBox" in raw_svg:
            raw_svg = _strip_root_svg_size(raw_svg)

        def _rewrite_ids(txt: str, prefix: str) -> str:
            # Collect ids
            ids = re.findall(r'\bid="([^"]+)"', txt)
            if not ids:
                return txt
            # Skip font glyphs to avoid disrupting text rendering
            skip_prefixes = (
                "DejaVu",
                "CM",
                "STIX",
                "Nimbus",
                "Bitstream",
                "Arial",
                "Times",
                "Helvetica",
            )
            mapping = {}
            for i in ids:
                if i.startswith(skip_prefixes):
                    continue
                mapping[i] = f"{prefix}{i}"
            if not mapping:
                return txt

            # Replace id definitions
            def repl_id(m: re.Match) -> str:
                old = m.group(1)
                new = mapping.get(old, old)
                return f'id="{new}"'

            txt = re.sub(r'\bid="([^"]+)"', repl_id, txt)

            # Replace url(#id) everywhere (attributes and styles)
            def repl_url(m: re.Match) -> str:
                old = m.group(1).strip()
                new = mapping.get(old, old)
                return f"url(#{new})"

            txt = re.sub(r"url\(#\s*([^\)\s]+)\s*\)", repl_url, txt)

            # Replace href/xlink:href references supporting both quote styles
            def repl_href(m: re.Match) -> str:
                attr = m.group(1)
                quote = m.group(2)
                old = m.group(3).strip()
                new = mapping.get(old, old)
                return f"{attr}={quote}#{new}{quote}"

            txt = re.sub(
                r'(xlink:href|href)\s*=\s*(["\"])#\s*([^"\"]+)\s*\2',
                repl_href,
                txt,
            )
            return txt

        if not debug_mode:
            raw_svg = _rewrite_ids(
                raw_svg, f"mgr_{content_hash}_{uuid.uuid4().hex[:6]}_"
            )

        alt_default = f"Multiplot av {len(exprs)} funksjoner"
        alt = merged.get("alt", alt_default)

        width_opt = merged.get("width")
        percent = isinstance(width_opt, str) and width_opt.strip().endswith("%")

        def _augment(m):
            tag = m.group(0)
            if "class=" not in tag:
                tag = tag[:-1] + ' class="graph-inline-svg"' + ">"
            else:
                tag = tag.replace('class="', 'class="graph-inline-svg ')
            if alt and "aria-label=" not in tag:
                tag = tag[:-1] + f' role="img" aria-label="{alt}"' + ">"
            if width_opt:
                if percent:
                    wval = width_opt.strip()
                else:
                    wval = width_opt.strip()
                    if wval.isdigit():
                        wval += "px"
                style_frag = f"width:{wval}; height:auto; display:block; margin:0 auto;"
                if "style=" in tag:
                    tag = re.sub(
                        r'style="([^"]*)"',
                        lambda mm: f'style="{mm.group(1)}; {style_frag}"',
                        tag,
                        count=1,
                    )
                else:
                    tag = tag[:-1] + f' style="{style_frag}"' + ">"
            return tag

        raw_svg = re.sub(r"<svg\b[^>]*>", _augment, raw_svg, count=1)
        if alt and "<title" not in raw_svg:
            raw_svg = re.sub(
                r"(<svg\b[^>]*>)",
                r"\1<title>" + re.escape(alt) + r"</title>",
                raw_svg,
                count=1,
            )

        figure = nodes.figure()
        figure.setdefault("classes", []).extend(
            ["adaptive-figure", "multi-plot-figure", "no-click"]
        )
        raw_node = nodes.raw("", raw_svg, format="html")
        raw_node.setdefault("classes", []).extend(
            ["graph-image", "no-click", "no-scaled-link"]
        )
        figure += raw_node

        extra_classes = merged.get("class")
        if extra_classes:
            figure["classes"].extend(extra_classes)
        figure["align"] = merged.get("align", "center")

        caption_lines = list(self.content)[caption_idx:]
        while caption_lines and not caption_lines[0].strip():
            caption_lines.pop(0)
        if caption_lines:
            caption = nodes.caption()
            caption += nodes.Text("\n".join(caption_lines))
            figure += caption

        if explicit_name:
            self.add_name(figure)
        return [figure]


def setup(app):  # pragma: no cover
    app.add_directive("multi-plot", MultiPlotDirective)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}

r"""Plot directive — full reference (supports rich SymPy expressions)

This directive builds flexible, textbook‑style mathematical plots using a
compact YAML‑like front matter plus repeated keys for geometric *primitives*.
It powers interactive / pedagogical figures while remaining deliberately
fault‑tolerant: malformed items are skipped instead of aborting the build.

NEW / EXTENDED FEATURES (summary)
---------------------------------
* Unified expression evaluator: almost every numeric field now accepts SymPy
  expressions (``pi``, ``sqrt(2)``, ``exp(1/3)``, arithmetic, trig, etc.).
* Function domains & exclusions accept expressions: ``(0, 2*sqrt(5))`` or
  ``( -pi, pi ) \ { -pi/2, pi/2 }``.
* Points, polygons, fill‑polygons, line‑segments, vectors, angle‑arcs,
  circles, ellipses, and parametric curves all evaluate coordinates via SymPy.
* New primitives: ``circle``, ``ellipse``, ``curve`` (parametric ``x(t), y(t)``).
* Style / color tokens order‑independent for line‑segment, circle, ellipse,
  curve, angle‑arc (after required numeric parts).
* Palette mapping: colors first resolved through ``plotmath.COLORS`` then
  fall back to the literal token then a sensible default.

Quick start (MyST)
------------------
:::{plot}
function: sin(x)/x, f(x), (-6*pi, 6*pi) \ {0}
curve: cos(t), sin(2*t), (0, 2*pi), dashed, orange
circle: (0,0), 2*pi/6, dotted, green
ellipse: (1, -1), 3, sqrt(5), red
point: (pi, f(pi))
line-segment: (0,0), (2*sqrt(2), 2), dashed, purple
vector: 0, 0, 2*cos(pi/6), 2*sin(pi/6), teal
angle-arc: (0,0), 2.5, 0, 60, dashed
annotate: (pi, f(pi)), (pi, 0), "Maximum?", 0.25
xmin: -10
xmax: 10
ymin: -5
ymax: 5
grid: on
ticks: true
fontsize: 22
width: 100%
xlabel: $x$
ylabel: $y$
:::

MyST *or* classic reST (``.. plot::``) forms are accepted. All examples below
use MyST for brevity.

Front matter
------------
* Provide a fenced block introduced by ``:::{plot}`` (preferred) or use an
  unfenced reST directive. Within the block, write ``key: value`` lines.
* A blank line ends the front matter; remaining lines become the caption.
* Repeated keys (multi‑valued): ``function``, ``point``, ``annotate``, ``text``,
  ``vline``, ``hline``, ``line``, ``line-segment``, ``polygon``, ``fill-polygon``,
  ``bar``, ``axis``, ``vector``, ``angle-arc``, ``circle``, ``ellipse``, ``curve``.

Global figure & layout options
------------------------------
width          CSS width (``100%`` or pixels).
figsize        ``(w, h)`` in inches; applied at the end.
align          ``left|center|right``.
class          Extra CSS classes.
name           Stable output filename / anchor.
alt            Alt text (accessibility).
nocache        Force regeneration (ignore cache).
debug          Keep raw SVG size & emit sidecar PDF if possible.
fontsize       Base font size (default 20).
lw             Default line width for plotted curves (default 2.5).
alpha          Global alpha for function / curve lines (optional).
xmin,xmax,ymin,ymax   Axis bounds (defaults ±6).
xstep,ystep    Tick spacing (default 1).
ticks          ``true|false`` master toggle for ticks/labels.
xticks|yticks  ``off`` to remove one axis’s ticks.
grid           ``true|false`` (independent of ``ticks``).
xlabel,ylabel  Axis labels; can add a pad: ``xlabel: $t$, 8``.
axis           Repeated key for special modes: ``off``, ``equal`` (may combine).

Expression support
------------------
All numeric coordinates (centers, radii, interval endpoints, slopes, etc.) may
be SymPy expressions. Allowed names include: ``pi``, ``E``, ``sqrt``, ``exp``,
``log``, ``sin``, ``cos``, ``tan``, ``asin``, ``acos``, ``atan``, ``Abs`` plus
basic arithmetic. A small, safe namespace is used; arbitrary Python execution
is not performed. If evaluation fails the item is skipped silently.

Functions
---------
Forms:
1. ``function: expr`` — variable is ``x``.
2. ``function: expr, label``
3. ``function: expr (a,b)`` — domain restriction (open interval).
4. ``function: expr (a,b) \ {x1, x2}`` — exclusions inside domain.
5. List / tuple literal mixing expression, label, domain, exclusion set in
   any order: ``function: [expr, "f(x)", (a,b), {x1, x2}]``.

Notes:
* Discontinuities and exclusions are split to avoid vertical strokes.
* Single‑letter labels are preserved (``g`` no longer coerced into a color).
* Labels auto‑wrapped for math; don’t include surrounding ``$``.

Points
------
``point: (x, y)`` where each coordinate can be an expression or a *function
label call* of the form ``label(number)`` (e.g. ``point: (2, f(2))``).

Vertical / horizontal lines
---------------------------
``vline: x[, ymin, ymax][, linestyle][, color]``
``hline: y[, x0, x1][, linestyle][, color]``
Linestyles: ``solid|dotted|dashed|dashdot`` (order with color is free). Omitted
range endpoints default to current axis min/max.

General line and segments
-------------------------
``line: a, (x0, y0)[, linestyle][, color]`` — draws ``y = a*(x - x0) + y0``.
``line: a, b[, linestyle][, color]`` — draws ``y = a*x + b``.
``line-segment: (x1, y1), (x2, y2)[, linestyle][, color]`` — finite segment.

Polygons
--------
``polygon: (x1, y1), (x2, y2), ...[, show_vertices]`` — edges.
``fill-polygon: (..)[, color][, alpha]`` — filled interior; first non‑numeric
extra = color, first numeric extra = alpha (default 0.1).
Coordinates accept expressions and function label calls.

Bars
----
``bar: (x, y), length, orientation`` where orientation is one of
``h|hor|horiz|horizontal`` or ``v|vert|vertical``.

Vectors
-------
``vector: x, y, dx, dy[, color]`` — all four numeric fields accept expressions.
Color mapped through palette then fallback to literal then black.

Angle arcs
----------
``angle-arc: (cx, cy), radius, start_deg, end_deg[, linestyle][, color]``.
Angles in *degrees* (mathematical CCW convention). All numeric parts allow
expressions. Optional style/color order‑independent after the first three
expressions.

Circles & ellipses
------------------
Circle: ``circle: (cx, cy), r[, linestyle][, color]`` (r > 0).
Ellipse: ``ellipse: (cx, cy), a, b[, linestyle][, color]`` (a,b > 0).
Both sample 1024 points; style/color optional and order‑independent.

Parametric curves
-----------------
``curve: x_expr, y_expr, (t0, t1)[, linestyle][, color]`` — samples 1024 points
with ``t`` symbol. Interval endpoints may be expressions (auto‑swapped if
reversed). Style/color optional.

Annotations & text
------------------
``annotate: (xytext), (xy), "text"[, arc]`` — arrow annotation; coordinates &
arc curvature can be expressions.
``text: [x, y, string[, pos][, bbox]]`` — position tokens: ``top-left``,
``center-center``, etc.; *long* variants shift further (e.g. ``longtop-left``).

Axis overrides: off / equal
---------------------------
``axis: off`` hides frame & ticks (manual artists still drawn).
``axis: equal`` enforces 1:1 aspect (may combine with ``off``). Additional
``axis: tight`` etc. still applied in visible‑axis mode.

Color & linestyle resolution
----------------------------
1. Try ``plotmath.COLORS[name]``.
2. Fallback to the literal (Matplotlib named or hex) token.
3. Fallback default (e.g. black, red, blue depending on primitive).
Single‑letter Matplotlib shorthands are *disabled for function labels* to
avoid ambiguity.

Safety & robustness
-------------------
* Expression evaluation uses SymPy in a restricted namespace (no exec / eval).
* Any parsing failure for an individual primitive silently skips that item.
* Cached SVGs stored under ``_static/plot/`` keyed by a content hash unless a
  ``name:`` override is supplied.

Caption
-------
Lines after a blank line (or after the front matter fence) become the caption.

This docstring is intentionally exhaustive; HOWTOWRITE.md contains user‑facing
Norwegian examples.
"""

from __future__ import annotations

import ast
import hashlib
import os
import re
import shutil
import uuid
from typing import Any, Callable, Dict, List, Tuple

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


# ------------------------------------
# Utilities
# ------------------------------------


def _hash_key(*parts) -> str:
    h = hashlib.sha1()
    for p in parts:
        if p is None:
            p = "__NONE__"
        h.update(str(p).encode("utf-8"))
        h.update(b"||")
    return h.hexdigest()[:12]


def _compile_function(expr: str) -> Callable:
    import sympy, numpy as np

    expr = expr.strip()
    x = sympy.symbols("x")
    try:
        sym = sympy.sympify(expr)
    except Exception as e:
        raise ValueError(f"Ugyldig funksjonsuttrykk '{expr}': {e}")
    # If the expression does not depend on x, treat it as a constant function
    if not sym.free_symbols or sym.free_symbols.isdisjoint({x}):
        const_val = float(sym.evalf())

        def f(arr):
            a = np.asarray(arr, dtype=float)
            return np.full_like(a, fill_value=const_val, dtype=float)

        _ = f([0.0, 1.0])
        return f

    fn_np = sympy.lambdify(x, sym, modules=["numpy"])

    def f(arr):
        return fn_np(np.asarray(arr, dtype=float))

    _ = f([0.0, 1.0])
    return f


def _parse_bool(val, default: bool | None = None) -> bool | None:
    if val is None:
        return default
    if isinstance(val, bool):
        return val
    s = str(val).strip().lower()
    if s == "":
        return True
    if s in {"true", "yes", "on", "1"}:
        return True
    if s in {"false", "no", "off", "0"}:
        return False
    return default


def _strip_root_svg_size(svg_text: str) -> str:
    def repl(m):
        tag = m.group(0)
        tag = re.sub(r'\swidth="[^"]+"', "", tag)
        tag = re.sub(r'\sheight="[^"]+"', "", tag)
        return tag

    return re.sub(r"<svg\b[^>]*>", repl, svg_text, count=1)


def _rewrite_ids(txt: str, prefix: str) -> str:
    ids = re.findall(r'\bid="([^"]+)"', txt)
    if not ids:
        return txt
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

    def repl_id(m: re.Match) -> str:
        old = m.group(1)
        new = mapping.get(old, old)
        return f'id="{new}"'

    txt = re.sub(r'\bid="([^"]+)"', repl_id, txt)

    def repl_url(m: re.Match) -> str:
        old = m.group(1).strip()
        new = mapping.get(old, old)
        return f"url(#{new})"

    txt = re.sub(r"url\(#\s*([^\)\s]+)\s*\)", repl_url, txt)

    def repl_href(m: re.Match) -> str:
        attr = m.group(1)
        quote = m.group(2)
        old = m.group(3).strip()
        new = mapping.get(old, old)
        return f"{attr}={quote}#{new}{quote}"

    txt = re.sub(r'(xlink:href|href)\s*=\s*(["\"])#\s*([^"\"]+)\s*\2', repl_href, txt)
    return txt


def _safe_literal(val: str):
    try:
        return ast.literal_eval(val)
    except Exception:
        return None


def _split_list(val: str) -> List[str]:
    s = str(val or "").strip()
    if not s:
        return []
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    s = s.replace(";", ",")
    return [p.strip() for p in s.split(",") if p.strip()]


def _parse_text_positioning(pos: str) -> Tuple[str, str]:
    """Map positioning string to (va, ha). Default is (top, left).

    Accepted values (case-insensitive, hyphen or underscore allowed):
      - top-left, top-right, bottom-left, bottom-right,
      - top-center, bottom-center, center-left, center-right
    """
    if not isinstance(pos, str):
        return ("top", "left")
    key = pos.strip().lower().replace("_", "-")

    # Map onto the opposites to make intuitive sense.
    # Matplotlib expects the position to refer to where the object is relative to the text.
    # Thus "left" means the object is to the "left" of the text.
    # Here "left" will mean "move the text to the left of the object"
    mapping = {
        "top-left": ("bottom", "right"),
        "top-right": ("bottom", "left"),
        "bottom-left": ("top", "right"),
        "bottom-right": ("top", "left"),
        "top-center": ("bottom", "center"),
        "bottom-center": ("top", "center"),
        "center-left": ("center", "right"),
        "center-right": ("center", "left"),
        # Longer distance from point
        "longtop-left": ("longbottom", "left"),
        "longtop-longleft": ("longbottom", "longright"),
        "longbottom-right": ("longtop", "right"),
        "longbottom-left": ("longtop", "left"),
        "longtop-center": ("longbottom", "center"),
        "longbottom-center": ("longtop", "center"),
        "longtop-longright": ("longbottom", "longleft"),
        "longbottom-longright": ("longtop", "longleft"),
        "longtop-longleft": ("longbottom", "longright"),
        "longbottom-longleft": ("longtop", "longright"),
        "top-longleft": ("bottom", "longright"),
        "top-longright": ("bottom", "longleft"),
        "bottom-longleft": ("top", "longright"),
        "bottom-longright": ("top", "longleft"),
        "center-longleft": ("center", "longright"),
        "center-longright": ("center", "longleft"),
        "center-center": ("center", "center"),
    }
    return mapping.get(key, ("top", "left"))


class PlotDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    option_spec = {
        # presentation / misc
        "width": directives.length_or_percentage_or_unitless,
        "align": lambda a: directives.choice(a, ["left", "center", "right"]),
        "class": directives.class_option,
        "name": directives.unchanged,
        "nocache": directives.flag,
        "debug": directives.flag,
        "alt": directives.unchanged,
        # axes options (optional in YAML too)
        "xmin": directives.unchanged,
        "xmax": directives.unchanged,
        "ymin": directives.unchanged,
        "ymax": directives.unchanged,
        "xstep": directives.unchanged,
        "ystep": directives.unchanged,
        "fontsize": directives.unchanged,
        "ticks": directives.unchanged,
        "grid": directives.unchanged,
        "xticks": directives.unchanged,
        "yticks": directives.unchanged,
        "lw": directives.unchanged,
        "alpha": directives.unchanged,
        "figsize": directives.unchanged,
        # axis labels
        "xlabel": directives.unchanged,
        "ylabel": directives.unchanged,
    }

    def _parse_kv_block(self) -> Tuple[Dict[str, Any], Dict[str, List[str]], int]:
        """Parse front matter supporting repeated keys for function/point/annotate.

        Returns: (scalars, lists, caption_idx)
        """
        lines = list(self.content)
        scalars: Dict[str, Any] = {}
        lists: Dict[str, List[str]] = {
            "function": [],
            "point": [],
            "annotate": [],
            "text": [],
            "vline": [],
            "hline": [],
            "line": [],
            "polygon": [],
            "axis": [],
            "fill-polygon": [],
            "bar": [],
            "vector": [],
            "line-segment": [],
            "angle-arc": [],
            "circle": [],
            "ellipse": [],
            "curve": [],
        }
        # YAML-like fenced front matter
        if lines and lines[0].strip() == "---":
            idx = 1
            while idx < len(lines) and lines[idx].strip() != "---":
                line = lines[idx].rstrip()
                if not line.strip():
                    idx += 1
                    continue
                m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
                if m:
                    key, value = m.group(1), m.group(2)
                    if key in lists:
                        lists[key].append(value)
                    else:
                        scalars[key] = value
                idx += 1
            # Skip closing fence if present
            if idx < len(lines) and lines[idx].strip() == "---":
                idx += 1
            # Skip trailing blanks before caption
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            return scalars, lists, idx

        # Fallback: non-fenced lines until first non "key: value" or a blank separator
        caption_start = 0
        for i, line in enumerate(lines):
            if not line.strip():
                caption_start = i + 1
                continue
            m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
            if m:
                key, value = m.group(1), m.group(2)
                if key in lists:
                    lists[key].append(value)
                else:
                    scalars[key] = value
                caption_start = i + 1
            else:
                break
        return scalars, lists, caption_start

    def run(self):
        env = self.state.document.settings.env
        app = env.app
        try:
            import plotmath  # type: ignore
            import numpy as np  # used for x sampling when plotting functions
        except Exception as e:
            err = nodes.error()
            err += nodes.paragraph(text=f"Kunne ikke importere plotmath: {e}")
            return [err]

        scalars, lists, caption_idx = self._parse_kv_block()
        merged: Dict[str, Any] = {**scalars, **self.options}

        # debug print removed

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
        figsize_raw = merged.get("figsize")
        try:
            alpha = float(alpha_raw) if alpha_raw not in (None, "") else None
        except Exception:
            alpha = None

        ticks_flag = _parse_bool(merged.get("ticks"), default=None)
        grid_flag = _parse_bool(merged.get("grid"), default=None)

        # Set defaults: if neither is specified, both default to True
        if ticks_flag is None and grid_flag is None:
            ticks_flag = True
            grid_flag = True
        else:
            # If ticks not explicitly set, default to True (independent of grid setting)
            if ticks_flag is None:
                ticks_flag = True
            else:
                ticks_flag = bool(ticks_flag)

            # If grid not explicitly set, default to True (independent of ticks setting)
            if grid_flag is None:
                grid_flag = True
            else:
                grid_flag = bool(grid_flag)

        # Compile functions (may be zero or many) and parse optional labels, optional domain (xmin,xmax), exclusions and color
        raw_fn_items = lists.get("function", [])
        fn_exprs: List[str] = []
        fn_labels_list: List[str] = []
        fn_domains_list: List[Tuple[float, float] | None] = []
        fn_exclusions_list: List[List[float]] = []
        fn_colors_list: List[str] = []
        functions: List[Callable] = []

        def _parse_function_item(
            s: str,
        ) -> Tuple[
            str,
            str | None,
            Tuple[float, float] | None,
            List[float],
            str | None,
        ]:
            s = str(s).strip()

            # Heuristic to detect if a string token looks like a color
            def _looks_like_color(tok: str) -> bool:
                if not isinstance(tok, str):
                    return False
                t = tok.strip()
                if not t:
                    return False
                # hex colors
                if re.match(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$", t):
                    return True
                # IMPORTANT: single-letter matplotlib shorthands intentionally
                # NOT treated as colors here so that users can name functions
                # with letters like 'g' without it being consumed as green.
                # Use full names (e.g. 'green') or color=green instead.
                if t.lower().startswith("tab:"):
                    return True
                if re.match(r"^C\d+$", t):
                    return True
                # plotmath named colors
                try:
                    import plotmath as _pm

                    if _pm.COLORS.get(t) is not None:
                        return True
                except Exception:
                    pass
                return False

            # Try literal list/tuple like ("expr", "label") or ("expr", (xmin,xmax)) or ("expr", "label", (xmin,xmax)) in any order
            lit = _safe_literal(s)
            if isinstance(lit, (list, tuple)) and len(lit) >= 1:
                expr = str(lit[0]).strip()
                label: str | None = None
                domain: Tuple[float, float] | None = None
                excludes: List[float] = []
                color: str | None = None
                for item in list(lit[1:]):
                    # Detect domain tuple/list of two numbers
                    if (
                        domain is None
                        and isinstance(item, (list, tuple))
                        and len(item) == 2
                    ):
                        try:
                            d0 = float(item[0])
                            d1 = float(item[1])
                            domain = (d0, d1)
                            continue
                        except Exception:
                            pass
                    # Detect exclusions as a collection of numbers (not a 2-tuple domain)
                    if isinstance(item, (set, list, tuple)) and not (
                        isinstance(item, (list, tuple)) and len(item) == 2
                    ):
                        for v in item:
                            try:
                                excludes.append(float(v))
                            except Exception:
                                pass
                    # Else string-like: support label/color, order-independent
                    if isinstance(item, str):
                        tok = item.strip()
                        if tok.lower().startswith("label="):
                            if label is None:
                                label = tok.split("=", 1)[1].strip()
                            continue
                        if tok.lower().startswith("color="):
                            if color is None:
                                color = tok.split("=", 1)[1].strip()
                            continue
                        if color is None and _looks_like_color(tok):
                            color = tok
                        elif label is None:
                            lab = tok
                            label = lab if lab else None
                return expr, label, domain, excludes, color
            # Fallback: attempt to locate a (domain) pattern (expr_a, expr_b) with fully balanced parentheses
            # and optional exclusions of the form \{a,b,c}. Supports nested parentheses in each endpoint
            # (e.g. (0, 2*sqrt(5)) or (pi/4, 3*pi/2 + sqrt(2))).
            domain: Tuple[float, float] | None = None
            excludes: List[float] = []
            color: str | None = None

            def _sym_eval_num(txt: str) -> float:
                import sympy

                allowed = {
                    k: getattr(sympy, k)
                    for k in [
                        "pi",
                        "E",
                        "exp",
                        "sqrt",
                        "log",
                        "sin",
                        "cos",
                        "tan",
                        "asin",
                        "acos",
                        "atan",
                        "Rational",
                    ]
                    if hasattr(sympy, k)
                }
                expr = sympy.sympify(txt, locals=allowed)
                return float(expr.evalf())

            def _extract_domain_and_exclusions(text: str):
                """Return (domain_tuple|None, exclusions_list, text_without_domain).
                Heuristic: find the first parenthesis block whose top-level content
                splits into exactly two parts by a single top-level comma.
                """
                n = len(text)
                i = 0
                while i < n:
                    if text[i] == "(":
                        depth = 1
                        j = i + 1
                        while j < n and depth > 0:
                            ch = text[j]
                            if ch == "(":
                                depth += 1
                            elif ch == ")":
                                depth -= 1
                            j += 1
                        if depth != 0:
                            # unbalanced, give up
                            break
                        content = text[i + 1 : j - 1].strip()
                        # Find a single top-level comma in content
                        depth2 = 0
                        comma_index: int | None = None
                        for k, ch in enumerate(content):
                            if ch == "(":
                                depth2 += 1
                            elif ch == ")":
                                depth2 -= 1
                            elif ch == "," and depth2 == 0:
                                if comma_index is None:
                                    comma_index = k
                                else:
                                    # more than one top-level comma => not domain
                                    comma_index = None
                                    break
                        if comma_index is not None:
                            left = content[:comma_index].strip()
                            right = content[comma_index + 1 :].strip()
                            if left and right:
                                # Optional exclusions right after ) like \{a,b}
                                k2 = j
                                excl_list: List[float] = []
                                # skip whitespace
                                while k2 < n and text[k2].isspace():
                                    k2 += 1
                                if k2 < n and text[k2] == "\\":
                                    k2 += 1
                                    while k2 < n and text[k2].isspace():
                                        k2 += 1
                                    if k2 < n and text[k2] == "{":
                                        k2 += 1
                                        excl_start = k2
                                        # read until matching '}' (no nesting expected here)
                                        while k2 < n and text[k2] != "}":
                                            k2 += 1
                                        excl_content = text[excl_start:k2]
                                        if k2 < n and text[k2] == "}":
                                            k2 += 1  # consume '}'
                                        for tok in [
                                            t.strip()
                                            for t in excl_content.split(",")
                                            if t.strip()
                                        ]:
                                            try:
                                                excl_list.append(_sym_eval_num(tok))
                                            except Exception:
                                                pass
                                # Attempt numeric evaluation of endpoints
                                dom_tuple: Tuple[float, float] | None = None
                                try:
                                    d0 = _sym_eval_num(left)
                                    d1 = _sym_eval_num(right)
                                    dom_tuple = (d0, d1)
                                except Exception:
                                    dom_tuple = None
                                # Remove the consumed substring from original text
                                new_text = (text[:i] + text[k2:]).strip()
                                return dom_tuple, excl_list, new_text
                        # Move past this parenthesis group and continue scanning
                        i = j
                        continue
                    i += 1
                return None, [], text

            domain, excludes, s_wo_dom = _extract_domain_and_exclusions(s)
            # Tokenize on commas to robustly drop empty segments created by domain removal
            parts = [p.strip() for p in s_wo_dom.split(",") if p.strip()]
            if parts:
                expr = parts[0]
                label = None
                # Scan remaining tokens for label/color using heuristics
                for tok in parts[1:]:
                    t = tok.strip()
                    if t.lower().startswith("label="):
                        if label is None:
                            label = t.split("=", 1)[1].strip()
                        continue
                    if t.lower().startswith("color="):
                        if color is None:
                            color = t.split("=", 1)[1].strip()
                        continue
                    if color is None and _looks_like_color(t):
                        color = t
                    elif label is None:
                        label = t
                return expr, label, domain, excludes, color
            # Only expression provided (or empty after cleanup)
            return s_wo_dom.strip(), None, domain, excludes, None

        for item in raw_fn_items:
            expr, label, domain, excludes, color = _parse_function_item(item)
            try:
                functions.append(_compile_function(expr))
                fn_exprs.append(expr)
                fn_labels_list.append(label or "")
                fn_domains_list.append(domain)
                fn_exclusions_list.append(sorted(excludes))
                fn_colors_list.append(color or "")
            except Exception as ex:
                return [
                    self.state_machine.reporter.error(
                        f"Ugyldig funksjon '{expr}': {ex}", line=self.lineno
                    )
                ]

        # ------------------------------------
        # Unified numeric expression evaluator
        # Supports:
        #  * Plain numbers
        #  * Arithmetic & SymPy functions (sqrt, pi, sin, ...)
        #  * References to previously defined function labels: f(2), g(pi/4+1)
        # Limitations: nested user function calls deeper than 50 rewrites are blocked.
        # ------------------------------------
        _num_cache: Dict[str, float] = {}

        def _eval_expr(val) -> float:
            import sympy, re

            if val is None:
                raise ValueError("Empty value")
            if isinstance(val, (int, float)):
                return float(val)
            s0 = str(val).strip()
            if not s0:
                raise ValueError("Blank numeric expression")
            if s0 in _num_cache:
                return _num_cache[s0]
            s = s0
            # Replace user function label calls iteratively.
            # Allow nested parentheses now by a balanced scan: we match label( ... ) at top-level of that paren group.
            pat = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)\(")
            # Simpler: fallback to previous non-nested approach but broaden attempt; for safety keep prior pattern.
            pat_simple = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)\(([^()]+)\)")
            for _ in range(50):
                m = pat_simple.search(s)
                if not m:
                    break
                lbl, arg_expr = m.group(1), m.group(2)
                if lbl in fn_labels_list:
                    try:
                        arg_val = _eval_expr(arg_expr)
                        idx = fn_labels_list.index(lbl)
                        f = functions[idx]
                        yv = float(f([arg_val])[0])
                        s = s[: m.start()] + f"{yv}" + s[m.end() :]
                        continue
                    except Exception:
                        # leave unresolved for sympy
                        pass
                # If not user function, just proceed to next occurrence
                # Remove nothing to avoid infinite loop: break
                break
            allowed = {
                k: getattr(sympy, k)
                for k in [
                    "pi",
                    "E",
                    "exp",
                    "sqrt",
                    "log",
                    "sin",
                    "cos",
                    "tan",
                    "asin",
                    "acos",
                    "atan",
                    "Rational",
                ]
                if hasattr(sympy, k)
            }
            try:
                expr = sympy.sympify(s, locals=allowed)
                valf = float(expr.evalf())
                _num_cache[s0] = valf
                return valf
            except Exception as e:
                raise ValueError(f"Kunne ikke tolke numerisk uttrykk '{val}': {e}")

        # Points
        point_vals: List[Tuple[float, float]] = []
        for p in lists.get("point", []):
            lit = _safe_literal(p)
            if isinstance(lit, (list, tuple)) and len(lit) == 2:
                try:
                    x0 = _eval_expr(lit[0])
                    y0 = _eval_expr(lit[1])
                    point_vals.append((x0, y0))
                except Exception:
                    pass
            else:
                # Support dynamic evaluation referencing previously defined function labels, e.g. (5, f(5))
                # Simple pattern match for a parenthesized pair allowing arbitrary (non-comma) inner expressions.
                ps = str(p).strip()
                m_pair = re.match(r"^\(\s*([^,]+?)\s*,\s*([^,]+?)\s*\)$", ps)
                if m_pair:
                    x_raw = m_pair.group(1).strip()
                    y_raw = m_pair.group(2).strip()
                    try:
                        x_val = _eval_expr(x_raw)
                    except Exception:
                        # If x itself references a function call label(arg)
                        m_fx = re.match(
                            r"^([A-Za-z_][A-Za-z0-9_]*)\(\s*([+-]?(?:\d+(?:\.\d+)?))\s*\)$",
                            x_raw,
                        )
                        if m_fx:
                            lbl = m_fx.group(1)
                            arg = float(m_fx.group(2))
                            try:
                                idx = fn_labels_list.index(lbl)
                                x_val = float(functions[idx]([arg])[0])
                            except Exception:
                                continue  # give up on this point
                        else:
                            continue
                    # y may be a direct float or a function label call like f(5)
                    try:
                        y_val = _eval_expr(y_raw)
                    except Exception:
                        m_fy = re.match(
                            r"^([A-Za-z_][A-Za-z0-9_]*)\(\s*([+-]?(?:\d+(?:\.\d+)?))\s*\)$",
                            y_raw,
                        )
                        if not m_fy:
                            continue
                        lbl = m_fy.group(1)
                        arg = float(m_fy.group(2))
                        if lbl in fn_labels_list:
                            try:
                                idx = fn_labels_list.index(lbl)
                                y_val = float(functions[idx]([arg])[0])
                            except Exception:
                                continue
                        else:
                            continue
                    try:
                        point_vals.append((float(x_val), float(y_val)))
                    except Exception:
                        pass

        # Annotations: [(xytext), (xy), "text", arc] OR without outer brackets:
        # (xytext), (xy), "text"[, arc]
        ann_vals: List[Tuple[Tuple[float, float], Tuple[float, float], str, float]] = []

        def _annotate_fallback_parse(raw: str):
            """Fallback parser for annotate lines containing arbitrary expressions.
            Expected pattern: (expr_x1, expr_y1), (expr_x2, expr_y2), "text"[, arc]
            Returns list of ( (x1,y1), (x2,y2), text, arc_expr|None ).
            """
            s = raw.strip()
            out: List[Tuple[Tuple[str, str], Tuple[str, str], str, str | None]] = []

            # Find first two balanced tuples
            def _grab_tuple(start_index: int) -> Tuple[int, int, str] | None:
                if start_index >= len(s) or s[start_index] != "(":
                    return None
                depth = 0
                for j in range(start_index, len(s)):
                    if s[j] == "(":
                        depth += 1
                    elif s[j] == ")":
                        depth -= 1
                        if depth == 0:
                            inner = s[start_index + 1 : j]
                            return (start_index, j, inner)
                return None

            # locate first '('
            i1 = s.find("(")
            if i1 == -1:
                return out
            t1 = _grab_tuple(i1)
            if not t1:
                return out
            i2_search = t1[1] + 1
            # skip commas/space
            while i2_search < len(s) and s[i2_search] in " ,":
                i2_search += 1
            if i2_search >= len(s) or s[i2_search] != "(":
                return out
            t2 = _grab_tuple(i2_search)
            if not t2:
                return out
            rest = s[t2[1] + 1 :].strip()

            # Split tuple inners on top-level comma
            def _split_pair(inner: str) -> Tuple[str, str] | None:
                depth = 0
                for k, ch in enumerate(inner):
                    if ch == "(":
                        depth += 1
                    elif ch == ")":
                        depth -= 1
                    elif ch == "," and depth == 0:
                        left = inner[:k].strip()
                        right = inner[k + 1 :].strip()
                        if left and right:
                            return (left, right)
                return None

            p1 = _split_pair(t1[2])
            p2 = _split_pair(t2[2])
            if not (p1 and p2):
                return out
            # Extract quoted text
            # Regex to capture either a double-quoted or single-quoted string
            m_txt = re.search(
                r"\"([^\"\\]*(?:\\.[^\"\\]*)*)\"|'([^'\\]*(?:\\.[^'\\]*)*)'", rest
            )
            if not m_txt:
                return out
            text = m_txt.group(1) if m_txt.group(1) is not None else m_txt.group(2)
            after = rest[m_txt.end() :].strip().lstrip(",").strip()
            arc_expr = after if after else None
            out.append(((p1[0], p1[1]), (p2[0], p2[1]), text, arc_expr))
            return out

        for a in lists.get("annotate", []):
            lit = _safe_literal(a)
            # If user omitted surrounding brackets, try wrapping in [] for parsing
            if not (isinstance(lit, (list, tuple)) and len(lit) >= 3):
                lit_wrapped = _safe_literal(f"[{a}]")
                if isinstance(lit_wrapped, list) and len(lit_wrapped) >= 3:
                    lit = lit_wrapped
            added_before = len(ann_vals)
            if isinstance(lit, (list, tuple)) and len(lit) >= 3:
                xytext, xy, text = lit[0], lit[1], lit[2]
                # arc (arrow curvature) may be an expression
                try:
                    arc = _eval_expr(str(lit[3])) if len(lit) > 3 else 0.3
                except Exception:
                    try:
                        arc = float(lit[3]) if len(lit) > 3 else 0.3
                    except Exception:
                        arc = 0.3
                try:
                    # Allow expression coordinates. Expect xytext and xy to be (x,y)-like iterables
                    xyt0 = _eval_expr(str(xytext[0]))
                    xyt1 = _eval_expr(str(xytext[1]))
                    xy0 = _eval_expr(str(xy[0]))
                    xy1 = _eval_expr(str(xy[1]))
                    xytext = (float(xyt0), float(xyt1))
                    xy = (float(xy0), float(xy1))
                    text = str(text)
                    ann_vals.append((xytext, xy, text, float(arc)))
                except Exception:
                    # Fallback: attempt plain float conversion
                    try:
                        xytext = (float(xytext[0]), float(xytext[1]))
                        xy = (float(xy[0]), float(xy[1]))
                        text = str(text)
                        ann_vals.append((xytext, xy, text, float(arc)))
                    except Exception:
                        pass
            # Fallback parsing if nothing appended
            if len(ann_vals) == added_before:
                for (
                    (x1_expr, y1_expr),
                    (x2_expr, y2_expr),
                    text_s,
                    arc_expr,
                ) in _annotate_fallback_parse(str(a)):
                    try:
                        x1 = _eval_expr(x1_expr)
                        y1 = _eval_expr(y1_expr)
                    except Exception:
                        continue
                    try:
                        x2 = _eval_expr(x2_expr)
                        y2 = _eval_expr(y2_expr)
                    except Exception:
                        continue
                    # arc expression optional
                    arc_val = 0.3
                    if arc_expr:
                        try:
                            arc_val = _eval_expr(arc_expr)
                        except Exception:
                            try:
                                arc_val = float(arc_expr)
                            except Exception:
                                pass
                    ann_vals.append(
                        (
                            (float(x1), float(y1)),
                            (float(x2), float(y2)),
                            str(text_s),
                            float(arc_val),
                        )
                    )

        # Text: x, y, text, optional positioning, optional bbox flag
        # Accepted forms:
        #  - [x, y, text]
        #  - [x, y, text, pos]
        #  - [x, y, text, bbox]  # where bbox can be 'bbox' or a boolean (true/false)
        #  - [x, y, text, pos, bbox]
        # CSV fallback supports the same arities; for 4 tokens, the 4th can be pos or bbox
        text_vals: List[Tuple[float, float, str, str, bool]] = []
        for t in lists.get("text", []):
            lit = _safe_literal(t)
            if isinstance(lit, (list, tuple)) and (3 <= len(lit) <= 5):
                try:
                    # Allow expressions for x and y
                    x = _eval_expr(str(lit[0]))
                    y = _eval_expr(str(lit[1]))
                    text = str(lit[2])
                    pos = "top-left"
                    bbox_flag = False
                    if len(lit) == 4:
                        token = lit[3]
                        # If token is an explicit bbox flag
                        if isinstance(token, str) and token.strip().lower() == "bbox":
                            bbox_flag = True
                        else:
                            b = _parse_bool(token, default=None)
                            if isinstance(b, bool):
                                bbox_flag = bool(b)
                            else:
                                pos = str(token)
                    elif len(lit) == 5:
                        pos = str(lit[3])
                        token = lit[4]
                        if isinstance(token, str) and token.strip().lower() == "bbox":
                            bbox_flag = True
                        else:
                            b = _parse_bool(token, default=None)
                            if isinstance(b, bool):
                                bbox_flag = bool(b)
                    text_vals.append((x, y, text, pos, bbox_flag))
                    continue
                except Exception:
                    pass
            # Fallback: allow unquoted tokens like top-left using a CSV-style parse
            try:
                import csv

                s = str(t).strip()
                # strip surrounding brackets/parentheses if present
                if (s.startswith("[") and s.endswith("]")) or (
                    s.startswith("(") and s.endswith(")")
                ):
                    s = s[1:-1]
                # parse as a single CSV row
                row = next(csv.reader([s], skipinitialspace=True))
                if len(row) in (3, 4, 5):
                    # Evaluate x,y as expressions
                    x = _eval_expr(row[0].strip())
                    y = _eval_expr(row[1].strip())
                    text = row[2].strip()
                    pos_keys = {
                        "top-left",
                        "top-right",
                        "bottom-left",
                        "bottom-right",
                        "top-center",
                        "bottom-center",
                        "center-left",
                        "center-right",
                    }
                    pos = "top-left"
                    bbox_flag = False
                    if len(row) == 4:
                        tok = row[3].strip()
                        if tok.lower() in pos_keys:
                            pos = tok
                        else:
                            if tok.strip().lower() == "bbox":
                                bbox_flag = True
                            else:
                                b = _parse_bool(tok, default=None)
                                if isinstance(b, bool):
                                    bbox_flag = bool(b)
                                else:
                                    # treat as position if not a boolean
                                    pos = tok
                    elif len(row) == 5:
                        pos = row[3].strip()
                        tok = row[4].strip()
                        if tok.strip().lower() == "bbox":
                            bbox_flag = True
                        else:
                            b = _parse_bool(tok, default=None)
                            if isinstance(b, bool):
                                bbox_flag = bool(b)
                    text_vals.append((x, y, text, pos, bbox_flag))
            except Exception:
                pass

        # vlines: x[, ymin, ymax][, linestyle][, color] (style/color any order)
        vline_vals: List[
            Tuple[float, float | None, float | None, str | None, str | None]
        ] = []
        _allowed_styles = {"solid", "dotted", "dashed", "dashdot"}
        for v in lists.get("vline", []):
            lit = _safe_literal(v)
            tokens: List[str] = []
            if isinstance(lit, (list, tuple)):
                tokens = [str(x).strip() for x in lit]
            else:
                tokens = [p.strip() for p in str(v).split(",") if p.strip()]

            nums: List[float] = []  # evaluated numeric tokens (expressions allowed)
            extras: List[str] = []  # potential style/color tokens
            for t in tokens:
                # Attempt expression evaluation (supports arithmetic & function labels)
                try:
                    val = _eval_expr(t)
                    nums.append(val)
                    continue
                except Exception:
                    pass
                extras.append(t)
            x_val: float | None = None
            y0_val: float | None = None
            y1_val: float | None = None
            if len(nums) >= 1:
                x_val = nums[0]
            if len(nums) >= 3:
                y0_val, y1_val = nums[1], nums[2]

            style: str | None = None
            color: str | None = None
            for e in extras:
                el = e.lower()
                if el in _allowed_styles and style is None:
                    style = e
                elif color is None:
                    color = e
            if x_val is not None:
                vline_vals.append((x_val, y0_val, y1_val, style, color))

        # polygons: (x,y), (x,y), ... [ , show_vertices]
        # Extended: each coordinate may be an expression with user function calls.
        poly_vals: List[Tuple[List[Tuple[float, float]], bool]] = []

        # We avoid a complex fragile regex here and instead perform a small
        # balanced-parentheses scan so expressions like (2*sqrt(5), f(3+pi/4)) work.
        def _extract_coord_pairs(seq: str) -> List[Tuple[str, str]]:
            pairs: List[Tuple[str, str]] = []
            i = 0
            n = len(seq)
            while i < n:
                if seq[i] == "(":  # potential tuple start
                    depth = 0
                    j = i
                    while j < n:
                        ch = seq[j]
                        if ch == "(":
                            depth += 1
                        elif ch == ")":
                            depth -= 1
                            if depth == 0:
                                inner = seq[i + 1 : j].strip()
                                # split inner on a top-level comma
                                depth2 = 0
                                comma_index = -1
                                for k, ch2 in enumerate(inner):
                                    if ch2 == "(":
                                        depth2 += 1
                                    elif ch2 == ")":
                                        depth2 -= 1
                                    elif ch2 == "," and depth2 == 0:
                                        comma_index = k
                                        break
                                if comma_index != -1:
                                    x_expr = inner[:comma_index].strip()
                                    y_expr = inner[comma_index + 1 :].strip()
                                    if x_expr and y_expr:
                                        pairs.append((x_expr, y_expr))
                                i = j  # jump to end of tuple
                                break
                        j += 1
                i += 1
            return pairs

        for p in lists.get("polygon", []):
            s = str(p).strip()
            show_vertices = False
            if re.search(r"(^|,)\s*show_vertices\s*(?=,|$)", s, flags=re.IGNORECASE):
                show_vertices = True
                s = re.sub(
                    r"(^|,)\s*show_vertices\s*(?=,|$)", ",", s, flags=re.IGNORECASE
                )
                s = re.sub(r",{2,}", ",", s).strip().strip(",")
            pts: List[Tuple[float, float]] = []
            for x_expr, y_expr in _extract_coord_pairs(s):
                try:
                    xv = _eval_expr(x_expr)
                    yv = _eval_expr(y_expr)
                    pts.append((xv, yv))
                except Exception:
                    # Ignore malformed or unevaluable pair
                    pass
            if pts:
                poly_vals.append((pts, show_vertices))

        # Re-introduce a plain numeric tuple matcher for other primitives still expecting numeric-only coordinates.
        tup_pat = re.compile(
            r"\(\s*([+-]?\d+(?:\.\d+)?)\s*,\s*([+-]?\d+(?:\.\d+)?)\s*\)"
        )

        # bar: (x, y), length, orientation
        # Accept both literal list/tuple and CSV-like fallback
        bar_vals: List[Tuple[Tuple[float, float], float, str]] = []
        for b in lists.get("bar", []):
            lit = _safe_literal(b)
            if isinstance(lit, (list, tuple)) and len(lit) >= 3:
                try:
                    xy_raw, length_raw, orient_raw = lit[0], lit[1], lit[2]
                    xy = (float(xy_raw[0]), float(xy_raw[1]))
                    length = float(length_raw)
                    orientation = str(orient_raw).strip().lower()
                    if orientation in {"h", "hor", "horiz", "horizontal"}:
                        orientation = "horizontal"
                    elif orientation in {"v", "vert", "vertical"}:
                        orientation = "vertical"
                    bar_vals.append((xy, length, orientation))
                    continue
                except Exception:
                    pass
            # Fallback CSV: (x,y), length, orientation
            try:
                import csv as _csv

                s = str(b).strip()
                # Attempt to peel off the first tuple
                m = tup_pat.search(s)
                if not m:
                    continue
                x = float(m.group(1))
                y = float(m.group(2))
                # Remove tuple substring, then split the rest by commas
                a, c = m.span()
                rest = (s[:a] + s[c:]).strip()
                parts = [p.strip() for p in rest.split(",") if p.strip()]
                if len(parts) >= 2:
                    length = float(parts[0])
                    orientation = parts[1].strip().lower()
                    if orientation in {"h", "hor", "horiz", "horizontal"}:
                        orientation = "horizontal"
                    elif orientation in {"v", "vert", "vertical"}:
                        orientation = "vertical"
                    bar_vals.append(((x, y), length, orientation))
            except Exception:
                pass

        hline_vals: List[
            Tuple[float, float | None, float | None, str | None, str | None]
        ] = []
        for h in lists.get("hline", []):
            lit = _safe_literal(h)
            tokens_h: List[str] = []
            if isinstance(lit, (list, tuple)):
                tokens_h = [str(x).strip() for x in lit]
            else:
                tokens_h = [p.strip() for p in str(h).split(",") if p.strip()]

            nums_h: List[float] = []  # numeric (expressions) for y, x0, x1
            extras_h: List[str] = []  # style/color tokens
            for t in tokens_h:
                try:
                    val = _eval_expr(t)
                    nums_h.append(val)
                    continue
                except Exception:
                    pass
                extras_h.append(t)
            y_val: float | None = None
            x0_val: float | None = None
            x1_val: float | None = None
            if len(nums_h) >= 1:
                y_val = nums_h[0]
            if len(nums_h) >= 3:
                x0_val, x1_val = nums_h[1], nums_h[2]

            style_h: str | None = None
            color_h: str | None = None
            for e in extras_h:
                el = e.lower()
                if el in _allowed_styles and style_h is None:
                    style_h = e
                elif color_h is None:
                    color_h = e
            if y_val is not None:
                hline_vals.append((y_val, x0_val, x1_val, style_h, color_h))

        # lines: a, b, color, linestyle OR a, (x, y), color, linestyle
        # color and linestyle optional and order-independent; linestyle defaults to dashed
        line_vals: List[Tuple[float, float, str | None, str | None]] = (
            []
        )  # (a, b, style, color)
        _allowed_styles_line = {"solid", "dotted", "dashed", "dashdot"}

        def _split_top_level_line(val: str) -> List[str]:
            s = str(val or "").strip()
            if not s:
                return []
            if (s.startswith("[") and s.endswith("]")) or (
                s.startswith("(") and s.endswith(")")
            ):
                s = s[1:-1].strip()
            out: List[str] = []
            cur: List[str] = []
            depth = 0
            for ch in s:
                if ch in "([{":
                    depth += 1
                    cur.append(ch)
                elif ch in ")]}":
                    depth = max(0, depth - 1)
                    cur.append(ch)
                elif ch == "," and depth == 0:
                    part = "".join(cur).strip()
                    if part:
                        out.append(part)
                    cur = []
                else:
                    cur.append(ch)
            tail = "".join(cur).strip()
            if tail:
                out.append(tail)
            return out

        num_re_line = r"[+-]?\d+(?:\.\d+)?"
        tup_pat_line = re.compile(rf"\(\s*({num_re_line})\s*,\s*({num_re_line})\s*\)")
        for l in lists.get("line", []):
            a_val: float | None = None
            b_val: float | None = None
            style_line: str | None = None
            color_line: str | None = None
            lit_line = _safe_literal(l)
            if isinstance(lit_line, (list, tuple)) and len(lit_line) >= 2:
                try:
                    a_val = float(lit_line[0])
                except Exception:
                    a_val = None
                second = lit_line[1]
                if isinstance(second, (list, tuple)) and len(second) == 2:
                    try:
                        x0p = float(second[0])
                        y0p = float(second[1])
                        if a_val is not None:
                            b_val = y0p - a_val * x0p
                    except Exception:
                        pass
                else:
                    try:
                        b_val = float(second)
                    except Exception:
                        pass
                for extra in list(lit_line[2:]):
                    if isinstance(extra, str):
                        e = extra.strip().strip("\"'")
                        if e.lower() in _allowed_styles_line and style_line is None:
                            style_line = e.lower()
                        elif color_line is None:
                            color_line = e
                if a_val is not None and b_val is not None:
                    line_vals.append((a_val, b_val, style_line, color_line))
                    continue
            parts = _split_top_level_line(str(l))
            if len(parts) >= 2:
                try:
                    a_val = float(parts[0])
                except Exception:
                    a_val = None
                mpt = tup_pat_line.match(parts[1])
                if mpt is not None:
                    try:
                        x0p = float(mpt.group(1))
                        y0p = float(mpt.group(2))
                        if a_val is not None:
                            b_val = y0p - a_val * x0p
                    except Exception:
                        pass
                else:
                    try:
                        b_val = float(parts[1])
                    except Exception:
                        pass
                for extra in parts[2:]:
                    e = str(extra).strip().strip("\"'")
                    if e.lower() in _allowed_styles_line and style_line is None:
                        style_line = e.lower()
                    elif color_line is None:
                        color_line = e
                if a_val is not None and b_val is not None:
                    line_vals.append((a_val, b_val, style_line, color_line))

        # fill-polygons: (x,y), (x,y), ... [, color] [, alpha]
        # Extended: coordinate expressions support arithmetic & function calls like polygons.
        # Defaults: color -> plotmath.COLORS.get("blue"), alpha -> 0.1
        poly_fill_vals: List[
            Tuple[List[Tuple[float, float]], str | None, float | None]
        ] = []
        for fp in lists.get("fill-polygon", []):
            s = str(fp).strip()
            pts_fp: List[Tuple[float, float]] = []
            # Reuse polygon balanced-parentheses extractor defined earlier.
            # We reconstruct remaining extras by removing the matched tuple spans.
            consumed: List[Tuple[int, int]] = []
            for x_expr, y_expr in _extract_coord_pairs(s):
                # Find the substring to mark as consumed (naively search first occurrence of '(' + content + ')')
                pattern = f"({x_expr},{y_expr})"  # simplified; if spaces existed they were stripped
                # We'll just evaluate; for extras we approximate removal by replacing once later.
                try:
                    xv = _eval_expr(x_expr)
                    yv = _eval_expr(y_expr)
                    pts_fp.append((xv, yv))
                except Exception:
                    pass
            # Remove coordinate tuples crudely: replace occurrences of '(...)' that correspond to points
            rest = s
            # Simple loop removing parenthesized pairs counted earlier; risk: may remove unrelated parentheses if same text repeats
            # but acceptable for directive usage.
            # A safer approach would replicate extraction with span tracking; to keep patch minimal we do a regex wipe of tuples.
            rest = re.sub(r"\([^()]*?,[^()]*?\)", "", rest)
            rest = re.sub(r",{2,}", ",", rest)
            extras = [tok.strip() for tok in rest.split(",") if tok.strip()]
            color_fp: str | None = None
            alpha_fp: float | None = None
            # Interpret extras in any order: first numeric -> alpha, first non-numeric -> color
            for tok in extras:
                if alpha_fp is None:
                    try:
                        alpha_fp = _eval_expr(tok)
                        continue
                    except Exception:
                        pass
                if color_fp is None:
                    color_fp = tok
                # Stop early if both parsed
                if color_fp is not None and alpha_fp is not None:
                    break
            if pts_fp:
                poly_fill_vals.append((pts_fp, color_fp, alpha_fp))

        # line-segment: (x1,y1), (x2,y2)[, linestyle][, color]  (style/color optional, any order)
        line_segment_vals: List[
            Tuple[Tuple[float, float], Tuple[float, float], str | None, str | None]
        ] = []
        _allowed_seg_styles = {"solid", "dotted", "dashed", "dashdot"}
        for ls in lists.get("line-segment", []):
            s = str(ls).strip()
            # Use the same balanced extractor as polygons but ensure exactly two points are taken.
            pairs = _extract_coord_pairs(s)
            if len(pairs) < 2:
                continue
            pcoords: List[Tuple[float, float]] = []
            for x_expr, y_expr in pairs[:2]:
                try:
                    xv = _eval_expr(x_expr)
                    yv = _eval_expr(y_expr)
                    pcoords.append((float(xv), float(yv)))
                except Exception:
                    pcoords = []
                    break
            if len(pcoords) != 2:
                continue
            # Precisely remove the first two top-level tuples (with balanced parentheses)
            spans: List[Tuple[int, int]] = []
            depth = 0
            i = 0
            n = len(s)
            while i < n and len(spans) < 2:
                if s[i] == "(":
                    depth = 1
                    j = i + 1
                    while j < n and depth > 0:
                        if s[j] == "(":
                            depth += 1
                        elif s[j] == ")":
                            depth -= 1
                        j += 1
                    if depth == 0:
                        # captured tuple from i to j
                        inner = s[i + 1 : j - 1]
                        # verify it contains a top-level comma (treat as coordinate tuple)
                        d2 = 0
                        has_comma = False
                        for ch in inner:
                            if ch == "(":
                                d2 += 1
                            elif ch == ")":
                                d2 -= 1
                            elif ch == "," and d2 == 0:
                                has_comma = True
                                break
                        if has_comma:
                            spans.append((i, j))
                    i = j
                else:
                    i += 1
            # Build rest excluding spans
            if spans:
                parts_rest: List[str] = []
                last = 0
                for a, b in spans:
                    if a > last:
                        parts_rest.append(s[last:a])
                    last = b
                if last < len(s):
                    parts_rest.append(s[last:])
                rest = "".join(parts_rest)
            else:
                rest = s
            rest = re.sub(r",{2,}", ",", rest)
            tokens = [
                tok.strip().strip("'\"") for tok in rest.split(",") if tok.strip()
            ]
            style_seg: str | None = None
            color_seg: str | None = None
            for tok in tokens:
                low = tok.lower()
                if low in _allowed_seg_styles and style_seg is None:
                    style_seg = low
                    continue
                if color_seg is None:
                    # Accept token as color (will map later during draw)
                    color_seg = tok
            line_segment_vals.append((pcoords[0], pcoords[1], style_seg, color_seg))

        # axis commands: allow repeated keys like axis: equal / axis: off
        axis_cmds: List[str] = []
        for a in lists.get("axis", []):
            s = str(a).strip()
            # Allow comma-separated in one line as a convenience
            parts = [part.strip() for part in s.split(",") if part.strip()]
            for part in parts:
                # strip optional quotes
                if (part.startswith("'") and part.endswith("'")) or (
                    part.startswith('"') and part.endswith('"')
                ):
                    part = part[1:-1].strip()
                if part:
                    axis_cmds.append(part)

        # vectors: x, y, dx, dy[, color] with expression support
        vector_vals: List[Tuple[float, float, float, float, str]] = []
        for vline in lists.get("vector", []):
            s = str(vline).strip()
            # allow surrounding brackets/parentheses
            if (s.startswith("[") and s.endswith("]")) or (
                s.startswith("(") and s.endswith(")")
            ):
                s = s[1:-1].strip()
            # split by top-level commas (vectors unlikely to embed parentheses beyond simple expressions, but keep safe)
            depth_vec = 0
            cur_tok: List[str] = []
            parts: List[str] = []
            for ch in s:
                if ch == "(":
                    depth_vec += 1
                    cur_tok.append(ch)
                elif ch == ")":
                    depth_vec -= 1
                    cur_tok.append(ch)
                elif ch == "," and depth_vec == 0:
                    tok = "".join(cur_tok).strip()
                    if tok:
                        parts.append(tok)
                    cur_tok = []
                else:
                    cur_tok.append(ch)
            tail_tok = "".join(cur_tok).strip()
            if tail_tok:
                parts.append(tail_tok)
            if len(parts) < 4:
                continue
            try:
                x_v = float(_eval_expr(parts[0]))
                y_v = float(_eval_expr(parts[1]))
                dx_v = float(_eval_expr(parts[2]))
                dy_v = float(_eval_expr(parts[3]))
                color_v = parts[4] if len(parts) >= 5 and parts[4] else "black"
                vector_vals.append((x_v, y_v, dx_v, dy_v, color_v))
            except Exception:
                # skip silently to preserve robustness
                continue

        # angle-arc: (x, y), radius, start_angle_deg, end_angle_deg[, linestyle][, color]
        # Expression support for center, radius and angles; optional linestyle/color tokens in any order after the first three numeric expressions.
        angle_arcs: List[
            Tuple[float, float, float, float, float, str | None, str | None]
        ] = []
        _allowed_arc_styles = {"solid", "dotted", "dashed", "dashdot"}
        for arc in lists.get("angle-arc", []):
            raw_arc = str(arc).strip()
            # Find first balanced parenthesis group for center
            idx_arc = raw_arc.find("(")
            if idx_arc == -1:
                continue
            depth_arc = 0
            end_center = -1
            for j in range(idx_arc, len(raw_arc)):
                ch = raw_arc[j]
                if ch == "(":
                    depth_arc += 1
                elif ch == ")":
                    depth_arc -= 1
                    if depth_arc == 0:
                        end_center = j
                        break
            if end_center == -1:
                continue
            center_inner = raw_arc[idx_arc + 1 : end_center]
            # Split center_inner by top-level comma
            depth_c = 0
            cur_bits: List[str] = []
            center_parts: List[str] = []
            for ch in center_inner:
                if ch == "(":
                    depth_c += 1
                    cur_bits.append(ch)
                elif ch == ")":
                    depth_c -= 1
                    cur_bits.append(ch)
                elif ch == "," and depth_c == 0:
                    token = "".join(cur_bits).strip()
                    if token:
                        center_parts.append(token)
                    cur_bits = []
                else:
                    cur_bits.append(ch)
            tail_cp = "".join(cur_bits).strip()
            if tail_cp:
                center_parts.append(tail_cp)
            if len(center_parts) != 2:
                continue
            rest_arc = raw_arc[end_center + 1 :].lstrip(",").strip()
            if not rest_arc:
                continue
            # Split rest by top-level commas
            depth_r = 0
            cur_r: List[str] = []
            tokens_r: List[str] = []
            for ch in rest_arc:
                if ch == "(":
                    depth_r += 1
                    cur_r.append(ch)
                elif ch == ")":
                    depth_r -= 1
                    cur_r.append(ch)
                elif ch == "," and depth_r == 0:
                    tk = "".join(cur_r).strip()
                    if tk:
                        tokens_r.append(tk)
                    cur_r = []
                else:
                    cur_r.append(ch)
            tail_r = "".join(cur_r).strip()
            if tail_r:
                tokens_r.append(tail_r)
            if len(tokens_r) < 3:
                continue
            radius_expr = tokens_r[0]
            start_expr = tokens_r[1]
            end_expr = tokens_r[2]
            style_arc: str | None = None
            color_arc: str | None = None
            for extra_tok in tokens_r[3:]:
                low = extra_tok.lower()
                if low in _allowed_arc_styles and style_arc is None:
                    style_arc = low
                elif color_arc is None:
                    color_arc = extra_tok
            try:
                cx_val = float(_eval_expr(center_parts[0]))
                cy_val = float(_eval_expr(center_parts[1]))
                r_val = float(_eval_expr(radius_expr))
                if r_val <= 0:
                    continue
                start_deg_val = float(_eval_expr(start_expr))
                end_deg_val = float(_eval_expr(end_expr))
                angle_arcs.append(
                    (
                        cx_val,
                        cy_val,
                        r_val,
                        start_deg_val,
                        end_deg_val,
                        style_arc,
                        color_arc,
                    )
                )
            except Exception:
                continue

        # circles: (x,y), radius[, linestyle][, color]  (style/color optional, any order)
        # Accept expressions for x, y, radius. Optional tokens may appear in any order
        # after the radius token. Supported linestyles: solid, dotted, dashed, dashdot.
        circle_vals: List[Tuple[float, float, float, str | None, str | None]] = []
        _allowed_circle_styles = {"solid", "dotted", "dashed", "dashdot"}
        for c in lists.get("circle", []):
            raw = str(c).strip()
            # Expect something like: (expr_x, expr_y), radius_expr
            # We'll find first balanced tuple then split remaining by comma for radius.
            idx = raw.find("(")
            if idx == -1:
                continue
            # Grab balanced tuple
            depth = 0
            end_idx = -1
            for j in range(idx, len(raw)):
                if raw[j] == "(":
                    depth += 1
                elif raw[j] == ")":
                    depth -= 1
                    if depth == 0:
                        end_idx = j
                        break
            if end_idx == -1:
                continue
            inner = raw[idx + 1 : end_idx]
            # split inner into x,y
            depth2 = 0
            comma_i = -1
            for k, ch in enumerate(inner):
                if ch == "(":
                    depth2 += 1
                elif ch == ")":
                    depth2 -= 1
                elif ch == "," and depth2 == 0:
                    comma_i = k
                    break
            if comma_i == -1:
                continue
            x_expr = inner[:comma_i].strip()
            y_expr = inner[comma_i + 1 :].strip()
            # Remaining after tuple for radius
            rest = raw[end_idx + 1 :].strip().lstrip(",").strip()
            if not rest:
                continue
            # Split rest into top-level comma tokens (radius + optional style/color)
            depth3 = 0
            tokens: List[str] = []
            cur: List[str] = []
            for ch in rest:
                if ch == "(":
                    depth3 += 1
                    cur.append(ch)
                elif ch == ")":
                    depth3 -= 1
                    cur.append(ch)
                elif ch == "," and depth3 == 0:
                    part = "".join(cur).strip()
                    if part:
                        tokens.append(part)
                    cur = []
                else:
                    cur.append(ch)
            tail = "".join(cur).strip()
            if tail:
                tokens.append(tail)
            if not tokens:
                continue
            r_token = tokens[0]
            style_circle: str | None = None
            color_circle: str | None = None
            for tok in tokens[1:]:
                low = tok.lower()
                if low in _allowed_circle_styles and style_circle is None:
                    style_circle = low
                elif color_circle is None:
                    color_circle = tok
            try:
                xv = _eval_expr(x_expr)
                yv = _eval_expr(y_expr)
                rv = _eval_expr(r_token)
                if rv <= 0:
                    continue
                circle_vals.append(
                    (float(xv), float(yv), float(rv), style_circle, color_circle)
                )
            except Exception:
                # Silently skip invalid circle
                pass

        # ellipses: (x0,y0), a, b[, linestyle][, color]
        # Parameterization: x = x0 + a*cos(t), y = y0 + b*sin(t), t in [0, 2*pi]
        ellipse_vals: List[
            Tuple[float, float, float, float, str | None, str | None]
        ] = []
        _allowed_ellipse_styles = _allowed_circle_styles
        for e in lists.get("ellipse", []):
            raw = str(e).strip()
            idx = raw.find("(")
            if idx == -1:
                continue
            depth = 0
            end_idx = -1
            for j in range(idx, len(raw)):
                if raw[j] == "(":
                    depth += 1
                elif raw[j] == ")":
                    depth -= 1
                    if depth == 0:
                        end_idx = j
                        break
            if end_idx == -1:
                continue
            inner = raw[idx + 1 : end_idx]
            # split inner center on top-level comma
            depth2 = 0
            comma_i = -1
            for k, ch in enumerate(inner):
                if ch == "(":
                    depth2 += 1
                elif ch == ")":
                    depth2 -= 1
                elif ch == "," and depth2 == 0:
                    comma_i = k
                    break
            if comma_i == -1:
                continue
            x0_expr = inner[:comma_i].strip()
            y0_expr = inner[comma_i + 1 :].strip()
            rest = raw[end_idx + 1 :].strip().lstrip(",").strip()
            if not rest:
                continue
            # tokenize rest top-level commas
            depth3 = 0
            tokens: List[str] = []
            cur: List[str] = []
            for ch in rest:
                if ch == "(":
                    depth3 += 1
                    cur.append(ch)
                elif ch == ")":
                    depth3 -= 1
                    cur.append(ch)
                elif ch == "," and depth3 == 0:
                    part = "".join(cur).strip()
                    if part:
                        tokens.append(part)
                    cur = []
                else:
                    cur.append(ch)
            tail = "".join(cur).strip()
            if tail:
                tokens.append(tail)
            if len(tokens) < 2:  # need a and b at least
                continue
            a_expr = tokens[0]
            b_expr = tokens[1]
            style_e: str | None = None
            color_e: str | None = None
            for tok in tokens[2:]:
                low = tok.lower()
                if low in _allowed_ellipse_styles and style_e is None:
                    style_e = low
                elif color_e is None:
                    color_e = tok
            try:
                x0v = _eval_expr(x0_expr)
                y0v = _eval_expr(y0_expr)
                av = _eval_expr(a_expr)
                bv = _eval_expr(b_expr)
                if av <= 0 or bv <= 0:
                    continue
                ellipse_vals.append(
                    (float(x0v), float(y0v), float(av), float(bv), style_e, color_e)
                )
            except Exception:
                pass

        explicit_name = merged.get("name")
        debug_mode = "debug" in merged
        # curves: x_expr, y_expr, (t_start, t_end)[, linestyle][, color]
        curve_specs: List[Tuple[str, str, float, float, str | None, str | None]] = []
        _allowed_curve_styles = {"solid", "dotted", "dashed", "dashdot"}
        for c_line in lists.get("curve", []):
            s_line = str(c_line).strip()
            # Split top-level commas
            depth_c = 0
            parts_c: List[str] = []
            cur_c: List[str] = []
            for ch in s_line:
                if ch == "(":
                    depth_c += 1
                    cur_c.append(ch)
                elif ch == ")":
                    depth_c -= 1
                    cur_c.append(ch)
                elif ch == "," and depth_c == 0:
                    token = "".join(cur_c).strip()
                    if token:
                        parts_c.append(token)
                    cur_c = []
                else:
                    cur_c.append(ch)
            tail_c = "".join(cur_c).strip()
            if tail_c:
                parts_c.append(tail_c)
            if len(parts_c) < 3:
                continue
            x_expr_c = parts_c[0]
            y_expr_c = parts_c[1]
            interval_token = parts_c[2]
            m_iv = re.match(r"^\(\s*(.+?)\s*,\s*(.+?)\s*\)$", interval_token)
            if not m_iv:
                continue
            t0_expr = m_iv.group(1)
            t1_expr = m_iv.group(2)
            style_cur: str | None = None
            color_cur: str | None = None
            for tok in parts_c[3:]:
                low = tok.lower()
                if low in _allowed_curve_styles and style_cur is None:
                    style_cur = low
                elif color_cur is None:
                    color_cur = tok
            try:
                t0_val = _eval_expr(t0_expr)
                t1_val = _eval_expr(t1_expr)
                if t1_val < t0_val:
                    t0_val, t1_val = t1_val, t0_val
                curve_specs.append(
                    (
                        x_expr_c,
                        y_expr_c,
                        float(t0_val),
                        float(t1_val),
                        style_cur,
                        color_cur,
                    )
                )
            except Exception:
                continue

        # Parse figsize early (string like (6,4) or [6,4]) but apply at end
        def _parse_figsize(val: Any):
            if not isinstance(val, str):
                return None
            s = val.strip()
            if not s:
                return None
            lit = _safe_literal(s)
            if isinstance(lit, (list, tuple)) and len(lit) >= 2:
                try:
                    w = float(lit[0])
                    h = float(lit[1])
                    if w > 0 and h > 0:
                        return (w, h)
                except Exception:
                    return None
            # fallback simple regex (a,b)
            m = re.match(
                r"\(\s*([0-9]+(?:\.[0-9]+)?)\s*,\s*([0-9]+(?:\.[0-9]+)?)\s*\)", s
            )
            if m:
                try:
                    w = float(m.group(1))
                    h = float(m.group(2))
                    if w > 0 and h > 0:
                        return (w, h)
                except Exception:
                    return None
            return None

        parsed_figsize = _parse_figsize(figsize_raw)

        # Hash includes all content affecting the image
        content_hash = _hash_key(
            "|".join(fn_exprs),
            "|".join(fn_labels_list),
            "|".join(["" if d is None else f"{d[0]},{d[1]}" for d in fn_domains_list]),
            "|".join([("|".join([str(x) for x in exs])) for exs in fn_exclusions_list]),
            ";".join([f"{x},{y}" for x, y in point_vals]),
            ";".join(
                [
                    f"{xt[0]},{xt[1]}->{xy[0]},{xy[1]}:{t}:{arc}"
                    for (xt, xy, t, arc) in ann_vals
                ]
            ),
            ";".join(
                [
                    (f"{x}" if y0 is None or y1 is None else f"{x},{y0},{y1}")
                    + f":{st or ''}:{col or ''}"
                    for (x, y0, y1, st, col) in vline_vals
                ]
            ),
            ";".join(
                [
                    (f"{y}" if x0 is None or x1 is None else f"{y},{x0},{x1}")
                    + f":{st or ''}:{col or ''}"
                    for (y, x0, x1, st, col) in hline_vals
                ]
            ),
            ";".join(
                [
                    f"{int(show)}:" + "|".join([f"{x},{y}" for (x, y) in pts])
                    for (pts, show) in poly_vals
                ]
            ),
            ";".join(
                [
                    (color or "")
                    + ":"
                    + ("" if alpha is None else str(alpha))
                    + ":"
                    + "|".join([f"{x},{y}" for (x, y) in pts])
                    for (pts, color, alpha) in poly_fill_vals
                ]
            ),
            ";".join(
                [
                    f"{p1[0]},{p1[1]}->{p2[0]},{p2[1]}:{(st or '')}:{(col or '')}"
                    for (p1, p2, st, col) in line_segment_vals
                ]
            ),
            ";".join(
                [
                    f"{cx},{cy}:{r}:{sa}:{ea}:{(st or '')}:{(col or '')}"
                    for (cx, cy, r, sa, ea, st, col) in angle_arcs
                ]
            ),
            ";".join(
                [
                    f"{xy[0]},{xy[1]}:{length}:{orientation}"
                    for (xy, length, orientation) in bar_vals
                ]
            ),
            ";".join(
                [f"{x},{y}:{dx},{dy}:{col}" for (x, y, dx, dy, col) in vector_vals]
            ),
            "|".join(axis_cmds),
            ";".join(
                [f"{a},{b}:{(st or '')}:{(col or '')}" for (a, b, st, col) in line_vals]
            ),
            ";".join(
                [
                    f"{x},{y}:{txt}:{pos}:{int(1 if bbox else 0)}"
                    for (x, y, txt, pos, bbox) in text_vals
                ]
            ),
            "|".join(fn_colors_list),
            xmin,
            xmax,
            ymin,
            ymax,
            xstep,
            ystep,
            fontsize,
            lw,
            alpha,
            str(merged.get("xlabel", "")),
            str(merged.get("ylabel", "")),
            int(bool(ticks_flag)),
            int(bool(grid_flag)),
            str(merged.get("xticks", "")),
            str(merged.get("yticks", "")),
            str(parsed_figsize),
        )
        base_name = explicit_name or f"plot_{content_hash}"

        rel_dir = os.path.join("_static", "plot")
        abs_dir = os.path.join(app.srcdir, rel_dir)
        os.makedirs(abs_dir, exist_ok=True)
        svg_name = f"{base_name}.svg"
        abs_svg = os.path.join(abs_dir, svg_name)

        regenerate = ("nocache" in merged) or not os.path.exists(abs_svg)
        if regenerate:
            import matplotlib

            matplotlib.use("Agg")
            try:
                # Determine axis flags early
                axis_off = any(str(c).lower() == "off" for c in axis_cmds)
                axis_equal = any(str(c).lower() == "equal" for c in axis_cmds)

                if axis_off:
                    # Create a plain figure/axes (no plotmath.plot) so nothing (ticks/grid)
                    # is drawn before we hide the axes.
                    import matplotlib.pyplot as _plt

                    fig, ax = _plt.subplots()
                    # Provide a reasonable default size similar to plotmath defaults
                    fig.set_size_inches(6.0, 6.0)
                    ax.set_xlim(xmin, xmax)
                    ax.set_ylim(ymin, ymax)
                    # Hide coordinate system
                    try:
                        ax.axis("off")
                    except Exception:
                        pass
                    # Apply equal aspect if requested
                    if axis_equal:
                        try:
                            ax.axis("equal")
                        except Exception:
                            pass
                else:
                    # Standard path: delegate axis setup (ticks, grid, labels) to plotmath
                    fig, ax = plotmath.plot(
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
                        lw=lw,
                        alpha=alpha,
                        fontsize=fontsize,
                    )
                    # If equal requested (without off), apply after plot creation
                    if axis_equal:
                        try:
                            ax.axis("equal")
                        except Exception:
                            pass

                # Plot requested functions directly on ax, with optional labels, per-function domains, and exclusions
                if functions:
                    import numpy as np

                    any_label = False
                    for f, lbl, dom, exs, col_fun in zip(
                        functions,
                        fn_labels_list,
                        fn_domains_list,
                        fn_exclusions_list,
                        fn_colors_list,
                    ):
                        x0, x1 = dom if dom is not None else (xmin, xmax)
                        N = int(2**12)
                        x = np.linspace(x0, x1, N)
                        y = f(x)
                        # Ensure float array and blank out non-finite values
                        y = np.asarray(y, dtype=float)
                        y[~np.isfinite(y)] = np.nan
                        # More robust exclusion handling: blank a window around each excluded x
                        exs_in = [e for e in exs if x0 < e < x1]
                        if exs_in and N > 1:
                            dx = (x1 - x0) / (N - 1)
                            # Window width larger than step to ensure a gap; include tiny absolute floor
                            w = max(4 * dx, 1e-6 * (1.0 + max(abs(e) for e in exs_in)))
                            for e in exs_in:
                                try:
                                    mask = np.abs(x - e) <= w
                                    if mask.any():
                                        y[mask] = np.nan
                                    # Also blank the nearest index and a couple of neighbors to guarantee a break
                                    j = int(np.argmin(np.abs(x - e)))
                                    for k in (j - 2, j - 1, j, j + 1, j + 2):
                                        if 0 <= k < y.size:
                                            y[k] = np.nan
                                except Exception:
                                    # Last resort: nearest index only
                                    try:
                                        j = int(np.argmin(np.abs(x - e)))
                                        if 0 <= j < y.size:
                                            y[j] = np.nan
                                    except Exception:
                                        pass
                        # Additionally, break lines across steep jumps or extreme values
                        # Determine a reasonable y-span for thresholds
                        y_span = (
                            abs(ymax - ymin)
                            if (ymax is not None and ymin is not None)
                            else np.nan
                        )
                        if not (isinstance(y_span, (int, float)) and y_span > 0):
                            finite_y = y[np.isfinite(y)]
                            if finite_y.size > 0:
                                y_span = float(
                                    np.nanmax(finite_y) - np.nanmin(finite_y)
                                )
                        if not (isinstance(y_span, (int, float)) and y_span > 0):
                            y_span = 1.0
                        # Break where adjacent points jump too much relative to span
                        jump_factor = 0.5  # half the axis span signals discontinuity
                        finite_pair = np.isfinite(y[:-1]) & np.isfinite(y[1:])
                        big_jump = finite_pair & (
                            np.abs(y[1:] - y[:-1]) > (jump_factor * y_span)
                        )
                        if big_jump.any():
                            idx_break = np.where(big_jump)[0]
                            for i_b in idx_break:
                                if 0 <= i_b + 1 < y.size:
                                    y[i_b + 1] = np.nan
                        # Mask values far outside typical range to avoid vertical spikes drawing across
                        mag_factor = 50.0
                        too_big = np.isfinite(y) & (np.abs(y) > (mag_factor * y_span))
                        if too_big.any():
                            y[too_big] = np.nan
                        # Resolve per-function color if provided
                        _col_use = None
                        if isinstance(col_fun, str) and col_fun.strip():
                            try:
                                _col_map = plotmath.COLORS.get(col_fun)
                            except Exception:
                                _col_map = None
                            _col_use = _col_map if _col_map else col_fun

                        if lbl:
                            any_label = True
                            ax.plot(
                                x,
                                y,
                                lw=lw,
                                alpha=alpha,
                                label=f"${lbl}$",
                                **({"color": _col_use} if _col_use else {}),
                            )
                        else:
                            ax.plot(
                                x,
                                y,
                                lw=lw,
                                alpha=alpha,
                                **({"color": _col_use} if _col_use else {}),
                            )
                    if any_label:
                        ax.legend(fontsize=int(fontsize))

                # Annotations
                for xytext, xy, text, arc in ann_vals:
                    plotmath.annotate(
                        xy=xy, xytext=xytext, s=text, arc=arc, fontsize=int(fontsize)
                    )

                # Lines (y = a*x + b); draw before points so markers remain visible
                if line_vals:
                    import numpy as _np_l

                    style_map_line = {
                        "solid": "-",
                        "dotted": ":",
                        "dashed": "--",
                        "dashdot": "-.",
                    }
                    default_color_line = plotmath.COLORS.get("red")
                    try:
                        from matplotlib import colors as _mcolors
                    except Exception:
                        _mcolors = None
                    x_line = _np_l.array([xmin, xmax], dtype=float)
                    for a_l, b_l, st_l, col_l in line_vals:
                        y_line = a_l * x_line + b_l
                        ls = style_map_line.get((st_l or "dashed").lower(), "--")
                        # Resolve color via plotmath.COLORS if provided; fallback to original token then default
                        if col_l:
                            _mapped = plotmath.COLORS.get(col_l)
                        else:
                            _mapped = None
                        col_use = (_mapped if _mapped else col_l) or default_color_line
                        if _mcolors is not None:
                            try:
                                _ = _mcolors.to_rgba(col_use)
                            except Exception:
                                col_use = default_color_line
                        try:
                            ax.plot(
                                x_line,
                                y_line,
                                linestyle=ls,
                                color=col_use,
                                lw=lw,
                                alpha=alpha,
                            )
                        except Exception:
                            ax.plot(
                                x_line,
                                y_line,
                                linestyle=ls,
                                color=default_color_line,
                                lw=lw,
                                alpha=alpha,
                            )

                # Bars
                for xy, length, orientation in bar_vals:
                    try:
                        # Prefer plotmath.make_bar if available
                        if hasattr(plotmath, "make_bar"):
                            plotmath.make_bar(xy, length, orientation)
                        else:
                            # Fallback: use annotate directly on this axes
                            x, y = xy
                            if orientation == "horizontal":
                                ax.annotate(
                                    "",
                                    xy=xy,
                                    xycoords="data",
                                    xytext=(x + length, y),
                                    textcoords="data",
                                    arrowprops=dict(
                                        arrowstyle="|-|,widthA=0.5,widthB=0.5",
                                        color="black",
                                    ),
                                )
                            else:
                                ax.annotate(
                                    "",
                                    xy=xy,
                                    xycoords="data",
                                    xytext=(x, y + length),
                                    textcoords="data",
                                    arrowprops=dict(
                                        arrowstyle="|-|,widthA=0.5,widthB=0.5",
                                        color="black",
                                    ),
                                )
                    except Exception:
                        pass

                # Angle arcs
                if "angle_arcs" in locals() and angle_arcs:
                    try:
                        import numpy as _np_ang
                    except Exception:
                        _np_ang = None
                    if _np_ang is not None:
                        style_map_arc = {
                            "solid": "-",
                            "dotted": ":",
                            "dashed": "--",
                            "dashdot": "-.",
                        }
                        default_arc_color = plotmath.COLORS.get("black") or "black"
                        for cx, cy, r, sa_deg, ea_deg, st_a, col_a in angle_arcs:
                            try:
                                sa = _np_ang.deg2rad(sa_deg)
                                ea = _np_ang.deg2rad(ea_deg)
                                theta = _np_ang.linspace(sa, ea, 1024)
                                xs = cx + r * _np_ang.cos(theta)
                                ys = cy + r * _np_ang.sin(theta)
                                ls_use = style_map_arc.get(
                                    (st_a or "solid").lower(), "-"
                                )
                                # Resolve color via plotmath palette
                                if col_a:
                                    _mapped = plotmath.COLORS.get(col_a)
                                else:
                                    _mapped = None
                                col_use = (
                                    _mapped if _mapped else col_a
                                ) or default_arc_color
                                ax.plot(xs, ys, lw=1, color=col_use, linestyle=ls_use)
                            except Exception:
                                pass

                # text with optional positioning and optional bbox

                xmin, xmax = ax.get_xlim()
                ymin, ymax = ax.get_ylim()
                ax_dx = xmax - xmin
                ax_dy = ymax - ymin

                # Determine axes pixel size for consistent visual offsets
                try:
                    fig.canvas.draw()  # ensure layout is realized
                    _bbox_px = ax.get_window_extent()
                    _ax_w_px, _ax_h_px = _bbox_px.width, _bbox_px.height
                    if _ax_w_px <= 0 or _ax_h_px <= 0:
                        _ax_w_px = _ax_h_px = None
                except Exception:
                    _ax_w_px = _ax_h_px = None

                for x0, y0, text, pos, use_bbox in text_vals:
                    va, ha = _parse_text_positioning(pos)
                    # Factors as fractions of axes size; keep long* ~3.3x larger
                    _fx_short = 0.015
                    _fy_short = 0.015
                    _fx_long = 0.03
                    _fy_long = 0.03

                    # Resolve long* into base alignment while keeping larger factors
                    _use_fx = _fx_short
                    _use_fy = _fy_short
                    if va == "longbottom":
                        va = "bottom"
                        _use_fy = _fy_long
                    elif va == "longtop":
                        va = "top"
                        _use_fy = _fy_long
                    if ha == "longright":
                        ha = "right"
                        _use_fx = _fx_long
                    elif ha == "longleft":
                        ha = "left"
                        _use_fx = _fx_long

                    if _ax_w_px and _ax_h_px:
                        # Pixel-based offsets converted back to data units
                        dx_px = 0.0
                        dy_px = 0.0
                        if ha == "right":
                            dx_px = -_ax_w_px * _use_fx
                        elif ha == "left":
                            dx_px = _ax_w_px * _use_fx
                        if va == "bottom":
                            dy_px = _ax_h_px * _use_fy
                        elif va == "top":
                            dy_px = -_ax_h_px * _use_fy
                        x_disp, y_disp = ax.transData.transform((x0, y0))
                        x1, y1 = ax.transData.inverted().transform(
                            (x_disp + dx_px, y_disp + dy_px)
                        )
                        dx = x1 - x0
                        dy = y1 - y0
                    else:
                        # Fallback to fractions of data span
                        if va == "bottom":
                            dy = (
                                _fy_short * ax_dy
                                if _use_fy == _fy_short
                                else _fy_long * ax_dy
                            )
                        elif va == "top":
                            dy = -(
                                _fy_short * ax_dy
                                if _use_fy == _fy_short
                                else _fy_long * ax_dy
                            )
                        else:
                            dy = 0.0
                        if ha == "right":
                            dx = -(
                                _fx_short * ax_dx
                                if _use_fx == _fx_short
                                else _fx_long * ax_dx
                            )
                        elif ha == "left":
                            dx = (
                                _fx_short * ax_dx
                                if _use_fx == _fx_short
                                else _fx_long * ax_dx
                            )
                        else:
                            dx = 0.0

                    bbox_kwargs = (
                        dict(
                            boxstyle="round,pad=0.4",
                            fc="white",
                            ec="black",
                            lw=1.5,
                            alpha=0.7,
                        )
                        if use_bbox
                        else None
                    )

                    if bbox_kwargs:
                        ax.text(
                            x0 + 1.5 * dx,
                            y0 + 1.5 * dy,
                            text,
                            fontsize=int(fontsize),
                            ha=ha,
                            va=va,
                            bbox=bbox_kwargs,
                        )
                    else:
                        ax.text(
                            x0 + dx, y0 + dy, text, fontsize=int(fontsize), ha=ha, va=va
                        )

                # line segments (draw before vlines/hlines so guides overlay if needed)
                if "line_segment_vals" in locals() and line_segment_vals:
                    style_map_seg = {
                        "solid": "-",
                        "dotted": ":",
                        "dashed": "--",
                        "dashdot": "-.",
                    }
                    default_seg_color = plotmath.COLORS.get("red")
                    try:
                        from matplotlib import colors as _mcolors_seg
                    except Exception:
                        _mcolors_seg = None
                    for p1, p2, st_seg, col_seg in line_segment_vals:
                        (x1s, y1s), (x2s, y2s) = p1, p2
                        ls_use = style_map_seg.get((st_seg or "solid").lower(), "-")
                        if col_seg:
                            _mapped_seg = plotmath.COLORS.get(col_seg)
                        else:
                            _mapped_seg = None
                        col_use = (
                            _mapped_seg if _mapped_seg else col_seg
                        ) or default_seg_color
                        if _mcolors_seg is not None:
                            try:
                                _ = _mcolors_seg.to_rgba(col_use)
                            except Exception:
                                col_use = default_seg_color
                        try:
                            ax.plot(
                                [x1s, x2s],
                                [y1s, y2s],
                                linestyle=ls_use,
                                color=col_use,
                                lw=lw,
                            )
                        except Exception:
                            pass
                # Circles
                if "circle_vals" in locals() and circle_vals:
                    try:
                        from matplotlib import patches as _mpatches_c
                    except Exception:
                        _mpatches_c = None
                    if _mpatches_c is not None:
                        style_map_circle = {
                            "solid": "-",
                            "dotted": ":",
                            "dashed": "--",
                            "dashdot": "-.",
                        }
                        default_circle_color = plotmath.COLORS.get("black") or "black"
                        for cx, cy, r_c, st_c, col_c in circle_vals:
                            try:
                                # Resolve color
                                if col_c:
                                    mapped = plotmath.COLORS.get(col_c)
                                else:
                                    mapped = None
                                col_use = (
                                    mapped if mapped else col_c
                                ) or default_circle_color
                                # Resolve linestyle -> we pass as linestyle on patch edge
                                ls_use = style_map_circle.get(
                                    (st_c or "solid").lower(), "-"
                                )
                                circ = _mpatches_c.Circle(
                                    (cx, cy),
                                    r_c,
                                    fill=False,
                                    edgecolor=col_use,
                                    facecolor="none",
                                    linestyle=ls_use,
                                    lw=lw,
                                )
                                ax.add_patch(circ)
                            except Exception:
                                pass
                # Ellipses
                if "ellipse_vals" in locals() and ellipse_vals:
                    try:
                        import numpy as _np_el
                    except Exception:
                        _np_el = None
                    if _np_el is not None:
                        style_map_ellipse = {
                            "solid": "-",
                            "dotted": ":",
                            "dashed": "--",
                            "dashdot": "-.",
                        }
                        default_ellipse_color = plotmath.COLORS.get("black") or "black"
                        for x0e, y0e, a_e, b_e, st_e, col_e in ellipse_vals:
                            try:
                                t = _np_el.linspace(0, 2 * _np_el.pi, 1024)
                                xs = x0e + a_e * _np_el.cos(t)
                                ys = y0e + b_e * _np_el.sin(t)
                                if col_e:
                                    mapped = plotmath.COLORS.get(col_e)
                                else:
                                    mapped = None
                                col_use = (
                                    mapped if mapped else col_e
                                ) or default_ellipse_color
                                ls_use = style_map_ellipse.get(
                                    (st_e or "solid").lower(), "-"
                                )
                                ax.plot(xs, ys, color=col_use, linestyle=ls_use, lw=lw)
                            except Exception:
                                pass

                # Curves (parametric x(t), y(t))
                if "curve_specs" in locals() and curve_specs:
                    try:
                        import sympy as _sp_curve
                        import numpy as _np_curve
                    except Exception:
                        _sp_curve = None
                        _np_curve = None
                    if _sp_curve is not None and _np_curve is not None:
                        style_map_curve = {
                            "solid": "-",
                            "dotted": ":",
                            "dashed": "--",
                            "dashdot": "-.",
                        }
                        default_curve_color = plotmath.COLORS.get("black") or "black"
                        for x_expr_s, y_expr_s, t0_c, t1_c, st_c, col_c in curve_specs:
                            try:
                                t_sym = _sp_curve.symbols("t")
                                # Sympify with local symbol t; rely on SymPy's safe parsing (no arbitrary exec)
                                x_sym = _sp_curve.sympify(x_expr_s, locals={"t": t_sym})
                                y_sym = _sp_curve.sympify(y_expr_s, locals={"t": t_sym})
                                fx = _sp_curve.lambdify(t_sym, x_sym, "numpy")
                                fy = _sp_curve.lambdify(t_sym, y_sym, "numpy")
                                t_arr = _np_curve.linspace(t0_c, t1_c, 1024)
                                xs = fx(t_arr)
                                ys = fy(t_arr)
                                # Basic sanity checks
                                try:
                                    _ = len(xs)
                                    _ = len(ys)
                                except Exception:
                                    continue
                                mapped = plotmath.COLORS.get(col_c) if col_c else None
                                col_use = (
                                    mapped if mapped else col_c
                                ) or default_curve_color
                                ls_use = style_map_curve.get(
                                    (st_c or "solid").lower(), "-"
                                )
                                ax.plot(xs, ys, color=col_use, linestyle=ls_use, lw=lw)
                            except Exception:
                                continue

                # vlines
                style_map = {
                    "solid": "-",
                    "dotted": ":",
                    "dashed": "--",
                    "dashdot": "-.",
                }
                default_color = plotmath.COLORS.get("red")
                for x_v, y0, y1, st, col in vline_vals:
                    y_min = ymin if y0 is None else y0
                    y_max = ymax if y1 is None else y1
                    ls_val = style_map.get((st or "dashed").lower(), ":")
                    # Resolve user color through plotmath.COLORS, then fallback to original, then default
                    _mapped = plotmath.COLORS.get(col) if col else None
                    color_to_try = (_mapped if _mapped else col) or default_color
                    try:
                        ax.vlines(
                            x=x_v,
                            ymin=y_min,
                            ymax=y_max,
                            colors=color_to_try,
                            lw=lw,
                            alpha=1,
                            ls=ls_val,
                        )
                    except Exception:
                        ax.vlines(
                            x=x_v,
                            ymin=y_min,
                            ymax=y_max,
                            colors=default_color,
                            lw=lw,
                            alpha=1,
                            ls=ls_val,
                        )

                # hlines
                for y_h, x0, x1, st_h, col_h in hline_vals:
                    x_min = xmin if x0 is None else x0
                    x_max = xmax if x1 is None else x1
                    ls_val_h = style_map.get((st_h or "dashed").lower(), ":")
                    # Resolve user color through plotmath.COLORS, then fallback to original, then default
                    _mapped_h = plotmath.COLORS.get(col_h) if col_h else None
                    color_to_try_h = (
                        _mapped_h if _mapped_h else col_h
                    ) or default_color
                    try:
                        ax.hlines(
                            y=y_h,
                            xmin=x_min,
                            xmax=x_max,
                            colors=color_to_try_h,
                            lw=lw,
                            alpha=1,
                            ls=ls_val_h,
                        )
                    except Exception:
                        ax.hlines(
                            y=y_h,
                            xmin=x_min,
                            xmax=x_max,
                            colors=default_color,
                            lw=lw,
                            alpha=1,
                            ls=ls_val_h,
                        )

                # polygons
                for pts, show in poly_vals:
                    kwargs = {"show_vertices": True} if show else {}
                    try:
                        plotmath.polygon(*pts, **kwargs)
                    except Exception:
                        # ignore to avoid breaking the build on a single bad polygon
                        pass

                # filled polygons
                default_fill_color = plotmath.COLORS.get("blue")
                for pts, color_fp, alpha_fp in poly_fill_vals:
                    # Resolve user color through plotmath.COLORS, then fallback to original, then default
                    if color_fp:
                        _mapped_fp = plotmath.COLORS.get(color_fp)
                    else:
                        _mapped_fp = None
                    c = (_mapped_fp if _mapped_fp else color_fp) or default_fill_color
                    a = 0.1 if alpha_fp is None else alpha_fp
                    try:
                        plotmath.polygon(*pts, edges=False, color=c, alpha=a)
                    except Exception:
                        try:
                            plotmath.polygon(*pts, edges=False, facecolor=c, alpha=a)
                        except Exception:
                            plotmath.polygon(*pts, edges=False, alpha=a)

                # Vectors (quiver) drawn before points so markers overlay arrow heads
                if vector_vals:
                    default_vector_color = plotmath.COLORS.get("black") or "black"
                    try:
                        for x_v, y_v, dx_v, dy_v, col_v in vector_vals:
                            # Resolve color through palette first
                            if col_v:
                                _mapped_vec = plotmath.COLORS.get(col_v)
                            else:
                                _mapped_vec = None
                            color_use = (
                                _mapped_vec if _mapped_vec else col_v
                            ) or default_vector_color
                            ax.quiver(
                                x_v,
                                y_v,
                                dx_v,
                                dy_v,
                                angles="xy",
                                scale_units="xy",
                                scale=1,
                                width=0.0065,
                                headwidth=4,
                                headlength=4.5,
                                color=color_use,
                            )
                    except Exception:
                        pass

                # Plot points
                for x0, y0 in point_vals:
                    ax.plot(x0, y0, "o", markersize=10, alpha=0.8, color="black")

                # axis commands (run sequentially) — retain for legacy commands; we
                # skip reapplying 'off'/'equal' earlier logic is already applied but
                # they are harmless if repeated.
                for cmd in axis_cmds:
                    try:
                        ax.axis(cmd)
                    except Exception:
                        pass

                # Axis labels: allow optional labelpad via "label, pad"
                def _split_label_and_pad(val: Any) -> tuple[str | None, float | None]:
                    if not isinstance(val, str):
                        return None, None
                    s = val.strip()
                    if not s:
                        return None, None
                    # Try literal form [label, pad] or (label, pad)
                    lit = _safe_literal(s)
                    if isinstance(lit, (list, tuple)) and len(lit) >= 1:
                        label = str(lit[0]).strip()
                        pad: float | None = None
                        if len(lit) >= 2:
                            try:
                                pad = float(lit[1])
                            except Exception:
                                pad = None
                        return (label if label else None), pad
                    # CSV fallback: split on last comma so labels with commas still work when quoted
                    parts = [p.strip() for p in s.split(",")]
                    if len(parts) >= 2:
                        try:
                            pad = float(parts[-1])
                            label = ",".join(parts[:-1]).strip()
                            return (label if label else None), pad
                        except Exception:
                            pass
                    return (s if s else None), None

                xl_raw = merged.get("xlabel")
                yl_raw = merged.get("ylabel")
                xl_text, xl_pad = _split_label_and_pad(xl_raw)
                yl_text, yl_pad = _split_label_and_pad(yl_raw)

                if isinstance(yl_text, str) and yl_text.strip():
                    try:
                        kwargs = dict(
                            fontsize=int(fontsize), loc="top", rotation="horizontal"
                        )
                        if yl_pad is not None:
                            kwargs["labelpad"] = yl_pad
                        ax.set_ylabel(yl_text, **kwargs)
                    except Exception:
                        ax.set_ylabel(yl_text, fontsize=int(fontsize))
                if isinstance(xl_text, str) and xl_text.strip():
                    try:
                        kwargs = dict(fontsize=int(fontsize), loc="right")
                        if xl_pad is not None:
                            kwargs["labelpad"] = xl_pad
                        ax.set_xlabel(xl_text, **kwargs)
                    except Exception:
                        ax.set_xlabel(xl_text, fontsize=int(fontsize))

                # Apply user figsize at the very end if provided
                if parsed_figsize is not None:
                    try:
                        fig.set_size_inches(*parsed_figsize)
                    except Exception:
                        pass

                # Handle individual tick control (xticks/yticks off)
                xticks_raw = merged.get("xticks")
                yticks_raw = merged.get("yticks")

                if isinstance(xticks_raw, str) and xticks_raw.strip().lower() == "off":
                    try:
                        ax.set_xticks([])
                    except Exception:
                        pass

                if isinstance(yticks_raw, str) and yticks_raw.strip().lower() == "off":
                    try:
                        ax.set_yticks([])
                    except Exception:
                        pass

                # Apply tight_layout to prevent label clipping
                try:
                    fig.tight_layout()
                except Exception:
                    pass

                fig.savefig(
                    abs_svg,
                    format="svg",
                    transparent=True,
                )
                if debug_mode:
                    # Sidecar PDF (optional for debugging)
                    try:
                        fig.savefig(
                            os.path.join(abs_dir, f"{base_name}.pdf"),
                            format="pdf",
                            transparent=True,
                        )
                    except Exception:
                        pass

                matplotlib.pyplot.close(fig)
            except Exception as e:
                return [
                    self.state_machine.reporter.error(
                        f"Feil under generering av figur: {e}", line=self.lineno
                    )
                ]

        if not os.path.exists(abs_svg):
            return [
                self.state_machine.reporter.error(
                    "plot: SVG mangler.", line=self.lineno
                )
            ]

        env.note_dependency(abs_svg)
        # copy into build _static
        try:
            out_static = os.path.join(app.outdir, "_static", "plot")
            os.makedirs(out_static, exist_ok=True)
            shutil.copy2(abs_svg, os.path.join(out_static, svg_name))
        except Exception:
            pass

        try:
            raw_svg = open(abs_svg, "r", encoding="utf-8").read()
        except Exception as e:
            return [
                self.state_machine.reporter.error(
                    f"plot inline: kunne ikke lese SVG: {e}", line=self.lineno
                )
            ]

        if not debug_mode and "viewBox" in raw_svg:
            raw_svg = _strip_root_svg_size(raw_svg)

        if not debug_mode:
            raw_svg = _rewrite_ids(
                raw_svg, f"cpl_{content_hash}_{uuid.uuid4().hex[:6]}_"
            )

        alt_default = "Tilpasset figur"
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
        # Deliberately do not inject a <title> element: browsers display it as a tooltip
        # on hover which is distracting for readers. Accessibility is still ensured via
        # role="img" and aria-label attributes already added in _augment(). If a title
        # is ever desired for a specific figure, that can be added manually after build
        # or a future directive option could re-enable this behavior.

        figure = nodes.figure()
        figure.setdefault("classes", []).extend(
            ["adaptive-figure", "plot-figure", "no-click"]
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
    app.add_directive("plot", PlotDirective)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}

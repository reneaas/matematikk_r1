"""
Animate the bisection method on a given interval [a0, b0], using plotmath for axes and function.

Outputs a GIF (or MP4 fallback) to the corresponding 'figurer' directory when save=True.
"""

from __future__ import annotations

import os
import pathlib
from typing import Callable, List, Tuple

import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np
import plotmath


def _bisection_steps(
    f: Callable[[float], float],
    a: float,
    b: float,
    max_iters: int = 10,
    tol: float = 1e-10,
) -> List[Tuple[float, float, float]]:
    """Precompute (a, b, m) per iteration. Stops early if interval or |f(m)| is small."""
    steps: List[Tuple[float, float, float]] = []
    fa, fb = f(a), f(b)
    if fa == 0:
        return [(a, a, a)]
    if fb == 0:
        return [(b, b, b)]
    if fa * fb > 0:
        raise ValueError("[a,b] has no sign change: f(a)*f(b) > 0.")

    for _ in range(max_iters):
        m = 0.5 * (a + b)
        fm = f(m)
        steps.append((a, b, m))
        if abs(fm) < tol or abs(b - a) < tol:
            break
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm

    # Ensure the last state reflects the final midpoint
    if not steps or steps[-1][2] != 0.5 * (a + b):
        steps.append((a, b, 0.5 * (a + b)))
    return steps


def animate_bisection(
    f: Callable[[float], float] | None = None,
    a0: float = 0.0,
    b0: float = 2.0,
    max_iters: int = 9,
    fps: int = 1,
    save: bool = True,
    dirname: str | None = None,
) -> None:
    """Create and save (or show) an animation of the bisection method.

    If dirname is None and save=True, the output path is resolved by replacing
    the last 'koder' segment in the current file's directory with 'figurer'.
    """
    # Default function: matches the example in bisection_method.py
    if f is None:

        def f(x: float) -> float:
            return (x + 1) ** 2 - 3

    # Plot axes and function using plotmath
    fig, ax = plotmath.plot(
        functions=[f],
        fn_labels=True,
        xmin=-6,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=True,
        xstep=1,
        ystep=1,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=False,
        fontsize=20,
        figsize=None,
    )

    steps = _bisection_steps(f, a0, b0, max_iters=max_iters)

    # Visual elements: short vlines from x-axis up a small height, and markers at the axis
    a0_x, b0_x, m0_x = steps[0]
    small_h = 0.05 * (ax.get_ylim()[1] - ax.get_ylim()[0])
    # Line2D segments drawn with plot() so we can control y extents
    (a_line,) = ax.plot([a0_x, a0_x], [0, small_h], color="tab:red", ls="--", lw=2.5)
    (b_line,) = ax.plot([b0_x, b0_x], [0, small_h], color="tab:red", ls="--", lw=2.5)
    (m_line,) = ax.plot([m0_x, m0_x], [0, small_h], color="tab:green", lw=2.5)
    # Markers at (a,0), (b,0), (m,0)
    (a_pt,) = ax.plot([a0_x], [0], marker="o", color="tab:red", ms=6)
    (b_pt,) = ax.plot([b0_x], [0], marker="o", color="tab:red", ms=6)
    (m_pt,) = ax.plot([m0_x], [0], marker="o", color="tab:green", ms=6)

    def _init():
        a, b, m = steps[0]
        a_line.set_data([a, a], [0, small_h])
        b_line.set_data([b, b], [0, small_h])
        m_line.set_data([m, m], [0, small_h])
        a_pt.set_data([a], [0])
        b_pt.set_data([b], [0])
        m_pt.set_data([m], [0])
        return a_line, b_line, m_line, a_pt, b_pt, m_pt

    def _update(i: int):
        a, b, m = steps[i]
        a_line.set_data([a, a], [0, small_h])
        b_line.set_data([b, b], [0, small_h])
        m_line.set_data([m, m], [0, small_h])
        a_pt.set_data([a], [0])
        b_pt.set_data([b], [0])
        m_pt.set_data([m], [0])
        return a_line, b_line, m_line, a_pt, b_pt, m_pt

    anim = animation.FuncAnimation(
        fig,
        _update,
        init_func=_init,
        frames=len(steps),
        interval=1000,
        blit=False,
        repeat=False,
    )

    if save:
        # Resolve output directory
        if dirname is None:
            current_dir = str(pathlib.Path(__file__).resolve().parent)
            parts = current_dir.split("/")
            for i in range(len(parts)):
                if parts[~i] == "koder":
                    parts[~i] = "figurer"
                    break
            dirname = "/".join(parts)
        os.makedirs(dirname, exist_ok=True)
        outpath = os.path.join(dirname, "bisection_animation.gif")
        try:
            from matplotlib.animation import PillowWriter

            anim.save(outpath, writer=PillowWriter(fps=fps))
        except Exception:
            # Fallback to mp4 if Pillow not available or fails
            try:
                anim.save(outpath.replace(".gif", ".mp4"), writer="ffmpeg", fps=fps)
            except Exception as e2:
                raise RuntimeError(f"Could not save animation to GIF or MP4: {e2}")
    else:
        plotmath.show()


if __name__ == "__main__":
    # Default: save to the mirrored 'figurer' directory next to this file
    current_dir = str(pathlib.Path(__file__).resolve().parent)
    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break
    dirname = "/".join(parts)

    animate_bisection(a0=0.0, b0=2.0, max_iters=9, fps=1, save=True, dirname=dirname)

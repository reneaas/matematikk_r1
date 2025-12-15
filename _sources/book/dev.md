# Dev


::::{multi-plot2}
---
rows: 2
cols: 2
ymin: -20
ymax: 20
fontsize: 25
---


:::{plot}
function: 2*x - 3 + x**2 * exp(-x), A
ticks: off
:::


:::{plot}
function: -2*x + 3 + x**2 * exp(-x), B
ticks: off
:::


:::{plot}
function: -2*x + 3 - x**2 * exp(-x), C
ticks: off
:::


:::{plot}
function: 2*x - 3 - x**2 * exp(-x), D
ticks: off
:::




::::
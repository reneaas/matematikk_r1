# Dev

:::{plot}
width: 50%
axis: equal
axis: off
line-segment: (0, 1), (cos(-pi/6), sin(-pi/6)), blue
line-segment: (0, 1), (cos(pi + pi/6), sin(pi + pi/6)), blue
ellipse: (0, sin(-pi/6)), cos(-pi/6), 0.2, blue, dashed
line-segment: (0, sin(-pi/6)), (cos(-pi/6), sin(-pi/6)), black, solid
line-segment: (0, sin(-pi/6)), (0, 1), black, solid
text: 0.5 * cos(-pi/6), sin(-pi/6) - 0.1, "$r$", center-center
text: 0.1, 0.25, "$h$", center-center
text: 0.25, 0.15, "$9$", top-right
fontsize: 30
lw: 3
nocache:
:::



---


:::{plot}
width: 70%
function: exp(-2*x) - 2*x * exp(-2*x) + 2 * x * exp(-4*x) - 4 * x**2 * exp(-4*x), f'
ymin: -3
ymax: 3
xmin: -3
xmax: 3
ticks: off
:::



::::{multi-plot2}
---
rows: 2
cols: 2
---


:::{plot}
function: -4 * exp(-2*x) + 2* exp(-4*x) + 4*x * exp(-2*x) - 16 * x * exp(-4*x) + 16 * x**2 * exp(-4*x), A
ticks: off 
ymin: -3
ymax: 3
xmin: -3
xmax: 3
:::


:::{plot}
function: x * exp(-2*x) + x**2 * exp(-4*x), B 
ticks: off
ymin: -1
ymax: 1
xmin: -3
xmax: 3
:::


:::{plot}
function: -(-4 * exp(-2*x) + 2* exp(-4*x) + 4*x * exp(-2*x) - 16 * x * exp(-4*x) + 16 * x**2 * exp(-4*x)), C
ticks: off 
ymin: -3
ymax: 3
xmin: -3
xmax: 3
:::


:::{plot}
function: -(x * exp(-2*x) + x**2 * exp(-4*x)), D
ticks: off
ymin: -1
ymax: 1
xmin: -3
xmax: 3
:::







::::
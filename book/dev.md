# Dev

:::{plot}
width: 100%
function: -2 * sqrt(x + 4) + 3, [-4, 5), f, blue
function-endpoints: true
:::


:::{plot}
width: 100%
function: -1/2 * (x - 1)**3 + 1, [-1, 3), g, blue
function-endpoints: true
:::


:::{plot}
function: exp(-x) - 3, (-2, 3), blue
function-endpoints: true 
:::


:::{plot}
function: exp(-x**2 + 1), (-2, 2], blue
function-endpoints: true 
:::


:::{plot}
function: 2*cbrt(abs(x)) * sign(x), [-3, 3], blue
function-endpoints: true
:::


:::{plot}
function: -0.125 * x**3 + 1, (-3, 3], blue 
function-endpoints: true
:::


:::{plot}
width: 100%
function: 2*sqrt(x + 2) - 3, [-1, 2], blue
function: 0.5 * (x - 4)**2 + 1, (2, 4], blue
function-endpoints: true
xmin: -3
ymin: -3
:::








::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
xstep: 2
ystep: 2
xmin: -12
xmax: 12
ymin: -12
ymax: 12
---
:::{plot}
function: 2 * sqrt(2) * sqrt(8 - x) - 6, [-10, 8), blue
function-endpoints: true
text: 8, 10, "A", center-center, bbox
:::


:::{plot}
function: -6 + sqrt(8*x + 64), [-8, 10), blue
function-endpoints: true
text: 8, 10, "B", center-center, bbox
:::



:::{plot}
function: -1/8 * ((x + 6)**2 - 64), [-6, 6), blue
function-endpoints: true
text: 8, 10, "C", center-center, bbox
:::


:::{plot}
function: 1/8 * ((x + 6)**2 - 64), [-6, 6), blue
function-endpoints: true
text: 8, 10, "D", center-center, bbox
:::
::::




:::{signchart-2}
width: 80%
function: x * (x - b) * (x + a), f(x) 
:::

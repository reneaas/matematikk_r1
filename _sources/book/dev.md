# Dev

::::{multi-plot2}
---
rows: 1
cols: 2
---

:::{animate}
animate-var: a, 0, 10, 20
fps: 10
format: webp
function: sin(a*x)
xmin: -10
xmax: 10
ymin: -2
ymax: 2
grid: true
width: 100%
:::


:::{animate} 
animate-var: a, -4, 4, 128
fps: 16
format: webp
function: x**3 - 3*x + 2, f
ymin: -10
ymax: 10
xmin: -5
xmax: 5
point: (a, f(a))
tangent: a, f, solid, red
text: 2, -6, "a = {a:.2f}", center-center
width: 100%
:::
::::

---


:::{interactive-graph}
interactive-var: a, 0, 2*pi, 128
interactive-var-start: 0
xmin: -1.5
xmax: 1.5
ymin: -1.5
ymax: 1.5
curve: cos(t), sin(t), (0, a), solid, blue
point: (cos(a), sin(a))
text: 1, -1, "a = {a*180/pi:.2f}°", center-center
grid: true
width: 70%
:::





:::{interactive-graph}
interactive-var: a, -4, 4, 50
function: x**3 - 3*x + 2, f
ymin: -10
ymax: 10
xmin: -5
xmax: 5
point: (a, f(a))
tangent: a, f, solid, red
text: 2, -6, "a = {a:.2f}", center-center
grid: true
width: 70%
:::


## Multi Interactive Graph Test

::::{multi-interactive-graph}
---
rows: 1
cols: 2
interactive-var: a, -4, 4, 50
---

:::{interactive-graph}
function: x**3 - 3*x + 2, f
ymin: -10
ymax: 10
ystep: 2
xmin: -5
xmax: 5
point: (a, f(a))
tangent: a, f, solid, red
text: 2, -6, "a = {a:.2f}", center-center
grid: false
fontsize: 25
:::

:::{interactive-graph}
function: 3 * x**2 - 3, g
xmin: -5
xmax: 5
ymin: -6
ymax: 6
point: (a, g(a))
text: a, g(a), "({a:.2f}, {g(a):.2f})", bottom-right
grid: false
fontsize: 25
:::
::::


## Multi Interactive With 2x2 Grid

::::{multi-interactive-graph}
---
rows: 2
cols: 2
interactive-var: a, -3, 3, 40
---

:::{interactive-graph}
function: x**2 + a*x
xmin: -5
xmax: 5
ymin: -10
ymax: 10
grid: true
:::

:::{interactive-graph}
function: a*x**3
xmin: -3
xmax: 3
ymin: -10
ymax: 10
grid: true
:::

:::{interactive-graph}
function: sin(a*x)
xmin: -6.28
xmax: 6.28
ymin: -2
ymax: 2
grid: true
:::

:::{interactive-graph}
function: exp(a*x/5)
xmin: -5
xmax: 5
ymin: 0
ymax: 5
grid: true
:::
::::

---

## Test Comprehensive Math Functions

:::{interactive-graph}
interactive-var: a, 0, 2*pi, 50
interactive-var-start: pi/4
xmin: -pi
xmax: pi
ymin: -3
ymax: 3
curve: t, sinh(t), (-a, a), solid, purple
curve: t, cosh(t), (-a, a), dashed, green  
point: (a, sinh(a))
point: (a, cosh(a))
text: 0.5, 2, "a = {a:.2f}", center-center
grid: true
width: 80%
:::

Test with logarithms and exponentials:

:::{interactive-graph}
interactive-var: a, 0.1, 3, 40
interactive-var-start: 1
xmin: 0.01
xmax: 3
ymin: -2
ymax: 3
function: log(x)
function: exp(a*x), f
point: (a, f(a))
point: (a, log(a))
grid: true
width: 80%
:::



---


:::{interactive-graph} 
interactive-var: k, -2, 2, 64
interactive-var-start: -2
function: -x**2 + (2 + k) * x, (-10, k), blue
function: x**2 + (2 - k) * x, [k, 10), red
function-endpoints: true
ymin: -16
ymax: 16
yticks: off
grid: off
width: 80%
:::



:::::::::::::::{exercise} Oppgave X

::::{solution}
:::{interactive-graph} 
interactive-var: k, -2, 2, 64
interactive-var-start: -2
function: -x**2 + (2 + k) * x, (-10, k), blue
function: x**2 + (2 - k) * x, [k, 10), red
function-endpoints: true
ymin: -16
ymax: 16
yticks: off
grid: off
width: 80%
:::
::::
:::::::::::::::
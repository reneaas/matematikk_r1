# Dev


:::{plot}
width: 80%
function: x**2 * exp(-x), f
xmin: -2
xmax: 6
ymin: -0.2
ymax: 1.4
yticks: off
grid: false
nocache:
point: (0, f(0))
point: (2, f(2))
point: (2 + sqrt(2), f(2 + sqrt(2)))
point: (2 - sqrt(2), f(2 - sqrt(2)))
:::



:::{plot}
width: 80%
function: (2*x - x**2) * exp(-x), f'
xmin: -2
xmax: 6
ymin: -1.4
ymax: 1.4
point: (0, 0)
point: (2, 0)
point: (2 + sqrt(2), f'(2 + sqrt(2)))
point: (2 - sqrt(2), f'(2 - sqrt(2)))
yticks: off
grid: false
nocache:
:::


:::{plot}
width: 80%
function: (x**2 - 4*x + 2) * exp(-x), f''
xmin: -2
xmax: 6
ymin: -1.4
ymax: 1.4
yticks: off
grid: false
nocache:
point: (2 - sqrt(2), 0)
point: (2 + sqrt(2), 0)
:::



:::{plot}
width: 70%
function: (x**2 - 1) * exp(-x), A
xmin: -2
xmax: 6
ymin: -1.5
ymax: 1.5
grid: off
yticks: off
:::


:::{plot}
width: 70%
function: exp(-x) - 4 * x * exp(-x) + x**2 * exp(-x), B
xmin: -2
xmax: 6
ymin: -1.5
ymax: 1.5
grid: off
yticks: off
:::


:::{plot}
width: 70%
function: 2 * x * exp(-x) - exp(-x) * (x**2 - 1), C
xmin: -2
xmax: 6
ymin: -1.5
ymax: 1.5
grid: off
yticks: off
:::




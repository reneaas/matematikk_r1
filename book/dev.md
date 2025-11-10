# Dev

:::{plot}
width: 70%
function: sqrt(x**2 + 4) + sqrt((9 - x)**2 + 16), L, (0, 11)
xmin: -1
xmax: 10
ymin: -1
ymax: 24
ticks: off
figsize: (3.5, 4)
point: (3, L(3))
fontsize: 16
vline: 3, 0, L(3)
hline: L(3), 0, 3
text: 3, 0, $x_\mathrm{minst}$, bottom-center
text: 0, L(3), $L_\mathrm{minst}$, center-left
:::


:::{plot}
width: 70%
function: 10*x + x*sqrt(100 - x**2), A, (0, 10)
xmin: -0.5
xmax: 10.5
ymin: -0.5
ymax: 160
ticks: off
point: (8.66, A(8.66))
vline: 8.66, 0, A(8.66)
hline: A(8.66), 0, 8.66
text: 8.66, 0, $x_\mathrm{maks}$, bottom-center
text: 0, A(8.66), $A_\mathrm{maks}$, center-left
figsize: (4, 4)
fontsize: 16
:::



:::{plot}
width: 70%
function: x / (4*pi) * (sqrt(pi**2 * x**2 + 2*pi*100) - pi * x)**2, V, (0, 50)
xmin: -0.5
xmax: 30
ymin: -0.5
ymax: 100
ticks: off
xlabel: $h$
ylabel: $V(h)$
point: (4.61, V(4.61))
vline: 4.61, 0, V(4.61)
hline: V(4.61), 0, 4.61
text: 4.61, 0, $h_\mathrm{maks}$, bottom-center
text: 0, V(4.61), $V_\mathrm{maks}$, center-left
figsize: (6, 4)
:::


:::{plot}
width: 70%
function: x**3 * cbrt(abs(x - 1))**2, f, (-1, 2)
xmin: -0.1
xmax: 1.5
ymin: -0.1
ymax: 0.3
ticks: off
point: (1, f(1))
point: (9/11, f(9/11))
annotate: (0.2, f(9/11) + 0.05), (9/11, f(9/11)), "Lokalt toppunkt", -0.3
annotate: (0.2, f(1) - 0.1), (1, f(1)), "Lokalt bunnpunkt, men ikke deriverbar"
:::


:::{plot}
width: 70%
function: x**4 * exp(-x), f, (0, 100)
point: (2, f(2))
line: 2.17, -2.17
point: (6, f(6))
line: -1.07, 9.64
xmin: -1
xmax: 15
ymin: -1
ticks: off
:::


:::{polydiv}
---
p: x^3 - 8
q: x^2 - 4
width: 80%
---
:::


:::{polydiv}
---
p: x^2 + 2x - 3
q: x - 5
width: 80%
---
:::



:::{plot}
width: 70%
vline: 0, 0, 10, gray, solid
hline: 0, -1, 8, gray, solid
function: (-3/2)*x + 6, (0, 4)
vector: 0, 6, 0, -2, red
vector: 4, 0, 1.5, 0, red
ymax: 8
ymin: -1
xmin: -1
ticks: off 
axis: off
:::



:::{interactive-code}
def f(x):
    return x**3  - 3*x + 2

x = 2
y = f(x)

print(y)
:::









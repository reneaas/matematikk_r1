# Oversikt: Omvendte funksjoner

::::::::{grid} 1 1 2 2
---
gutter: 2
---
::::::{grid-item-card}
**Omvendte funksjoner**
^^^
**Definisjon**:
$f$ og $g$ er omvendte funksjoner hvis

$$
f(g(x)) = x \qog g(f(x)) = x
$$

**Finne den omvendte funksjonen**:
1. Løs likningen

$$
f(x) = y \liff x = g(y)
$$

2. Sett $f^{-1}(x) = g(x)$

**Definisjonsmengder og verdimengder**:
* Verdimengen til $f$ er lik definisjonsmengden til $f^{-1}$. Altså $V_f = D_{f^{-1}}$
* Definisjonsmengden til $f$ er lik verdimengden til $f^{-1}$. Altså $D_f = V_{f^{-1}}$
::::::


::::::{grid-item-card}
**Grafisk sammenheng**
^^^
* Grafen til $f$ og $f^{-1}$ er speilet om linja $y = x$
* Et punkt $(a, b)$ på grafen til $f$ tilsvarer punktet $(b, a)$ på grafen til $f^{-1}$
* $f(a) = b \liff f^{-1}(b) = a$

:::{plot}
width: 100%
function: x**3 + 1, f, (-2, 2], blue
function: (abs(x - 1))**(1/3) * (x - 1) / abs(x - 1), f^{-1}, (-7, 9], red
line: 1, 0, dashed, gray
xmin: -8
xmax: 11.5
ymin: -8
ymax: 10
point: (1.5, f(1.5))
point: (f(1.5), 1.5)
function-endpoints: true
ticks: off
text: 1.5, f(1.5), "$(a, b)$", top-right
text: f(1.5), 1.5, "$(b, a)$", top-right
fontsize: 25
:::


::::::


::::::{grid-item-card}
**Eksistens av omvendte funksjoner**
^^^
En funksjon $f$ med definisjonsmengde $D_f$ har en omvendt funksjon hvis (fra det strengeste kravet til det svakeste):
1. $f$ er 1-til-1 (også kalt *én-entydig*). For hver $y$-verdi finnes det bare én $x$-verdi slik at $f(x) = y$.
2. $f$ ikke har noen ekstremalpunkter på innsiden av $D_f$. Da er $f$ strengt voksende eller strengt avtangende på $D_f$. 


:::{plot}
fontsize: 25
width: 100%
xmin: -4
xmax: 4
ymin: -2
ymax: 1.2
ticks: off
function: (x - 1/2)**3 * exp(-(x - 1/2)**2 + 1) - 1/2, f, [(-sqrt(6) + 1)/2, (sqrt(6) + 1)/2], blue
function: (x - 1/2)**3 * exp(-(x - 1/2)**2 + 1) - 1/2, (-20, (-sqrt(6) + 1)/2), red
function: (x - 1/2)**3 * exp(-(x - 1/2)**2 + 1) - 1/2, ((sqrt(6) + 1)/2, 20) red
function-endpoints: true
nocache:

Den blå delen og den rød delen, utgjør hver siden del av grafen til $f$ som har en omvendt funksjon $f^{-1}$.
:::





::::::


::::::{grid-item-card}
**Den deriverte av en omvendt funksjon**
^^^
* Hvis et punkt $(a, b)$ ligger på grafen til $f$, så er 

$$
\left(f^{-1}\right)'(b) = \dfrac{1}{f'(a)}
$$

forutsatt at $f'(a) \neq 0$. 

* Hvis en tangent i punktet $(a, b)$ på grafen til $f$ har stigningstall $f'(a)$, så har en tangent til grafen til $f^{-1}$ i punktet $(b, a)$ stigningstall $\dfrac{1}{f'(a)}$


:::{plot}
function: x**2 + 1, f, (0, 2], blue
function: sqrt(x - 1), f^{-1}, (1, 5], red
function-endpoints: true
ticks: off
fontsize: 25
tangent: sqrt(2), f, dashed, gray
point: (sqrt(2), f(sqrt(2)))
text: sqrt(2), f(sqrt(2)), "$(a, b)$", center-right
tangent: 2, g, dashed, red
point: (f(sqrt(2)), sqrt(2))
text: f(sqrt(2)), sqrt(2), "$(b, a)$", top-center
line: 1/(2*sqrt(2)), (3, sqrt(2)), dashed, gray
xmin: -1
xmax: 6
ymin: -1
ymax: 6
annotate: (-2, 5), (sqrt(2), f(sqrt(2))), "Stigningstall: $f'(a)$"
annotate: (2, -2), (3, sqrt(2)), "Stigningstall: $\displaystyle \frac{1}{f'(a)}$"
:::

::::::








::::::::




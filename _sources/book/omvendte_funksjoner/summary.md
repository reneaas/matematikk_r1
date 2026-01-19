# Oppsummering: Omvendte funksjoner

::::::::{grid} 1 1 1 1
---
gutter: 2
---
::::::{grid-item-card}
**Definisjon**
^^^
$f$ og $g$ er omvendte funksjoner hvis

$$
f(g(x)) = x \qog g(f(x)) = x
$$

Vi skriver ofte at $g = f^{-1}$ som leses som "$f$-invers".

::::::


::::::{grid-item-card}
**Definisjonsmengde og verdimengde**
^^^
* Definisjonsmengden til $f$ er lik verdimengden til $f^{-1}$:

$$
D_f = V_{f^{-1}}
$$

* Verdimengden til $f$ er lik definisjonsmengden til $f^{-1}$:

$$
V_f = D_{f^{-1}}
$$

::::::


::::::{grid-item-card}
**Finne $f^{-1}(x)$**
^^^
1. Løs likningen $f(x) = y$ for $x$ slik at du får $x = g(y)$
2. Sett $f^{-1}(x) = g(x)$
::::::


::::::{grid-item-card}
**Grafisk sammenheng**
^^^

:::{plot}
width: 100%
align: right
figsize: (5, 4)
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

* Grafen til $f^{-1}$ er grafen til $f$ speilet om linja $y = x$.
* Hvis et punkt $(a, b)$ er på grafen til $f$, så er punktet $(b, a)$ på grafen til $f^{-1}$
* $f(a) = b \liff f^{-1}(b) = a$


::::::


::::::{grid-item-card}
**Eksistens av omvendte funksjoner**
^^^

:::{plot}
width: 100%
align: right
fontsize: 25
figsize: (5, 4)
xmin: -4
xmax: 4
ymin: -2
ymax: 1.2
ticks: off
function: (x - 1/2)**3 * exp(-(x - 1/2)**2 + 1) - 1/2, f, [(-sqrt(6) + 1)/2, (sqrt(6) + 1)/2], blue
function: (x - 1/2)**3 * exp(-(x - 1/2)**2 + 1) - 1/2, (-20, (-sqrt(6) + 1)/2), red
function: (x - 1/2)**3 * exp(-(x - 1/2)**2 + 1) - 1/2, ((sqrt(6) + 1)/2, 20) red
function-endpoints: true
:::

**Kontinuerlige og deriverbare funksjoner**:

Det finnes en omvendt funksjon til $f$ dersom:
* $f$ har ingen ekstremalpunkter på innsiden av definisjonsmengden $D_f$ (ingen topp- eller bunnpunkter).
* Grafen til $f$ snur aldri og er enten strengt voksende eller strengt avtakende på $D_f$ (monoton).

Den blå delen av grafen til $f$, og den røde delen av grafen til $f$, har hver sin del av definisjonsmengden der $f$ har en omvendt funksjon $f^{-1}$.



:::{plot}
fontsize: 25
width: 100%
align: right
function: -1/3 * (x + 5) + 3, [-5, -2), f, blue
function: (3*x + 4) / (x + 4), [-2, 4], blue
ymax: 4
ymin: -2
function-endpoints: true
:::

**Funksjoner med delt forskrift**:

For en funksjon $f$ med delt forskrift, har den en omvendt funksjon hvis 

* $f$ er **1-til-1** (også kalt én-entydig). For hver $y$-verdi finnes det bare én $x$-verdi slik at $f(x) = y$.
* Grafen til $f$ har bare ett skjæringspunkt med alle linjer $y = k$. 
::::::


::::::{grid-item-card}
**Den deriverte av en omvendt funksjon**
^^^

:::{plot}
width: 100%
align: right
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

* Hvis et punkt $(a, b)$ ligger på grafen til $f$, så er 

$$
\left(f^{-1}\right)'(b) = \dfrac{1}{f'(a)}
$$

forutsatt at $f'(a) \neq 0$. 

* Hvis en tangent i punktet $(a, b)$ på grafen til $f$ har stigningstall $f'(a)$, så har en tangent til grafen til $f^{-1}$ i punktet $(b, a)$ stigningstall $\dfrac{1}{f'(a)}$


::::::








::::::::




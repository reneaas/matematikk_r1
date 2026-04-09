# Formler

::::::::{grid}
---
gutter: 2
columns: 12
---
::::::{grid-item-card}
---
columns: 3
---
**Potensregler**
^^^
$$
\begin{align*}
    x^{p} \cdot x^q &= x^{p+q} \\
    \\
    \dfrac{x^{p}}{x^q} &= x^{p-q} \\
    \\
    (x^p)^q &= x^{p \cdot q} \\
    \\
    x^0 &= 1 \\
    \\
    x^{-p} &= \dfrac{1}{x^p} \\
\end{align*}
$$

::::::

::::::{grid-item-card}
**Logaritmeregler**
^^^
$$
\begin{align*}
    x &= \log_a y \liff y = a^x \\
    \\
    \log_a(xy) &= \log_a x + \log_a y \\
    \\
    \log_a\left(\dfrac{x}{y}\right) &= \log_a x - \log_a y \\
    \\
    \log_a(x^p) &= p \cdot \log_a x \\
    \\
    \log_a 1 &= 0 \\
\end{align*}
$$


::::::

::::::{grid-item-card}
**Derivasjonsregler**
^^^
$$
\begin{align*}
    (x^p)' &= p x^{p-1} \\
    \\
    (e^x)' &= e^x \\
    \\
    (\ln ax)' &= \dfrac{1}{x} \\
    \\
    (a^x)' &= a^x \ln a \\
    \\
    (\log_a x)' &= \dfrac{1}{x \ln a} \\
    \\
\end{align*}
$$
::::::

::::::{grid-item-card} 
**Derivasjonssetninger**
^^^
$$
\begin{align*}
    (fg)' &= f' g + f g' \\
    \\
    \left(\dfrac{f}{g}\right)' &= \dfrac{f' g - f g'}{g^2} \\
    \\
    \left(f(g(x))\right)' &= f'(g(x)) \cdot g'(x) \\
\end{align*}
$$

::::::

::::::{grid-item-card}
**Den deriverte og numerisk derivasjon**
^^^

$$
\begin{align*}
    f'(a) &= \lim_{x \to a} \dfrac{f(x) - f(a)}{x - a} \\
    \\
    f'(x) &= \lim_{h \to 0} \dfrac{f(x+h) - f(x)}{h} \\
    \\
    f'(x) &\approx \dfrac{f(x+h) - f(x)}{h} \\
\end{align*}
$$
::::::

::::::{grid-item-card}
**Funksjonsdrøfting**
^^^
Toppunkt $(m, f(m))$ 
: $f'(m) = 0$ og $f''(m) < 0$ 

Bunnpunkt $(m, f(m))$
: $f'(m) = 0$ og $f''(m) > 0$

Vendepunkt $(m, f(m))$
: $f''(m) = 0$ og $f''(x)$ skifter fortegn når $x$ går gjennom $m$
::::::


::::::{grid-item-card}
**Tangenter**
^^^

$$
y = f(a) + f'(a) \cdot (x - a)
$$


:::{plot}
width: 100%
function: x * exp(-x**2), f
tangent: 1, f
ticks: off
xmin: -1
xmax: 3
ymin: -0.2
ymax: 1
point: (1, f(1))
text: 1, f(1), "$(a, f(a))$", top-right
:::




::::::


::::::{grid-item-card}
**Grenseverdier**
^^^


Grunnleggende grenser
: $$
\begin{align*}
    \lim_{x\to \infty} e^x &= \infty && \lim_{x\to \infty} e^{-x} = 0 \\
    \\
    \lim_{x \to 0^+} \ln x &= -\infty && \lim_{x \to \infty} \ln x = \infty \\
\end{align*}
$$

L'Hopitals regel
: $$
\begin{align*}
    \lim_{x \to a} \dfrac{f(x)}{g(x)} &\overset{[\frac{0}{0}]}{=} \lim_{x \to a} \dfrac{f'(x)}{g'(x)} \\
    \\
    \lim_{x \to a} \dfrac{f(x)}{g(x)} &\overset{[\frac{\infty}{\infty}]}{=} \lim_{x \to a} \dfrac{f'(x)}{g'(x)} 
\end{align*}
$$

::::::



::::::{grid-item-card}
**Asymptoter**
^^^

:::{plot}
width: 100%
function: x + 1 - 1/(x + 1) + 1 / (x - 2)**2, (-1, 20)
function: (x - 1) / (x + 1), (-20, -1), blue
vline: -1
vline: 2
hline: 1
line: 1, 1
ticks: off
ymax: 10
xmin: -6
xmax: 6
:::

Skrå asymptote $y = ax + b$
: $\lim\limits_{x \to \pm \infty} \left(f(x) - (ax + b)\right) = 0$

Vertikal asymptote $x = a$
: $\lim\limits_{x \to a^{\pm}} f(x) = \pm \infty$

Horisontal asymptote $y = a$
: $\lim\limits_{x \to \pm \infty} f(x) = a$

::::::


::::::{grid-item-card}
**Kontinuitet og deriverbarhet**
^^^

Eksistens av grenseverdi
: $\lim\limits_{x \to a} f(x)$ finnes hvis $\lim\limits_{x \to a^-} f(x) = \lim\limits_{x \to a^+} f(x)$

Kontinuitet i $x = a$
: $\lim\limits_{x \to a} f(x) = f(a)$

Deriverbarhet i $x = a$
: $f'(a) = \lim\limits_{x \to a} \dfrac{f(x) - f(a)}{x - a}$ må eksistere

Funksjon med delt forskrift
: $
f(x) =
\begin{cases}
    g(x) & \qhvis x < a \\
    \\
    h(x) & \qhvis x \geq a
\end{cases}
$

: Kontinuerlig i $a$ hvis $g(a) = h(a)$
: Deriverbar i $a$ hvis kontinuerlig i $a$ og $g'(a) = h'(a)$

::::::


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
**Grafisk sammenheng mellom omvendte funksjoner**
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
---
columns: 6
---
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
---
columns: 6
---
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


::::::{grid-item-card}
**Vektorer**
^^^
:::{plot}
width: 100%
vector: 0, 0, 1, 2, blue
xmin: -0.1
xmax: 1.5
ymin: -0.2
ymax: 2.2
ticks: off
text: 0.5 * (1 + 0), 0.5 * (2 + 0), "$\vec{a}$", top-left
hline: 0, 0, 1, dashed, gray
vline: 1, 0, 2, dashed, gray
polygon: (1, 0), (0.9, 0), (0.9, 0.225), (1, 0.225)
axis: off
text: 0.5, 0, "$a_x$", bottom-center
text: 1, 1, "$a_y$", center-right
fontsize: 25
:::

$$
\vec{a} = [a_x, a_y]
$$

$$
\abs{\vec{a}} = \sqrt{a_x^2 + a_y^2}
$$

$$
k \vec{a} = [k a_x, k a_y]
$$

$$
\abs{k\vec{a}} = \abs{k} \abs{\vec{a}}
$$
::::::


::::::{grid-item-card}
**Posisjonsvektorer**
^^^
:::{plot}
width: 100%
vector: 0, 0, 1, 2, blue
point: (1, 2)
point: (0, 0)
text: 1, 2, "$P(x, y)$", top-right
text: 0, 0, "$O$", bottom-left
text: 0, 0, "$O$", bottom-left
xmin: -1
xmax: 2
ymin: -1
ymax: 3
ticks: off
text: 0.5 * (1 + 0), 0.5 * (2 + 0), "$\overrightarrow{OP}$", top-left
fontsize: 30
:::

$$
\lvec{OP} = [x, y]
$$

::::::

::::::{grid-item-card}
**Vektorer mellom punkter**
^^^

:::{plot}
width: 100%
vector: (1, 1), (3, 2), blue
vector: (0, 0), (1, 1), red
vector: (0, 0), (3, 2), red
point: (1, 1)
point: (3, 2)
text: 1, 1, "$A$", top-center
text: 3, 2, "$B$", top-right
text: 0.5 * (1 + 0), 0.5 * (1 + 0), "$\overrightarrow{OA}$", top-left
text: 0.5 * (3 + 0), 0.5 * (2 + 0), "$\overrightarrow{OB}$", bottom-right
text: 0.5 * (1 + 3), 0.5 * (1 + 2), "$\overrightarrow{AB}$", top-left
xmin: -0.5
xmax: 3.5
ymin: -1
ymax: 2.5
ticks: off
fontsize: 30
:::

$$
\lvec{AB} = \lvec{OB} - \lvec{OA}
$$

::::::

::::::{grid-item-card}
**Linjer**
^^^
:::{plot}
ticks: off
width: 100%
ymin: -0.5
xmin: -0.5
ymax: 3.5
xmax: 5
line: 0.5, 1, solid, blue
point: (2, 2)
text: 2, 2, "$A$", top-left
vector: (0, 0), (2, 2), red
text: 0.5 * 2, 0.5 * 2, "$\overrightarrow{OA}$", center-left 
vector: (2, 2), (4, 3), red
vector: (0, 0), (4, 3), red
text: 0.5 * (2 + 4), 0.5 * (2 + 3), "$\vec{v} \cdot t$", top-left
text: 0.5 * 4, 0.5 * 3, "$\vec{r}(t) = \overrightarrow{OB} = \overrightarrow{OA} + \vec{v} \cdot t$", bottom-right
text: -1/2, 3/4, "$\ell$", center-left
point: (4, 3)
text: 4, 3, "$B$", bottom-right
fontsize: 22
:::
::::::


::::::{grid-item-card}
**Skalarproduktet**
^^^
:::{plot}
figsize: (3, 3)
width: 100%
axis: off
vector: 0, 0, 1.5, 0, red
vector: 0, 0, 1, 1, blue
angle-arc: (0, 0), 0.3, 0, 45
xmin: -0.2
ymin: -0.5 
ymax: 1.3
xmax: 1.7
text: 0.45 * cos(pi/4), 0.1 * sin(pi/4), "$\varphi$", top-right
text: 0.75, 0, "$\vec{a}$", bottom-center
text: 0.5, 0.5, "$\vec{b}$", top-left
fontsize: 18
:::

$$
\vec{a} = [a_x, a_y] \qog \vec{b} = [b_x, b_y]
$$

$$
\vec{a} \cdot \vec{b} = a_x b_x + a_y b_y
$$

$$
\vec{a} \cdot \vec{b} = \abs{\vec{a}} \cdot \abs{\vec{b}} \cdot \cos \varphi
$$


::::::

::::::{grid-item-card}
**Tverrvektor**
^^^
$$
\vec{a} = [x, y]
$$

$$
\vec{a}_{\perp} = [-y, x] \qeller \vec{a}_{\perp} = [y, -x]
$$
::::::

::::::{grid-item-card}
Areal
^^^
:::{plot}
width: 100%
figsize: (4, 4)
point: (0, 0)
point: (3, 0)
point: (2, 1)
vector: 0, 0, 3, 0, blue
vector: 0, 0, 2, 1, red
line-segment: (3, 0), (2, 1), dashed, gray 
xmin: -0.5
xmax: 3.5
ymin: -0.5
ymax: 1.5
ticks: off
axis: off
text: 1.5, 0, "$\vec{a}$", bottom-center
text: 1, 0.5, "$\vec{b}$", top-left
fontsize: 20
text: 0, 0, "$A$", bottom-left
text: 3, 0, "$B$", bottom-right
text: 2, 1, "$C$", top-right
:::

$$
T = \dfrac{1}{2} \abs{\vec{a} \cdot \vec{b}_\perp}
$$

::::::

::::::{grid-item-card}
Avstand fra punkt til linje
^^^
:::{plot}
figsize: (4, 3)
width: 100%
line: 1, -2, solid, blue
point: (1, 3)
text: 1, 3, "$R$", top-left
text: 0.5 * (1 + 3), 0.5 * (1 + 3), "$h$", top-right
line-segment: (1, 3), (3, 1), dashed, gray
axis: equal
xmin: -1
xmax: 5
ymin: -1
ymax: 5
polygon: (2.6, 0.6), (3, 1), (2.6, 1.4), (2.2, 1)
axis: off
fontsize: 20
text: 5, 3, "$\ell$", top-right
point: (0, -2)
text: -0.15, -2, "$Q$", center-left
vector: (0, -2), (1.75, -0.25), red
text: 0.5 * (0 + 1.75), 0.5 * (-2 + -0.25), "$\vec{v}$", bottom-right
vector: (0, -2), (1, 3), red
text: 0.5 * (0 + 1), 0.5 * (-2 + 3), "$\overrightarrow{QR}$", top-left
:::

$$
h = \dfrac{|\lvec{QR} \cdot \vec{v}_\perp|}{\abs{\vec{v}}}
$$

::::::


::::::{grid-item-card}
**Dekomponering langs en linje**
^^^
:::{plot}
figsize: (4, 3)
width: 100%
line: 1, -2, solid, blue
point: (1, 3)
text: 1, 3, "$R$", top-left
vector: (3, 1), (1, 3), red
text: 0.5 * (1 + 3), 0.5 * (1 + 3), "$\vec{h}$", top-right
axis: equal
xmin: -1
xmax: 5
ymin: -1
ymax: 5
polygon: (2.6, 0.6), (3, 1), (2.6, 1.4), (2.2, 1)
axis: off
fontsize: 20
text: 5, 3, "$\ell$", top-right
point: (0, -2)
text: -0.15, -2, "$Q$", center-left
vector: (0, -2), (1, 3), red
text: 0.5 * (0 + 1), 0.5 * (-2 + 3), "$\overrightarrow{QR}$", top-left
vector: (0, -2), (3, 1), red
text: 0.5 * (0 + 3), 0.5 * (-2 + 1), "$\vec{p}$", bottom-right
:::


$$
\vec{p} = \dfrac{\overrightarrow{QR} \cdot \vec{v}}{\abs{\vec{v}}^2} \cdot \vec{v}
$$

$$
\vec{h} = \dfrac{\overrightarrow{QR} \cdot \vec{v}_\perp}{\abs{\vec{v}_\perp}^2} \cdot \vec{v}_\perp
$$


::::::



::::::::




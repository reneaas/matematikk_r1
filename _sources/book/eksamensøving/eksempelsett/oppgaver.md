# Eksempelsett

## Del 1 – 3 timer – Uten hjelpemidler


:::::::::::::::{exercise} Oppgave 1
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Deriver funksjonen

$$
f(x) = x^4 - 2x + \ln x
$$
:::::::::::::


:::::::::::::{tab-item} b
Deriver funksjonen

$$
g(x) = x^7 e^x
$$
:::::::::::::



:::::::::::::{tab-item} c
Deriver funksjonen

$$
h(x) = \dfrac{\ln (2x)}{x^2}
$$
:::::::::::::
::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen

$$
4^x - 2 \cdot 2^x = 8
$$
:::::::::::::



:::::::::::::{tab-item} b
Bestem $a \in \natural$ slik at 

$$
(\log_a 25)^2 - \log_a 5 = 3
$$
:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
Firkanten $ABCD$ er gitt ved $A(-2, 1)$, $B(2, -1)$, $C(4, 2)$ og $D(t, 3)$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør om $\lvec{AB} \perp \lvec{BC}$.


:::::::::::::


:::::::::::::{tab-item} b
Bruk vektorregning til å bestemme $t$ slik at $\lvec{AB} \perp \lvec{AD}$.


:::::::::::::


:::::::::::::{tab-item} c
Bestem $t$ slik at arealet av firkanten $ABCD$ er lik $10$.


:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
:::{plot}
axis: equal
fontsize: 28
width: 100%
align: right
xmin: -1
ymin: -1
xmax: 3
ymax: 3
function: sqrt(4 - x**2), (0, 2)
def: f(x) = sqrt(4 - x**2)
let: a = 1.4
let: Ox = 0
let: Oy = 0
let: Ax = a
let: Ay = 0
let: Bx = a
let: By = f(a)
let: Cx = 0
let: Cy = f(a)
polygon: (Ox, Oy), (Ax, Ay), (Bx, By), (Cx, Cy)
ticks: off
text: Ox, Oy, "$O$", bottom-left
text: Ax, Ay, "$A(x, 0)$", bottom-center
text: Bx, By, "$B$", top-right
text: Cx, Cy, "$C$", center-left
fill-between: f(x), f(a), (0, a), blue, 0.2, where=above
fill-between: f(x), 0, (a, 2), blue, 0.2, where=above
nocache:
:::

Figuren til høyre viser en kvartsirkel med radius $2$. Funksjonen for kvartsirkelen er gitt ved

$$
f(x) = \sqrt{4 - x^2} \qfor 0 \leq x \leq 2.
$$

Firkanten $OABC$ er et rektangel, der $O$ er origo, $A$ ligger på $x$-aksen, $B$ ligger på kvartsirkelen og $C$ ligger på $y$-aksen.


:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en eksakt verdi for arealet når $x = 1$.


:::::::::::::



:::::::::::::{tab-item} b
Bestem det minste arealet det fargelagte området kan ha.

:::::::::::::


::::::::::::::

:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 5
Funksjonen $f$ er gitt ved

$$
f(x) = \begin{cases}
    x^2 + bx & \qhvis x \lt 1 \\
    \\
    e^{a(x - 1)} + 3 & \qhvis x \geq 1
\end{cases}
$$

Bestem $a$ og $b$ slik at $f$ er kontinuerlig og deriverbar i $x = 1$.

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 6
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem grenseverdien

$$
\lim_{x\to 4} \dfrac{x - 4}{2 - \sqrt{x}}
$$


::::{answer}
$$
\lim_{x\to 4} \dfrac{x - 4}{2 - \sqrt{x}} = -4
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $a$ slik at grenseverdien nedenfor eksisterer.

$$
\lim_{x\to a} \dfrac{8 - \sqrt{ax}}{x - a}
$$


Bestem grenseverdien for denne verdien av $a$.
:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 7
For to vektorer $\vec{a}$ og $\vec{b}$ er

* $\abs{\vec{a}} = 4$
* $\abs{\vec{b}} = 5$
* $\cos \varphi = \dfrac{1}{2}$ der $\varphi$ er vinkelen mellom $\vec{a}$ og $\vec{b}$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\vec{a} \cdot \vec{b}$.


:::::::::::::



:::::::::::::{tab-item} b
En vektor $\vec{p}$ er gitt ved

$$
\vec{p} = 2\vec{a} + t \cdot \vec{b}
$$

Bestem $t$ slik at $\abs{\vec{p}}$ er minst mulig.
:::::::::::::


::::::::::::::

:::::::::::::::


## Del 2 – 2 timer – Med hjelpemidler



:::::::::::::::{exercise} Oppgave 1
To golfballer blir slått ut samtidig fra et tak som er 20 meter over bakkenivå.

Posisjonen til ball 1 er gitt ved vektorfunksjonen

$$
\vec{r}_1(t) = [17t, -5t^2 + 29t + 20]
$$

Posisjonen til ball 2 er gitt ved vektorfunksjonen

$$
\vec{r}_2(t) = [24t, -5t^2 + 25t + 20]
$$

Her er $t$ tiden (målt i sekunder) etter at ballene blir slått ut fra taket, og koordinatene er gitt i meter. Førstekoordinaten er posisjon i horisontal retning, og andrekoordinaten er høyden til ballen over bakkenivå.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvor lang tid tar det før hver av golfballene treffer bakken?

:::::::::::::


:::::::::::::{tab-item} b
Bestem banefarten til hver av de to golfballene idet de forlater taket.


:::::::::::::



:::::::::::::{tab-item} c
Ved et tidspunkt vil de to golfballene ha samme fartsretning.

Bestem hvilken vinkel fartsvektorene danner med bakken.
:::::::::::::




::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2
Funksjonen $f$ er gitt ved

$$
f(x) = \dfrac{1}{3}x^3 - 2x^2 + 3x + 1
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem det største intervallet $I = [a, b]$ der $f$ har en omvendt funksjon og $2 \in I$.


:::::::::::::


:::::::::::::{tab-item} b
La $g$ være den omvendte funksjonen til $f$.

Bestem 
:::::::::::::


::::::::::::::
:::::::::::::::


# Omvendte funksjoner: Blandede oppgaver

:::::::::::::::{exercise} Oppgave 1
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Funksjonen $f$ er gitt ved 

$$
f(x) = 2x - 1, \quad D_f = \langle -2, 3]
$$

Bestem $f^{-1}(x)$.


::::{answer}
$$
f^{-1}(x) = \dfrac{x + 1}{2} \, , \quad D_{f^{-1}} = \langle -5, 5]
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Funksjonen $g$ er gitt ved

$$
g(x) = x^2 - 1 , \quad D_g = [0, 4\rangle
$$

Bestem $g^{-1}(x)$.

::::{answer}
$$
g^{-1}(x) = \sqrt{x + 1} \, , \quad D_{g^{-1}} = [-1, 15\rangle
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Funksjonen $h$ er gitt ved 

$$
h(x) = -x^2 + 4x + 1 \, , \quad D_h = \langle \gets, 2]
$$

Bestem $h^{-1}(x)$.


::::{answer}
$$
h^{-1}(x) = 2 - \sqrt{5 - x} \, , \quad D_{h^{-1}} = \langle\gets, 5]
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
Funksjonen $p$ er gitt ved

$$
p(x) = e^{x^2 - 4} \, , \quad D_p = \langle 2, \to \rangle
$$

Bestem $p^{-1}(x)$.


::::{answer}
$$
p^{-1}(x) = \sqrt{\ln x + 4} \, , \quad D_{p^{-1}} = \langle 0, 1]
$$
::::


:::::::::::::
::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2
Nedenfor viser grafene til fire funksjoner. 

1. Avgjør hvilke funksjoner som har en omvendt funksjon.
2. Bestem definisjonsmengden til de omvendte funksjonene hvis de eksisterer.

::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 30
---
:::{plot}
function: (x - 1)**2 - 4, (1, 4], blue
function-endpoints: true 
text: -4, 4, "A", center-center, bbox
:::

:::{plot}
function: 0.125 * (x - 1) * (x + 2) * (x - 3) + 1, [-3, 3], blue
function-endpoints: true 
text: -4, 4, "B", center-center, bbox
:::

:::{plot}
function: -log(x + 3) / log(2) + 1, [-2, 5), blue
function-endpoints: true 
text: -4, 4, "C", center-center, bbox
:::

:::{plot}
function: -2 * (x + 3) + 4, [-2, 1), blue
function: 1 * (x - 1) + 1, [1, 4), blue
function-endpoints: true 
text: -4, 4, "D", center-center, bbox
:::

::::


::::{answer}
* Graf A og C har omvendte funksjoner.
* Definsjonsmengden til $A^{-1}$ er lik $\langle -4, 5]$.
* Definisjonsmengden til $C^{-1}$ er lik $\langle -2, 1]$.
::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
Nedenfor vises seks grafer der to og to er omvendte funksjoner til hverandre.

Avgjør hvilke grafer som hører sammen.


::::{multi-plot2}
---
rows: 3
cols: 2
fontsize: 30
---
:::{plot}
function: 0.25*(x + 2)**2 - 4, [-2, 4), blue
function-endpoints: true 
text: -4, 4, "A", center-center, bbox
:::

:::{plot}
function: -0.25*(x - 2)**2 + 4, [2, -4), blue
function-endpoints: true 
text: -4, 4, "B", center-center, bbox
:::

:::{plot}
function: 2 - 2 * sqrt(4 - x), (-5, 4], blue
function-endpoints: true 
text: -4, 4, "C", center-center, bbox
:::

:::{plot}
function: 2*log(x + 4) / log(2) - 2, (-3, 4], blue
function-endpoints: true 
text: -4, 4, "D", center-center, bbox
:::

:::{plot}
function: -2 + 2 * sqrt(x + 4), [-4, 5), blue
function-endpoints: true 
text: -4, 4, "E", center-center, bbox
:::

:::{plot}
function: -4 + 2**((x + 2)/2), (-2, 4], blue
function-endpoints: true 
text: -4, 4, "F", center-center, bbox
:::

::::


::::{answer}
* $A^{-1} = E$
* $B^{-1} = C$
* $D^{-1} = F$
::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 4
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

Funksjonen $f$ er gitt ved

$$
f(x) = -2x^3 + 24x
$$


Bestem det største intervallet $I = [a, b]$ slik at $f$ har en omvendt funksjon $f^{-1}$ på $I$ og $0 \in I$.

::::{answer}
$$
I = [-2, 2]
$$
::::

:::::::::::::


:::::::::::::{tab-item} b

Funksjonen $g$ er gitt ved

$$
g(x) = x e^{-ax^2} \, ,\quad D_g = [-2, 3]
$$


For hvilke verdier av $a$ har $g$ en omvendt funksjon?

::::{answer}
$$
a \in \left\langle \gets, \dfrac{1}{8}\right]
$$
::::


:::::::::::::


:::::::::::::{tab-item} c

Funksjonen $h$ er gitt ved

$$
h(x) = 
\begin{cases}
2x + 3, & x < a \\
\\
x + 7, & x \geq a
\end{cases}
$$

For hvilke verdier av $a$ har $h$ en omvendt funksjon? 

::::{answer}
$$
a \leq 4
$$
::::
:::::::::::::


::::::::::::::
:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 5
For en funksjon $f$ kjenner vi disse verdiene for $f(x)$ og $f'(x)$:

| $x$ | $-2$ | $0$ | $1$ | $3$ |
|-----|:-----:|:-----:|:-----:|:-----:|
| $f(x)$ | $0$ | $-3$ | $5$ | $2$ | 
| $f'(x)$ | $4$ | $-2$ | $1$ | $-3$ |

<br>

La $g = f^{-1}$ være den omvendte funksjonen til $f$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $g(5)$.

::::{answer}
$$
g(5) = 1
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $g(2)$.


::::{answer}
$$
g(2) = 3
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $g'(-3)$.


::::{answer}
$$
g'(-3) = -\dfrac{1}{2}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
Det finnes bare én tangent til grafen til $g$ som har stigningstall $\dfrac{1}{4}$.

Bestem koordinatene til punktet tangenten treffer grafen til $g$.


::::{answer}
$$
(0, -2)
$$
::::


:::::::::::::


::::::::::::::



:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 6
I figuren nedenfor vises grafen til en funksjon $f$.


:::{plot}
width: 60%
function: 2 * (x + 4) - 2, [-4, -1), blue
function: -0.5 * (x - 1) + 6, [-1, 5], blue
function-endpoints: true
xmin: -7
xmax: 7
ymin: -4
ymax: 8
fontsize: 24
:::

Avgjør hvilke påstander nedenfor som er sanne.

Rett opp i eventuelle påstander som er gale.


:::::{grid} 1 2 2 2
---
gutter: 2
---
::::{grid-item-card}
**Påstand 1**
^^^
$$
f^{-1}(6) = 1
$$
::::

::::{grid-item-card}
**Påstand 2**
^^^
$$
\left(f^{-1}\right)'(0) = \dfrac{1}{2}
$$
::::

::::{grid-item-card}
**Påstand 3**
^^^
$$
\left(f^{-1}\right)'(5) = -\dfrac{1}{2}
$$
::::


::::{grid-item-card}
**Påstand 4**
^^^
$$
(f^{-1})'(x) > 0 \qfor x \in \langle 2, 4\rangle
$$
::::
:::::


::::{answer}
Påstand 1, 2 og 4 er sanne.

Påstand 3 er korrekt hvis dersom $(f^{-1})'(5) = -2$.
::::





:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 7

:::{cas-popup}
---
layout: sidebar
---
:::


Når du bruker blitsen på et fotokamera, vil batteriet lade den opp igjen. Ladningen $Q$ i blitsen $t$ sekunder etter at den går av, er gitt ved 

$$
Q(t) = Q_0 \left(1 - e^{-2.3 t}\right) \, , \quad t \geq 0
$$

Her er $Q_0$ den maksimale ladningen i blitsen.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem den omvendte funksjonen til $Q$.


::::{answer}
$$
t(Q) = -\dfrac{10}{23}\ln \left(1 - \dfrac{Q}{Q_0}\right)
$$
::::
:::::::::::::


:::::::::::::{tab-item} b
Hvor lang tid tar det før blitsen har fått 90 prosent av den maksimale ladningen?

::::{answer}
$$
t(0.9 \cdot Q_0) = \dfrac{10}{23} \ln 10 \approx 1 \, \mathrm{sekunder}
$$
::::
:::::::::::::


::::::::::::::


:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 8
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En funksjon $f$ er gitt ved

$$
f(x) = e^{4 - 2x} \qfor x \in \mathbb{R}
$$

Bestem $(f^{-1})'(1)$.


::::{answer}
$$
(f^{-1})'(1) = -\dfrac{1}{2}
$$
::::
:::::::::::::


:::::::::::::{tab-item} b
Funksjonen $g$ er gitt ved 

$$
g(x) = x^2 \ln x \qfor x > 0
$$

Bestem $(g^{-1})'(0)$.

::::{answer}
$$
(g^{-1})'(0) = 1
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Funksjonen $h$ er gitt ved 

$$
h(x) = x e^{x^2} \qfor x \in \mathbb{R}
$$

Bestem $(h^{-1})'(e)$.


::::{answer}
$$
(h^{-1})'(e) = \dfrac{1}{3e}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Funksjonen $p$ er gitt ved 

$$
p(x) = \ln \left(\dfrac{2 - x}{x^2}\right) \, , \quad D_p = \langle 0, 2\rangle
$$

Bestem $(p^{-1})'(\ln 6)$.


::::{answer}
$$
(p^{-1})'(\ln 6) = -\dfrac{3}{14}
$$
::::


:::::::::::::


::::::::::::::
:::::::::::::::




---


:::::::::::::::{exercise} Oppgave 9

:::{cas-popup}
---
layout: sidebar
---
:::


Om en andregradsfunksjon $f$ får du vite at
* Punktet $(2, 5)$ ligger på grafen til $f$.
* $(f^{-1})'(5) = \dfrac{1}{9}$.
* Den største mulige definisjonsmengden til $f$ der $f^{-1}$ eksisterer er $D_f = [-1, \to\rangle$.

Bestem $f(x)$.

::::{answer}
$$
f(x) = \dfrac{3}{2}x^2 + 3x - 8
$$
::::

:::::::::::::::





---




:::::::::::::::{exercise} Oppgave 10
Om to funksjoner $f$ og $g$ får du vite at

* Grafen til $f$ skjærer $x$-aksen i punktet $(3, 0)$.
* $\left(f^{-1}\right)'(0) = -2$.
* $\lim\limits_{x\to 1} g(x)$ eksisterer. 
* $\left(g^{-1}\right)'(0) = \dfrac{1}{2}$.

Avgjør hvilken graf som viser grafen til $f$ og hvilken graf som viser grafen til $g$.

::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 30
---
:::{plot}
function: -2*x + 3, [-1, 1], blue
function: 0.5 * (x - 3), (1, 5), blue
function-endpoints: true
text: 5, 4, "A", center-center, bbox
:::

:::{plot}
function: -0.5 * (x - 3), [1, 5), blue
function: 2*x + 3, (-1, 1), blue
function-endpoints: true 
text: 5, 4, "B", center-center, bbox 
:::

:::{plot}
function: 0.5 * x + 3, (-2, 2), blue
function: -2 * (x - 3), (2, 5), blue
function-endpoints: true 
text: 5, 4, "C", center-center, bbox 
:::

:::{plot}
function: -0.5 * x + 3, (-4, 2), blue
function: 2*x - 6, (2, 4), blue
function-endpoints: true 
text: 5, 4, "D", center-center, bbox
:::

::::


::::{answer}
* $B = f$.
* $D = g$.
::::

:::::::::::::::



---



:::::::::::::::{admonition} Oppgave 11
---
class: exercise, full-width
---
Nedenfor ser du åtte grafer.

* En av grafene er grafen til en funksjon på formen $f(x) = a^x$ der $a$ er positivt helt tall.
* Tre av grafene er grafer til funksjoner på formen $f(x) = x^b - c$ der $b$ og $c$ er positive hele tall.
* Fire av grafene er grafene til den dobbeltderiverte til de fire funksjonene som er beskrevet ovenfor.



::::{multi-plot2}
---
rows: 2
cols: 4
fontsize: 30
---
:::{plot}
function: 2**(x - 1)
lw: 4
text: -4, 4, "A", center-center, bbox
:::

:::{plot}
function: x**3 - 1
lw: 4
text: -4, 4, "B", center-center, bbox
:::

:::{plot}
function: 6*x
lw: 4
text: -4, 4, "C", center-center, bbox
:::


:::{plot}
function: 3 * x**2
lw: 4
text: -4, 4, "D", center-center, bbox
:::


:::{plot}
function: x**2 - 2
lw: 4
text: -4, 4, "E", center-center, bbox
:::


:::{plot}
function: x**4 - 1
lw: 4
text: -4, 4, "F", center-center, bbox
:::


:::{plot}
function: 2**x
lw: 4
text: -4, 4, "G", center-center, bbox
:::


:::{plot}
function: 2
lw: 4
text: -4, 4, "H", center-center, bbox
:::

::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Sorter grafene i par.

De to grafene i hvert par skal være grafen til en funksjon og grafen til den dobbeltderiverte til funksjonen.


::::{answer}
* $G'' = A$
* $E'' = H$
* $B'' = C$
* $F'' = D$
::::


:::::::::::::

:::::::::::::{tab-item} b
Hvilke av de åtte grafene ovenfor er grafen til funksjoner som har en omvendt funksjon?


::::{answer}
$A$, $B$, $C$ og $G$ har omvendte funksjoner.
::::


:::::::::::::
::::::::::::::


:::::::::::::::



---



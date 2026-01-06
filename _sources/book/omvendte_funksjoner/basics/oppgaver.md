# Oppgaver: Omvendte funksjoner


:::::::::::::::{exercise} Oppgave 1
To funksjoner $f$ og $g$ er omvendte funksjoner dersom

$$
f(g(x)) = x \qog g(f(x)) = x
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis at funksjonene nedenfor er omvendte funksjoner.

$$
f(x) = 10^x \qog g(x) = \lg (x)
$$

:::::::::::::


:::::::::::::{tab-item} b
Vis at funksjonene nedenfor er omvendte funksjoner.

$$
f(x) = \ln (2x) \qog g(x) = \frac{1}{2} e^x
$$

:::::::::::::


:::::::::::::{tab-item} c
Vis at funksjonene nedenfor er omvendte funksjoner.

$$
f(x) = x^3 - 4 \qog g(x) = \sqrt[3]{x + 4}
$$

:::::::::::::


:::::::::::::{tab-item} d
Vis at funksjonene nedenfor er omvendte funksjoner.

$$
f(x) = \frac{2x + 3}{5} \qog g(x) = \frac{5x - 3}{2}
$$
:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2

For hver av funksjonene nedenfor:

1. Bestem funksjonsuttrykket til den omvendte funksjonen.
2. Bestem definisjonsmengden til den omvendte funksjonen.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En funksjon $f$ er gitt ved

$$
f(x) = \sqrt{x} + 3 \qder D_f = [0, 4\rangle
$$



::::{answer}
$$
f^{-1}(x) = (x - 3)^2 \qder D_{f^{-1}} = [3, 5\rangle.
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
En funksjon $g$ er gitt ved

$$
g(x) = \ln (x - 5) \qder D_g = \langle 5, \to\rangle.
$$

::::{answer}
$$
g^{-1}(x) = e^x + 5 \qder D_{g^{-1}} = \real
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
En funksjon $h$ er gitt ved

$$
h(x) = x^2 + 3 \qder D_h = [0, 2\rangle.
$$


::::{answer}
$$
h^{-1}(x) = \sqrt{x - 3} \qder D_{h^{-1}} = [3, 7\rangle
$$
::::


:::::::::::::



:::::::::::::{tab-item} d
En funksjon $k$ er gitt ved

$$
k(x) = \frac{2x + 1}{x - 1} \qder D_k = \real \setminus \{1\}.
$$


::::{answer}
$$
k^{-1}(x) = \dfrac{x + 1}{x - 2} \qder D_{k^{-1}} = \real \setminus \{2\}.
$$
::::

:::::::::::::



::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
Grafen til en funksjon $f$ er vist i figuren nedenfor.


:::{plot}
width: 70%
function: (x - 1)**2 - 4, f, [1, 4), blue
function-endpoints: true
xmin: -2
xmax: 5
ymin: -6
ymax: 6
:::

La $g$ være den omvendte funksjonen til $f$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $D_f$ og $V_f$.


::::{answer}
$$
D_f = [1, 4\rangle \qog V_f = [-4, 5\rangle.
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $D_g$ og $V_g$.


::::{answer}
$$
D_g = [-4, 5\rangle \qog V_g = [1, 4\rangle.
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $g(-3)$. 


::::{answer}
$$
g(-3) = 2.
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Bestem $g(0)$. 


::::{answer}
$$
g(0) = 3.
$$
::::

:::::::::::::



:::::::::::::{tab-item} e
Én av grafene nedenfor viser grafen til $g$.

Avgjør hvilken. Husk å argumentere for svaret ditt.

::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
---

:::{plot}
function: 1 - sqrt(x + 4), A, [-4, 5), blue
function-endpoints: true 
:::

:::{plot}
function: -1 + sqrt(x + 4), B, [-4, 5), blue
function-endpoints: true 
:::

:::{plot}
function: 1 + sqrt(x + 4), C, [-4, 5), blue
function-endpoints: true 
:::

:::{plot}
function: 1 + sqrt(x + 4), D, (-4, 5], blue
function-endpoints: true 
:::

::::


::::{answer}
Graf C.
::::


:::::::::::::



::::::::::::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Om en funksjon $f$ får du vite at
* $f$ har en omvendt funksjon $g$.
* $f(2) = 3$
* $f(3) = -4$.


Bestem $g(-4)$ og $g(3)$.

::::{answer}
$$
g(-4) = 3
$$

$$
g(3) = 2
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Om en funksjon $f$ får du vite at

* $f$ har en omvendt funksjon $g$.
* $f(1) = 5$
* $f(4) = 0$.

Bestem $g(0)$ og $g(5)$.


::::{answer}
$$
g(0) = 4
$$

$$
g(5) = 1
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
I tabellen nedenfor ser du en verditabell for en funksjon $f$ med definisjonsmengden

$$
D_f = \{-2, -1, 0, 1, 2, 5\}.
$$

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $5$ |
|:-----:|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|
| $f(x)$ | $3$ | $2$ | $1$ | $-2$ | $4$ | $0$ | 


<br>

Sett sammen riktig funksjonsverdier for den omvendte funksjonen $g$. 

:::::::{pair-puzzle}
$g(3)$ : $-2$
$g(2)$ : $-1$
$g(1)$ : $0$
$g(-2)$ : $1$
$g(4)$ : $2$
$g(0)$ : $5$
:::::::



:::::::::::::


::::::::::::::

:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 5
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I figuren nedenfor vises grafene til fire funksjoner. 

Avgjør hvilke av funksjonene som har en omvendt funksjon. Husk å argumentere for svaret ditt. 

::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
---


:::{plot}
function: 0.25 * x**2, A, (-4, 4), blue
function-endpoints: true
:::


:::{plot}
function: -0.125 * x**3 + 1, B, (-3, 3], blue 
function-endpoints: true
:::


:::{plot}
function: x**3 - 2*x + 1, C, [-2, 2), blue
function-endpoints: true
:::


:::{plot}
function: sinh(x), D, [-2, 2), blue
function-endpoints: true
:::

::::



::::{answer}
Graf B og D.
::::


:::::::::::::



:::::::::::::{tab-item} b
I figuren nedenfor vises grafene til fire funksjoner. 

Avgjør hvilke av funksjonene som har en omvendt funksjon. Husk å argumentere for svaret ditt. 


::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
xmin: -4
xmax: 5
ymin: -4
ymax: 4
---


:::{plot}
function: sqrt(x + 1), A, (1, 4], blue
function-endpoints: true
:::


:::{plot}
function: 2*cbrt(abs(x)) * sign(x), B, [-3, 3], blue
function-endpoints: true
:::


:::{plot}
function: x * exp(-x), C, (-1, 3], blue
function-endpoints: true
:::


:::{plot}
function: x**3 * exp(-x) + 1, D, [-1, 3), blue
function-endpoints: true
:::




::::


::::{answer}
Graf A, B og D.
::::


:::::::::::::



:::::::::::::{tab-item} c
I figuren nedenfor vises grafene til fire funksjoner. 

Avgjør hvilke av funksjonene som har en omvendt funksjon. Husk å argumentere for svaret ditt. 

::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
---



:::{plot}
function: exp(-x) - 3, A, (-2, 3), blue
function-endpoints: true 
:::


:::{plot}
function: -ln(x + 2), B, [-1, 3), blue 
function-endpoints: true
:::


:::{plot}
function: exp(-x**2 + 1), C, (-2, 2], blue
function-endpoints: true 
:::


:::{plot}
function: ln(x - 1)**2 , D, [2, 5], blue
function-endpoints: true 
:::





::::


::::{answer}
Graf A, B, og D.
::::




:::::::::::::


:::::::::::::{tab-item} d
I figuren nedenfor vises grafene til fire funksjoner. 

Avgjør hvilke av funksjonene som har en omvendt funksjon. Husk å argumentere for svaret ditt. 



::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
---

:::{plot}
function: -2 * exp(-x) + 2, A, [-1, 4), blue
function-endpoints: true 
:::

:::{plot}
function: ln(x + 3) - ln(3 - x), B, (-2, 2], blue
function-endpoints: true 
:::


:::{plot}
function: -(x - 1) * (x**2 + 1), C, (-1, 2), blue
function-endpoints: true
:::

:::{plot}
function: x**4 + 2*x - 2, D, [-1, 1], blue
function-endpoints: true
ymax: 2
ymin: -4
xmax: 3
xmin: -3
:::







::::


::::{answer}
Graf A, B og C.
::::



:::::::::::::



::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 6
1. Avgjør om funksjonene nedenfor har en omvendt funksjon.
2. Bestem definisjonsmengden til den omvendte funksjonen i de tilfellene der den eksisterer.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{plot}
width: 70%
function: sqrt(x + 1) + 1, (-1, 3], f, blue
function-endpoints: true 
xmin: -2
xmax: 4
ymin: 0
ymax: 5
:::


::::{answer}
1. Funksjonen har en omvendt funksjon.
2. $D_{f^{-1}} = \langle 1, 3]$.
::::

:::::::::::::


:::::::::::::{tab-item} b
:::{plot}
width: 70%
function: (x - 1)**2 - 4, [1, 4), g, blue
function-endpoints: true
xmin: -1
xmax: 5
ymin: -6
ymax: 7
:::

::::{answer}
1. Funksjonen har en omvendt funksjon.
2. $D_{g^{-1}} = [-4, 5\rangle$.
::::

:::::::::::::



:::::::::::::{tab-item} c
:::{plot}
width: 70%
function: (x - 1) / (x + 2), h, blue
hline: 1, dashed, red
vline: -2, dashed, red
:::


::::{answer}
1. Funksjonen har en omvendt funksjon.
2. $D_{h^{-1}} = \real \setminus \{1\}$
::::

:::::::::::::


:::::::::::::{tab-item} d
:::{plot}
width: 70%
function: -sqrt(x + 4) + 2, [-4, 5], k, blue
function-endpoints: true
xmin: -6
xmax: 6
ymin: -3
ymax: 4
:::


::::{answer}
1. Funksjonen har en omvendt funksjon.
2. $D_{k^{-1}} = [-1, 2]$.
::::

:::::::::::::


::::::::::::::
:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 7

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I figuren nedenfor vises grafene til fire funksjoner.


1. Avgjør hvilke funksjoner som har en omvendt funksjon.
2. Bestem definisjonsmengden til de omvendte funksjonene der de eksisterer.


::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
xmin: -6
xmax: 6
---
:::{plot}
function: 1 / x**2, [-4, 4], f, blue 
ymax: 7
ymin: -1
function-endpoints: true
:::


:::{plot}
function: -1/96 * x**3 + 19/24 * x + 7/2, [-4, 4], g, blue
ymax: 7
ymin: -1
function-endpoints: true
:::


:::{plot}
function: -1/3 * (x + 5) + 3, [-5, -2), h, blue
function: (3*x + 4) / (x + 4), [-2, 4], blue
ymax: 4
ymin: -2
function-endpoints: true
:::


:::{plot}
function: -3 * x / (x + 8), [-4, 4), k, blue
ymax: 4
ymin: -2
function-endpoints: true
:::

::::



::::{answer}
Funksjonene $g$, $h$ og $k$ har omvendte funksjoner.

Definisjonsmengdene til de omvendte funksjonene er

$$
\begin{align*}
D_{g^{-1}} &= [1, 6] \\
\\
D_{h^{-1}} &= [-1, 3] \\
\\
D_{k^{-1}} &= \langle -1, 3]
\end{align*}
$$

::::


:::::::::::::



:::::::::::::{tab-item} b

I figuren nedenfor vises grafene til fire funksjoner.


1. Avgjør hvilke funksjoner som har en omvendt funksjon.
2. Bestem definisjonsmengden til de omvendte funksjonene der de eksisterer.

::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
---
:::{plot}
width: 100%
function: (x - 1) / (x + 2), [-5, -3), f, blue
function: (x - 1) / (x + 2), (-1, 1), blue
function-endpoints: true
xmax: 3
ymin: -4
:::

:::{plot}
width: 100%
function: 2*sqrt(x + 2) - 3, [-1, 2], g, blue
function: 0.5 * (x - 4)**2 + 1, (2, 4], blue
function-endpoints: true
xmin: -3
ymin: -3
:::

:::{plot}
width: 100%
function: x / (x - 2)**2, [1, 4), h, blue
function-endpoints: true
xmin: -1
xmax: 6
ymin: -1
ymax: 6
:::

:::{plot}
width: 100%
function: 4 * cbrt(abs(x + 1)) * sign(x + 1), [-2, 7), k, blue
xmin: -4
xmax: 9
ymin: -6
ymax: 10
function-endpoints: true
:::

::::


::::{answer}
Funksjonene $f$ og $k$ har omvendte funksjoner.

Definisjonsmengdene til de omvendte funksjonene er

$$
\begin{align*}
D_{f^{-1}} &= \langle -2, 0\rangle \cup [2, 4\rangle \\
\\
D_{k^{-1}} &= [-4, 8\rangle
\end{align*}
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
I figuren nedenfor vises grafene til fire funksjoner.


1. Avgjør hvilke funksjoner som har en omvendt funksjon.
2. Bestem definisjonsmengden til de omvendte funksjonene der de eksisterer.


::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
---
:::{plot}
width: 100%
function: 4 * (log(x) / log(2))**2 - 1, [1, 2), f, blue
function-endpoints: true
xmin: 0
xmax: 3
ymin: -2
ymax: 5
:::

:::{plot}
width: 100%
function: -(x + 1)**2 + 4, [-3, 1), g, blue
function-endpoints: true
xmin: -4
xmax: 2
ymin: -1
ymax: 5
:::


:::{plot}
width: 100%
function: -1/2 * (log(x + 1) / log(2))**2 + 2, (0, 3), h, blue
function-endpoints: true
xmin: -1
xmax: 4
ymin: -1
ymax: 3
:::


:::{plot}
width: 100%
function: -1/3 * (x + 2)**2 + 4, (-2, 1], k, blue
function: 1.5 * x - 3.5, (1, 3), blue
function-endpoints: true
xmin: -3
xmax: 4
ymin: -4
ymax: 5
:::



::::


::::{answer}
Funksjonene $f$, $h$ og $k$ har omvendte funksjoner.


Definisjonsmengdene til de omvendte funksjonene er

$$
\begin{align*}
D_{f^{-1}} &= [-1, 3\rangle \\
\\
D_{h^{-1}} &= \langle 0, 2\rangle \\
\\
D_{k^{-1}} &= \langle -2, 4\rangle
\end{align*}
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
f(x) = x^4 \qder D_f = \real.
$$

Avgjør om $f$ har en omvendt funksjon. Hvis ja, bestem definisjonsmengden til den omvendte funksjonen.


::::{answer}
$f$ har ikke en omvendt funksjon.
::::

:::::::::::::


:::::::::::::{tab-item} b
En funksjon $g$ er gitt ved

$$
g(x) = e^{-(x - 2)^2} \qder D_g = [2, \to\rangle.
$$

Avgjør om $g$ har en omvendt funksjon. Hvis ja, bestem definisjonsmengden til den omvendte funksjonen.


::::{answer}
1. $g$ har en omvendt funksjon.
2. $D_g = \langle 0, 1]$.
::::


:::::::::::::


:::::::::::::{tab-item} c
En funksjon $h$ er gitt ved

$$
h(x) = (x - 1)^2 - 4 \qder D_h = [a, \to\rangle.
$$

1. Bestem $a$ slik at $h$ har en omvendt funksjon og $D_h$ er størst mulig.
2. Bestem definisjonsmengden til den omvendte funksjonen.


::::{answer}
1. $a = 1$
2. $D_{h^{-1}} = [-4, \to \rangle$.
::::

:::::::::::::



:::::::::::::{tab-item} d
En funksjon $k$ er gitt ved

$$
k(x) = x^2 e^{-x} \qder D_k = [0, a].
$$

1. Bestem $a$ slik at $k$ har en omvendt funksjon og $D_k$ er størst mulig.
2. Bestem definisjonsmengden til den omvendte funksjonen.


::::{answer}
1. $a = 2$
2. $D_{k^{-1}} = \left[0, \dfrac{4}{e^2}\right]$
::::

:::::::::::::


::::::::::::::
:::::::::::::::





---




:::::::::::::::{exercise} Oppgave 9

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{cas-popup}
---
layout: sidebar
---
:::



En funksjon $f$ er gitt ved

$$
f(x) = x^3 - 6x.
$$

Bestem det største intervallet $I = [a, b]$ slik at 
* $1 \in I$
* $f$ har en omvendt funksjon når $I$ er definisjonsmengden til $f$.


::::{answer}
$$
I = \left[-\sqrt{2}, \sqrt{2}\right]
$$
::::
:::::::::::::



:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::


En funksjon $g$ er gitt ved

$$
g(x) = x^4 - 6x^2 + 2 \qder D_g = [a, b].
$$

Bestem $a$ og $b$ slik at

1. $g$ har en omvendt funksjon når $D_g = [a, b]$.
2. Definisjonsmengden til den omvendte funksjonen blir så stor som mulig.
3. $-2 \in D_g$.


::::{answer}
$$
a = -\sqrt{3} \and b = 0
$$
::::



:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::



En funksjon $h$ er gitt ved

$$
h(x) = (\log_2 x)^2 - \log_2 x + 1 \qder D_h = \langle a, \to\rangle.
$$

1. Bestem det minste tallet $a$ slik at $h$ har en omvendt funksjon.
2. Bestem definisjonsmengden til den omvendte funksjonen for dette tallet $a$.


::::{answer}
1. $a = \sqrt{2}$.
2. $D_{h^{-1}} = \left[\dfrac{3}{4}, \to\right\rangle$
::::


:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 10
Nedenfor vises tre funksjoner $f$, $g$ og $h$.

::::{multi-plot2}
---
rows: 1
cols: 3
fontsize: 30
---
:::{plot}
width: 100%
function: x**2 + 3, [0, 2), f, blue
function-endpoints: true
xmin: -1
xmax: 3
ymin: -1
ymax: 9
:::


:::{plot}
width: 100%
function: 1 * (x + 2) - 3, (-2, 1), g, blue
function: -2 * (x - 1) + 2, [1, 2], blue
function-endpoints: true
xmin: -3
xmax: 3
ymin: -4
ymax: 3
:::


:::{plot}
width: 100%
function: x**3 - 2 * x + 5, [-2, 2), h, blue
function-endpoints: true
xmin: -3
xmax: 3
ymin: -1
ymax: 10
:::

::::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør hvilke av funksjonene som har en omvendt funksjon.


::::{answer}
$f$ og $g$ har omvendte funksjoner.
::::


:::::::::::::


:::::::::::::{tab-item} b


:::{cas-popup}
---
layout: sidebar
---
:::



Bestem et mulig funksjonsuttrykk og definisjonsmengden til de omvendte funksjonene dersom de eksisterer.


:::{clear}
:::

::::{answer}
$$
f^{-1}(x) = \sqrt{x - 3} \qder D_{f^{-1}} = [3, 7\rangle.
$$

$$
g^{-1}(x) = \begin{cases}
    x + 1, & -3 < x < 0 \\
    \\
    -\dfrac{x + 4}{2}, & 0 \leq x \leq 2
\end{cases}
$$
::::



:::::::::::::


::::::::::::::



:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 11

:::{cas-popup}
---
layout: sidebar
---
:::


Funksjonen $f$ er gitt ved

$$
f(x) = x^4 - bx^3 + 2 \qder D_f = [-3, \to \rangle.
$$


For hvilke verdier av $b$ har $f$ en omvendt funksjon?


::::{hints} Hvordan kommer jeg i gang?
Tegn to fortegnslinjer for $f'(x)$ – én der du antar at $b > 0$ og én der du antar at $b < 0$. 
::::


::::{answer}
$$
b \in \langle \gets, -4]
$$
::::
:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 12

:::{cas-popup}
---
layout: sidebar
---
:::


En funksjon $f$ er gitt ved

$$
f(x) = \begin{cases}
    -x^2 + (2 + k)x, & x < k \\
    \\
    x^2 + (2 - k)x, & x \geq k
\end{cases}
$$

der $k \in \real$.

For hvilke verdier av $k$ har $f$ en omvendt funksjon?


::::{hints} Hvordan kommer jeg i gang?
Tegn en fortegnslinje for den deriverte til hver forskrift av funksjonen. Let etter et området der de deriverte overlapper med samme fortegn slik at $f$ blir enten strengt voksende eller strengt synkende i hele sin definisjonsmengde.

::::


::::{answer}
$$
k \in \langle -2, 2 \rangle
$$
::::


:::::::::::::::


# Eksamen vår 2025

> Eksamen våren 2025 var todelt med 2 timer på del 1 og 3 timer på del 2. Våren 2026 vil eksamen være todelt med 3 timer på del 1 og 2 timer på del 2.


## Del 1 (Uten hjelpemidler – 2 timer)


:::::::::::::::{exercise} Oppgave 1 (2 poeng)
Deriver funksjon $f$ gitt ved

$$
f(x) = e^{-2x} + \dfrac{1}{5}x^5 - 2\pi
$$


::::{answer}
$$
f'(x) = -2e^{-2x} + x^4
$$
::::

::::{solution}
$$
\begin{align*}
f'(x) &= \left(e^{-2x} + \dfrac{1}{5}x^5 - 2\pi\right)' \\
\\
&= (e^{-2x})' + \left(\dfrac{1}{5}x^5\right)' - (2\pi)' \\
\\
&= -2e^{-2x} + x^4 - 0 \\
\\
&= -2e^{-2x} + x^4
\end{align*}
$$
::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2 (5 poeng)
Funksjonen $g$ er gitt ved

$$
g(x) = \dfrac{1}{2}e^x \cdot (2x - 1)^2.
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem eventuelle nullpunkter til funksjonen $g$.


::::{answer}
$$
x = \dfrac{1}{2}
$$
::::

::::{solution}
Vi løser likningen $g(x) = 0$:

$$
g(x) = 0 \liff \dfrac{1}{2}e^x \cdot (2x - 1)^2 = 0
$$

som gir

$$
2x - 1 = 0 \liff x = \dfrac{1}{2}.
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
Vis at

$$
g'(x) = \dfrac{1}{2}e^x (2x - 1)(2x + 3).
$$


::::{solution}
Vi bruker produktregelen for derivasjon:

$$
\begin{align*}
g'(x) &= \left(\dfrac{1}{2}e^x\right)' \cdot (2x - 1)^2 + \dfrac{1}{2}e^x \cdot \left((2x - 1)^2\right)' \\
\\
&= \dfrac{1}{2}e^x \cdot (2x - 1)^2 + \dfrac{1}{2}e^x \cdot 2(2x - 1) \cdot (2) \\
\\
&= \dfrac{1}{2}e^x (2x - 1)^2 + 2e^x (2x - 1) \\
\\
&= \dfrac{1}{2}e^x (2x - 1)(2x - 1 + 4) \\
\\
&= \dfrac{1}{2}e^x (2x - 1)(2x + 3).
\end{align*}
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Finn koordinatene til eventuelle topp- og bunnpunkter på grafen til $g$.



::::{solution}
Vi løser først likningen $g'(x) = 0$:

$$
g'(x) = 0 \liff \dfrac{1}{2}e^x (2x - 1)(2x + 3) = 0
$$

som gir

$$
2x - 1 = 0 \or 2x + 3 = 0 \liff x = \dfrac{1}{2} \or x = -\dfrac{3}{2}.
$$

Den første løsningen er et nullpunkt, så koordinatene til det ene stasjonære punktet er bare $\left(\dfrac{1}{2}, 0\right)$. Så setter vi inn disse $x$-verdien til det andre stasjonære punktet i funksjonen $g$ for å finne de tilhørende $y$-verdiene:

$$
g\left(-\dfrac{3}{2}\right) = \dfrac{1}{2}e^{-3/2} \cdot \left(2 \cdot \left(-\dfrac{3}{2}\right) - 1\right)^2 = \dfrac{1}{2}e^{-3/2} \cdot (-4)^2 = \dfrac{8}{e^{3/2}}
$$


Vi tegner en fortegnslinje for $g'(x)$ for å avgjøre om det stasjonære punktet $\left(-\dfrac{3}{2}, \dfrac{8}{e^{3/2}}\right)$ er et topp- eller bunnpunkt:

:::{signchart-2}
width: 80%
function: exp(x)*(2*x - 1) * (2*x + 3), g'(x)
:::

Grafen til $g$ stiger før og synker etter $x = -\dfrac{3}{2}$ så dette svarer til et toppunkt. Grafen til $g$ synker før og stiger etter $x = \dfrac{1}{2}$ så dette svarer til et bunnpunkt. Dermed er koordinatene til toppunktet $\left(-\dfrac{3}{2}, \dfrac{8}{e^{3/2}}\right)$ og koordinatene til bunnpunktet $\left(\dfrac{1}{2}, 0\right)$.

::::


:::::::::::::



::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3 (4 poeng)
Løs likningene


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
3^{x + 2} - 5 = 76
$$


::::{answer}
$$
x = 2
$$
::::

::::{solution}
$$
3^{x + 2} - 5 = 76 \liff 3^{x + 2} = 81
$$

$$
3^{x + 2} = 3^4 \liff x + 2 = 4 \liff x = 2
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
$$
3 \lg x + 2 \lg x^2 + \lg \dfrac{1}{x^9} = 2.
$$


::::{answer}
$$
x = \dfrac{1}{10}
$$
::::

::::{solution}
For forenkler venstresiden med logaritmereglene:

$$
3 \lg x + 2 \lg x^2 + \lg \dfrac{1}{x^9} = 3 \lg x + 4 \lg x - 9 \lg x = -2 \lg x
$$

Altså har vi at

$$
-2\lg x = 2 \liff \lg x = -1 \liff x = 10^{-1} = \dfrac{1}{10}.
$$

::::
:::::::::::::



::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4 (4 poeng)
Bestem grenseverdiene 


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\lim\limits_{x\to 3} \dfrac{3(x^2 - 3)}{x - 3}
$$



::::{answer}
$$
\lim\limits_{x\to 3} \dfrac{3(x^2 - 3)}{x - 3} = \pm \infty
$$
::::

::::{solution}
Vi prøver å sette inn $x = 3$ direkte i uttrykket for å finne grenseverdien:
$$
\lim\limits_{x\to 3} \dfrac{3(x^2 - 3)}{x - 3} &= \dfrac{3\cdot (3^2 - 3)}{3 - 3} = \pm \infty
$$
::::
:::::::::::::



:::::::::::::{tab-item} b
$$
\lim\limits_{x\to 4} \dfrac{\sqrt{x} - 2}{x - 2}
$$


::::{answer}
$$
\lim\limits_{x\to 4} \dfrac{\sqrt{x} - 2}{x - 2} = \dfrac{1}{4}
$$
::::

::::{solution}
Vi får et $0/0$-uttrykk når vi setter inn $x = 4$, så vi bruker L'Hôpitals regel for å finne grenseverdien:

$$
\lim\limits_{x\to 4} \dfrac{\sqrt{x} - 2}{x - 2} = \lim\limits_{x\to 4} \dfrac{\dfrac{1}{2\sqrt{x}}}{1} = \dfrac{1}{4}.
$$
::::
:::::::::::::

::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 5 (2 poeng)
Funksjonen $f$ er gitt ved 

$$
f(x) = 
\begin{cases}
    x^2 + 2, && x \lt 0 \\
    \\
    2e^{x}, && x \geq 0 
\end{cases}
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør om $f$ er kontinuerlig i $x = 0$.


::::{answer}
$f$ er kontinuerlig i $x = 0$.
::::

::::{solution}
La $g(x) = x^2 + 2$ og $h(x) = 2e^x$. For at $f$ skal være kontinuerlig i $x = 0$, må

$$
g(0) = h(0)
$$

Vi finner først $g(0)$:

$$
g(0) = 0^2 + 2 = 2.
$$

Så finner vi $h(0)$:

$$
h(0) = 2e^0 = 2.
$$

Siden $g(0) = h(0)$, så er $f$ kontinuerlig i $x = 0$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Avgjør om $f$ er deriverbar i $x = 0$.


::::{answer}
$f$ er ikke deriverbar i $x = 0$.
::::

::::{solution}
Vi lar $g(x) = x^2 + 2$ og $h(x) = 2e^x$. For at $f$ skal være deriverbar i $x = 0$, må

$$
h'(0) = g'(0).
$$

Vi finner først $g'(0)$:

$$
g'(x) = 2x \liff g'(0) = 0.
$$

Så finner vi $h'(0)$:

$$
h'(x) = 2e^x \liff h'(0) = 2.
$$

Siden $h'(0) \neq g'(0)$, så er ikke $f$ deriverbar i $x = 0$.
::::



:::::::::::::
::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 6 (6 poeng)
Jelena, Nils og Ahmad spiller basketball. Tenk deg at vi legger et koordinatsytem over banen.

Ved et tidspunkt befinner Jelena seg i punktet $J(0, 0)$, Nils befinner seg i punktet $N(-1, 2)$ og Ahmad befinner seg i punktet $A(1, 1)$. 

Enheten langs aksene er meter.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvor langt er det mellom Nils og Ahmad?


:::::::::::::



:::::::::::::{tab-item} b
En basketball ligger i punktet $(-1, a)$ der $a \in \real$. Vektren som går fra Jelena til ballen er parallell med vektoren som går fra Nils til Ahmad.

Bestem $a$.

:::::::::::::


:::::::::::::{tab-item} c
Nils flytter seg til et punkt $M$. $M$ er det nærmeste punktet som er plassert slik at avstanden mellom Jelena og Nils er $\sqrt{10}$ meter. Vinkelen mellom Nils, Ahmad og Jelena, $\angle MAJ$, er $90$ grader.

Bestem koordinatene til $M$.
:::::::::::::


::::::::::::::


:::::::::::::::


## Del 2 (Med hjelpemidler – 3 timer)
# Anvendelser av derivasjon



## Topp- og bunnpunkter

:::::::::::::::{summary} Topp- og bunnpunkter
For å bestemme topp- og bunnpunkter til en funksjon $f$, gjør vi følgende:
1. Vi bestemmer ekstremalpunktene $x$ ved å løse likningen $f'(x) = 0$.
2. For å avgjøre om et ekstremalpunkt $x$ er et toppunkt eller bunnpunkt, kan vi bruke den andrederiverttesten:
   * Hvis $f''(x) > 0$, er punktet et bunnpunkt.
   * Hvis $f''(x) < 0$, er punktet et toppunkt.
   * Hvis $f''(x) = 0$, så kan vi ikke trekke noen konklusjon. 


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 1
Bestem koordinatene til eventuelle topp- og bunnpunkter for $f$ gitt ved

$$
f(x) = x^3 - 3x^2 + 4.
$$


::::{answer}
* Toppunkt i $(0, 4)$
* Bunnpunkt i $(2, 0)$
::::


:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 2
En funksjon $f$ er gitt ved

$$
f(x) = x^2 e^{-x}
$$

Bestem koordinatene til eventuelle topp- og bunnpunktene på grafen til $f$.


::::{answer}
Bunnpunkt i $(0, 0)$ og toppunkt i $\left(2, \dfrac{4}{e^2}\right)$.
::::

:::::::::::::::




---



## Tangenter

:::::::::::::::{summary} Tangenter
Tangenten til grafen til en funksjon $f$ i et punkt $(a, f(a))$ er gitt ved likningen

$$
y = f(a) + f'(a) \cdot (x - a)
$$


:::{plot}
width: 70%
function: (x**2 - 1) * exp(-x), f
xmin: -1.5
xmax: 4
ymin: -1.5
ymax: 1
ticks: off
point: (1.2, f(1.2))
tangent: 1.2, f
annotate: (0.5, 0.8), (1.6, 0.37), "Tangent"
text: 1.2, f(1.2), "$(a, f(a))$"
:::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
En funksjon $f$ er gitt ved

$$
f(x) = x^3 - 6x^2 + 2
$$

Bestem likningen for tangenten til grafen til $f$ i punktet $(1, f(1))$.

::::{answer}
$$
y = -9x + 6
$$
::::
:::::::::::::::


---




:::::::::::::::{exercise} Oppgave 4
En funksjon $f$ er gitt ved

$$
f(x) = \sqrt{x}
$$

Bestem likningen for tangenten til grafen til $f$ i punktet $(4, f(4))$.

::::{answer}
$$
y = \dfrac{1}{4}x + 1
$$
::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
En funksjon $f$ er gitt ved

$$
f(x) = \ln x
$$

Bestem likningen for tangenten til $f$ i punktet $(e, f(e))$.


::::{answer}
$$
y = \dfrac{1}{e}x
$$
::::

:::::::::::::::



## Vendepunkter og vendetangenter

:::::::::::::::{summary} Vendepunktene til en funksjon $f$
**Vendepunktene** er punkter på grafen til $f$ der $f''(x) = 0$. Det er punkter hvor grafen snur fra å være konkav til å bli konveks, eller omvendt. Se figuren nedenfor.
* En **vendetangent** er en tangent til grafen i et vendepunkt.
* Vendepunktene er punkter hvor grafen er **brattest** eller **slakest** (*lokalt* – opplagt er den mye brattere helt til venstre i figuren nedenfor).

:::{plot}
width: 70%
function: (x**2 - 1) * exp(-x), f
xmin: -1.5
xmax: 6
ymin: -1.5
ymax: 1
ticks: off
point: (2 + sqrt(3), f(2 + sqrt(3)))
point: (2 - sqrt(3), f(2 - sqrt(3)))
tangent: 2 + sqrt(3), f
tangent: 2 - sqrt(3), f
annotate: (2, -0.5), (2 + sqrt(3), f(2 + sqrt(3))), "Vendepunkter"
annotate: (2, -0.5), (2 - sqrt(3), f(2 - sqrt(3))), "Vendepunkter", -0.3
nocache:
:::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6
En funksjon $f$ er gitt ved

$$
f(x) = x^3 - 3x^2 + 8
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til vendepunktet til $f$.


::::{answer}
$$
(1, 6)
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem likningen til vendetangenten til $f$.


::::{answer}
$$
y = -3x + 9
$$
::::

:::::::::::::



::::::::::::::
:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 7
En funksjon $f$ er gitt ved

$$
f(x) = x e^x
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem eventuelle vendepunkter på grafen til $f$.


::::{answer}
$$
\left(-2, -\dfrac{2}{e^2}\right)
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem likningene til eventuelle vendetangenter til grafen til $f$.


::::{answer}
$$
y = -\dfrac{1}{e^2}x - \dfrac{4}{e^2}
$$
::::


:::::::::::::



::::::::::::::




:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 8
En funksjon $f$ er gitt ved

$$
f(x) = (x^2 + 1)e^{-x}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til eventuelle vendepunkter til $f$.


::::{answer}
$$
\left(1, \dfrac{2}{e}\right) \qog \left(3, \dfrac{10}{e^3}\right)
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem likningene til vendetangentene til $f$.


::::{answer}
* Vendetangent i $(1, f(1))$ er gitt ved $y = \dfrac{2}{e}$
* Vendetangent i $(3, f(3))$ er gitt ved $y = \dfrac{10}{e^3} - \dfrac{4}{e^3}(x - 3)$
::::


:::::::::::::


::::::::::::::



:::::::::::::::



---




## Blandede oppgaver


:::::::::::::::{exercise} Oppgave 9
En funksjon $f$ er gitt ved

$$
f(x) = (\ln x)^2 - 4 \ln x + 3
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem i hvilke punkter grafen til $f$ skjærer $x$-aksen.


::::{answer}
$$
x = e \or x = e^3
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem eventuelle topp- eller bunnpunkter på grafen til $f$.

::::{answer}
Bunnpunkt i $\left(e^2 , -1\right)$.
::::

:::::::::::::



::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 10
Nedenfor vises tre figurer der 
* Én figur viser grafen til $f$ 
* Én figur viser grafen til $f'$
* Én figur viser grafen til $f''$

Avgjør hvilken figur som viser grafen til $f$ og $f'$ og $f''$. 



:::{multi-plot}
width: 100%
functions: x*exp(-x), -2*exp(-x) + x*exp(-x), exp(-x) - x*exp(-x)
function-names: A, B, C
rows: 1
cols: 3
xmin: -1
xmax: 5
ymin: -0.7
ymax: 0.7
ticks: off
:::



::::{answer}
* Figur A viser $f$
* Figur C viser $f'$
* Figur B viser $f''$
::::



:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 11
En funksjon $f$ er gitt ved

$$
f(x) = 1 - x^2 \qder D_f = [0, 1].
$$


La $a \in \langle 0, 1 \rangle$ og la $O$ være origo.

En tangent til grafen til $f$ i punktet $P(a, f(a))$ skjærer $y$-aksen i et punkt $A$ og $x$-aksen i et punkt $B$. Se figuren nedenfor.


:::{plot}
width: 70%
function: 1 - x**2, f, (0, 1)
xmin: -0.2
xmax: 1.3
ymin: -0.3
ymax: 1.5
ticks: off
point: (3/5, f(3/5))
tangent: 3/5, f
point: (0, (3/5)**2 + 1)
point: (((3/5)**2 + 1) / (2*3/5), 0)
text: 3/5, f(3/5), "$P(a, f(a))$", top-right
text: 0, (3/5)**2 + 1, "$A$", bottom-left
text: ((3/5)**2 + 1) / (2*3/5), 0, "$B$", bottom-left
:::





::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til punktet $A$.

::::{answer}
$$
A = \left(0, a^2 + 1\right)
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem koordinatene til punktet $B$.


::::{answer}
$$
B = \left(\dfrac{a^2 + 1}{2a}, 0\right)
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Punktene $O$, $A$ og $B$ danner en trekant $\triangle OAB$. 

Bestem det *minste* mulige arealet $\triangle OAB$ kan ha.


::::{answer}
$$
A_\text{minst} = \dfrac{4\sqrt{3}}{9}
$$
::::
:::::::::::::


::::::::::::::



:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 12
Nedenfor vises tre figurer der 
* Én figur viser grafen til $f$ 
* Én figur viser grafen til $f'$
* Én figur viser grafen til $f''$

Avgjør hvilken figur som viser grafen til $f$ og $f'$ og $f''$. 



:::{multi-plot}
width: 100%
functions: (x**2 - 4*x + 1) * exp(-x), (-x**2 + 2*x + 1) * exp(-x), (x**2 - 1) * exp(-x)
function-names: A, B, C
rows: 1
cols: 3
xmin: -2
xmax: 5
ymin: -2
ymax: 6
ticks: off
:::



::::{answer}
* Figur C viser $f$
* Figur B viser $f'$
* Figur A viser $f''$
::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 13
En funksjon $f$ er gitt ved

$$
f(x) = -e^{2x} + 3e^x - 2
$$

Én av grafene nedenfor viser grafen til $f$. 

Avgjør hvilken graf som viser grafen til $f$.


:::{multi-plot}
width: 100%
functions: -exp(2*x) + 3*exp(x) - 2, exp(2*x) - 3*exp(x) + 2, x*(x - log(2)) * exp(-x), -x * (x - log(2)) * exp(-x)
function-names: A, B, C, D
rows: 2
cols: 2
ticks: off
ymax: 2
ymin: -2
xmin: -2
xmax: 3
:::


::::{answer}
Graf A viser grafen til $f$.
::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 14
For en funksjon $f$ vises fortegnslinjen til $f'(x)$.

Bestem hvilket ekstremalpunkt som er et bunnpunkt og hvilket som er et toppunkt.


:::{signchart}
width: 100%
function: (x - exp(1)) * (x + exp(1)), f'(x)
factors: false 
:::


::::{answer}
$x = -e$ er et toppunkt og $x = e$ er et bunnpunkt.
::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 15
En funksjon $f$ er kontinuerlig og dobbelt deriverbar for alle $x \in \mathbb{R}$.


Nedenfor vises noen påstander. Avgjør om påstanden er sann og husk å argumentere for å svaret ditt.



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Dersom $f'(a) = 0$ og $f''(a) > 0$, så har grafen til $f$ et bunnpunkt i punktet $(a, f(a))$.

::::{answer}
Påstanden er sann.
::::
:::::::::::::


:::::::::::::{tab-item} b
Dersom $f'(b) = 0$ og $f''(b) = 0$, så har grafen til $f$ et terrassepunkt i $(b, f(b))$.



::::{answer}
Påstanden er usann.
::::

:::::::::::::


:::::::::::::{tab-item} c
Dersom $f$ har to ekstremalpunkter $m_1, m_2 \in \langle a, b\rangle$, så finnes det *minst* ett punkt $c \in \langle a, b \rangle$ slik at

$$
f'(c) = \dfrac{f(b) - f(a)}{b - a}
$$

::::{answer}
Påstanden er sann.
::::
:::::::::::::



::::::::::::::

:::::::::::::::

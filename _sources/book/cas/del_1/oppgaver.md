# Krasjkurs 1

:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke CAS til å regne funksjoner og bestemme funksjonsverdier, den deriverte, ekstremalpunkter og ukjente koeffisienter.
* Kunne bruke CAS til å løse likninger, likningssystemer og ulikheter
* Kjenne til matematiske funksjoner i CAS som $\ln x$, $\log_a (x)$ og $e^x$. 
:::


## Funksjoner

Det er noen matematiske funksjoner i R1 som vi må kunne bruke i CAS. Her er en oversikt over de vi trenger:

| Funksjon | Notasjon i CAS | Eksempel |
|----------|----------------|----------|
| $\ln(x)$ | `ln(x)` | `ln(5)` |
| $\lg(x)$ | `lg(x)` | `lg(100)` gir $\lg(100)$ |
| $\log_a(x)$ | `log(a, x)` | `log(2, 8)` gir $\log_2 (8)$ |
| $e^x$ | `exp(x)` | `exp(3)` gir $e^3$ |


### Funksjonsverdier
Det er i blant nyttig å kunne regne ut funksjonsverdier $f(x)$, og det kan gjøres raskt og enkelt med CAS. 

:::::::::::::::{explore} Utforsk 1
I gif-en nedenfor regner vi ut $f(2)$ eksakt og numerisk for funksjonen

$$
f(x) = x \ln x
$$

Å regne ut **eksakte** verdier gjør vi med {ggb-icon}`mode_evaluate` – dette er det vi får som standard ved å bare trykke på enter <kbd style="font-size: 1.5em;">&#9166;</kbd>. Å regne ut **numeriske** verdier gjør vi ved å trykke på {ggb-icon}`mode_numeric`. 

:::{cas-popup}
---
layout: sidebar
---
:::


Bruk CAS-vinduet og følge eksempelet i gif-en.

:::{figure} ./gifer/funksjonsverdier_1.gif
---
class: no-click, adaptive-figure
width: 80%
---
Først defineres funksjon $f(x)$. Det er viktig å bruke `:=` og ikke bare `=` for at det skal bli en funksjon. Deretter regner vi ut $f(2)$ både eksakt og numerisk ved å bruke {ggb-icon}`mode_evaluate` og {ggb-icon}`mode_numeric`.
:::



:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 1
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


Bestem $f(3)$ eksakt og numerisk for

$$
f(x) = e^{x^2}
$$


::::{answer}
:::{figure} ./løsninger/underveisoppgave_1/a.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::



:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::


Bestem $g(5)$ eksakt og numerisk for

$$
g(x) = \lg(x + 10)
$$


::::{answer}
:::{figure} ./løsninger/underveisoppgave_1/b.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::

:::::::::::::


:::::::::::::{tab-item} c

:::{cas-popup}
---
layout: sidebar
---
:::


Bestem $h(-3)$ eksakt og numerisk for

$$
h(x) = \log_2(x^2 + 4)
$$


::::{answer}
:::{figure} ./løsninger/underveisoppgave_1/c.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::

:::::::::::::


::::::::::::::
:::::::::::::::


---

### Funksjonsverdier til $f'$ og $f''$

Vi kan også regne ut funksjonsverdier for den deriverte $f'$, eller den andrederiverte $f''$ for en gitt funksjon $f$. 

:::::::::::::::{explore} Utforsk 2
I gif-en nedenfor regner vi ut $f'(x)$, $f''(x)$, $f'(1)$ og $f''(1)$ for funksjonen

$$
f(x) = x^3 e^{-x}
$$

For å få den deriverte skriver vi bare `f'(x)` og for den andrederiverte `f''(x)`. 

:::{cas-popup}
---
layout: sidebar
---
:::


Bruk CAS-vinduet og følg eksempelet. 

:::{figure} ./gifer/funksjonsverdier_2.gif
---
class: no-click, adaptive-figure
width: 70%
---
:::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2
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
f(x) = x \ln (x + 1)
$$

1. Bestem $f'(x)$.
2. Bestem $f'(2)$ eksakt og numerisk.



::::{answer}
:::{figure} ./løsninger/underveisoppgave_2/a.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
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
g(x) = \dfrac{1}{1 + e^{-x}}
$$

1. Bestem $g'(x)$.
2. Bestem $g'(-2)$ eksakt og numerisk.


::::{answer}
:::{figure} ./løsninger/underveisoppgave_2/b.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
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
h(x) = e^{\sqrt{x + 1}}
$$

1. Bestem $h''(x)$
2. Bestem $h''(3)$ eksakt og numerisk.


::::{answer}
:::{figure} ./løsninger/underveisoppgave_2/c.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::

:::::::::::::


:::::::::::::{tab-item} d
:::{cas-popup}
---
layout: sidebar
---
:::


En funksjon $p$ er gitt ved

$$
p(x) = \log_2 (2x^2 + 4)
$$

1. Bestem $p''(x)$.
2. Bestem $p''(4)$ eksakt og numerisk.


::::{answer}
:::{figure} ./løsninger/underveisoppgave_2/d.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::

:::::::::::::


::::::::::::::
:::::::::::::::


---


### Bestemme $f(x)$ med likningssystem

I en del sammenhenger ønsker vi å bestemme koeffisientene til en funksjon $f$ gitt ved et funksjonsuttrykk med ukjente koeffisienter, før vi skal bruke funksjonen videre til å løse andre problemstillinger med funksjonen. Dette er det neste vi skal se på.



:::::::::::::::{explore} Utforsk 3


:::{plot}
align: right
width: 400
function: (x - 1)**2 - 4, f
point: (-2, f(-2))
point: (3, f(3))
point: (1, f(1)) 
text: -2, f(-2), "$(-2, 5)$", center-right
text: 1, f(1), "$(1, -4)$", bottom-center
text: 3, f(3), "$(3, 0)$", bottom-right
ticks: off
fontsize: 28
xmin: -4
:::



I figuren til høyre vises en andregradsfunksjon

$$
f(x) = ax^2 + bx + c
$$

sammen med noen punkter på grafen til $f$. 

:::{clear}
:::

I gif-en nedenfor vises det hvordan man bestemmer koeffisientene $a$, $b$ og $c$ med et likningssystem og setter de inn i $f(x)$. Oppskriften er:

1. Lag en **testfunksjon** $g(x)$ med de ukjente koeffisientene.
2. Løs et likningssystem for koeffisientene ved å bruke punktene på grafen til $f$.
3. Erstatt koeffisientene i testfunksjonen $g(x)$ med CAS-funksjonen `ByttUt` og definer $f(x)$ med det nye uttrykket.

:::{cas-popup}
---
layout: sidebar
---
:::


Prøv med CAS-vinduet og følg eksempelet i gif-en nedenfor.

:::{figure} ./gifer/bestemme_f.gif
---
class: no-click, adaptive-figure
width: 70%
---
Først definerer vi en testfunksjon $g(x)$ med de ukjente koeffisientene. Deretter lager vi et likningssystem og løser det med {ggb-icon}`mode_solve`. Til slutt bruker vi `ByttUt(uttrykk, liste med forandringer)` til å definere $f(x)$ med de riktige koeffisientene.
:::



:::::::::::::::



---




:::::::::::::::{exercise} Underveisoppgave 3

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{plot}
align: right
width: 100%
function: x**3 - 3*x + 2, f
point: (-1, f(-1))
text: -1, f(-1), "$(-1, 4)$", top-center
point: (1, f(1))
text: 1, f(1), "$(1, 0)$", bottom-center
point: (2, f(2))
text: 2, f(2), "$(2, 4)$", bottom-right
point: (-2, f(-2))
text: -2, f(-2), "$(-2, 0)$", top-left
ticks: off
fontsize: 28
ymin: -3
:::



I figuren til høyre vises grafen til en funksjon $f$ gitt ved

$$
f(x) = ax^3 + bx^2 + cx + d
$$

Bestem $f(x)$. 

:::{cas-popup}
:::



:::{clear}
:::


::::{answer}
:::{figure} ./løsninger/underveisoppgave_3/a.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::


:::::::::::::

:::::::::::::{tab-item} b
:::{plot}
align: right
width: 100%
function: 100 / (1 + 9 * exp(log(4/9) * x / 5)), f
point: (0, f(0))
point: (5, f(5))
ymax: 110
xmax: 30
ticks: off
text: 0, 10, "$(0, 10)$", top-left
text: 5, 20, "$(5, 20)$", bottom-right
fontsize: 28
:::



I figuren til høyre vises grafen til en funksjon $f$ gitt ved

$$
f(x) = \dfrac{100}{1 + a\cdot e^{-bx}}
$$


Bestem $f(x)$.


:::{cas-popup}
:::


:::{clear}
:::


::::{answer}
:::{figure} ./løsninger/underveisoppgave_3/b.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::



:::::::::::::


:::::::::::::{tab-item} c

:::{plot}
align: right
width: 100%
function: 2 * exp(-2*x) + 1, f
xmin: -1
ymin: -0.5
ymax: 4
point: (0, f(0))
point: (2, f(2))
text: 0, f(0), "$(0, 3)$", top-right
text: 2, f(2), "$\left(2, \displaystyle\frac{2}{e^4} + 1\right)$", top-center
ticks: off
fontsize: 28
:::



I figuren til høyre vises grafen til

$$
f(x) = a \cdot e^{-bx} + 1
$$


Bestem $f(x)$.


:::{cas-popup}
:::



:::{clear}
:::

::::{answer}
:::{figure} ./løsninger/underveisoppgave_3/c.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::



:::::::::::::



:::::::::::::{tab-item} d

:::{plot}
align: right
width: 100%
function: 2*(log(x) / log(3) - 1) * (log(x) / log(3) - 2), f
xmin: -1
xmax: 10
ymin: -2
point: (3, f(3))
point: (9, f(9))
point: (1, f(1))
text: 1, 4, "$(1, 4)$", top-right
text: 3, 0, "$(3, 0)$", bottom-left
text: 9, 0, "$(9, 0)$", top-center
ticks: off
fontsize: 28
:::


I figuren til høyre vises grafen til

$$
f(x) = a\cdot \left(\log_3 x\right)^2 + b \cdot \log_3 x + c
$$

Bestem $f(x)$.


:::{cas-popup}
:::


:::{clear}
:::

::::{answer}
:::{figure} ./løsninger/underveisoppgave_3/d.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::


:::::::::::::



::::::::::::::



:::::::::::::::



---


## Likninger
De fleste likningene vi jobber med vil være tilknyttet funksjoner. Denne typen problemstillinger egner seg godt for CAS. 

### Eksakt løsning


:::::::::::::::{explore} Utforsk 4

:::{plot}
align: right
width: 100%
function: exp(2*x) - 2*exp(x) - 8, f
ymin: -11
ymax: 10
xmin: -4
xmax: 4
ticks: off
fontsize: 28
:::


I figuren til høyre vises grafen til funksjonen

$$
f(x) = e^{2x} - 2e^{x} - 8
$$

Vi skal bestemme følgende eksakt:

1. Nullpunktet til $f$.
2. Koordinatene til bunnpunktet til $f$.



:::{clear}
:::

:::{cas-popup}
:::


Bruk CAS-vinduet og følg løsningen nedenfor – eller prøv selv først og sjekk løsningen etterpå! 

::::{solution}
---
dropdown: 0
---
1. Vi løser $f(x) = 0$ og $f'(x) = 0$ eksakt ved å bruke {ggb-icon}`mode_solve`. 
2. Så regner vi ut koordinatene til bunnpunktet til slutt ved å bruke løsningen av $f'(x) = 0$.

:::{figure} ./gifer/likninger_1.gif
---
class: no-click, adaptive-figure
width: 80%
---
:::


::::

:::::::::::::::






---


:::::::::::::::{exercise} Underveisoppgave 4

::::::::::::::{tab-set}
---
class: tabs-parts
---


:::::::::::::{tab-item} a
:::{plot}
align: right
width: 100%
function: (x**2 - 1) * exp(-x**2 + 1), f
ymax: 1
ymin: -3.5
xmin: -3
xmax: 3
ticks: off
fontsize: 28
lw: 3
:::

I figuren til høyre vises grafen til

$$
f(x) = (x^2 - 1)e^{-x^2 + 1}
$$

1. Bestem nullpunktene til $f$.
2. Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $f$.


:::{cas-popup}
:::


:::{clear}
:::

::::{answer}
:::{figure} ./løsninger/underveisoppgave_4/a.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::


:::::::::::::


:::::::::::::{tab-item} b

:::{plot}
align: right
width: 100%
function: (x**2 - 3) * exp(-x), g
xmin: -2.5
xmax: 6
ymin: -6
ymax: 4
ticks: off
lw: 3
fontsize: 28
:::


I figuren til høyre vises grafen til 

$$
g(x) = (x^2 - 3) e^{-x}
$$

1. Bestem nullpunktene til $g$.
2. Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $g$.

:::{cas-popup}
:::


:::{clear}
:::


::::{answer}
:::{figure} ./løsninger/underveisoppgave_4/b.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::



:::::::::::::


:::::::::::::{tab-item} c
:::{plot}
align: right
width: 100%
function: (log(x**2 + 4) - 1) / (log(x**2 + 4) + 1) - 1/2, h
fontsize: 28
lw: 3
ticks: off
ymin: -1
ymax: 1
xmin: -6
xmax: 6
:::


I figuren til høyre vises grafen til

$$
h(x) = \dfrac{\ln(x^2 + 4) - 1}{\ln(x^2 + 4) + 1} - \dfrac{1}{2}
$$

1. Bestem nullpunktene til $h$.
2. Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $h$.


:::{cas-popup}
:::


:::{clear}
:::


::::{answer}
:::{figure} ./løsninger/underveisoppgave_4/c.png
---
class: no-click, adaptive-figure
width: 100%
---
:::
::::



:::::::::::::


:::::::::::::{tab-item} d
:::{plot}
align: right
width: 100%
function: (log(x)/log(10))**2 - 3 * (log(x)/log(10)) + 2, p
ticks: off
xmin: -1
xmax: 120
ymin: -0.5
ymax: 2
fontsize: 28
lw: 3
:::


I figuren til høyre vises grafen til 

$$
p(x) = (\lg x)^2 - 3 \lg x + 2
$$

1. Bestem nullpunktene til $p$.
2. Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $p$.


:::{cas-popup}
:::



:::{clear}
:::

::::{answer}
:::{figure} ./løsninger/underveisoppgave_4/d.png
---
class: no-click, adaptive-figure
width: 100%
---
:::
::::


:::::::::::::


::::::::::::::


:::::::::::::::









### Numerisk løsning

::::{margin}
:::{figure} ./memes/løs_vs_nløs.png
---
class: no-click
width: 100%
---
:::
::::


Med noen likninger, vil det være **umulig** å få $x$ alene uansett hvor hardt vi prøver. Da er det numerisk løsning som er vår eneste utvei. 


:::::::::::::::{explore} Utforsk 5

:::{plot}
align: right
width: 100%
function: x**2 * exp(x) - 2, f
ticks: off
lw: 3
fontsize: 28
xmin: -4
xmax: 2
ymin: -3
ymax: 3
:::


I figuren til høyre vises grafen til 

$$
f(x) = x^2 e^{x} - 2
$$

Vi skal bestemme nullpunktet til $f$. 


:::{clear}
:::

:::{cas-popup}
:::


Bruk CAS-vinduet til å følge løsningen nedenfor. 

::::{solution}
---
dropdown: 0
---
Vi prøver å løse likningen $f(x) = 0$ eksakt med {ggb-icon}`mode_solve`, men da får vi `{?}` fordi det ikke er mulig å få $x$ alene. Derfor må vi bruke {ggb-icon}`mode_nsolve` for å finne løsningene numerisk. 


:::{figure} ./gifer/numerisk_løsning.gif
---
class: no-click, adaptive-figure
width: 70%
---
:::


::::



:::::::::::::::


:::::::::::::::{exercise} Underveisoppgave 5

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
:::{plot}
align: right
width: 100%
function: (x + 3) * log(x**2 + 1), f
fontsize: 28
lw: 3
ticks: off
:::


I figuren til høyre vises grafen til

$$
f(x) = (x+3) \ln (x^2 + 1)
$$

1. Bestem nullpunktene til $f$.
2. Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $f$.

:::{cas-popup}
:::


:::{clear}
:::


::::{answer}
:::{figure} ./løsninger/underveisoppgave_5/a.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::



:::::::::::::

:::::::::::::{tab-item} b
:::{plot}
align: right
width: 100%
function: x**3 * exp(-x**2 + 1) - 1/2, g
ticks: off
xmin: -4
xmax: 4
ymin: -2
ymax: 1.5
fontsize: 28
lw: 3
:::


I figuren til høyre vises grafen til 

$$
g(x) = x^3 e^{-x^2 + 1} - \dfrac{1}{2}
$$

1. Bestem nullpunktene til $g$ numerisk.
2. Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $g$ numerisk.

:::{cas-popup}
:::



:::{clear}
:::


::::{answer}
:::{figure} ./løsninger/underveisoppgave_5/b.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::


:::::::::::::



:::::::::::::{tab-item} c

:::{plot}
align: right
width: 100%
function: x**4 * log(x**2) - x**2 - 1, h
ticks: off
xmin: -2
xmax: 2
ymin: -3
ymax: 1.5
fontsize: 28
lw: 3
:::


I figuren til høyre vises grafen til

$$
h(x) = x^4 \ln(x^2 + 1) - x^2 - 1
$$

1. Bestem nullpunktene til $h$ numerisk.
2. Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $h$ numerisk.

:::{cas-popup}
:::


:::{clear}
:::




::::{answer}
:::{figure} ./løsninger/underveisoppgave_5/c.png
---
class: no-click, adaptive-figure
width: 80%
---
:::
::::


:::::::::::::


:::::::::::::{tab-item} d
:::{plot}
align: right
width: 100%
function: (x * exp(-x) + 2) / (log(x**2 + 1) + 1), p
xmin: -2.5
xmax: 6
ymin: -3
ymax: 3.5
ticks: off
lw: 3
fontsize: 28
:::

Figuren til høyre viser grafen til

$$
p(x) = \dfrac{x e^{-x} + 2}{\ln(x^2 + 1) + 1}
$$


1. Bestem nullpunktene til $p$ numerisk.
2. Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $p$ numerisk.


:::{cas-popup}
:::



:::{clear}
:::

::::{answer}
:::{figure} ./løsninger/underveisoppgave_5/d.png
---
class: no-click, adaptive-figure
width: 100%
---
:::
::::


:::::::::::::


::::::::::::::


:::::::::::::::


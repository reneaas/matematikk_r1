# Oppgavesamling 1

> Oppgaver der en CAS-knapp er vist, kan tenkes på som en "del 2"-oppgave

:::::::::::::::{exercise} Oppgave 1

Løs likningene

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
3 \cdot 2^x = 4 \cdot 5^{x}
$$


::::{answer}
$$
x = \dfrac{\ln 4 - \ln 3}{\ln 2 - \ln 5}
$$
::::

::::{solution}
$$
3 \cdot 2^x = 4 \cdot 5^x
$$

$$
\ln (3 \cdot 2^x) = \ln (4 \cdot 5^x)
$$

$$
\ln 3 + \ln 2^x = \ln 4 + \ln 5^x
$$

$$
\ln 3 + x \cdot \ln 2 = \ln 4 + x \cdot \ln 5
$$

$$
x \ln 2 - x \ln 5 = \ln 4 - \ln 3
$$

$$
x\left(\ln 2 - \ln 5\right) = \ln 4 - \ln 3
$$

$$
x = \dfrac{\ln 4 - \ln 3}{\ln 2 - \ln 5}
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
$$
e^{2x} - e^x - 6 = 0
$$


::::{answer}
$$
x = \ln 3
$$
::::

::::{solution}
Vi gjør variabelskifte $u = e^x$ slik at likningen kan skrives om til

$$
u^2 - u - 6 = 0
$$

Så løser vi likningen for $u$ med $abc$-formelen:

$$
u = \dfrac{1 \pm \sqrt{(-1)^2 - 4 \cdot 1 \cdot (-6)}}{2 \cdot 1} = \dfrac{1 \pm \sqrt{25}}{2} = \dfrac{1 \pm 5}{2}
$$

$$
u = -2 \or u = 3
$$

Da får vi 

$$
e^x = -2 \or e^x = 3
$$

Den første av de likningene har ingen løsningen siden vi ikke kan opphøye $e$ med noe som gir et negativt tall. Dermed får vi bare

$$
e^x = 3 \liff x = \ln 3
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\lg (x - 3) + \lg x = 1
$$


::::{answer}
$$
x = 5
$$
::::

::::{solution}
$$
\lg (x - 3) + \lg x = 1
$$

$$
\lg \left((x - 3) \cdot x\right) = 1
$$

$$
\lg (x^2 - 3x) = 1
$$

$$
x^2 - 3x = 10^1
$$

$$
x^2 - 3x - 10 = 0
$$

$$
x = \dfrac{3 \pm \sqrt{(-3)^2 - 4 \cdot 1 \cdot (-10)}}{2 \cdot 1} = \dfrac{3 \pm \sqrt{49}}{2} = \dfrac{3 \pm 7}{2}
$$

$$
x = -2 \or x = 5
$$

Vi må forkaste $x = -2$, fordi vi ikke kan ta logaritmen av et negativt tall – noe vi ville gjort i den opprinnelige likningen hvis vi satt i $x = -2$. Dermed får vi bare

$$
x = 5
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
$$
(\lg x)^2 + 3 \lg x - 4 = 0
$$


::::{answer}
$$
x = 10^{-4} \or x = 10^1
$$
::::

::::{solution}
Vi gjør variabelskifte $u = \lg x$ slik at vi får andregradslikningen

$$
u^2 + 3u - 4 = 0
$$

Så løser vi likningen for $u$ med $abc$-formelen:

$$
u = \dfrac{-3 \pm \sqrt{3^2 - 4 \cdot 1 \cdot (-4)}}{2 \cdot 1} = \dfrac{-3 \pm \sqrt{25}}{2} = \dfrac{-3 \pm 5}{2}
$$

$$
u = -4 \or u = 1
$$

Dermed får vi at

$$
\lg x = -4 \or \lg x = 1
$$

som gir

$$
x = 10^{-4} \or x = 10
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 2
Bestem grenseverdiene

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\lim_{x \to 2} \dfrac{x - 2}{x^3 - 8}
$$


::::{answer}
$$
\lim_{x \to 2} \dfrac{x - 2}{x^3 - 8} = \dfrac{1}{12}
$$
::::


::::{solution}
$$
\begin{align*}
    \lim_{x \to 2} \dfrac{x - 2}{x^3 - 8} & \overset{[\frac{0}{0}]}{=} \lim_{x \to 2} \dfrac{1}{3x^2} = \dfrac{1}{3 \cdot 2^2} = \dfrac{1}{12}
\end{align*}
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
$$
\lim_{x \to \infty} \dfrac{3x^2 + 4x + 1}{2x^2 - x + 5}
$$


::::{answer}
$$
\lim_{x \to \infty} \dfrac{3x^2 + 4x + 1}{2x^2 - x + 5} = \dfrac{3}{2}
$$
::::

::::{solution}
$$
\begin{align*}
    \lim_{x \to \infty} \dfrac{3x^2 + 4x + 1}{2x^2 - x + 5} & \overset{[\frac{\infty}{\infty}]}{=} \lim_{x \to \infty} \dfrac{6x + 4}{4x - 1} \overset{[\frac{\infty}{\infty}]}{=} \lim_{x \to \infty} \dfrac{6}{4} = \dfrac{3}{2}
\end{align*}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\lim_{x \to 0} \dfrac{e^x - e^{-x}}{x}
$$


::::{answer}
$$
\lim_{x \to 0} \dfrac{e^x - e^{-x}}{x} = 2
$$
::::

::::{solution}
$$
\begin{align*}
    \lim_{x \to 0} \dfrac{e^x - e^{-x}}{x} & \overset{[\frac{0}{0}]}{=} \lim_{x \to 0} \dfrac{e^x + e^{-x}}{1} = e^0 + e^0 = 2
\end{align*}
$$
::::




:::::::::::::

:::::::::::::{tab-item} d
$$
\lim_{x \to 1} \dfrac{\ln x}{x - 1}
$$


::::{answer}
$$
\lim_{x \to 1} \dfrac{\ln x}{x - 1} = 1
$$
::::


::::{solution}
$$
\begin{align*}
    \lim_{x \to 1} \dfrac{\ln x}{x - 1} & \overset{[\frac{0}{0}]}{=} \lim_{x \to 1} \dfrac{\frac{1}{x}}{1} = \dfrac{1}{1} = 1
\end{align*}
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    x^2 - 4 & \qhvis x < 2 \\
    \\
    ax + b & \qhvis x \geq 2
\end{cases}
$$

Bestem $a$ og $b$ slik at $f$ er kontinuerlig og deriverbar i $x = 2$.

::::{answer}
$$
a = 4 \and b = -8
$$
::::


::::{solution}
Vi lar $g(x) = x^2 - 4$ og $h(x) = ax + b$. Da er $f(x) = g(x)$ når $x < 2$ og $f(x) = h(x)$ når $x \geq 2$. For at $f$ skal være kontinuerlig i $x = 2$, må vi ha at

$$
g(2) = h(2) \liff 2^2 - 4 = a \cdot 2 + b \liff 0 = 2a + b
$$

For at $f$ skal være deriverbar i $x = 2$, må vi ha at

$$
g'(2) = h'(2) \liff 2 \cdot 2 = a \liff 4 = a
$$

Setter vi inn $a = 4$ i den første likningen, får vi

$$
0 = 2 \cdot 4 + b \liff b = -8
$$

Altså er $f$ kontinuerlig og deriverbar i $x = 2$ når

$$
a = 4 \and b = -8
$$




::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 4
Deriver funksjonene

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
f(x) = e^{4x} + \ln 3x + \pi
$$


::::{answer}
$$
f'(x) = 4e^{4x} + \dfrac{1}{x}
$$
::::

::::{solution}
$$
\begin{align*}
    f'(x) &= \left(e^{4x} + \ln 3x + \pi \right)' \\
    \\
    &= (e^{4x})' + (\ln 3x)' + (\pi)' \\
    \\
    &= 4e^{4x} + \dfrac{1}{x}
\end{align*}
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
$$
g(x) = x e^{-2x}
$$


::::{answer}
$$
g'(x) = (1 - 2x)e^{-2x}
$$
::::

::::{solution}
$$
\begin{align*}
    g'(x) &= \left(x e^{-2x}\right)' \\
    \\
    &= (x)' \cdot e^{-2x} + x \cdot (e^{-2x})' \\
    \\
    &= 1 \cdot e^{-2x} + x \cdot (-2e^{-2x}) \\
    \\
    &= e^{-2x} - 2xe^{-2x} \\
    \\
    &= (1 - 2x)e^{-2x}
\end{align*}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
h(x) = \dfrac{\ln x}{x}
$$


::::{answer}
$$
h'(x) = \dfrac{1 - \ln x}{x^2}
$$
::::

::::{solution}
$$
\begin{align*}
h'(x) &= \left(\dfrac{\ln x}{x}\right)' \\
\\
&= \dfrac{(\ln x)' \cdot x - \ln x \cdot (x)'}{x^2} \\
\\
&= \dfrac{\dfrac{1}{x} \cdot x - \ln x \cdot 1}{x^2} \\
\\
&= \dfrac{1 - \ln x}{x^2}
\end{align*}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
p(x) = \sqrt{\ln x}
$$


::::{answer}
$$
p'(x) = \dfrac{1}{2x\sqrt{\ln x}}
$$
::::

::::{solution}
$$
\begin{align*}
p'(x) &= \left(\sqrt{\ln x}\right)' \\
\\
&= \dfrac{1}{2\sqrt{\ln x}} \cdot (\ln x)' \\
\\
&= \dfrac{1}{2\sqrt{\ln x}} \cdot \dfrac{1}{x} \\
\\
&= \dfrac{1}{2x\sqrt{\ln x}}
\end{align*}
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---




:::::::::::::::{exercise} Oppgave 5
En funksjon $f$ er gitt ved

$$
f(x) = (x + 1)e^{-x}
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem eventuelle nullpunkter for $f$.


::::{answer}
$$
x = -1
$$
::::


::::{solution}
For å bestemme eventuelle nullpunkter for $f$, så løser vi likningen $f(x) = 0$:

$$
f(x) = 0 \liff (x + 1)e^{-x} = 0
$$

Da får vi at

$$
x + 1 = 0 \or e^{-x} = 0
$$

Den andre likningen har ingen løsning, siden $e^{-x}$ aldri er lik null. Dermed får vi bare

$$
x + 1 = 0 \liff x = -1
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $f$.

Husk å begrunne om punktene er topp- eller bunnpunkter.


::::{answer}
Toppunkt i $(0, 1)$. 
::::


::::{solution}
For å bestemme eventuelle topp- og bunnpunkter på grafen til $f$, løser vi $f'(x) = 0$. 

Først deriverer vi:

$$
\begin{align*}
f'(x) &= \left((x + 1)e^{-x}\right)' \\
\\
&= (x + 1)' \cdot e^{-x} + (x + 1) \cdot (e^{-x})' \\
\\
&= 1 \cdot e^{-x} + (x + 1) \cdot (-e^{-x}) \\
\\
&= e^{-x} - (x + 1)e^{-x} \\
\\
&= (1 - (x + 1))e^{-x} \\
\\
&= -x e^{-x}    
\end{align*}
$$

Så løser vi likningen $f'(x) = 0$:

$$
f'(x) = 0 \liff -x e^{-x} = 0
$$

Det gir oss at

$$
x = 0 \or e^{-x} = 0
$$

Den andre likningen har ingen løsning, siden $e^{-x}$ aldri er lik null. Dermed får vi bare

$$
x = 0
$$

For å avgjøre om det er et toppunkt eller bunnpunkt, kan vi tegne en fortegnslinje for $f'(x)$:

:::{signchart}
width: 100%
function: -x * exp(-x), f'(x)
:::

> Her er $e^x$ vist som en av faktorene i fortegnsskjema ovenfor, så skyldes at $e^{-x} = \dfrac{1}{e^x}$ 

Altså stiger grafen før $x = 0$ og synker etter. Dermed har vi et toppunkt i $x = 0$. For å finne $y$-verdien, setter vi inn i $f$:

$$
f(0) = (0 + 1)e^{0} = 1
$$

Altså har grafen til $f$ et toppunkt i $(0, 1)$.

::::

:::::::::::::


::::::::::::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 6
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En funksjon $f$ er gitt ved

$$
f(x) = e^{-2x} + \dfrac{1}{5}x^5 - 2\pi
$$

Bestem likningen for tangenten til grafen til $f$ i punktet $(0, f(0))$.

::::{answer}
$$
y = -2x + 1 - 2\pi
$$
::::


::::{solution}
Likningen til tangenten er gitt ved 

$$
y = f(0) + f'(0)\cdot (x - 0) = f(0) + f'(0) \cdot x.
$$

Vi har at 

$$
f(0) = e^{-2\cdot 0} + \dfrac{1}{5}\cdot 0^5 - 2\pi = 1 + 0 - 2\pi 1 - 2\pi
$$

Så deriverer vi for å bestemme $f'(0)$. Da har vi 

$$
\begin{align*}
f'(x) &= \left(e^{-2x} + \dfrac{1}{5}x^5 - 2\pi\right)' \\
\\
&= (e^{-2x})' + \left(\dfrac{1}{5}x^5\right)' - (2\pi)' \\
\\
&= -2e^{-2x} + \dfrac{1}{5}\cdot 5 x^4 - 0 \\
\\
&= -2e^{-2x} + x^4
\end{align*}
$$

Så regner vi ut $f'(0)$:

$$
f'(0) = -2e^{-2\cdot 0} + 0^4 = -2 \cdot 1 + 0 = -2
$$

Dermed er likningen til tangenten gitt ved

$$
y = f(0) + f'(0)x = 1 - 2\pi - 2x = -2x + 1 - 2\pi
$$
::::


:::::::::::::



:::::::::::::{tab-item} b
En funksjon $g$ er gitt ved

$$
g(x) = xe^{-x} + 1
$$


Bestem likningen for tangenten til grafen til $g$ i $(2, g(2))$.


::::{answer}
$$
y = -\dfrac{1}{e^2}x + \dfrac{4}{e^2} + 1
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
En funksjon $h$ er gitt ved

$$
h(x) = \ln (x^2 + e^2)
$$

Bestem liknngen til tangenten til grafen til $h$ i punktet $(e, h(e))$.

::::{answer}
$$
y = \dfrac{1}{e}x + \ln 2 + 1
$$
::::


:::::::::::::




::::::::::::::






:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 7

:::{cas-popup}
---
layout: sidebar
---
:::



En influensaepidemi bryter ut på en videregående skole med 1000 elever. I starten er det få smittede, men antallet øker raskt. Antallet smittede elever $S(t)$ etter $t$ dager er tilnærmet gitt ved

$$
S(t) = \dfrac{300}{1 + 28 \cdot e^{-0.3t}}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvor lang tid tar det før 100 elever er smittet?


::::{answer}
Det tar omtrent 9 dager før 100 elever er smittet.
::::

::::{solution}
For å avgjøre hvor lang tid det tar før 100 elever er smittet, så kan vi løse likningen

$$
S(t) = 100
$$

Vi bruker CAS til å løse likningen:


:::{figure} ./figurer/oppgave_6/a.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Altså vil det ta omtrent $9$ dager før 100 elever er smittet.


::::


:::::::::::::


:::::::::::::{tab-item} b 
På hvilket tidspunkt blir flest smittet?

Omtrent hvor mange elever blir smittet den dagen?


::::{answer}
* Flest blir smittet etter ca. 11 dager. 
* På den dagen blir omtrent 23 elever smittet.
::::


::::{solution}
For å avgjøre når flest blir smittet, så må vi vite når "stigningen" til grafen er størst. Det vil være i vendepunktet til grafen til $S$, så vi kan bestemme ved å løse likningen

$$
S''(t) = 0
$$

Vi gjør det med CAS og får: 

:::{figure} ./figurer/oppgave_6/b_1.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Altså vil flest elever bli smittet etter omtrent $11$ dager.

For å finne omtrent hvor mange elever som blir smittet på dette tidspunktet, så regner vi ut $S'(t)$ på dette tidspunktet (siden det gir oss "stigningen" eller da antall som smittes per dag – på den dagen):

:::{figure} ./figurer/oppgave_6/b_2.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Altså får vi at omtrent $23$ elever smittes den dagen.

::::

:::::::::::::


:::::::::::::{tab-item} c
Undersøk om $S$ har asymptoter, og forklar hvilken praktisk tolkning asymptotene eventuelt har.



::::{solution}
For å undersøke om $S$ har noen asymptoter, er det enklest å merke seg at

$$
\lim_{t \to \infty} e^{-0.3 t} = 0 \and \lim_{t \to -\infty} e^{-0.3 t} = \infty
$$

Da får vi at

$$
\lim_{t \to \infty} S(t) = \lim_{t \to \infty} \dfrac{300}{1 + 28 \cdot e^{-0.3t}} = \dfrac{300}{1 + 28 \cdot 0} = 300
$$

og 

$$
\lim_{t \to -\infty} S(t) = \lim_{t \to -\infty} \dfrac{300}{1 + 28 \cdot e^{-0.3t}} = \dfrac{300}{1 + 28 \cdot \infty} = 0
$$

Den første grenseverdien forteller oss at maksimalt 300 elever kan bli smittet i løpet av epidemien, mens den andre grenseverdien forteller oss at ingen var smittet lenge før epidemien startet.

Funksjonen vil ellers ikke ha noen vertikale asymptoter fordi vi ikke kan få nevneren til å bli null på noe vis.


::::

:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 8
En funksjon $f$ er gitt ved

$$
f(x) = \dfrac{1}{2}e^x (2x - 1)^2
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem eventuelle nullpunkter til $f$.

::::{answer}
$$
x = \dfrac{1}{2}
$$
::::
:::::::::::::


:::::::::::::{tab-item} b
Vis at 

$$
f'(x) = \dfrac{1}{2}e^x (2x - 1)(2x + 3)
$$
:::::::::::::



:::::::::::::{tab-item} c
Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $f$.

::::{answer}
* Toppunkt i $\left(-\dfrac{3}{2}, \dfrac{8}{\sqrt{e^3}}\right)$
* Bunnpunkt i $\left(\dfrac{1}{2}, 0\right)$
::::

:::::::::::::



::::::::::::::

:::::::::::::::


---



:::{margin} Tips: Oppgave 9
For å angripe oppgaver av denne typen kan det være lurt å først se etter hva som skiller de ulike grafene fra hverandre. Deretter kan du velge å undersøke egenskaper som:
* Nullpunkter
* Topp- og bunnpunkter
* Asymptoter

Bruk de egenskapene som lar deg skille mellom de ulike grafene.
:::



:::::::::::::::{exercise} Oppgave 9
En funksjon $f$ er gitt ved

$$
f(x) = (1 - x^2) e^x
$$

Hvilken figur nedenfor viser grafen til $f$?

:::{multi-plot}
width: 100%
functions: (x**2 - 1) * exp(x), (x**2 - 1) * exp(-x), (1 - x**2) * exp(-x), (1 - x**2) * exp(x)
function-names: A, B, C, D
rows: 2
cols: 2
ticks: off
ymin: -4
ymax: 4
:::


::::{answer}
Graf D. 
::::


::::{solution}
Vi kan se at grafene har ulik oppførsel når $x\to \infty$ og når $x \to -\infty$. Derfor kan det være hensiktsmessig å sjekke disse grensene først:

$$
\lim_{x \to \infty} f(x) = \lim_{x \to \infty} (1 - x^2)e^x = -\infty
$$

Det er bare graf D som går mot $-\infty$ når $x \to \infty$. Dermed må graf D vise grafen til $f$.
::::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 10
Anna og Bjørn ser på eksponentiallikningen

$$
2^x = a
$$

Nedenfor vises løsningene til Anna og Bjørn for å bestemme $x$:


::::{grid}
---
gutter: 3
---
:::{grid-item-card}

**Annas løsning**
^^^

$$
2^x = a
$$

$$
\log_2 2^x = \log_2 a
$$

$$
x = \log_2 a
$$
:::

:::{grid-item-card}
**Bjørns løsning**
^^^

$$
2^x = a
$$

$$
\ln 2^x = \ln a
$$

$$
x \ln 2 = \ln a
$$

$$
x = \dfrac{\ln a}{\ln 2}
$$
:::
::::

Bruk løsningene til Anna og Bjørn til å finne en sammenheng mellom $\ln a$ og $\log_2 a$.


::::{answer}
$$
\log_2 a = \dfrac{\ln a}{\ln 2}
$$
::::


::::{solution}
Siden løsningen til likningen kan skrives på to måter:

$$
x = \log_2 a \and x = \dfrac{\ln a}{\ln 2}
$$

så må det bety at

$$
\log_2 a = \dfrac{\ln a}{\ln 2}
$$
::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 11
En funksjon $f$ er gitt ved

$$
f(x) = \log_2 x + 8
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---


:::::::::::::{tab-item} a
Bestem $f'(x)$.


::::{hints}
Tenk på sammenhengen mellom $\log_2 x$ og $\ln x$ som du fant i oppgave 10 og bruk denne til å bestemme $f'(x)$. 
::::


::::{answer}
$$
f'(x) = \dfrac{1}{x \ln 2}
$$
::::


::::{solution}
Fra oppgave 8 vet vi at

$$
\log_2 x = \dfrac{\ln x}{\ln 2}
$$

Dermed har vi at

$$
f(x) = \log_2 x + 8 = \dfrac{\ln x}{\ln 2} + 8
$$

Deriverer vi dette, får vi

$$
\begin{align*}
f'(x) &= \left(\dfrac{\ln x}{\ln 2} + 8\right)' \\
\\
&= \dfrac{1}{\ln 2} \cdot (\ln x)' + (8)' \\
\\
&= \dfrac{1}{\ln 2} \cdot \dfrac{1}{x} + 0 \\
\\
&= \dfrac{1}{x \ln 2}
\end{align*}
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
Bestem likningen for tangenten til grafen til $f$ i punktet $(4, f(4))$. 


::::{answer}
$$
y = \dfrac{1}{4 \ln 2} \left(x - 4\right) + 10
$$
::::


::::{solution}
Likningen for tangenten i et punkt $a$ vil være

$$
y = f'(a)\cdot (x - a) + f(a)
$$

Her er $a = 4$, så vi får

$$
y = f'(4) \cdot (x - 4) + f(4)
$$

Vi har at 

$$
f(4) = \log_2 4 + 8 = 2 + 8 = 10
$$

og

$$
f'(4) = \dfrac{1}{4 \ln 2}
$$

Dermed blir likningen til tangenten

$$
y = f'(4) \cdot (x - 4) + f(4) = \dfrac{1}{4 \ln 2} \left(x - 4\right) + 10
$$
::::

:::::::::::::
::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 12
:::{plot}
align: right
width: 350
function: -x + 5 - 1 / (x - 1) ** 2, f
ticks: off
vline: 1
line: -1, 5
ymax: 20
ymin: -20
lw: 4
fontsize: 30
:::

Grafen til en funksjon $f$ er vist i figuren til høyre.


:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Nedenfor vises fire alternativer om egenskaper ved grafen til $f$. Kun én av de stemmer – hvilken?


::::{grid} 1 1 2 2
---
gutter: 2
---
:::{grid-item-card}
**Alternativ 1**
^^^

$$
\begin{align*}
\lim_{x \to 1^+} f(x) &= \infty \\
\\
\lim_{x \to -\infty} \left(f(x) - x\right) &= 5
\end{align*}
$$
:::

:::{grid-item-card}
**Alternativ 2**
^^^

$$
\begin{align*}
\lim_{x \to 1^-} f(x) &= -\infty \\
\\
\lim_{x \to \infty} \left(f(x) + x\right) &= 5 \\
\end{align*}
$$
:::

:::{grid-item-card}
**Alternativ 3**
^^^

$$
\begin{align*}
\lim_{x \to 1^+} f(x) &= \infty \\
\\
\lim_{x \to \infty} \left(f(x) - (x - 5)\right) &= 0 \\
\end{align*}
$$
:::

:::{grid-item-card}
**Alternativ 4**
^^^

$$
\begin{align*}
\lim_{x \to 1^-} f(x) &= -\infty \\
\\
\lim_{x \to \infty} \left(f(x) - x\right) &= 5 \\
\end{align*}
$$
:::


::::

::::{answer}
Alternativ 2
::::


::::{solution}
Hvis en linje $y = ax + b$ er en skrå asymptote for en funksjon $f$, så må 

$$
\lim_{x \to \pm \infty} \left(f(x) - (ax + b)\right) = 0
$$

Alternativ 2 viser denne betingelsen skrevet på en litt annen måte, men vi kan skrive den om: 


$$
\lim_{x \to \infty} \left(f(x) + x\right) = 5
$$

$$
\lim_{x \to \infty} \left(f(x) + x - 5\right) = 0
$$

$$
\lim_{x \to \infty} \left(f(x) - (-x + 5)\right) = 0
$$

Altså er linjen $y = -x + 5$ en skrå asymptote. Dette passer med figuren. I tillegg skal $f(x) \to -\infty$ når $x \to 1^-$, som også stemmer med figuren. Dermed er alternativ 2 riktig.

::::



:::::::::::::


:::::::::::::{tab-item} b
Én av figurene nedenfor viser grafen til $f'$. Bestem hvilken.

::::{multi-plot2}
---
rows: 2
cols: 2
ymin: -10
ymax: 10
ticks: off
lw: 3.5
fontsize: 30
---

:::{plot}
function: 1 + 2 / (x - 1)**3, A
vline: 1
hline: 1
:::

:::{plot}
function: 1 - 2 / (x - 1)**3, B
vline: 1
hline: 1
:::

:::{plot}
function: -1 + 2 / (x - 1)**3, C
vline: 1
hline: -1
:::

:::{plot}
function: -1 - 2 / (x - 1)**3, D
vline: 1
hline: -1
:::




::::


::::{answer}
Graf C.
::::


::::{solution}
Grafen til $f$ synker *før* den vertikale asymptoten og stiger etter. Det betyr at den deriverte må være negativ før og positiv etter. I tillegg så må $f'(x) \to -1$ når $x\to \pm\infty$ siden dette var stigningstallet til den skrå asymptoten. Disse kriteriene er oppfylt av graf C. 
::::

:::::::::::::


::::::::::::::






:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 13
En funksjon $f$ er gitt ved

$$
f(x) = \dfrac{2x - 3}{e^x}
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem i hvilke punkter grafen til $f$ skjærer $x$-aksen.

::::{answer}
$$
x = \frac{3}{2}
$$
::::


::::{solution}
$$
f(x) = 0 \liff 2x - 3 = 0 \liff x = \dfrac{3}{2}
$$
::::



:::::::::::::



:::::::::::::{tab-item} b
Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $f$.

::::{answer}
Toppunkt i $\left(\dfrac{5}{2}, \dfrac{2}{e^{5/2}}\right)$
::::


::::{solution}
Vi må løse $f'(x) = 0$ for å se etter kandidater for topp- og bunnpunkter. Vi deriverer først:

$$
\begin{align*}
f'(x) &= \left(\dfrac{2x - 3}{e^x}\right)' = \left((2x - 3)e^{-x}\right)' \\
\\
&= (2x - 3)' \cdot e^{-x} + (2x - 3) \cdot (e^{-x})' \\
\\
&= 2 \cdot e^{-x} + (2x - 3) \cdot (-e^{-x}) \\
\\
&= 2e^{-x} - (2x - 3)e^{-x} \\
\\
&= (2 - (2x - 3))e^{-x} \\
\\
&= (5 - 2x)e^{-x}
\end{align*}
$$

Så løser vi likningen $f'(x) = 0$:

$$
5 - 2x = 0 \liff 2x = 5 \liff x = \dfrac{5}{2}
$$

For å avgjøre om dette er et topp- eller bunnpunkt, kan vi tegne en fortegnslinje for $f'(x)$:

:::{signchart}
width: 100%
function: (5 - 2*x) * exp(-x), f'(x)
:::

Fra fortegnslinja til $f'(x)$ ser vi at grafen til $f$ først stiger og deretter synker etter punktet, som betyr at $x = \dfrac{5}{2}$ gir et toppunkt. For å finne $y$-verdien, setter vi inn i $f$:

$$
f\left(\dfrac{5}{2}\right) = \dfrac{2 \cdot \dfrac{5}{2} - 3}{e^{5/2}} = \dfrac{5 - 3}{e^{5/2}} = \dfrac{2}{e^{5/2}}
$$

Altså har grafen til $f$ et toppunkt i $\left(\dfrac{5}{2}, \dfrac{2}{e^{5/2}}\right)$.


::::


:::::::::::::


::::::::::::::

:::::::::::::::



---


::::{margin} Tips: Oppgave 14
Når det står `h = 1e-6`{l=python} i programmet, så betyr det at `h`{l=python} er satt til $10^{-6}$. Det har ikke noe med Eulers tall $e$ å gjøre. 
::::


:::::::::::::::{exercise} Oppgave 14
Anna har skrevet programmet nedenfor.


Bestem en eksakt verdi for verdien programmet skriver ut når det kjøres. 

Kjør programmet og sjekk svaret ditt.

:::{interactive-code}
---
predict:
---
def f(x):
    return (20 - x**2) ** 0.5

x = 2
h = 1e-6

dfdx = (f(x + h) - f(x)) / h
print(dfdx)
:::


::::{answer}
Programmet skriver ut en numerisk tilnærming til

$$
f'(2) = -\dfrac{1}{2}
$$
::::


::::{solution}
Programmet finner en tilnærming til $f'(2)$ som vi kan se fra linje 7 der det står

```python
dfdx = (f(x + h) - f(x)) / h
```

og fra linje 4 og 5 der `x = 2`{l=python} og `h = 1e-6`{l=python} er definert. Funksjonen $f$ er gitt ved 

$$
f(x) = \sqrt{20 - x^2}
$$

Så vi bestemmer $f'(x)$ først og deretter regner ut $f'(2)$. 

$$
\begin{align*}
f'(x) &= \left(\sqrt{20 - x^2}\right)' \\
\\
&= \dfrac{1}{2\sqrt{20 - x^2}} \cdot (20 - x^2)' \\
\\
&= \dfrac{1}{2\sqrt{20 - x^2}} \cdot (-2x) \\
\\
&= \dfrac{-2x}{2\sqrt{20 - x^2}} \\
\\
&= \dfrac{-x}{\sqrt{20 - x^2}} 
\end{align*}
$$

Så setter vi inn $x = 2$: 


$$
\begin{align*}
f'(2) &= \dfrac{-2}{\sqrt{20 - 2^2}} \\
\\
&= \dfrac{-2}{\sqrt{20 - 4}} \\
\\
&= \dfrac{-2}{\sqrt{16}} \\
\\
&= \dfrac{-2}{4} \\
\\
&= -\dfrac{1}{2}
\end{align*}
$$

Altså vil programmet skrive ut en tilnærming til 

$$
f'(2) = -\dfrac{1}{2}
$$
::::


:::::::::::::::




---


:::::::::::::::{exercise} Oppgave 15
En funksjon $f$ er gitt ved


$$
f(x) = e^{x} + 3e^{-x} - 4
$$

Hvilken graf nedenfor viser grafen til $f$?


:::{multi-plot}
width: 100%
functions: exp(2 * x) - 4 * exp(x) + 3, exp(x) + 3*exp(-x) - 4, -(exp(x) + 3*exp(-x) - 4), -(exp(2 * x) - 4 * exp(x) + 3)
function-names: A, B, C, D
rows: 2
cols: 2
ticks: off
:::


::::{answer}
Graf B.
::::


::::{solution}
Vi kan se at det som skiller grafene er hva som skjer med $y$-verdien når $x \to -\infty$. Vi undersøker derfor denne grensen: 

$$
\lim_{x \to -\infty} f(x) = \lim_{x \to -\infty} \left(e^{x} + 3e^{-x} - 4\right) = 0 + \infty - 4 = \infty
$$

Altså går $f(x) \to \infty$ når $x \to -\infty$. Dette skjer bare for graf B. Dermed må graf B vise grafen til $f$.

::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 16

:::{cas-popup}
---
layout: sidebar
---
:::


Antall rotter som har forvillet seg inn i Jul i Vinterland kan antas å følge en modell på formen

$$
R(x) = \dfrac{500}{1 + ae^{-bx}}
$$

der $a$ og $b$ er konstanter, og $x$ er antall dager etter 1. desember. Vi antar at det var 20 rotter den 1. desember og at antall rotter etter 5 dager vil være 100.  


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$ og $b$.

::::{answer}
$$
a = 24 \and b = \dfrac{1}{5} \ln 6
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $R'(5)$ og gi en praktisk tolkning av svaret.

::::{answer}
$$
R'(5) \approx 28.67
$$

som betyr at det kom omtrent 29 nye rotter til Jul i Vinterland i løpet av dag 5.
::::
:::::::::::::


:::::::::::::{tab-item} c
Hvilken dag i desember vil det komme flest rotter til Jul i Vinterland? Hvor mange rotter kom inn til Jul i Vinterland den dagen?

::::{answer}
Etter ca. 9 dager, så den 10.desember. Da kom det ca. 45 rotter til Jul i Vinterland.
::::

:::::::::::::



:::::::::::::{tab-item} d
Hvor mange rotter vil kan det maksimalt bli, ifølge modellen?

::::{answer}
500
::::

:::::::::::::


::::::::::::::




:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 17

:::{cas-popup}
---
layout: sidebar
---
:::



I figuren nedenfor vises grafen til en funksjon $f$ som er gitt ved 

$$
f(x) = a (\log_2 x - b) (\log_2 x - c) \qder b < c
$$


Bestem $a$, $b$ og $c$.


:::{plot}
width: 70%
function: 3 * (log(x) / log(2) - 1) * (log(x) / log(2) - 2)
xmin: -1
xmax: 10
ymin: -2
ymax: 10
:::


::::{answer}
$$
a = 3 \and b = 1 \and c = 2
$$
::::

::::{solution}
Vi har at $f(2) = 0$ og $f(4) = 0$. Vi har også at 

$$
f(x) = 0 \liff a(\log_2 x - b) (\log_2 x - c) = 0
$$

som betyr at 

$$
\log_2 x = b \or \log_2 x = c
$$

For det første nullpunktet får vi 

$$
\log_2 2 = b \liff b = 1
$$

Og for det andre nullpunktet får vi 

$$
\log_2 4 = c \liff c = 2
$$

Da har vi at 

$$
f(x) = a \left(\log_2 x - 1\right)(\log_2 x - 2)
$$

Så ser vi at grafen går gjennom $(1, 6)$ som betyr at 

$$
f(1) = 6 \liff a \cdot (\log_2 1 - 1)(\log_2 1 - 2) = 6 
$$

som gir

$$
a\cdot (-1) \cdot (-2) = 6 
$$

$$
2a = 6 \liff a = 3
$$

Altså er 

$$
a = 3 \and b = 1 \and c = 2
$$
::::



:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 18
:::{plot}
align: right
width: 350
function: x * exp(-x**2), f
ticks: off
ymin: -1
ymax: 1
xmin: -4
xmax: 4
fontsize: 30
lw: 4
:::


I figuren til høyre vises grafen til en funksjon $f$.

Avgjør hvilken av grafene nedenfor som viser grafen til $f'$. 


::::{multi-plot2}
---
rows: 2
cols: 2
ymin: -2
ymax: 2
xmin: -4
xmax: 4
fontsize: 26
lw: 3.5
ticks: off
---

:::{plot}
function: -(1 - 2*x**2) * exp(-x**2), A
:::


:::{plot}
function: (2*x**2 - 1)**2 * exp(-x**2), B
:::


:::{plot}
function: (1 - 2*x**2) * exp(-x**2), C
:::


:::{plot}
function: -(2*x**2 - 1)**2 * exp(-x**2), D
:::


::::

::::{answer}
Graf C 
::::


::::{solution}
Grafen til $f$ har et vendepunkt i $x = 0$. Det betyr at den deriverte $f'$ må ha et ekstremalpunkt der. Siden grafen til $f$ stiger raskest der, betyr det at den deriverte må ha et toppunkt. Dette passer med graf B og C.

Vi kan se at grafen til $f$ bare har to ekstremalpunkter, som betyr at $f'$ bare kan ha to nullpunkter. Dette stemmer bare med graf C. 

Graf C viser derfor grafen til $f'$. 
::::




:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 19
Anna jobber med en funksjon $f$ gitt ved

$$
f(x) = -(\ln x)^2 + \ln x + 6
$$

Anna har skrevet programmet nedenfor.

:::{code-block} python
---
linenos:
---
def f(x):
    from math import log
    return -log(x)**2 + log(x) + 6


x = 0.001
h = 1e-6
while (f(x + h) - f(x)) / h > 0:
    x = x + 0.01

print(x)
:::

Bestem en eksakt verdi for verdien programmet skriver ut når det kjøres.


::::{answer}
$$
x = \sqrt{e}
$$
::::


::::{solution}
Programmet kjører så lenge $f'(x) > 0$ som vi kan se fra linje 8 der det står

```python
while (f(x + h) - f(x)) / h > 0:
    ...
```

der det er brukt at 

$$
f'(x) \approx \dfrac{f(x + h) - f(x)}{h}
$$

Programmet stopper når $x$ blir stor nok til at $f'(x) \leq 0$ som betyr at vi øker verdien til $x$ frem til grafen til $f$ ikke lenger stiger, men begynner å synke. Programmet bestemmer derfor $x$-koordinaten til et toppunkt. For å bestemme den eksakte verdien til verdien programmet skriver ut når det kjøres, løser vi derfor $f'(x) = 0$. Vi deriverer først:

$$
\begin{align*}
f'(x) &= \left(-(\ln x)^2 + \ln x + 6\right)' \\
\\
&= -2 \ln x \cdot \dfrac{1}{x} + \dfrac{1}{x} + 0 \\
\\
&= \dfrac{-2 \ln x + 1}{x}
\end{align*}
$$

Så løser vi likningen $f'(x) = 0$:

$$
\dfrac{-2 \ln x + 1}{x} = 0 \liff -2 \ln x + 1 = 0 
$$

$$
2 \ln x = 1 \liff \ln x = \dfrac{1}{2}
$$

som betyr at

$$
x = e^{1/2} = \sqrt{e}
$$

Programmet skriver altså ut en tilnærming til $x = \sqrt{e}$.
::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 20
Nedenfor vises en grenseverdi.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem grenseverdien dersom den eksisterer.

$$
\lim_{x \to -2} \dfrac{x^2 - x + 2}{x^2 - 2x - 8}
$$


::::{answer}
$$
\lim_{x \to -2} \dfrac{x^2 - x + 2}{x^2 - 2x - 8} = \pm\infty
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
1. Bestem $a$ slik at grenseverdien eksisterer

$$
\lim_{x \to -2} \dfrac{x^2 + ax + 2}{x^2 - 2x - 8}
$$


2. Bestem grenseverdien for denne verdien av $a$.


::::{answer}
$$
a = 3 \qog \lim_{x \to -2} \dfrac{x^2 + 3x + 2}{x^2 - 2x - 8} = \dfrac{1}{6}
$$
::::


:::::::::::::


::::::::::::::





:::::::::::::::




---


:::::::::::::::{exercise} Oppgave 21

:::{plot}
align: right
width: 350
function: log(x**2 + 1) / (exp(x**2 - 1)), f
xmin: -3
xmax: 3
ymin: -1
ymax: 1
fontsize: 30
lw: 4
ticks: off
:::


I figuren til høyre vises grafen til en funksjon $f$. 

Nedenfor vises fire figurer der én viser grafen til $f'$ og én viser grafen til $f''$. 

Bestem hvilken figur som viser $f'$ og hvilken som viser $f''$.



::::{multi-plot2}
---
rows: 2
cols: 2
xmin: -3
xmax: 3
ticks: off
lw: 3.5
fontsize: 26
---

:::{plot}
function: ( -2*x * log(x**2 + 1) * exp(x**2 - 1) + 2*x * exp(x**2 - 1) / (x**2 + 1) ) / exp(x**2 - 1)**2, A
ymin: -2
ymax: 2
:::

:::{plot}
function: -( -2*x * log(x**2 + 1) * exp(x**2 - 1) + 2*x * exp(x**2 - 1) / (x**2 + 1) ) / exp(x**2 - 1)**2, B
ymin: -2
ymax: 2
:::

:::{plot}
function: -(-2 * log(x**2 + 1) + 6 * x**4 * log(x**2 + 1) + 4 * x**6 * log(x**2 + 1) - 8 * x**4 - 10 * x**2 + 2) / ((1 + 2 * x**2 + x**4) * exp(x**2 - 1)), C 
ymin: -8
ymax: 8
:::

:::{plot}
function: (-2 * log(x**2 + 1) + 6 * x**4 * log(x**2 + 1) + 4 * x**6 * log(x**2 + 1) - 8 * x**4 - 10 * x**2 + 2) / ((1 + 2 * x**2 + x**4) * exp(x**2 - 1)), D
ymin: -8
ymax: 8
:::





::::

::::{answer}
* Figur A viser grafen til $f'$
* Figur D viser grafen til $f''$
::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 22

:::{cas-popup}
---
layout: sidebar
---
:::



I figuren nedenfor vises kurven til en *ellipse* der punktene $(x, y)$ på kurven oppfyller likningen

$$
x^2 + \dfrac{y^2}{4} = 1
$$

Et rektangel med hjørner $(x, y)$, $(-x, y)$, $(x, -y)$ og $(-x, -y)$ er innskrevet i ellipsen.

Bestem $x$ og $y$ slik at arealet av rektangelet er størst mulig.


:::{plot}
width: 70%
ellipse: (0, 0), 1, 2, blue
point: (sqrt(2)/2, 2 * sqrt(1 - 1/2))
point: (-sqrt(2)/2, 2 * sqrt(1 - 1/2))
point: (sqrt(2)/2, -2 * sqrt(1 - 1/2))
point: (-sqrt(2)/2, -2 * sqrt(1 - 1/2))
polygon: [(sqrt(2)/2, 2 * sqrt(1 - 1/2)), (-sqrt(2)/2, 2 * sqrt(1 - 1/2)), (-sqrt(2)/2, -2 * sqrt(1 - 1/2)), (sqrt(2)/2, -2 * sqrt(1 - 1/2))]
text: sqrt(2)/2, 2 * sqrt(1 - 1/2), "$(x, y)$", top-right
text: -sqrt(2)/2, 2 * sqrt(1 - 1/2), "$(-x, y)$", top-left
text: sqrt(2)/2, -2 * sqrt(1 - 1/2), "$(x, -y)$", bottom-right
text: -sqrt(2)/2, -2 * sqrt(1 - 1/2), "$(-x, -y)$", bottom-left
axis: equal
ticks: off
:::


::::{answer}
$$
x = \dfrac{\sqrt{2}}{2} \and y = \sqrt{2}
$$
::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 23
Bjørn jobber med funksjonen

$$
f(x) = 
\begin{cases}
    \dfrac{x - 9}{\sqrt{x} - 3} & \qhvis x \neq 9 \\
    \\
    a & \qhvis x = 9
\end{cases}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$ slik at $f$ er kontinuerlig i $x = 9$.


::::{answer}
$$
a = 6
$$
::::


::::{solution}
$f$ er kontinuerlig i $x = 9$ dersom

$$
\lim_{x \to 9} f(x) = f(9) = a
$$

Vi regner ut grenseverdien: 


$$
\begin{align*}
\lim_{x \to 9} f(x) &= \lim_{x \to 9} \dfrac{x - 9}{\sqrt{x} - 3} \\
\\
&= \lim_{x \to 9} \dfrac{(\sqrt{x} - 3)(\sqrt{x} + 3)}{\sqrt{x} - 3} \\
\\
&= \lim_{x \to 9} (\sqrt{x} + 3) \\
\\
&= \sqrt{9} + 3 \\
\\
&= 3 + 3 \\
\\
&= 6
\end{align*}
$$

Altså må $a = 6$ for at $f$ skal være kontinuerlig i $x = 9$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bjørn har skrevet programmet nedenfor. 

:::{code-block} python
---
linenos:
---
def f(x):
    if x != 9:
        return (x - 9) / (x**0.5 - 3)
    else:
        return a


h = 1e-6
x = 9

dfdx = (f(x + h) - f(x)) / h
print(dfdx)
:::

Hva er det Bjørn prøver å regne ut med programmet? 


Bestem en eksakt verdi for verdien programmet skriver ut når det kjøres med riktig verdi for $a$.


::::{answer}
$$
f'(9) = \dfrac{1}{6}
$$
::::


::::{solution}
Programmet prøver å regne ut $f'(9)$ som vi kan se fra linje 11 der det står

```python
dfdx = (f(x + h) - f(x)) / h
```

og fra linje 8 og 9 der `h = 1e-6`{l=python} og `x = 9`{l=python} er definert. Vi kan bestemme den eksakte verdien for verdien programmet skriver ut når det kjøres ved å bruke definisjonen av den deriverte: 

$$
\begin{align*}
f'(9) &= \lim_{x \to 9} \dfrac{f(x) - f(9)}{x - 9} \\
\\
&= \lim_{x \to 9} \dfrac{\dfrac{x - 9}{\sqrt{x} - 3} - 6}{x - 9} \\
\\
&= \lim_{x \to 9} \dfrac{\dfrac{x - 9 - 6(\sqrt{x} - 3)}{\sqrt{x} - 3}}{x - 9} \\
\\
&= \lim_{x \to 9} \dfrac{x - 9 - 6\sqrt{x} + 18}{(x - 9)(\sqrt{x} - 3)} \\
\\
&= \lim_{x \to 9} \dfrac{x - 6\sqrt{x} + 9}{(x - 9)(\sqrt{x} - 3)} \\
\\
&= \lim_{x \to 9} \dfrac{(\sqrt{x} - 3)^2}{(x - 9)(\sqrt{x} - 3)} \\
\\
&= \lim_{x \to 9} \dfrac{\sqrt{x} - 3}{x - 9} \\
\\
&= \lim_{x \to 9} \dfrac{\sqrt{x} - 3}{(\sqrt{x} - 3)(\sqrt{x} + 3)} \\
\\
&= \lim_{x \to 9} \dfrac{1}{\sqrt{x} + 3} \\
\\
&= \dfrac{1}{\sqrt{9} + 3} \\
\\
&= \dfrac{1}{3 + 3} \\
\\
&= \dfrac{1}{6}
\end{align*}
$$

Altså skriver programmet ut en tilnærming til 

$$
f'(9) = \dfrac{1}{6}
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 24

:::{cas-popup}
---
layout: sidebar
---
:::


Ifølge Newtons avkjølingslov vil temperaturen $T$ til et objekt etter $t$ minutter være

$$
\ln (T - T_0) = -k\cdot t + r
$$

hvor $T_0$ er romtemperaturen, og $k$ og $r$ er konstanter.

I et rom med temperatur $22 \degree \mathrm{C}$ setter vi en kopp med kaffe. Ved tidspunktet $t = 0$ er temperaturen i kaffen $96 \degree \mathrm{C}$, og etter 10 minutter er temperaturen $70 \degree \mathrm{C}$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis at 

$$
T(t) = T_0 + e^{-kt + r}
$$


:::::::::::::


:::::::::::::{tab-item} b
Bestem $T_0$, $k$ og $r$. 


::::{answer}
$$
T_0 = 22 \and k = -\dfrac{3 \ln 2 + \ln 3 - \ln 37}{10} \and r = \ln 2 + \ln 37
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Hvor lang tid vil det ta før temperaturen i kaffen er mindre enn $30 \degree \mathrm{C}$?


::::{answer}
ca. 51 minutter.
::::

:::::::::::::


:::::::::::::{tab-item} d
Når vil temperaturen synke med $1 \, \degree \mathrm{C}$ per minutt?


::::{answer}
Etter ca. 27 minutter.
::::


:::::::::::::


::::::::::::::




:::::::::::::::





---



:::::::::::::::{exercise} Oppgave 25

:::{plot}
align: right
width: 350
function: (x**2 - 9)**4, (0, 3), f
xmin: -0.5
xmax: 3.5
ymin: -200
ymax: 7000
ticks: off
polygon: (0, 0), (1, 0), (1, f(1)), (0, f(1))
point: (0, 0)
point: (1, 0)
point: (1, f(1))
point: (0, f(1))
text: 1, f(1), "$(t, f(t))$", top-right
fontsize: 30
lw: 3.5
:::

Anna jobber med en oppgave om en funksjon $f$ og har laget seg figuren som er vist til høyre. 
Funksjonen $f$ er gitt ved

$$
f(x) = (x^2 - 9)^4 \qfor x \in \langle 0, 3 \rangle
$$

Anna har skrevet programmet nedenfor.

:::{clear}
:::

:::{code-block} python
---
linenos:
---
def A(x):
    return x * (x**2 - 9) ** 4


t = 0
dt = 0.01

while A(t) < A(t + dt):
    t = t + dt

print(t)
:::

1. Forklar hva Anna prøver å finne ut med programmet.
2. Bestem en eksakt verdi for verdien programmet skriver ut når det kjøres.


::::{answer}
1. Anna prøver å bestemme hvilken verdi for $t$ som gir størst evrdi for arealet av rektangelet.
2. Den eksakte verdien for $t$ som gir størst areal er $t = 1$. 
::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 26


:::{cas-popup}
---
layout: sidebar
---
:::



En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    2x^2 + 3x + a & \qhvis x < 1 \\
    \\
    -2x^2 + bx & \qhvis x \geq 1
\end{cases}
$$


Bestem $a$ og $b$ slik at $f$ er deriverbar i $x = 1$


::::{answer}
$$
a = 4 \and b = 11
$$
::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 27

:::{plot}
align: right
width: 350
function: exp(-x**2), f
point: (-1, 0)
point: (-1, f(-1))
point: (1, 0)
point: (1, f(1))
polygon: (-1, 0), (-1, f(-1)), (1, f(1)), (1, 0)
ymin: -0.2
ymax: 1.5
xmin: -3
xmax: 3
ticks: off
fontsize: 30
lw: 4
text: 1, 0, "$a$", bottom-center
text: -1, 0, "$-a$", bottom-center
:::


I figuren til høyre vises grafen til 

$$
f(x) = e^{-x^2}
$$

og et rektangel som er innskrevet under grafen.

Bestem det største mulige arealet et slikt rektangel kan ha.


:::{clear}
:::

::::{answer}
$$
\sqrt{\dfrac{2}{e}}
$$
::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 28
:::{cas-popup}
---
layout: sidebar
---
:::


En funksjon $f$ er gitt ved

$$
f(x) =
\begin{cases}
    a(x - 2)^2 + b &\qhvis x < 0 \\
    \\
    cx + 1 &\qhvis 0 \leq x < 2 \\
    \\
    -x^3 + dx^2 + 1 &\qhvis x \geq 2
\end{cases}
$$


Bestem $a$, $b$, $c$ og $k$ slik at $f$ er deriverbar i $x = 0$ og $x = 2$.

::::{answer}
$$
a = -1 \and b = 5 \and c = 4 \and d = 4
$$
::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 29

:::{plot}
align: right
width: 350
function: 3*x - 4 - 1/(x + 1), f
ticks: off
ymin: -20
ymax: 20
line: 3, -4
vline: -1
fontsize: 30
lw: 4
:::



Grafen til en funksjon $f$ er vist i figuren til høyre.


Nedenfor vises fire alternativer med mulige egenskaper for grafen til $f'$. 

Kun ett alternativ stemmer – hvilket?

<br><br><br><br> <br>

::::{grid} 1 2 2 2
---
gutter: 2
---

:::{grid-item-card}
**Alternativ 1**
^^^

$$
\begin{align*}
\lim_{x \to -1^-} f'(x) &= \infty \\
\\
\lim_{x\to -1^+} f'(x) &= -\infty \\
\\
\lim_{x \to -\infty} f'(x) &= 3
\end{align*}
$$
:::

:::{grid-item-card}
**Alternativ 2**
^^^

$$
\begin{align*}
\lim_{x \to -1^-} f'(x) &= -\infty \\
\\
\lim_{x\to -1^+} f'(x) &= -\infty \\
\\
\lim_{x \to \infty} f'(x) &= -3
\end{align*}
$$
:::


:::{grid-item-card}
**Alternativ 3**
^^^

$$
\begin{align*}
\lim_{x \to -1^-} f'(x) &= \infty \\
\\
\lim_{x\to -1^+} f'(x) &= \infty \\
\\
\lim_{x \to -\infty} f'(x) &= 3
\end{align*}
$$
:::


:::{grid-item-card}
**Alternativ 4**
^^^

$$
\begin{align*}
\lim_{x \to -1^-} f'(x) &= \infty \\
\\
\lim_{x\to -1^+} f'(x) &= \infty \\
\\
\lim_{x \to \infty} f'(x) &= -3
\end{align*}
$$
:::



::::


::::{answer}
Alternativ 3
::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 30

:::{plot}
align: right
width: 350
function: exp(-x**2), f'
ticks: off
ymin: -1.5
ymax: 1.5
xmin: -3
xmax: 3
fontsize: 30
lw: 3.5
:::


Grafen til $f'$ er vist i figuren til høyre.

Nedenfor vises fire grafer der én viser grafen til $f$ og én viser grafen til $f''$.

Bestem hvilken graf som viser $f$ og hvilken som viser $f''$.


::::{multi-plot2}
---
rows: 2
cols: 2
ticks: off
xmin: -3
xmax: 3
ymin: -1.5
ymax: 1.5
lw: 3.5
fontsize: 30
---

:::{plot}
function: 1/2 * erf(x), A
:::

:::{plot}
function: -2*x * exp(-x**2), B
:::

:::{plot}
function: -1/2 * erf(x), C
:::

:::{plot}
function: 2*x * exp(-x**2), D
:::



::::




::::{answer}
* Figur A viser grafen til $f$
* Figur B viser grafen til $f''$
::::






:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 31
En funksjon $f$ er gitt ved

$$
f(x) =
\begin{cases}
    \sqrt{x + a} &\qhvis -a < x < 0 \\
    \\
    x^2 + bx + 4 &\qhvis x \geq 0
\end{cases}
$$


Bestem $a$ og $b$ slik at $f$ er deriverbar i $x = 0$.


::::{answer}
$$
a = 16 \and b = \dfrac{1}{8}
$$
::::

:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 32
:::{cas-popup}
---
layout: sidebar
---
:::

En funksjon $f$ er gitt ved

$$
f(x) = 6x - x^2 \qfor x \in [0, 6]
$$

Nedenfor vises grafen til $f$ sammen med et rektangel $ABCD$.

I rektangelet er $A(a, 0)$ og $D(a, f(a))$ der $a \in \langle 0, 3\rangle$. Punktet $C$ ligger på grafen til $f$.

Bestem $a$ slik at arealet av rektangelet $ABCD$ er størst mulig.

:::{plot}
width: 70%
function: 6*x - x**2, (0, 6), f
polygon: (1, 0), (1, f(1)), (5, f(5)), (5, 0)
xmin: -1
ymin: -1
ymax: 10
xmax: 7
ticks: off
point: (1, 0)
point: (1, f(1))
point: (5, f(5))
point: (5, 0)
text: 1, 0, "$A$", bottom-left
text: 1, f(1), "$D$", top-left
text: 5, f(5), "$C$", top-right
text: 5, 0, "$B$", bottom-right
:::



::::{answer}
$$
a = -\sqrt{3} + 3
$$
::::





:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 33

:::{cas-popup}
---
layout: sidebar
---
:::



En funksjon $f$ er gitt ved


$$
f(x) = 
\begin{cases}
    2x^2 - 3x - 2 &\qhvis x \leq a \\
    \\
    x^2 + x + 3 &\qhvis x > a
\end{cases}
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
For hvilke verdier av $a$ er $f$ kontinuerlig?


::::{answer}
$$
a = -1 \or a = 5
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Undersøk om $f$ er deriverbar i $x = a$ for verdiene av $a$ du fant. 


::::{answer}
$f$ er ikke deriverbar for verdiene noen av verdiene. 
::::
:::::::::::::


::::::::::::::

:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 34
:::{cas-popup}
---
layout: sidebar
---
:::


Fire byer $A$, $B$, $C$ og $D$ ligger plassert slik at de danner et kvadrat med sidelengde $10$ km. 

Vi skal lage en veiforbindelse mellom disse fire byene. Veilengden mellom de fire byene blir kortest mulig dersom vi lager veiene via to punkter $E$ og $F$. Se figuren nedenfor.

Vi lar $x$ være avstanden mellom $E$ og $F$. 

Bestem $x$ slik at den samlede veilengden mellom byene blir kortest mulig.


:::{plot}
width: 70%
point: (0, 0)
point: (10, 0)
point: (10, 10)
point: (0, 10)
axis: off
axis: equal
point: (5, 2)
point: (5, 8)
line-segment: (0, 0), (5, 2)
line-segment: (10, 0), (5, 2)
line-segment: (10, 10), (5, 8)
line-segment: (0, 10), (5, 8)
line-segment: (5, 2), (5, 8)
line-segment: (0, 0), (10, 0), dashed, gray
line-segment: (10, 0), (10, 10), dashed, gray
line-segment: (10, 10), (0, 10), dashed, gray
line-segment: (0, 10), (0, 0), dashed, gray
text: 0, 0, "$A$", bottom-left
text: 10, 0, "$B$", bottom-right
text: 10, 10, "$C$", top-right
text: 0, 10, "$D$", top-left
text: 5, 2, "$E$", bottom-center
text: 5, 8, "$F$", top-center
text: 5, 5, "$x$", center-right
text: 2.5, 1, "$s$", top-left
text: 10 - 2.5, 1, "$s$", top-right
text: 2.5, 9, "$s$", bottom-left
text: 10 - 2.5, 9, "$s$", bottom-right
text: 5, 0, "$10$", bottom-center
text: 10, 5, "$10$", center-right
:::



::::{answer}
$$
x = \dfrac{-10\sqrt{3} + 30}{3}
$$
::::




:::::::::::::::















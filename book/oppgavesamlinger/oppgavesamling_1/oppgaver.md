# Oppgavesamling 1



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
    \lim_{x \to \infty} \dfrac{3x^2 + 4x + 1}{2x^2 - x + 5} & \overset{[\frac{0}{0}]}{=} \lim_{x \to \infty} \dfrac{6x + 4}{4x - 1} \overset{[\frac{0}{0}]}{=} \lim_{x \to \infty} \dfrac{6}{4} = \dfrac{3}{2}
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

Den første grenseverdien forteller oss at maksimalt 300 elever kan bli smittet i løpet av epidemien, mens den andre grenseverdien forteller oss at ingen var smittet lenge før epidemien startet (*duh*).

Funksjonen vil ellers ikke ha noen vertikale asymptoter fordi vi ikke kan få nevneren til å bli null på noe vis.


::::

:::::::::::::


::::::::::::::
:::::::::::::::


---



:::{margin} Tips: Oppgave 7
For å angripe oppgaver av denne typen kan det være lurt å finne ut en del om funksjonen først. Prøv å se etter 
* Nullpunkter
* Topp- og bunnpunkter
* Asymptoter
:::



:::::::::::::::{exercise} Oppgave 7
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
For å avgjøre hvilken figur som viser grafen til $f$, så bør vi finne ut mer om funksjonen. Vi tar utgangspunkt i bestemme
1. Nullpunkter
2. Topp- og bunnpunkter
3. Eventuelle asymptoter

Det er ikke sikkert vi trenger alt dette, men det er en liten sjekkliste vi kan ta utgangspunkt i.

Vi starter med nullpunkter. Vi bestemmer nullpunktene ved å løse likningen

$$
f(x) = 0 \liff (1 - x^2) e^x = 0
$$

Det gir oss at

$$
1 - x^2 = 0 \or e^x = 0
$$

Den andre likningen har ingen løsning, siden $e^x$ aldri er lik null. Dermed får vi bare

$$
1 - x^2 = 0 \liff x^2 = 1 \liff x = \pm 1
$$

Så går vi videre for å bestemme eventuelle topp- og bunnpunkter ved å løse likningen

$$
f'(x) = 0 
$$

Først trenger vi den deriverte:

$$
\begin{align*}
f'(x) &= \left((1 - x^2) e^x\right)' \\
\\
&= (1 - x^2)' \cdot e^x + (1 - x^2) \cdot (e^x)' \\
\\
&= (-2x) \cdot e^x + (1 - x^2) \cdot e^x \\
\\
&= (-2x + 1 - x^2) e^x \\
\\
&= (-x^2 - 2x + 1) e^x
\end{align*}
$$

Så løser vi likningen $f'(x) = 0$:

$$
f'(x) = 0 \liff (-x^2 - 2x + 1) e^x = 0
$$

Det gir oss at

$$
-x^2 - 2x + 1 = 0 \or e^x = 0
$$

Igjen, den andre likningen har ingen løsning, siden $e^x$ aldri er lik null. Dermed får vi bare

$$
-x^2 - 2x + 1 = 0 \liff x^2 + 2x - 1 = 0
$$

Vi løser denne med $abc$-formelen:

$$
x = \dfrac{-2 \pm \sqrt{2^2 - 4 \cdot 1 \cdot (-1)}}{2 \cdot 1} = \dfrac{-2 \pm \sqrt{8}}{2} = -1 \pm \sqrt{2}
$$

Vi har derfor to kandidater for topp- og bunnpunkter, men vi trenger å avgjøre hvilket som er et toppunkt og hvilket som er et bunnpunkt. Vi kan gjøre dette ved å tegne en fortegnslinje for $f'(x)$:

:::{signchart}
width: 100%
function: (-x**2 - 2*x + 1) * exp(x), f'(x)
:::

Fra fortegnslinja til $f$ så ser vi at grafen til $f$ synker før $x = -1 - \sqrt{2}$, stiger mellom $x = -1 - \sqrt{2}$ og $x = -1 + \sqrt{2}$, og synker igjen etter $x = -1 + \sqrt{2}$. Dermed har vi et bunnpunkt i $x = -1 - \sqrt{2}$ og et toppunkt i $x = -1 + \sqrt{2}$.


Altså vet vi nå at

* Grafen har nullpunkter i $x = -1$ og $x = 1$.
* Grafen har et bunnpunkt i $x = -1 - \sqrt{2}$.
* Grafen har et toppunkt i $x = -1 + \sqrt{2}$.

Fra informasjonen vi nå har hentet ut om grafen til $f$ så kan vi se at toppunktet må ligge mellom nullpunktene, mens bunnpunktet ligger på nedsiden av $x = -1$. Den første biten passer med både graf C og D, men det er bare graf D som oppfyller begge punkter. 

Derfor er graf D grafen til $f$.

::::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8
Anna og Bjørn ser på eksponentiallikningen

$$
2^x = a
$$

Nedenfor vises løsningene til Anna og Bjørn for å bestemme $x$:


::::{grid}
---
gutter: 3
---
:::{grid-item-card} Annas løsning

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

:::{grid-item-card} Bjørns løsning

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


:::::::::::::::{exercise} Oppgave 9
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
Tenk på sammenhengen mellom $\log_2 x$ og $\ln x$ som du fant i oppgave 8 og bruk denne til å bestemme $f'(x)$. 
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


:::::::::::::::{exercise} Oppgave 10
Om en funksjon $f$ får du vite at 

$$
\begin{align*}
    & \lim\limits_{x \to \pm\infty} \left(f(x) - (x + 1)\right) = 0 \\
    \\
    & \lim\limits_{x \to 1^-} f(x) = -\infty && \lim\limits_{x \to 1^+} f(x) = \infty 
\end{align*}
$$

Avgjør hvilken av figurene nedenfor som viser grafen til $f$.

Husk å begrunne svaret ditt. 


:::{multi-plot}
width: 100%
functions: -x + 1 + 1/(x - 1), x + 1 + 1/(x - 1), -x + 1 - 1/(x - 1)**2, x + 1 - 1/(x - 1)
function-names: A, B, C, D
rows: 2
cols: 2
ticks: off
lines: [(-1, 1), (1, 1), (-1, 1), (1, 1)]
vlines: 1, 1, 1, 1
ymax: 10
ymin: -10
:::


::::{answer}
Figur B viser grafen til $f$.
::::


::::{solution}
Den første egenskapen

$$
\lim\limits_{x \to \pm\infty} \left(f(x) - (x + 1)\right) = 0 
$$

forteller oss at grafen til $f$ har en skrå asymptote gitt ved linjen $y = x + 1$. Dette stemmer for graf B og D.

Den andre egenskapen 

$$
\lim\limits_{x \to 1^-} f(x) = -\infty \and \lim\limits_{x \to 1^+} f(x) = \infty 
$$

forteller oss at grafen til $f$ har en vertikal asymptote i $x = 1$ der grafen synker mot $-\infty$ på venstre side og stiger mot $+\infty$ på høyre side. Dette stemmer bare for graf B.

Dermed er graf B grafen til $f$.
::::



:::::::::::::::




---


:::::::::::::::{exercise} Oppgave 11
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
Vi ser at alle grafene har nullpunkter omtrent på samme sted, så det vil ikke være så nyttig å undersøke eventuelle nullpunkter for grafen. Vi kan derimot Se etter:
1. Eventuelle topp- og bunnpunkter
2. Asymptoter

siden disse to vil være forskjellig for de ulike grafene. 

Vi starter med å se etter eventuelle topp- eller bunnpunkter:

$$
\begin{align*}
f'(x) &= \left(e^{x} + 3e^{-x} - 4\right)' \\
\\
&= (e^{x})' + (3e^{-x})' - (4)' \\
\\
&= e^{x} - 3e^{-x} \\
\end{align*}
$$

Så løser vi likningen $f'(x) = 0$:

$$
e^x - 3e^{-x} = 0 \liff e^x = 3e^{-x} \liff e^{2x} = 3
$$

som gir at

$$
2x = \ln 3 \liff x = \dfrac{\ln 3}{2}
$$

Så må vi avgjøre om dette er et toppunkt eller bunnpunkt. Dette er kanskje enklest å gjøre ved å bruke den andrederiverte, så vi bestemmer $f''(x)$:


$$
\begin{align*}
f''(x) &= (e^{x} - 3e^{-x})' \\
\\
&= (e^{x})' - 3(e^{-x})' \\
\\
&= e^{x} + 3e^{-x} \\
\end{align*}
$$

både $e^x$ og $e^{-x}$ er alltid positive, så det betyr at $f''(x) > 0$ for alle $x$. Da *må* grafen være konveks som betyr at grafen har et bunnpunkt. Dette passer med graf A og B. Det mest vesentlig som skiller de to grafene er at graf A har en horisontal asymptote når $x \to -\infty$, mens graf B ikke har det. Så da bare sjekker vi hva som skjer med $f(x)$ når $x \to -\infty$:


$$
\lim_{x \to -\infty} f(x) = \lim_{x \to -\infty} \left(e^{x} + 3e^{-x} - 4\right) = 0 + \infty - 4 = \infty
$$

Dermed vil ikke $f$ ha en horisontal asymptote når $x \to -\infty$. Men da kan ikke $f$ være graf A, så da må graf B være grafen til $f$.

::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 12

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



:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 13
:::{plot}
align: right
width: 100%
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


:::{multi-plot}
width: 100%
functions: -(1 - 2*x**2) * exp(-x**2), (2*x**2 - 1)**2 * exp(-x**2),(1 - 2*x**2) * exp(-x**2), -(2*x**2 - 1)**2 * exp(-x**2)
function-names: A, B, C, D
rows: 2
cols: 2
ticks: off
ymin: -2
ymax: 2
xmin: -4
xmax: 4
:::


::::{answer}
Graf C 
::::




:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 14
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
while f(x + h) - f(x) > 0:
    x = x + 0.01

print(x)
:::

Bestem en eksakt verdi for verdien programmet skriver ut når det kjøres.


::::{answer}
$$
x = \sqrt{e}
$$
::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 15
Nedenfor vises en grenseverdi.

$$
\lim_{x \to -2} \dfrac{x^2 + ax + 2}{x^2 - 2x - 8}
$$

1) Bestem $a$ slik at grenseverdien eksisterer.
2) Bestem grenseverdien for denne verdien av $a$.


::::{answer}
$$
a = 3 \qog \lim_{x \to -2} \dfrac{x^2 + 3x + 2}{x^2 - 2x - 8} = \dfrac{1}{6}
$$
::::


:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 16
Nedenfor vises tre figurer der
* Én viser grafen til $f$
* Én viser grafen til $f'$
* Én viser grafen til $f''$.

Avgjør hvilken figur som viser $f$, $f'$ og $f''$. 



:::{multi-plot}
width: 100%
functions: ( -2*x * log(x**2 + 1) * exp(x**2 - 1) + 2*x * exp(x**2 - 1) / (x**2 + 1) ) / exp(x**2 - 1)**2, (-2 * log(x**2 + 1) + 6 * x**4 * log(x**2 + 1) + 4 * x**6 * log(x**2 + 1) - 8 * x**4 - 10 * x**2 + 2) / ((1 + 2 * x**2 + x**4) * exp(x**2 - 1)), log(x**2 + 1) / (exp(x**2 - 1))
function-names: A, B, C
rows: 1
cols: 3
ticks: off
ylims: [(-2, 2), (-6, 7), (-2, 2)]
xmin: -3
xmax: 3
:::


::::{answer}
* Figur A viser grafen til $f'$
* Figur B viser grafen til $f''$
* Figur C viser grafen til $f$
::::



:::::::::::::::





---



:::::::::::::::{exercise} Oppgave 17

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



:::::::::::::::{exercise} Oppgave 18
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

:::::::::::::


::::::::::::::

:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 19

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

Hvor lang tid vil det ta før temperaturen i kaffen er mindre enn $30 \degree \mathrm{C}$?

::::{answer}
ca. 51 minutter.
::::
:::::::::::::::





---



:::::::::::::::{exercise} Oppgave 20

:::{plot}
align: right
width: 100%
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
fontsize: 34
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







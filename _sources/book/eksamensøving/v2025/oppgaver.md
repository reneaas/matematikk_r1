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

::::{answer}
$$
\sqrt{5}
$$
::::

::::{solution}
Vektoren som peker fra Nils til Ahmad er

$$
\lvec{NA} = [1 - (-1), 1 - 2] = [2, -1].
$$

Avstanden mellom Nils og Ahmad er da 

$$
\abs{\lvec{NA}} = \sqrt{2^2 + (-1)^2} = \sqrt{5}.
$$
::::
:::::::::::::



:::::::::::::{tab-item} b
En basketball ligger i punktet $(-1, a)$ der $a \in \real$. Vektoren som går fra Jelena til ballen, er parallell med vektoren som går fra Nils til Ahmad.

Bestem $a$.


::::{answer}
$$
a = \dfrac{1}{2}
$$
::::


::::{solution}
Vektoren fra Nils til Ahmad fant vi i forrige oppgave og var gitt ved

$$
\lvec{NA} = [2, -1].
$$

La vektoren fra Jelena til ballen være $\lvec{JB}$. Da har vi at

$$
\lvec{JB} = \lvec{OB} - \lvec{OJ} = [-1, a] - [0, 0] = [-1, a].
$$

Samtidig skal $\lvec{JB} \parallel \lvec{NA}$, så det må finnes en skalar $k$ slik at

$$
\lvec{JB} = k \cdot \lvec{NA} \liff [-1, a] = k \cdot [2, -1] \liff [-1, a] = [2k, -k].
$$

Vektorlikningen krever at begge likninger er oppfylt samtidig slik at:

$$
-1 = 2k \and a = -k 
$$

Den første likningen gir 

$$
k = -\dfrac{1}{2}
$$

Det betyr at 

$$
a = -k = -\left(-\dfrac{1}{2}\right) = \dfrac{1}{2}.
$$

::::

:::::::::::::


:::::::::::::{tab-item} c
Nils flytter seg til et punkt $M$. $M$ er det nærmeste punktet som er plassert slik at avstanden mellom Jelena og Nils er $\sqrt{10}$ meter. Vinkelen mellom Nils, Ahmad og Jelena, $\angle MAJ$, er $90$ grader.

Bestem koordinatene til $M$.


::::{answer}
$$
M(-1, 3)
$$
::::


::::{solution}

:::{plot}
width: 100%
align: right
let: Jx = 0
let: Jy = 0
let: Nx = -1
let: Ny = 2
let: Ax = 1
let: Ay = 1
let: Mx = -1
let: My = 3
let: Mx2 = 3
let: My2 = -1
triangle: points=((Jx, Jy), (Ax, Ay), (Mx, My)), angles=(B), corner-labels=none, angle-radius=30
triangle: points=((Jx, Jy), (Ax, Ay), (Mx2, My2)), angles=(B), corner-labels=none, angle-radius=30
axis: equal
ticks: off
point: (Jx, Jy)
point: (Nx, Ny)
point: (Ax, Ay)
point: (Mx, My)
point: (Mx2, My2)
text: Jx, Jy, "$J$", bottom-left
text: Nx, Ny, "$N$", bottom-left
text: Ax, Ay, "$A$", top-right
text: Mx, My, "$M$", top-right
text: Mx2, My2, "$M'$", bottom-right
fontsize: 26
:::



Vi lager oss en hjelpefigur av situasjonen:

Vi skal finne det punktet $M$ som oppfyller at

1. $\abs{\lvec{JM}} = \sqrt{10}$
2. $\angle MAJ = 90^\circ$
3. $M$ ligger nærmest mulig $N$.

Vi kan merke oss at vi kan skrive $\lvec{JM}$ som

$$
\lvec{JM} = \lvec{JA} + \lvec{AM}.
$$

Siden $\angle MAJ = 90\degree$, så vil 

$$
\lvec{AM} = k \cdot \lvec{JA}_\perp
$$

der $\lvec{JA}_\perp$ er en tverrvektor til $\lvec{JA}$ og $k$ er en skalar. Vi starter med å finne $\lvec{JA}$:

$$
\lvec{JA} = [1 - 0, 1 - 0] = [1, 1].
$$

Vi vet også hvilken lengde $\lvec{JM}$ skal ha. Fra dette kan vi finne lengden til $\lvec{AM}$:

$$
\abs{\lvec{JM}} = \abs{\lvec{JA}}^2 + \abs{\lvec{AM}}^2
$$

$$
(\sqrt{10})^2 = 2 + 2|k|^2 
$$

der vi har brukt at $\abs{\lvec{JA}}^2 = \abs{\lvec{JA}_\perp}^2 = 2$. Da følger det at

$$
8 = 2|k|^2 \liff |k|^2 = 4 \liff |k| = 2.
$$

Med andre ord får vi to mulige løsninger for $M$:

$$
\lvec{OM}_1 = \lvec{JA} + 2 \cdot \lvec{JA}_\perp = [1, 1] + 2 \cdot [-1, 1] = [-1, 3]
$$

eller

$$
\lvec{OM}_2 = \lvec{JA} - 2 \cdot \lvec{JA}_\perp = [1, 1] - 2 \cdot [-1, 1] = [3, -1].
$$

Det punktet som ligger nærmest $N$ er $M(-1, 3)$, så derfor er dette det punktet Nils flytter seg til.

::::

:::::::::::::


::::::::::::::


:::::::::::::::


## Del 2 (Med hjelpemidler – 3 timer)


:::::::::::::::{exercise} Oppgave 1 (6 poeng)
Teknologiselskaper PowBat skal lansere en ny batteriteknologi i en by med 3 millioner husstander. PowBat regner med at antallet husstander som har batteriet $t$ uker etter lanseringen, vil følge modellen $S$ gitt ved

$$
S(t) = \dfrac{2~500~000}{1 + 2500\cdot e^{-0.08t}}
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvor lang tid vil det ta før halvparten av husstandene i byen har batteriet, ifølge modellen?


::::{answer}
Ca. 103 uker.
::::

::::{solution}
Det er $3~000~000$ husstander til sammen, så for å avgjøre hvor lang tid det før halvparten har batteriet, løser vi  $S(t) = 1~500~00$ med CAS:

:::{figure} ./figurer/del_2/1/a.png
---
class: no-click, adaptive-figure
width: 65%
---
:::

Vi ser at etter ca $103$ uker vil halvparten av husstandene i byen ha batteriet.


::::
:::::::::::::


:::::::::::::{tab-item} b
Bestem $S'(52)$. Gi en praktisk tolkning av svaret.


::::{solution}
$S'(52)$ vil gi oss omtrent hvor mange nye husstander som får batteriet iløpet av uke 52. Vi kan finne $S'(52)$ ved å bruke CAS:


:::{figure} ./figurer/del_2/1/b.png
---
class: no-click, adaptive-figure
width: 65%
---
:::

Altså er det ca. 4873 nye husstander som får batteriet i uke 52, ifølge modellen.

::::


:::::::::::::


:::::::::::::{tab-item} c

> Denne oppgaven er ikke relevant for halvdagsprøven. *Skip it*.

Det viser at konkurrenten BA3 planlegger å lansere et batteri med tilsvarende teknologi samtidig. Dette vil påvirke salget til PowBat.

Etter å ha hørt planene til BA3 antar PowBat at
* de totalt vil få solgt batteriet til 1,5 millioner husstander
* 500 husstander har batteriet når det lanseres
* flest nye husstander kjøper batteriet i uke 60

Bruk antakelsene ovenfor til å finne en ny logistisk modell $F$ for antallet husstander som har batteriet etter $t$ uker.


::::{answer}
$$
F(t) = \dfrac{1~500~000}{1 + 2999\exp\left(-\frac{\ln(2999)}{60}t\right)}.
$$
::::

::::{solution}
Vi starter med å sette opp en logistisk modell på formen

$$
F(t) = \dfrac{a}{1 + be^{-ct}}
$$

Vi vet at det maksimalt blir vil være $1~500~000$ husstander, så dette blir bareevnen $a$ i modellen. Altså har vi at

$$
F(t) = \dfrac{1~500~000}{1 + be^{-ct}}.
$$

Videre vet vi at $F(0) = 500$ siden det er $500$ husstander som har batteriet når det lanseres. Da får vi at

$$
F(0) = 500 \liff \dfrac{1~500~000}{1 + b} = 500 \liff 1 + b = \dfrac{1~500~000}{500} = 3000 \liff b = 2999.
$$


I tillegg skal flest husstander kjøpe batteriet i uke $60$, som tilsvarer at 

$$
F(60) = \dfrac{1}{2}} F(\infty) = \dfrac{1}{2} \cdot 1~500~000 = 750~000.
$$

Da får vi at

$$
\dfrac{1~500~000}{1 + 2999e^{-60c}} = 750~000
$$

$$
1~500~000 = 750~000 + 2999 \cdot 750~000 \cdot e^{-60c}
$$

$$
750~000 = 2999 \cdot 750~000 \cdot e^{-60c}
$$

$$
\dfrac{1}{2999} = e^{-60c} \liff -60c
$$

$$
c = \dfrac{\ln(2999)}{60}.
$$

Altså er den nye modellen for antallet husstander som har batteriet etter $t$ uker gitt ved

$$
F(t) = \dfrac{1~500~000}{1 + 2999\exp\left(-\frac{\ln(2999)}{60}t\right)}.
$$


::::
:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2 (6 poeng)
Funksjonen $f$ er gitt ved

$$
f(x) = \dfrac{1}{3}x^3 - 2x^2 - 1
$$

og har definisjonsmengden $I = [a, b]$ der $a, b \in \real$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem det største intervallet $I$, slik at $f$ har en omvendt funksjon $g$ når $2 \in I$.


::::{answer}
$$
I = [0, 4].
$$
::::


::::{solution}
For at $f$ skal ha en omvendt funksjon på intervallet $I$, kan ikke funksjonen ha et ekstremalpunkt på innsiden av intervallet. Vi leter ett eventuelle ekstremalpunkter først:

$$
f'(x) = x^2 - 4x = x(x - 4).
$$

som betyr at 

$$
f'(x) = 0 \liff x = 0 \or x = 4.
$$

Vi tegner et fortegnsskjema for $f'(x)$ for å avgjøre om punktene faktisk er ekstremalpunkter:


:::{signchart-2}
width: 80%
function: x**2 - 4*x, f'(x)
:::

Vi ser at begge punkter er ekstremalpunkter siden $f'(x)$ skifter fortegn rundt punktene. Setter vi $I = [0, 4]$ så vil ingen ekstremalpunkter ligge på innsiden av intervallet, og vi sikrer at $2 \in I$. Dermed er det største intervallet $I$ slik at $f$ har en omvendt funksjon $g$ når $2 \in I$, gitt ved

$$
I = [0, 4].
$$


::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem stigningstallet til tangenten til grafen til $g$ i punktet $(-10, 3)$.


::::{answer}
Stigningstallet til tangenten er $-\dfrac{1}{3}$
::::


::::{solution}
Punktet $(-10, 3)$ ligger på grafen til $g$ som betyr at punktet $(3, -10)$ ligger på grafen til $f$. Stigningstallet til tangenten til grafen til $f$ vil da være $f'(3)$, og stigningstallet til tangenten til grafen til $g$ er

$$
g'(-10) = \dfrac{1}{f'(3)}.
$$

Vi har at 

$$
f'(x) = x^2 - 4x \liff f'(3) = 3^2 - 4\cdot 3 = -3.
$$

Altså er 

$$
g'(-10) = \dfrac{1}{f'(3)} = \dfrac{1}{-3} = -\dfrac{1}{3}.
$$

Altså er stigningstallet til tangenten til grafen til $g$ i punktet $(-10, 3)$ gitt ved $-\dfrac{1}{3}$.
::::

:::::::::::::



:::::::::::::{tab-item} c
Grafen til $g$ har en annen tangent med samme stigningstallet som tangenten i punktet $(-10, 3)$. 

Bestem koordinatene til tangeringspunktet.


::::{answer}
$$
\left(-\dfrac{8}{3}, 1\right).
$$
::::


::::{solution}
Vi løser $f'(x) = -3$ for å finne det andre tangeringspunktet $(a, b)$ på grafen til $f$. Da vil koordinatene til tangeringspunktet på grafen til $g$ være $(b, a)$.

$$
f'(x) = -3 \liff x^2 - 4x = -3 \liff x^2 - 4x + 3 = 0 \liff (x - 1)(x - 3) = 0 \liff x = 1 \or x = 3.
$$

Altså vil det andre tangeringspunktet på grafen til $f$ være $(1, f(1))$. Vi finner $f(1)$:

$$
f(1) = \dfrac{1}{3} - 2 - 1 = -\dfrac{8}{3}.
$$

Dermed er koordinatene til det andre tangeringspunktet på grafen til $g$ gitt 

$$
\left(-\dfrac{8}{3}, 1\right).
$$
::::
:::::::::::::


::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 3 (3 poeng)
Amalie arbeider med en funksjon $f$ med delt forskrift og skal vise funksjonsuttrykket til de andre i klassen. Dessverre har hun søkt på arket sitt og klarer ikke å lese alt som står der.


$$
f(x) = \begin{cases}
    -9x - 15, && x \leq -2 \\
    \\
    g(x), && -2 \lt x \lt 1 \\
    \\
    \dfrac{x^2}{2} - x - \dfrac{7}{2}, && x \geq 1
\end{cases}
$$

Hun husker at $f$ er kontinuerlig og deriverbar for alle $x \in \real$.
Hun husker også at det midterste uttrykket er et tredjegradspolynom.

Bruk dette til å bestemme hele funksjonsuttrykket til $f$.


::::{answer}
Det midterste uttrykket må være

$$
g(x) = -\dfrac{13}{27}x^3 + \dfrac{7}{9}x^2 - \dfrac{1}{9}x - \dfrac{113}{27}
$$
::::

::::{solution}
Funksjonen $f$ er bygget opp av polynomer i hver forskrift, og disse er kontinuerlige overalt.

Vi lar 

$$
p(x) = -9x - 15 \qog q(x) = \dfrac{x^2}{2} - x - \dfrac{7}{2}
$$

For at $f$ skal være kontinuerlig og deriverbar i $x = -2$, så må

$$
p(-2) = g(-2) \and p'(-2) = g'(-2)
$$

For at $f$ skal være kontinuerlig og deriverbar i $x = 1$, så må

$$
q(1) = g(1) \and q'(1) = g'(1)
$$

Dette gir oss fire likninger og fire ukjente siden $g(x)$ er et tredjegradspolynom. Vi løser likningene med CAS:

:::{figure} ./figurer/del_2/3/sol.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Vi ser altså at $f$ er kontinuerlig og deriverbar overalt dersom vi setter det midterste uttrykket lik

$$
g(x) = -\dfrac{13}{27}x^3 + \dfrac{7}{9}x^2 - \dfrac{1}{9}x - \dfrac{113}{27}
$$

::::

:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 4 (8 poeng)
Posisjonen $\vec{r}$ til en fiskebåt $t$ timer etter at den drar fra land, er gitt ved

$$
\vec{r}(t) = [-1 + 5t, 4 + 8t].
$$

Enheten langs aksene er kilometer.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Farten til en båt måles vanligvis i knop, der $1$ knop er $1852$ meter per time.

Bestem farten til fiskebåten i knop.


::::{answer}
$$
\sqrt{89}~\mathrm{km/h} = \dfrac{\sqrt{89}}{1.852}~\mathrm{knop} \approx 5.1~\mathrm{knop}.
$$
::::

::::{solution}
Farten til båten er gitt ved

$$
v = \abs{\vec{r}'(t)} = \abs{[5, 8]} = \sqrt{5^2 + 8^2} = \sqrt{89}.
$$

Denne farten er i kilometer per time. For å konvertere til knop, kan vi gjøre følgende utregning:

$$
1~\mathrm{knop} = 1852~\mathrm{m/h} = 1.852~\mathrm{km/h} \liff 1~\mathrm{km/h} = \dfrac{1}{1.852}~\mathrm{knop}.
$$

Dermed har vi at

$$
\sqrt{89}~\mathrm{km/h} = \dfrac{\sqrt{89}}{1.852}~\mathrm{knop}
$$

Vi kan finne en tilnærmet verdi for dette med CAS:

:::{figure} ./figurer/del_2/4/a.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Altså er farten til båten ca. $5.1$ knop.

::::


:::::::::::::


:::::::::::::{tab-item} b
Et fyr står i posisjonen $(4, 7)$.

Bestem den minste avstanden mellom fiskebåten og fyret.


::::{answer}
$$
h = \dfrac{55}{\sqrt{89}} = \dfrac{55 \sqrt{89}}{89}
$$
::::


::::{solution}
Båten beveger seg langs en rett linje. En retningsvektor for linja vil være fartsvektoren

$$
\vec{v} = \vec{r}'(t) = [5, 8]
$$

Den minste avstanden fra fyret til båten vil være den korteste avstanden fra punktet $P(4, 7)$ til linja. Vi trenger også et punkt på linja. Vi lar dette punktet være

$$
\lvec{OQ} = \vec{r}(0) = [-1, 4].
$$

Da vil den korteste avstanden $h$ være

$$
h = \dfrac{\abs{\lvec PQ\cdot \vec{v}_\perp}}{\abs{\vec{v}}}
$$

Vi har at

$$
\lvec{PQ} = \lvec{OQ} - \lvec{OP} = [-1, 4] - [4, 7] = [-5, -3]
$$

og at en tverrvektor til $\vec{v}$ er

$$
\vec{v}_\perp = [-8, 5].
$$

Da får vi at

$$
\lvec{PQ} \cdot \vec{v}_\perp = [-5, -3] \cdot [-8, 5] = 55
$$

Dermed blir den korteste avstanden

$$
h = \dfrac{55}{\sqrt{89}} = \dfrac{55 \sqrt{89}}{89}
$$

::::


:::::::::::::


:::::::::::::{tab-item} c
En fiskestim er i punktet $(1, -3)$ ved tiden $t = 0$, og stimen svømmer med hastigheten $\vec{v} = [4, 11]$.

Vil fiskebåten treffe fiskestimen?


::::{answer}
Fiskebåten treffer ikke fiskestimen fordi de er i skjæringspunktet mellom kurvene sine på forskjellige tidspunkter.

::::


::::{solution}
La $\vec{r}_f(t)$ være posisjonen til fiskestimen etter $t$ timer. Posisjonsvektoren vil da være gitt ved

$$
\vec{r}_f(t) = \vec{r}_f(0) + \vec{v} \cdot t = [1, -3] + [4, 11] \cdot t = [1 + 4t, -3 + 11t].
$$

For å undersøke om de treffer hverandre, løser vi likningen

$$
\vec{r}_f(s) = \vec{r}(t)
$$

Dette gjør vi med CAS:

:::{figure} ./figurer/del_2/4/c.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Vi får forskjellig verdi for $s$ og $t$ som betyr at de er der på forskjellige tidspunkter. Fiskestimen er der akkurat litt senere enn fiskebåten. Dermed vil ikke fiskebåten treffe fiskestimen.


::::


:::::::::::::


:::::::::::::{tab-item} d
En annen fiskebåt er i punktet $(-2, 0)$ ved tiden $t = 0$ og holder konstant fart i retning langs $\vec{u} = [6, 4]$.

Bestem farten denne fiskebåten må holde for å treffe fiskestimen.


::::{answer}
$$
\abs{\vec{v}} = 3\sqrt{13}~\mathrm{km/h}.
$$
::::

::::{solution}
La først $\vec{r}_2(t)$ være posisjonen dersom fiskebåten starter i $(-2, 0)$ og kjører med fartsvektoren $\vec{v} = [6, 4]$. Da kan vi finne koordinatene til punktet der kurven til fiskestimen og kurven til denne fiskebåten skjærer hverandre ved å løse likningen

$$
\vec{r}_2(s) = \vec{r}_f(t)
$$

Vi gjør dette med CAS:

:::{figure} ./figurer/del_2/4/d1.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Altså vil fiskestimen være i skjæringspunktet $\left(\dfrac{17}{5}, \dfrac{18}{5}\right)$ etter $t = \dfrac{3}{5}$ timer. Fiskemåten må være der samtidig. La $\vec{v} = [a, b]$ være fartsvektoren til fiskebåten. Da må vi kreve at

$$
\left[\dfrac{17}{5}, \dfrac{18}{5}\right] = [-2, 0] + [a, b] \cdot \dfrac{3}{5}
$$

Vi løser likningen med CAS:

:::{figure} ./figurer/del_2/4/d2.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Altså må fartsvektoren være $\vec{v} = [9, 6] = 3[3, 2]$ som gir farten

$$
\abs{\vec{v}} = 3\sqrt{3^2 + 2^2} = 3\sqrt{13}.
$$

Altså må fiskebåten holde en fart på $3\sqrt{13}~\mathrm{km/h}$ for å treffe fiskestimen.
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 5 (4 poeng)
Grafen til en funksjonen $f$ gitt ved $f(x) = \ln x$ er vist i figuren nedenfor.

Et punkt $B$ på grafen til $f$ er plassert slik at tangenten til grafen i punktet $B$ går gjennom $A(0, 0)$.

Punktet $C$ er plassert på linja $y = x$ slik at $\angle ACB = 90\degree$.



:::{plot}
width: 55%
xmin: -1
ymin: -1
xmax: 4.5
ymax: 3.5
figsize: (5, 4)
let: Ax = 0
let: Ay = 0
let: Bx = exp(1)
let: By = 1
let: Cx = (exp(1) + 1) / 2
let: Cy = (exp(1) + 1) / 2
triangle: points=((Ax, Ay), (Bx, By), (Cx, Cy)), angles=(C), corner-labels=none, angle-radius=40, color=black
function: log(x + 1e-6), (0, 6), f, blue
point: (0, 0)
text: 0, 0, "$A$", top-left
point: (exp(1), 1)
text: exp(1), 1, "$B$", top-right
tangent: exp(1), f, solid, red
point: ((exp(1) + 1) / 2, (exp(1) + 1) / 2)
text: (exp(1) + 1) / 2, (exp(1) + 1) / 2, "$C$", top-left
line: 1, 0, dashed, gray
ticks: off
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem eksakte verdier for koordinatene til punktet $B$.



::::{answer}
$$
B(e, 1)
$$
::::


::::{solution}
Punktet $B$ ligger på en linje som er en tangent til grafen i et punkt $(x, f(x))$. Gitt punktet $x$, så vil stigningstallet til tangenten være gitt ved den deriverte av $f$ i punktet $x$:

$$
f(x) = \ln x \limplies f'(x) = \dfrac{1}{x}
$$

Siden punktet $A(0, 0)$ også ligger på tangenten og er i origo, vil $\lvec{AB}$ beskrive posisjonsvektoren til punktet $B$. Dette punktet vil ha koordinatene $(x, f(x)) = (x, \ln x)$. Dermed er 

$$
\lvec{AB} = [x, \ln x]
$$

Når vi øker $x$ med én enhet, vil $y$-verdien øke med stigningstallet til tangenten, altså $\frac{1}{x}$. Dermed kan vi uttrykke retningsvektoren til tangenten som

$$
\vec{v} = \left[1, \dfrac{1}{x}\right]
$$


Punktene på tangenten kan derfor beskrives som

$$
\vec{r}(t) = \lvec{OA} + \vec{v} \cdot t = [0, 0] + \left[1, \dfrac{1}{x}\right] \cdot t = \left[t, \dfrac{t}{x}\right]
$$

Vi må bestemme $t$ og $x$ slik at $\vec{r}(t) = \lvec{AB}$. Altså må vi løse likningen

$$
\left[t, \dfrac{t}{x}\right] = [x, \ln x]
$$

Dette gir oss to likninger:

$$
t = x \and \dfrac{t}{x} = \ln x
$$

Den første likningen forteller oss bare at $t = x$, så vi kan sette dette inn i den andre likningen som gir:

$$
\dfrac{x}{x} = \ln x \limplies 1 = \ln x
$$

Altså må $x = e$. Dermed er koordinatene til punktet $B$ gitt ved

$$
B(x, \ln x) = B(e, 1)
$$


::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem det eksakte arealet av $\triangle ABC$.



::::{answer}
$$
T = \dfrac{e^2 - 1}{4}
$$
::::

::::{solution}
For å bestemme arealet av $\triangle ABC$, må vi kjenne til to vektorer som spenner ut trekanten. Vi vet allerede at $\lvec{AB} = [e, 1]$. Vi trenger derfor bare én vektor til for én av sidene i trekanten. Vi kan finne $\lvec{AC}$ ved å regne ut projeksjonen av $\lvec{AB}$ ned på linja $y = x$ som har retningsvektor $\vec{v} = [1, 1]$. Da får vi

$$
\lvec{AC} = \dfrac{\lvec{AB} \cdot \vec{v}}{\abs{\vec{v}}^2} \vec{v}
$$

Vi regner ut skalarproduktet i telleren først:

$$
\lvec{AB} \cdot \vec{v} = [e, 1] \cdot [1, 1] = e + 1
$$

Så regner vi ut nevneren:

$$
\abs{\vec{v}}^2 = 1^2 + 1^2 = 2
$$

Dermed får vi

$$
\lvec{AC} = \dfrac{e + 1}{2} \cdot [1, 1]
$$

Arealet av $\triangle ABC$ er da gitt ved formelen

$$
T = \dfrac{1}{2} \abs{\lvec{AB} \cdot \lvec{AC}_\perp}
$$

der $\lvec{AC}_\perp$ er en tverrvektor til $\lvec{AC}$. En tverrvektor til $\lvec{AC}$ får vi vet å bytte plass på koordinatene og endre fortegn på én av dem:

$$
\lvec{AC}_\perp = \dfrac{e + 1}{2} \cdot [-1, 1]
$$


Nå kan vi regne ut skalarproduktet:

$$
\begin{align*}
\lvec{AB} \cdot \lvec{AC}_\perp &= [e, 1] \cdot \left(\dfrac{e + 1}{2} \cdot [-1, 1]\right) \\
\\
&= \dfrac{e + 1}{2} \cdot ( -e + 1) = \dfrac{-(e^2 - 1)}{2} \\
\\
&= \dfrac{1 - e^2}{2}
\end{align*}
$$

Altså er arealet av trekanten gitt ved

$$
\begin{align*}
T &= \dfrac{1}{2} \abs{\dfrac{1 - e^2}{2}} \\
\\
&= \dfrac{e^2 - 1}{4}
\end{align*}
$$



::::


:::::::::::::


::::::::::::::



:::::::::::::::
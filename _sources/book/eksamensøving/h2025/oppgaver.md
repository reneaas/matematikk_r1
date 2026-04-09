# Eksamen høsten 2025

> Eksamen høsten 2025 var todelt med 2 timer på del 1 og 3 timer på del 2. Våren 2026 vil eksamen være todelt med 3 timer på del 1 og 2 timer på del 2.

## Del 1 (Uten hjelpemidler – 2 timer)


:::::::::::::::{exercise} Oppgave 1 (5 poeng)
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Deriver funksjonen $f$ gitt ved

$$
f(x) = \dfrac{1}{3}x^3 + \sqrt{x} + 2
$$


::::{answer}
$$
f'(x) = x^2 + \dfrac{1}{2\sqrt{x}}
$$
::::

::::{solution}
$$
f'(x) = \left(\dfrac{1}{3}x^3\right)' + \left(\sqrt{x}\right)' + (2)' = x^2 + \dfrac{1}{2\sqrt{x}} + 0 = x^2 + \dfrac{1}{2\sqrt{x}}
$$
::::


:::::::::::::



:::::::::::::{tab-item} b
Funksjonen $g$ er gitt ved

$$
g(x) = \dfrac{2x - 3}{e^x}
$$

er kontinuerlig og deriverbar for alle $x \in \real$. 

Bestem $g'(2)$ og $g'(3)$.


::::{answer}
$$
g'(2) = \dfrac{1}{e^2} \qog g'(3) = -\dfrac{1}{e^3}
$$
::::

::::{solution}
Vi skriver om uttrykket til

$$
g(x) = (2x - 3)e^{-x}.
$$

Så bruker vi produktregelen for derivasjon:

$$
\begin{align*}
g'(x) &= (2x - 3)' \cdot e^{-x} + (2x - 3) \cdot (e^{-x})' \\
\\
&= 2e^{-x} + (2x - 3)(-e^{-x}) \\
\\
&= 2e^{-x} - (2x - 3)e^{-x} \\
\\
&= (2 - 2x + 3)e^{-x} \\
\\
&= (5 - 2x)e^{-x}.
\end{align*}
$$

Så regner vi ut de verdiene:

$$
g'(2) = (5 - 2 \cdot 2)e^{-2} = e^{-2} = \dfrac{1}{e^2}
$$

$$
g'(3) = (5 - 2 \cdot 3)e^{-3} = -e^{-3} = -\dfrac{1}{e^3}
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Hva forteller svarene i oppgave **b** om grafen til $g$ når $x \in [2, 3]$?


::::{answer}
Grafen til $g$ har et ekstremalpunkt på intervallet $[2, 3]$.
::::


::::{solution}
Siden $g'(x)$ har motsatt fortegn i endepunktene, må $g'(x) = 0$ for minst ett punkt $x \in \langle 2, 3\rangle$. Det betyr at grafen til $g$ har et ekstremalpunkt i intervallet $[2, 3]$. 
::::
:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2 (3 poeng)
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen

$$
\left(\lg x\right)^2 - 2 \lg x = 8
$$


::::{answer}
$$
x = 10^4 \or x = 10^{-2}.
$$
::::

::::{solution}
Vi setter $u = \lg x$ slik at likningen kan skrives som

$$
u^2 - 2u = 8 \liff u^2 - 2u - 8 = 0.
$$

Så bruker vi $abc$-formelen som gir:

$$
u = \dfrac{2 \pm \sqrt{(-2)^2 - 4 \cdot 1 \cdot (-8)}}{2 \cdot 1} = \dfrac{2 \pm 6}{2}.
$$

Altså må 

$$
u = 4 \or u = -2,
$$

som vil si at

$$
\lg x = 4 \or \lg x = -2.
$$

Det betyr at

$$
x = 10^4 \or x = 10^{-2}.
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $a$ slik at

$$
\log_a \dfrac{1}{64} = -3
$$


::::{answer}
$$
a = 4
$$
::::

::::{solution}
Vi bruker definisjonen av logartimen med grunntall $a$ som gir at

$$
\log_a \dfrac{1}{64} = -3 \liff \dfrac{1}{64} = a^{-3}
$$

Dermed har vi at

$$
\dfrac{1}{a^3} = \dfrac{1}{64} \liff a^3 = 64 \liff a = 4.
$$

Altså er $a = 4$.
::::


:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3 (3 poeng)
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem grenseverdien dersom den eksisterer:

$$
\lim_{x\to -2} \dfrac{x^2 - 4x + 2}{x^2 - 2x - 8}
$$


::::{answer}
Grenseverdien eksisterer ikke:

$$
\lim_{x\to -2} \dfrac{x^2 - 4x + 2}{x^2 - 2x - 8} = \pm \infty
$$
::::


::::{solution}
Vi prøver å sette inn $x = -2$ i uttrykket:

$$
\lim_{x\to -2} \dfrac{x^2 - 4x + 2}{x^2 - 2x - 8} = \dfrac{(-2)^2 - 4 \cdot (-2) + 2}{(-2)^2 - 2 \cdot (-2) - 8} = \dfrac{4 + 8 + 2}{4 + 4 - 8} = \dfrac{14}{0}.
$$

Dette forteller oss at grenseverdien går mot $\pm \infty$ når $x \to -2$, så grenseverdien eksisterer ikke.
::::

:::::::::::::


:::::::::::::{tab-item} b
1. Bestem $a$ slik at grenseverdien eksisterer:

$$
\lim_{x\to -2} \dfrac{x^2 + ax + 2}{x^2 - 2x - 8}
$$

2. Bestem grenseverdien for denne verdien av $a$.


::::{answer}
$$
a = 3 \and \lim_{x\to -2} \dfrac{x^2 + 3x + 2}{x^2 - 2x - 8} = \dfrac{1}{6}.
$$
::::

::::{solution}
For at grenseverdien skal eksistere, må vi for et $\dfrac{0}{0}$-uttrykk slik at vi kan bruke L'Hôpitals regel: 

$$
\lim_{x\to -2} \dfrac{x^2 + ax + 2}{x^2 - 2x - 8} = \dfrac{4 - 2a + 2}{0} = \dfrac{6 - 2a}{0}.
$$

Altså må vi kreve at 

$$
6 - 2a = 0 \liff a = 3.
$$

Når $a = 3$, kan vi bruke L'Hôpitals regel for å finne grenseverdien:

$$
\lim_{x\to -2} \dfrac{2x + a}{2x - 2} = \lim_{x\to -2} \dfrac{2x + 3}{2x - 2} = \dfrac{-4 + 3}{-4 - 2} = \dfrac{-1}{-6} = \dfrac{1}{6}.
$$

::::
:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4 (6 poeng)
I et koordinatsystem har vi gitt punktene $A(-2, 3)$ og $B(3, 2)$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem lengden av linjestykket $AB$.


::::{answer}
$$
AB = \sqrt{26}.
$$
::::

::::{solution}
Vi har at 

$$
\lvec{AB} = \lvec{OB} - \lvec{OA} = [3 - (-2), 2 - 3] = [5, -1].
$$

Lengden av linjestykket $AB$ er da

$$
AB = \abs{\lvec{AB}} = \sqrt{5^2 + (-1)^2} = \sqrt{26}.
$$
::::


:::::::::::::



:::::::::::::{tab-item} b
Linja gjennom $A$ og $B$ skjærer $x$-aksen i punktet $C$.

Bestem koordinatene til $C$.

::::{answer}
$C\left(13, 0\right)$
::::

::::{solution}
Vi lager en vektorfunksjon $\vec{r}(t)$ for linja. En retningsvektor for linja er

$$
\vec{v} = \lvec{AB} = [5, -1].
$$

Bruker vi $\lvec{OA}$ som startpunkt, får vi

$$
\vec{r}(t) = \lvec{OA} + t \cdot \vec{v} = [-2, 3] + t \cdot [5, -1] = [-2 + 5t, 3 - t].
$$

Vi vet at punktet $C$ ligger på $x$-aksen som betyr at $y$-komponenten til $\vec{r}(t)$ må være lik $0$:

$$
3 - t = 0 \liff t = 3.
$$

Så setter vi denne verdien inn i $x$-komponenten for å finne $x$-koordinaten til punktet $C$:

$$
x = -2 + 5 \cdot 3 = 13.
$$

Altså er koordinatene til punktet $C\left(13, 0\right)$.
::::


:::::::::::::


:::::::::::::{tab-item} c
Et punkt $D$ er gitt ved $D(2, t)$ der $t \in \real$.


Bestem $t$ slik at $\angle ABD$ blir $90\degree$.



::::{answer}
$$
t = -3.
$$
::::

::::{solution}
For at $\angle ABD = 90\degree$, så må prikkproduktet

$$
\lvec{BA} \cdot \lvec{BD} = 0.
$$

Vi har at

$$
\lvec{BA} = -\lvec{AB} = [-5, 1]
$$

og 

$$
\lvec{BD} = \lvec{OD} - \lvec{OB} = [2 - 3, t - 2] = [-1, t - 2].
$$

Dermed krever vi at

$$
\lvec{BA} \cdot \lvec{BD} = 0 \liff [-5, 1] \cdot [-1, t - 2] = 0
$$

som gir

$$
5 + t - 2 = 0 \liff t = -3.
$$

Altså vil $\angle ABD = 90\degree$ når $t = -3$.


::::


:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5 (4 poeng)
En funksjon $f$ er gitt ved

$$
f(x) = 4x^2 \cdot \ln x
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til eventuelle topp- og bunnpunkter på grafen til $f$.


::::{answer}
Bunnpunkt i $\left(e^{-\frac{1}{2}}, -\dfrac{2}{e}\right)$.
::::

::::{solution}
Vi løser $f'(x) = 0$ for å finne kandidater til ekstremalpunkter:

$$
f'(x) = 8x \ln x + 4x = 4x(2 \ln x + 1) = 0.
$$

Altså har vi at

$$
4x = 0 \or 2 \ln x + 1 = 0 \liff x = 0 \or x = e^{-\frac{1}{2}}.
$$

Vi tegner en fortegnslinje for $f'(x)$ for å avgjøre om det er et topp- eller bunnpunkt:

:::{signchart-2}
width: 80%
function: 4*x * (2 * log(x) + 1), f'(x)
nocache:
:::

Fra fortegnslinja til $f'(x)$ ser vi at $f'(x)$ skifter fra negativ til positiv i $x = e^{-\frac{1}{2}}$, så det er et bunnpunkt i dette punktet. Vi må ekskludere $x = 0$ fordi $\ln x$ er ikke definert i dette punktet. 

Vi finner $y$-koordinaten til det relevante punktet:

$$
f\left(e^{-\frac{1}{2}}\right) = 4 \cdot e^{-1} \cdot \ln(e^{-\frac{1}{2}}) = 4 \cdot e^{-1} \cdot \left(-\dfrac{1}{2}\right) = -\dfrac{2}{e}.
$$

Altså har grafen til $f$ et bunnpunkt 

$$
\left(e^{-\frac{1}{2}}, -\dfrac{2}{e}\right)
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
En elev jobber med funksjonen $f$ og har skrevet programmet nedenfor:

:::{code-block} python
---
linenos:
---
from math import log    # log(x) er kode for ln(x)

a = 0.1
b = 3

maks_avvik = 0.0001

def f(x):
    return 4 * x**2 * log(x)

m = (a + b) / 2

while abs(f(m)) > maks_avvik:   # abs() finner absoluttverdi

    if f(a) * f(m) < 0:
        b = m
    else:
        a = m

    m = (a + b) / 2

print(m)
:::

Hva ønsker eleven å finne ut?

Forklar hva programmet gjør i linje 11 - 20. 

Bestem verdien som blir skrevet ut når eleven kjører programmet.


::::{solution}
Eleven ønsker å bestemme et nullpunkt til $f$.

Fra linje 11 – 20, så starter eleven med et intervall $[a, b]$ og finner midtpunktet $m = \dfrac{a + b}{2}$ på intervallet. Herfra kjører eleven følgende algoritme:

Så lenge $|f(m)| > \mathrm{maks~avvik}$:
1. Sjekk om $f(a) \cdot f(m) < 0$. Hvis dette er sant, så skifter $f(x)$ fortegn på intervallet $[a, m]$ og må ha et nullpunkt der. Da settes $b = m$ slik at vi nå har et nytt mindre intervall $[a, m]$ som inneholder nullpunktet.
2. Hvis den forrige sjekken ikke stemmer, så må nullpunktet ligge på intervallet $[m, b]$. Så da setter vi $a = m$ slik at vi nå har et nytt mindre intervall $[m, b]$ som inneholder nullpunktet.
3. Regn ut et nytt midtpunkt $m = \dfrac{a + b}{2}$ for det nye intervallet.

Dette gjentar frem til $|f(m)| \leq \mathrm{maks~avvik}$, som betyr at $m$ til slutt er en god tilnærming til et nullpunkt til $f$ med en feilmargin på $0.0001$.


Det som skrives ut av programmet vil da være en tilnærming til løsningen av 

$$
f(x) = 0 \liff 4x^2 \ln x = 0 \liff x^2 = 0 \or \ln x = 0
$$

Den første likningen gir $x = 0$ som ikke er gyldig siden $\ln 0$ ikke er definert. Dermed har vi bare

$$
\ln x = 0 \liff x = e
$$

Altså skriver programmet ut en tilnærming til $x = e$.
::::

:::::::::::::


::::::::::::::

:::::::::::::::


## Del 2 (Med hjelpemidler – 3 timer)



:::::::::::::::{exercise} Oppgave 1 (6 poeng)
---
aids: true
---
Tabellen nedenfor viser folketallet på et lite tettsted, noen år i perioden $1960 – 1980$.

:::{table}
---
transpose: true
---
labels: År, Folketall
$1960$, $500$
$1961$, $604$
$1963$, $852$
$1965$, $1043$
$1967$, $1510$
$1971$, $2163$
$1975$, $2544$
$1977$, $2639$
$1980$, $2715$
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

> Denne oppgaven er ikke så relevant for halvdagsprøven. Ta gjerne funksjonsuttrykket fra fasiten og løs oppgave **b** og **c**.

Bruk informasjonen til å lage en modell $F$ på formen

$$
F(t) = \dfrac{B}{1 + a \cdot e^{-kt}}
$$

for antall personer $F(t)$ som bodde på dette tettstedet $t$ år etter $1960$.

Vurder modellens gyldighetsområde.


::::{answer}
$$
F(t) = \dfrac{2841}{1 + 5.1 \cdot e^{-0.25t}}. 
$$
::::


::::{solution}
Vi legger dataen inn i et regneark i Geogebra og sørger for at $x$-verdiene er antall år etter $1960$:

:::{figure} ./figurer/del_2/1/a/regneark.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Så bruker vi {ggb-icon}`mode_regression` og velger en **logistisk** modell:


:::{figure} ./figurer/del_2/1/a/modell.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

Altså er en rimelig modell 

$$
F(t) = \dfrac{2841}{1 + 5.1 \cdot e^{-0.25t}}. 
$$

Modellen er gyldig så lenge den gir rimelig prediksjoner. Den forutsier at når $t \to \infty$, så vil det bli ca. $2841$ personer som bor på tettstedet. Dette forutsetter at innbyggertallet etter hvert ikke vil øke, som kanskje ikke er rimelig å anta.

For verdier lavere enn $t = 0$, vil modellen raskt gi svært få innbyggere som gjør at modellen er urealistisk bare 10 år tidligere hvor $F(-10) \approx 45$. Gitt at veksten av nye innbyggere blir lavere over tid, så vil modellen være rimelig så lenge $t > 0$.


::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $F'(12)$ og $F''(12)$. 

Gi en praktisk tolkning av svarene.


::::{answer}
* $F'(12) \approx 115$ forteller oss at omtrent $115$ nye innbygger kom til tettstedet i det 12. året etter $1960$ (altså i $1972$).
* $F''(12) \approx -17$ forteller oss at i det 12.året, så kom det omtrent $17$ færre nye innbyggere enn i året før. 
::::


::::{solution}
Vi regner ut de to verdiene med CAS:

:::{figure} ./figurer/del_2/1/b/sol.png
---
class: no-click, adaptive-figure
width: 80%
---


* $F'(12) \approx 115$ forteller oss at omtrent $115$ nye innbygger kom til tettstedet i det 12. året etter $1960$ (altså i $1972$).
* $F''(12) \approx -17$ forteller oss at i det 12.året, så kom det omtrent $17$ færre nye innbyggere enn i året før. 



:::
::::


:::::::::::::


:::::::::::::{tab-item} c
Når økte antall personer som bodde på tettstedet, med mer enn 150 personer per år ifølge modellen?


::::{answer}
Ifølge modellen økte antall personer som bodde på tettstedet med mer enn $150$ personer per år i løpet av året $1963$ og i løpet av året $1970$.
::::

::::{solution}
For å finne ut når antall personer økte med mer enn $150$ personer per år, løser likningen

$$
F(t) = 150
$$

Vi gjør dette med CAS:

:::{figure} ./figurer/del_2/1/c/sol.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

Vi ser at det skjer to ganger:

* Først når $t \approx 3.18$ som tilsvarer i løpet av året $1963$.
* Så skjer det igjen når $t \approx 9.85$ som tilsvarer i løpet året $1970$.
::::

:::::::::::::



::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2 (4 poeng)
---
aids: true
---

Funksjonen $f$ er gitt ved

$$
f(x) = \begin{cases}
    ax + b, & x \leq -2 \\
    \\
    2x^3 + 2x^2 - 2x, & -2 \lt x \lt k, \qder a,b,c \in \real \qog k \in \langle -2, \to \rangle \\
    \\
    c, & x \geq k
\end{cases}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør om $f$ er kontinuerlig når $x = -2$ dersom $a = 2$ og $b = -2$.


::::{answer}
$f$ er *ikke* kontinuerlig i $x = -2$ når $a = 2$ og $b = -2$.
::::


::::{solution}
Vi lar

$$
p(x) = ax + b \qog q(x) = 2x^3 + 2x^2 - 2x \qog r(x) = c.
$$

For at $f$ skal være kontinuerlig i $x = -2$, så må vi ha at

$$
p(-2) = q(-2).
$$

Med $a = 2$ og $b = -2$ har vi at

$$
p(-2) = 2 \cdot (-2) - 2 = -6
$$

og 

$$
q(-2) = 2 \cdot (-2)^3 + 2 \cdot (-2)^2 - 2 \cdot (-2) = -16 + 8 + 4 = -4.
$$

Altså er ikke $f$ kontinuerlig i $x = -2$ når $a = 2$ og $b = -2$.


::::
:::::::::::::


:::::::::::::{tab-item} b
Bestem $a$, $b$, $c$ og $k$ slik at $f$ er kontinuerlig og deriverbar når $x = -2$ og når $x = k$.



::::{answer}
Vi får to gyldige muligheter. Enten så må

$$
a = 14 \and b = 24 \and c = 2 \and k = -1
$$

eller

$$
a = 14 \and b = 24 \and c = -\dfrac{10}{27} \and k = \dfrac{1}{3}.
$$
::::

::::{solution}
For at $f$ skal være kontinuerlig deriverbar i $x = -2$ må vi kreve at

$$
p(-2) = q(-2) \and p'(-2) = q'(-2)
$$

For at $f$ skal være kontinuerlig deriverbar i $x = k$ må vi kreve at

$$
q(k) = r(k) \and q'(k) = r'(k).
$$


Vi bruker CAS til å løse likningssystemet for $a$, $b$, $c$ og $k$:

:::{figure} ./figurer/del_2/2/sol.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Vi får to gyldige muligheter. Enten så må

$$
a = 14 \and b = 24 \and c = 2 \and k = -1
$$

eller

$$
a = 14 \and b = 24 \and c = -\dfrac{10}{27} \and k = \dfrac{1}{3}.
$$

::::


:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3 (4 poeng)
---
aids: true
---

Beboerne i et boligområde klager på lukt fra et biogassanlegg. Kommunen tar luftprøver og vurderer værdata som vind og temperatur.

Prøvene analyseres, og hver prøve gis en luktverdi $c$. Denne luktverdien er gitt i lukenheter (odour units) per kubikkmeter ($\mathrm{OU/m^3}$).

Sammenhengen mellom $c$ og luktintensiteten $I$ er gitt ved

$$
I = 1.4 \lg c - 0.3
$$

Biogassanlegget er pålagt å forholde seg til tabellen nedenfor:

:::{table}
width: 60%
labels: Luktintensitet ($I$), Vurdering
$\lt 1$, uproblematisk
$1 – 2$, akseptabelt
$2 – 3$, kan aksepteres kortvarig
$3 – 4$, plagsom lukt, bør begrenses
$\gt 4$, plagsomt, tiltak kreves
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Resultatet av prøvene viser luktverdien mellom $500~\mathrm{OU/m^3}$ og $1400~\mathrm{OU/m^3}$.

Har beboerne grunnlag for å klage?


::::{answer}
Ja.
::::


::::{solution}
Vi regner ut $I(c)$ for de to oppgitte verdiene med CAS:


:::{figure} ./figurer/del_2/3/a.png
---
class: no-click, adaptive-figure
width: 100%
---
:::

Vi ser at luktintensiteten $I \in [3.5, 4.1]$ som betyr at beboerne har grunnlag til å klage siden det havner innen for vurderingen "plagsom lukt, bør begrenses" og "plagsomt, tiltak kreves".

::::


:::::::::::::


:::::::::::::{tab-item} b
Biogassanlegget tar klagene på alvor og ønsker å redusere luktplagene.

Hvilken luktverdi må nye prøver vise for at luktintensiteten skal bli akseptabel?


::::{answer}
$c \in [8.5, 43.9]~\mathrm{OU/m^3}$
::::


::::{solution}
For at luktintensiten skal være vurdert som "akseptabel", må 

$$
I(c) \in [1, 2]
$$

Vi løser likningene $I(c) = 1$ og $I(c) = 2$ i CAS for å finne nedre og øvre grense for luktverdiene $c$:

:::{figure} ./figurer/del_2/3/b.png
---
class: no-click, adaptive-figure
width: 90%
---
:::

Altså må biogassanlegget sikte på at $c \in [8.5, 43.9]~\mathrm{OU/m^3}$ for at luktintensiteten skal være vurdert som "akseptabel".

::::
:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4 (6 poeng)
---
aids: true
---

Ina følger en sti fra ei hytte til et utsiktspunkt. I et koordinatsystem der enheten langs aksene er meter, ligger hytta i punktet $H(0, 300)$ og utsiktspunktet i $U(1200, 400)$. 

Stien mellom hytta og utsiktspunktet er en rett linja. Ina går med konstant fart.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Forklar at parameterframstillingen

$$
I : \begin{cases}
    x = 1200s, & \\
    & s \in [0, 1]\\
    y = 300 + 100s, &
\end{cases}
$$

gir den rette linja mellom hytta og utsiktspunktet.


::::{solution}
Parameterframstillingen er bare en vektorfunksjon

$$
\vec{r}(s) = [1200s, 300 + 100s] = [0, 300] + [1200, 100] \cdot s.
$$

Det første leddet gjenkjenner vi som startpunktet $\lvec{OH} = [0, 300]$. Retningsvektoren $\vec{v}$ til linja er gitt ved

$$
\vec{v} = \lvec{HU} = \lvec{OU} - \lvec{OH} = [1200, 400] - [0, 300] = [1200, 100].
$$

Altså er parameterframstillingen på formen

$$
\vec{r}(s) = \lvec{OH} + \vec{v} \cdot s
$$

som stemmer overens med opplysningene i oppgaven. Vi kan også se at når $s = 0$, så er $\vec{r}(0) = [0, 300]$ som er punktet $H$, og når $s = 1$, så er $\vec{r}(1) = [1200, 400]$ som er punktet $U$. Dermed gir parameterframstillingen den rette linja mellom hytta og utsiktspunktet.
::::

:::::::::::::



:::::::::::::{tab-item} b
Hele turen tar $20$ minutter.

Bestem posisjonen til Ina etter $5$ minutter.


::::{answer}
$$
(300, 325)
$$
::::


::::{solution}
Ina starter i punktet $H(0, 300)$ og beveger seg med en konstant fartsvektor $\vec{v} = [a, b]$ slik at hun etter $20$ minutter er i punktet $U(1200, 400)$. Altså må vi ha at

$$
[1200, 400] = [0, 300] + [a, b] \cdot 20 \liff [1200, 400] = [20a, 300 + 20b].
$$

Dermed er

$$
20a = 1200 \liff a = 60
$$

og 

$$
300 + 2b = 400 \liff 20b = 100 \liff b = 5.
$$

Dermed er fartsvektoren $\vec{v} = [60, 5]$. Posisjonen til Ina etter $t$ minutter er da

$$
\vec{r}_I(t) = [0, 300] + [60, 5] \cdot t = [60t, 300 + 5t].
$$

Etter $5$ minutter er Ina i posisjonen

$$
\vec{r}_I(5) = [60 \cdot 5, 300 + 5 \cdot 5] = [300, 325].
$$
::::



:::::::::::::


:::::::::::::{tab-item} c
Regn ut farten til Ina. Gi svaret i $\mathrm{m/s}$.


::::{answer}
$$
\abs{\vec{v}} \approx 1~\mathrm{m/s}.
$$
::::

::::{solution}
Fartsvektoren til Ina fant vi i oppgave **b** til å være

$$
\vec{v} = [60, 5]
$$

Farten til Ina er da

$$
\abs{\vec{v}} = \sqrt{60^2 + 5^2} = \sqrt{5^2 \cdot 12^2 + 5^2} = \sqrt{5^2} \cdot \sqrt{12^2 + 1} = 5 \sqrt{145}.
$$

Denne farten er i meter per minutt. Vi har at $1~\mathrm{min} = 60~\mathrm{s}$, så farten i $\mathrm{m/s}$ er gitt ved

$$
\abs{\vec{v}} = \dfrac{5 \sqrt{145}}{60}~\mathrm{m/s} = \dfrac{\sqrt{145}}{12}~\mathrm{m/s} \approx \dfrac{\sqrt{144}}{12}~\mathrm{m/s} = 1~\mathrm{m/s}. 
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Jonas er ute på tur i samme område som Ina. De to vennene møter hverandre.

Jonas sin posisjon $t$ minutter etter at han startet sin tur er gitt ved 

$$
j: \begin{cases}
    x = 520 - 20t \\
    \\
    y = 310 + 5t
\end{cases}
$$

Hvor langt har Ina gått når hun møter Jonas?



::::{answer}
Ca. $421$ meter.
::::

::::{solution}
Vi har allerede en beskrivelse linja Ina går på. Den er gitt ved

$$
\vec{r}_I(s) = [60s, 300 + 5s],
$$

der $s$ er en parameter som ikke nødvendigvis er lik tiden $t$ som den er for Jonas (vi vet ikke om de starter å gå samtidig eller ikke). Jonas sin posisjonen etter $t$ minutter kan derimot om til en vektorfunksjon:

$$
\vec{r}_J(t) = [520 - 20t, 310 + 5t].
$$

Nå løser vi likningen $\vec{r}_I(s) = \vec{r}_J(t)$ for å finne *hvor* de møtes. Vi gjør dette med CAS:

:::{figure} ./figurer/del_2/4/d.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

Så de to møtes i punktet $P(420, 335)$. Ina har gått fra punktet $H(0, 300)$ som betyr at hun har gått en avstand som tilsvarer lengden til linjestykket $HP$. Vi regner det ut med CAS:


:::{figure} ./figurer/del_2/4/d2.png
---
class: no-click, adaptive-figure
width: 80%
---
:::

Altså har Ina gått nøyaktig $35 \sqrt{145}$ meter som er ca. $421$ meter. 


::::


:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 5 (4 poeng)
---
aids: true
---

For $\vec{a}$ og $\vec{b}$ er $\abs{\vec{a}} = 4$, $\abs{\vec{b}} = 2 \sqrt{3}$ og vinkelen mellom $\vec{a}$ og $\vec{b}$ er $30 \degree$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Gitt at $\vec{p} = \vec{a} + \vec{b}$.

Regn ut den eksakte lengden til $\vec{p}$.


::::{answer}
$$
\abs{\vec{p}} = 2 \sqrt{13}
$$
::::


::::{solution}
Skalarproduktet er uavhengig av koordinatsystemet vi bruker, så vi kan lage oss to vektorer $\vec{a}$ og $\vec{b}$ som har egenskapene som er oppgitt. Lar vi $\vec{a}$ ligge langs $x$-aksen, har vi 

$$
\vec{a} = [4, 0] \qog \vec{b} = 2\sqrt{3} \cdot [\cos 30\degree, \sin 30\degree].
$$

Herfra kan vi bruke CAS til å gjøre resten av regningen:

:::{figure} ./figurer/del_2/5/a.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Altså er den eksakte lengden til $\vec{p}$ gitt ved

$$
\abs{\vec{p}} = 2 \sqrt{13}
$$

::::

:::::::::::::



:::::::::::::{tab-item} b
Gitt at $\vec{q} = t \cdot \vec{a} + \vec{b}$ der $t \in \real$.

Bestem $t$ slik at $\vec{p}$ og $\vec{q}$ er ortogonale.


::::{answer}
$$
t = -\dfrac{6}{7}
$$
::::

::::{solution}
Vi bruker samme strategi som i oppgave **a**. For at de to vektorene skal være ortogonale, må prikkproduktet være lik $0$:

$$
\vec{q} \cdot \vec{p} = 0
$$

Vi løser likningen med CAS:

:::{figure} ./figurer/del_2/5/b.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Altså vil $\vec{p}$ og $\vec{q}$ være ortogonale dersom

$$
t = -\dfrac{6}{7}
$$

::::

:::::::::::::


::::::::::::::


:::::::::::::::



---




:::::::::::::::{admonition} Oppgave 6 (6 poeng)
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


::::{solution}
* Både graf $A$ og graf $B$ representerer eksponentialfunksjoner. Vi kan se at $G(x) = a^x$ siden $G(0) = 1$. Dermed må $A(x) = G''(x) = a^x \cdot (\ln a)^2$.

* Graf $B$ er en tredjegradsfunksjon som betyr at $B''(x)$ må være en lineær funksjon. Da følger det at $C(x) = B''(x)$.

* Graf $F$ er en fjerdegradsfunksjon på formen $F(x) = x^4 - c$, så $F''(x)$ er en andregradsfunksjon som må gå gjennom origo. Derfor er $D(x) = F''(x)$.

* Graf $E$ viser en andregradsfunksjon $E(x) = x^2 - c$, som betyr at $E''(x) = 2$. Derfor må $H(x) = E''(x)$.
::::


:::::::::::::

:::::::::::::{tab-item} b
Hvilke av de åtte grafene ovenfor er grafen til funksjoner som har en omvendt funksjon?


::::{answer}
$A$, $B$, $C$ og $G$ har omvendte funksjoner.
::::


::::{solution}
For at en funksjon skal ha en omvendt funksjon, holder her å sjekke hvilke funksjoner som er monotone. Graf $A$, $B$, $C$ og $G$ er strengt voksende og har dermed omvendte funksjoner.
::::


:::::::::::::
::::::::::::::


:::::::::::::::






# Eksamen høsten 2024

> Eksamen høsten 2024 var todelt med 1 timer på del 1 og 4 timer på del 2. Fra våren 2026 vil eksamen være todelt med 3 timer på del 1 og 2 timer på del 2.


## Del 1 (Uten hjelpemidler - 1 time)

:::::::::::::::{exercise} Oppgave 1 (2 poeng)
Deriver funksjonen

$$
f(x) = \dfrac{e^{2x}}{x}
$$


::::{answer}
$$
f'(x) = \dfrac{e^{2x}(2x - 1)}{x^2}
$$
::::


::::{solution}
Vi bruker brøkregelen for derivasjon:

$$
\begin{align*}
    f'(x) &= \dfrac{(e^{2x})' \cdot x - e^{2x} \cdot (x)'}{x^2} \\
    \\
    &= \dfrac{2e^{2x} \cdot x - e^{2x} \cdot 1}{x^2} \\
    \\
    &= \dfrac{e^{2x}(2x - 1)}{x^2}
\end{align*}
$$
::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2 (2 poeng)
Bruk en egnet strategi for å bestemme verdien som skrives ut når programmet nedenfor kjøres.

:::{code-block} python
---
linenos:
---
def O(x):
    return -0.1 * x**2 + 2000 * x - 50000

x = 0

while O(x + 1) > O(x):
    x = x + 1

print(x)
:::


::::{answer}
Programmet skriver ut verdien $10~000$.
::::


::::{solution}
Programmet starter med $x = 0$ og øker verdien til $x$ med $1$ så lenge $O(x + 1) \gt O(x)$, som betyr at programmet øker $x$ så lenge neste funksjonsverdi er større enn den forrige. Programmet søker altså etter et toppunkt på grafen til $O$. Til slutt skrives bare ut $x$-koordinaten til punktet.

Vi kan finne denne verdien ved å løse $O'(x) = 0$. Vi har at 

$$
O(x) = -\dfrac{1}{10}x^2 + 2000x - 50~000
$$

Dermed er

$$
O'(x) = -\dfrac{1}{5}x + 2000
$$

Vi løser så $O'(x) = 0$:

$$
\dfrac{1}{5}x = 2000 \liff x = 10~000
$$

Altså skriver programmet ut verdien $10~000$.
::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 3 (2 poeng)
Løs likningen

$$
100^x - 3 \cdot 10^x = 4
$$


::::{answer}
$$
x = \lg 4
$$
::::

::::{solution}
Vi skriver om likningen til

$$
(10^x)^2 - 3 \cdot 10^x - 4 = 0
$$

Så setter vi $u = 10^x$ som gir oss andregradslikningen

$$
u^2 - 3 u - 4 = 0
$$

Vi bruker $abc$-formelen til å finne løsningene for $u$:

$$
u = \dfrac{3 \pm \sqrt{9 + 16}}{2} = \dfrac{3 \pm 5}{2}
$$

som gir

$$
u = -1 \or u = 4
$$

Vi setter tilbake definisjonen av $u$ som gir oss likningene

$$
10^x = -1 \or 10^x = 4
$$

Den første av de to likningene har ingen løsning, som betyr at den eneste løsningen til den opprinnelige likningen er

$$
10^x = 4 \liff x = \lg 4
$$
::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4 (2 poeng)
Finn grenseverdien hvis den eksisterer.

$$
\lim_{x\to \infty} \dfrac{x^2 + x - 12}{2x^2 - 18}
$$

::::{answer}
$$
\lim_{x\to \infty} \dfrac{x^2 + x - 12}{2x^2 - 18} = \dfrac{1}{2}
$$
::::


::::{solution}
Grenseverdien gir i utgangspunktet et ubestemt $\infty / \infty$-uttrykk, så vi bruker L'Hôpitals regel (2 ganger siden vi får et ubestemt uttrykk igjen etter første runde):

$$
\lim_{x\to \infty} \dfrac{x^2 + x - 12}{2x^2 - 18} \overset{[\frac{\infty}{\infty}]}{=} \lim_{x\to \infty} \dfrac{2x + 1}{4x} \overset{[\frac{\infty}{\infty}]}{=} \lim_{x\to \infty} \dfrac{2}{4} = \dfrac{1}{2} 
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5 (4 poeng)
Fire vektorer er gitt ved $\vec{u} = [3, -2]$, $\vec{v} = [4, -6]$, $\vec{w} = [2, -3]$ og $\vec{p} = [8, 12]$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør om noen av vektorene er 
* like lange
* ortogonale



::::{answer}
* Vektorene $\vec{u}$ og $\vec{w}$ er like lange
* Vektorene $\vec{p}$ og $\vec{u}$ er ortogonale
::::

::::{solution}
Vi kan se at 

$$
\vec{v} = [4, -6] = 2 \cdot [2, -3] = 2 \vec{w}
$$

Ergo er de to vektorene $\vec{v}$ og $\vec{w}$ verken like lange eller ortogonale.

Vi kan også se at

$$
\vec{p} = [8, 12] = 4 \cdot [2, 3] = 4 \cdot \vec{u}_\perp
$$

der $\vec{u}_\perp$ er en tverrvektor til $\vec{u}$. Da følger det at vektorene er ortogonale siden

$$
\vec{p} \cdot \vec{u} = 0,
$$

samtidig som vektorene ikke er like lange siden $\abs{\vec{p}} = 4 \abs{\vec{u}}$.


Vi kan også se at vektorene $\vec{u}$ og $\vec{w}$ er like lange:

$$
\abs{\vec{u}} = \sqrt{3^2 + (-2)^2} = \sqrt{13} \and \abs{\vec{w}} = \sqrt{2^2 + (-3)^2} = \sqrt{13}
$$

Men vektorene er ikke ortogonale siden $\vec{w}$ ikke er en tverrvektor til $\vec{u}$. 

Altså kan vi summere opp:

* Vektorene $\vec{u}$ og $\vec{w}$ er like lange
* Vektorene $\vec{p}$ og $\vec{u}$ er ortogonale


::::

:::::::::::::



:::::::::::::{tab-item} b
En vektor er gitt ved $\vec{q} = [2a - 3, 1 + 3b]$. 

Bestem $a$ og $b$ slik at $\vec{u} + 2\vec{q} = [7, 5]$. 


::::{answer}
$$
a = \dfrac{5}{2} \and b = \dfrac{5}{6}
$$
::::


::::{solution}
Vi har at 

$$
\begin{align*}
\vec{u} + 2 \vec{q} &= [3, -2] + 2 \cdot [2a - 3, 1 + 3b] \\
\\
&= [3, -2] + [4a - 6, 2 + 6b] \\
\\
&= [4a - 3, 6b]
\end{align*}
$$

Så krever vi at

$$
\vec{u} + 2\vec{q} = [7, 5] \liff [4a - 3, 6b] = [7, 5]
$$

som gir likningene

$$
4a - 3 = 7 \and 6b = 5
$$

som gir at

$$
a = \dfrac{5}{2} \and b = \dfrac{5}{6}
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::



----



:::::::::::::::{exercise} Oppgave 6 (2 poeng)
I koordinatsystemet nedenfor ser du grafene til tre funksjoner $f$, $g$ og $h$.

En av funksjonene har gjennomsnittlig vekstfart lik $\dfrac{1}{2}$ i intervallet $[0, 4]$, og derivert like $1$ når $x = 1$.

Hvilken av funksjonene er dette? Husk å begrunne svaret ditt.


:::{plot}
width: 70%
function: -1/4 * x * (x - 6), teal, f
function: 1/2 * x + 2, g, blue 
function: -5/24 * x**3 + 5/6 * x**2 + 4, red, h
xmin: -4
xmax: 10
ymin: -4
ymax: 10
ystep: 2
xstep: 2
:::



::::{answer}
Funksjonen $f$.
::::


::::{solution}
Funksjonen $h$ har en gjennomsnittlig vekstfart lik $0$ i intervallet $[0, 4]$ siden $h(0) = h(4)$, så denne kan vi utelukke.

Funksjonen $g$ er lineær og har den gjennomsnittlige vekstfarten i intervallet $[0, 4]$ lik:

$$
\dfrac{g(4) - g(0)}{4 - 0} = \dfrac{4 - 2}{4} = \dfrac{1}{2}
$$

Siden funksjonen er lineær vil dette være verdien til den deriverte overalt som betyr at $g'(1) = \dfrac{1}{2}$. 

Dermed må den riktige funksjonen være $f$.
::::


:::::::::::::::


---


## Del 2 (Med hjelpemidler - 4 timer)



:::::::::::::::{exercise} Oppgave 1 (6 poeng)
Et gammelt vannreservoar lekker vann. Mengden vann i reservoaret $V$ er gitt ved

$$
V(t) = 10~000 \cdot e^{-0.07 t} + 500
$$

Her er $t$ antall timer etter lekkasjen startet, og mangden vann er målt i antall liter.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvor lang tid vil det gå før vannmengden er halvert?


:::::::::::::



:::::::::::::{tab-item} b
Bestem $V'(12)$ og $V''(12)$. 

Gi en praktisk tolkning av svarene.
:::::::::::::


:::::::::::::{tab-item} c
Undersøk om $V$ har asymptoter, og gi en praktisk tolkning av verdiene til eventuelle asymptoter.


:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2 (6 poeng)
Avgjør om hver enkelt påstand nedenfor er sann eller usann.

Forklar tydelig hvordan du har resonnert.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
**Påstand**:

Hvis 

$$
\lim\limits_{x \to \infty} f(x) = \lim\limits_{x \to \infty} g(x) \qog \lim\limits_{x \to -\infty} f(x) = \lim\limits_{x \to -\infty} g(x)
$$

så er $f(x) = g(x)$.


::::{answer}
Usann.
::::


::::{solution}
Påstanden er usann, som vi kan vise med ett moteksempel.

La 

$$
f(x) = x \qog g(x) = x + 1
$$

Her vil 

$$
\lim_{x \to \infty} f(x) = \infty \and \lim_{x \to \infty} g(x) = \infty
$$

Altså er grensene like når $x \to \infty$.

Vi har også at

$$
\lim_{x \to -\infty} f(x) = -\infty \and \lim_{x \to -\infty} g(x) = -\infty
$$

Altså er grensene også like når $x \to -\infty$. Men her er $g(x) = f(x) + 1$ som betyr at $f(x) \neq g(x)$ for alle $x$. Ergo er påstanden usann.
::::


:::::::::::::


:::::::::::::{tab-item} b
**Påstand**:

Funksjonen $f(x) = \abs{x}$ er deriverbar for alle $x \in \real$, bortsett fra i $x = 0$.



::::{answer}
Sann.
::::

::::{solution}
Funksjonen kan skrives om til

$$
|x| = \begin{cases}
-x & \qhvis x \lt 0 \\
x & \qhvis x \geq 0 \\
\end{cases}
$$

For $x \lt 0$ vil stigningstallet til funksjonen være $-1$, mens for $x \gt 0$ vil stigningstallet være $1$. La $f_+(x) = x$ og $f_-(x) = -x$. Tar vi grensen ovenfra av den deriverte får vi $+1$. Tar vi grensen nedenfra av den deriverte får vi $-1$. Siden de to grensene ikke er like, så er ikke funksjonen deriverbar i $x = 0$. 

Funksjonen er ellers deriverbar i alle punkter siden både $x$ og $-x$ er deriverbare funksjoner i alle punkter.

Altså er påstanden sann.
::::

:::::::::::::


:::::::::::::{tab-item} c
**Påstand**:

For likningen $a^x = a^y$ der $a \in \real$, er løsningen alltid $x = y$.


::::{answer}
Usann.
::::

::::{solution}
Påstanden er usann, siden for $a = 0$ vil alle verdier for $x$ og $y$ tilfredsstille likningen bortsett fra $x = y = 0$. Da kan i utgangspunktet $x = 2$ og $y = 1$ tilfredsstille likningen siden $0^2 = 0^1 = 0$ som gir muligheten for at $x \neq y$ kan være en løsning til likningen.
::::

:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3 (8 poeng)

> Denne oppgaven trenger du ikke øve på før halvdagsprøven – vi skal først se på logisitiske modeller etter halvdagsprøven.

Forskere har registrert en ny fiskeart i en innsjø. I tabellen nedenfor ser du hvor mange fisk av arten som var i innsjøen noen måneder etter at arten først ble registrert.


:::{table}
---
transpose: true
---
labels: Måneder etter første registrering, Antall tusen fisk
$0$, $1$
$1$, $2.5$
$2$, $5.5$
$3$, $9$
$4$, $14$
$5$, $22$
$6$, $32$
$7$, $45$
$8$, $60$
:::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fiskepopulasjonen kan beskrives av en modell på formen

$$
A(t) = A_0 \cdot k^t
$$

der $A(t)$ er antall tusen fisk $t$ måneder etter første registrering.

Bestem $A_0$ og $k$, og gi en praktisk tolkning av disse verdiene.

:::::::::::::



:::::::::::::{tab-item} b
Fiskepopulasjonen kan også beskrives med en logistisk modell på formen

$$
N(t) = \dfrac{B}{1 + \dfrac{B - N_0}{N_0}e^{-r\cdot t}}
$$

der $B$ er bæreevnen, $N_0$ er antall tusen fisk ved $t = 0$ og $r$ er vekstparameteren.


Bestem $N_0$, $B$ og $r$. 
:::::::::::::



:::::::::::::{tab-item} c
Bestem den deriverte til funksjonene du fant i oppgavene **a** og **b**. 

Forklar hvordan vekstfarten endrer seg ifølge hver av de to modellene.
:::::::::::::


:::::::::::::{tab-item} d
Hvilken modell mener du beskriver den praktiske situasjonen best? 

Hvor mange fisk vil det være 12 måneder etter første registrering, ifølge denne modellen?
:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4 (2 poeng)
I koordinatssystemet nedenfor ser du grafen til en funksjon $f$ gitt ved

$$
f(x) = \log_a (x)
$$

Bestem $a$.

Husk å argumentere for at svaret ditt er riktig.


:::{plot}
width: 70%
function: log(x) / log(5), f
xmin: -1
xmax: 35
xstep: 5
ymin: -2
ymax: 4
ystep: 1
:::


::::{answer}
$$
a = 5
$$
::::


::::{solution}
Vi ser at grafen til $f$ går gjennom punktet $(5, 1)$ som betyr at

$$
\log_a(5) = 1 \liff a^1 = 5 \liff a = 5
$$

Altså må $a = 5$. 
::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 5 (4 poeng)
Nedenfor ser du grafene til funksjonene $f$, $g$ og $h$.

::::{multi-plot2}
---
rows: 1
cols: 3
---
:::{plot}
function: x**2 + 3, [0, 2), blue, f
function-endpoints: true
xmin: -0.5
xmax: 3
ymin: -0.5
ymax: 8
fontsize: 28
:::


:::{plot}
function: x - 1, (-2, 1), red, g
function: -2 * (x - 1) + 2, [1, 2], red
function-endpoints: true
xmin: -3
xmax: 3
ymin: -4
ymax: 3
fontsize: 28
:::


:::{plot}
xmin: -3
xmax: 3
ymin: -1
ymax: 10
function: x**3 - 2 * x + 5, [-2, 2), teal, h
function-endpoints: true
fontsize: 28
:::
::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør og begrunn for hver av funksjonene om de har en omvendt funksjon.


:::::::::::::



:::::::::::::{tab-item} b
Bestem funksjonsuttrykket og definisjonsmengden til den omvendte funksjonen i de tilfellene den eksisterer.


:::::::::::::

::::::::::::::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 6 (8 poeng)
To småfugler er ute og flyr. Posisjonen til de to fuglene er gitt ved

$$
\vec{r}_1(t) = [-10 + 6t, 35 - 3t] \qog \vec{r}_2(t) = [2 + 5t, 4t]
$$

Tiden $t$ er målt i sekunder, og enhetene langs aksene er målt i meter.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvor fort flyr hver av de to småfuglene?


:::::::::::::



:::::::::::::{tab-item} b
Hvor stor er avstanden mellom småfuglene når $t = 0$?


:::::::::::::



:::::::::::::{tab-item} c
På hvilket tidspunkt er småfuglene nærmest hverandre, og hvor langt unna hverandre er de da?

:::::::::::::


:::::::::::::{tab-item} d
En rovfugl er også ute og flyr, og oppdager småfuglene ved tidspunktet $t = 0$.

Posisjonen til rovfuglen de første $6$ sekundene er gitt ved

$$
\vec{r}_R(t) = [7t - 10, 2t^2 - 6t + 5]
$$


Gjør nødvendige bergninger og beskriv jakten rovfuglen har på småfuglene.
:::::::::::::

::::::::::::::

:::::::::::::::



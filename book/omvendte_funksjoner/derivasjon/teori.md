# Derivasjon og omvendte funksjoner

::::{admonition} Læringsmål
---
class: tip
---
* Kunne avgjøre om en funksjon har en omvendt funksjon ved hjelp av derivasjon, og bruke dette til å bestemme egenskaper ved funksjonen og dens omvendte funksjon.
* Kunne bestemme den deriverte av en omvendt funksjon.
* Kunne bruke digitale hjelpemidler til å bestemme den deriverte av en omvendt funksjon i et punkt.
::::


## Eksistens av omvendte funksjoner og derivasjon 


Hvis vi ikke har grafen til $f$, kan vi bruke den deriverte $f'(x)$ til å avgjøre om $f$ er en monoton funksjon og dermed om den har en omvendt funksjon. 

:::::::::::::::{summary} Monotone funksjoner og den deriverte
En tilstrekkelig betingelse for at en funksjon $f$ er monoton i sin definisjonsmengde, er at den deriverte $f'(x)$ har samme fortegn for alle $x$ i definisjonsmengden til $f$.


* Hvis $f'(x) > 0$ for alle $x$ i definisjonsmengden til $f$, så er $f$ strengt voksende.
* Hvis $f'(x) < 0$ for alle $x$ i definisjonsmengden til $f$, så er $f$ strengt avtakende.


Vi kan også tillate at $f'(x) = 0$ for enkelte verdier så lenge $f'(x)$ ikke bytter fortegn der.


::::{multi-plot2}
---
rows: 1
cols: 2
fontsize: 30
---
:::{plot}
width: 100%
function: (x - 1) * (x**2 - x + 1), (-1, 3], blue
function-endpoints: true
ticks: off
ymax: 18
ymin: -10
xmax: 4
xmin: -2
text: 0.5 * (4 + 0), 16, "Strengt voksende", top-center, bbox
text: -1, 5, "$f'(x) > 0$", top-center, bbox
:::

:::{plot}
width: 100%
function: -(x - 1) * (x**2 - x + 1), (-1, 3], blue
function-endpoints: true
ticks: off
ymax: 12
ymin: -16
xmax: 4
xmin: -2
text: 0.5 * (4 + 0), 10, "Strengt avtakende", top-center, bbox
text: -1, -7, "$f'(x) < 0$", top-center, bbox
:::


::::

:::::::::::::::



---



:::::::::::::::{example} Eksempel 1
En funksjon $f$ er gitt ved

$$
f(x) = x^3 - 12x + 2 \qder D_f = \langle -2, 2 \rangle.
$$

Avgjør om $f$ har en omvendt funksjon.


::::{solution}
---
dropdown: 0
---
Vi starter med å undersøke om $f$ er en monoton funksjon i definisjonsmengden sin. For å gjøre dette, tegner vi en fortegnslinje for $f'(x)$.

Vi starter med å løse $f'(x) = 0$ så vi kan faktorisere uttrykket:

$$
f'(x) = 3x^2 - 12 \limplies 3x^2 - 12 = 0 \limplies x^2 = 4 \limplies x = \pm 2
$$

$$
f'(x) = 0\limplies 3x^2 - 12 = 0
$$

$$
3x^2 = 12 \limplies x^2 = 4 \limplies x = \pm 2
$$

Altså kan vi faktorisere $f'(x)$ slik:

$$
f'(x) = 3(x + 2)(x - 2)
$$

Så tegner vi et fortegnsskjema for den deriverte:


:::{signchart}
width: 100%
function: 3*x**2 - 12, f'(x)
:::


Vi ser at $f'(x) < 0$ for alle $x \in \langle -2, 2 \rangle$. Dermed er $f$ strengt avtakende i definisjonsmengden sin, og vi kan konkludere med at $f$ har en omvendt funksjon.



::::


:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 1
En funksjon $f$ er gitt ved

$$
f(x) = x^3 - 3x + 1 \qder D_f = [1, \to\rangle.
$$


Avgjør om $f$ har en omvendt funksjon.


::::{solution}
Vi må undersøke om $f$ er strengt voksende eller avtakende i definisjonsmengden sin. For å gjøre dette, tegner vi en fortegnslinje for $f'(x)$.


Den deriverte er

$$
f'(x) = 3x^2 - 3
$$

Vi starter med å løse $f'(x) = 0$ så vi kan faktorisere uttrykket:

$$
f'(x) = 0 \limplies 3x^2 - 3 = 0 \limplies x^2 = 1 \limplies x = \pm 1
$$

Altså kan vi faktorisere $f'(x)$ slik:

$$
f'(x) = 3(x - 1)(x + 1)
$$

Så tegner vi et fortegnsskjema for den deriverte:

:::{signchart}
width: 100%
function: 3*x**2 - 3, f'(x)
:::

Vi kan se at $f'(x) > 0$ for alle $x \in \langle 1, \to\rangle$ og at $f'(1) = 0$. Dette betyr at $f$ er strengt voksende i definisjonsmengden sin og dermed har $f$ en omvendt funksjon.


::::



:::::::::::::::


---


I en del tilfeller, så ønsker vi å bestemme en definisjonsmengde for en funksjon slik at den har en omvendt funksjon. Da bruker vi også den deriverte til å finne en passende definisjonsmengde.


:::::::::::::::{example} Eksempel 2

:::{plot}
align: right
width: 100%
fontsize: 30
function: x * exp(-x), f, [0, 10], blue
xmin: -1
xmax: 3
ymin: -0.5
ymax: 0.6
vline: 1, 0, f(1), dashed, red
text: 1, 0, "$a$", bottom-center
ticks: off
:::


En funksjon $f$ er gitt ved

$$
f(x) = xe^{-x} \qder D_f = [0, a]
$$

for et tall $a > 0$.

1. Bestem hvilken verdi av $a$ som gjør at $f$ har en omvendt funksjon i en så stor definisjonsmengde som mulig.
2. Bestem definisjonsmengden til den omvendte funksjonen.


::::{solution}
---
dropdown: 0
---
Vi bestemmer først den deriverte (med produktregelen):

$$
f'(x) = e^{-x} - xe^{-x} = (1 - x)e^{-x}
$$

Deretter skal vi undersøke fortegnet til $f'(x)$. Vi trenger nullpunktene til $f'$ så vi kan tegne et fortegnsskjema:

$$
f'(x) = 0 \limplies (1 - x)e^{-x} = 0 \limplies x = 1
$$

Så tegner vi et fortegnsskjema:


:::{signchart}
width: 100%
function: (1 - x)*exp(-x), f'(x)
:::

Fra fortegnsskjema ser vi at $f'$ er strengt voksende når $x \leq 1$. Deretter endrer $f'(x)$ fortegn. Siden definisjonsmengden skal være på formen $D_f = [0, a]$, så vil den verdien av $a$ som både sikrer at $f$ har en omvendt funksjon, og som gir størst mulig definisjonsmengde, være $a = 1$.



Definisjonsmengden til den omvendte funksjonen vil være lik verdimengden til $f$ på $D_f = [0, 1]$. Siden funksjonen er strengt voksende, så holder å regne ut $f(0)$ og $f(1)$ for å finne verdimengden:

$$
f(0) = 0 \qog f(1) = \dfrac{1}{e}
$$

Dermed er verdimengden til $f$ gitt ved $V_f = \left[0, \dfrac{1}{e}\right]$. Dette er det samme som definisjonsmengden til den omvendte funksjonen, altså 

$$
D_{f^{-1}} = \left[0, \dfrac{1}{e}\right]
$$


::::


:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 2


:::{plot}
align: right
width: 100%
fontsize: 30
function: x * log(x), f, (0, 2), blue
xmin: -0.5
xmax: 2.5
ymin: -0.6
ymax: 0.6
ticks: off
vline: 1/exp(1), 0, f(1/exp(1)), dashed, red
text: 1/exp(1), 0, "$a$", top-center
:::



En funksjon $f$ er gitt ved

$$
f(x) = x \ln x \qder D_f = [a, \to\rangle
$$

der $a > 0$. 

Bestem $a$ slik at

1. $f$ har en omvendt funksjon og har en så stor definisjonsmengde som mulig.
2. Bestem definisjonsmengden til den omvendte funksjonen.


::::{solution}
Vi bestemmer først den deriverte (med produktregelen):

$$
f'(x) = (x \ln x)' = 1 \cdot \ln x + x \cdot \dfrac{1}{x} = \ln x + 1
$$

Deretter skal vi undersøke fortegnet til $f'(x)$. Vi trenger nullpunktene til $f'$ så vi kan tegne et fortegnsskjema:

$$
f'(x) = 0 \limplies \ln x + 1 = 0 \limplies \ln x = -1 \limplies x = \dfrac{1}{e}
$$

Vi kan merke oss at 

$$
\lim_{x \to 0^+} f'(x) = \lim_{x \to 0^+} (\ln x + 1) = -\infty
$$

og at

$$
\lim_{x \to \infty} f'(x) = \lim_{x \to \infty} (\ln x + 1) = \infty
$$

Dermed så vil $f'(x) < 0$ før $x = \dfrac{1}{e}$ og $f'(x) > 0$ etter $x = \dfrac{1}{e}$. Siden definisjonsmengden skal være på formen $D_f = [a, \to\rangle$, så vil den verdien av $a$ som både sikrer at $f$ har en omvendt funksjon, og som gir størst mulig definisjonsmengde, være

$$
a = \dfrac{1}{e}.
$$

Definisjonsmengden til den omvendte funksjonen vil være lik verdimengden til $f$ på $D_f = \left[\dfrac{1}{e}, \to\right\rangle$. Siden funksjonen er strengt voksende der, så holder å regne ut $f\left(\dfrac{1}{e}\right)$ for å finne verdimengden:

$$
f\left(\dfrac{1}{e}\right) = \dfrac{1}{e} \ln\left(\dfrac{1}{e}\right) = \dfrac{1}{e} \cdot (-1) = -\dfrac{1}{e}
$$

Når $x \to \infty$, så vil også $f(x) \to \infty$. Dermed er verdimengden til $f$ gitt ved 

$$
V_f = \left[-\dfrac{1}{e}, \to\right\rangle.
$$

Dette er det samme som definisjonsmengden til den omvendte funksjonen, altså

$$
D_{f^{-1}} = \left[-\dfrac{1}{e}, \to\right\rangle.
$$


::::


:::::::::::::::





## Den deriverte av den omvendte funksjonen

Selv om en funksjon $f$ har en omvendt funksjon $f^{-1}$ er det ikke alltid vi kan bestemme $f^{-1}(x)$ som en formel. I en del sammenhenger ønsker vi likevel å kunne bestemme den deriverte av den omvendte funksjonen, $\left(f^{-1}\right)'(x)$, og her skal vi se at dette er mulig å gjøre uten å kjenne formelen til den omvendte funksjonen. 


La $g = f^{-1}$ være den omvendte funksjonen til $f$. Fra definisjonen av omvendte funksjoner vet vi at

$$
g(f(x)) = x
$$

Vi deriverer likningen på hver side. Fra kjerneregelen for derivasjon får vi da

$$
(g(f(x)))' = x' \limplies g'(f(x)) \cdot f'(x) = 1
$$

som betyr at

$$
g'(f(x)) = \frac{1}{f'(x)}
$$

Altså kan vi bestemme den deriverte til en omvendt funksjon dersom vi kjenner til $f(x)$ og $f'(x)$. Formelen forutsetter at $f'(x) \neq 0$ slik at vi ikke deler på null.



:::::::::::::::{summary} Den deriverte av en omvendt funksjon
La $f$ være en funksjon og $g = f^{-1}$ være den omvendte funksjonen til $f$. Da er den deriverte til den omvendte funksjonen i $y = f(x)$ gitt ved

$$
g'(y) = \frac{1}{f'(x)}
$$


der $y = f(x)$ og $f'(x) \neq 0$.

Dersom vi ønsker å bruke $f^{-1}$ i formelen, så kan vi skrive den slik:

$$
\left(f^{-1}\right)'(y) = \frac{1}{f'(x)}
$$
:::::::::::::::


---


:::::::::::::::{example} Eksempel 3
En funksjon $f$ er gitt ved

$$
f(x) = x^2 - 4x + 3 \qder D_f = [2, \to\rangle.
$$

La $g$ være den omvendte funksjonen til $f$.

Bestem $g'(3)$.


::::{solution}
---
dropdown: 0
---
Først må vi løse likningen $f(x) = 3$ for å finne $x$-verdien som tilsvarer $y = 3$.

$$
f(x) = 3 \liff x^2 - 4x + 3 = 3
$$

$$
x^2 - 4x = 0 \liff x(x - 4) = 0
$$

som gir

$$
x = 0 \or x = 4
$$

Det er bare $x = 4 \in D_f$, så vi har at $f(4) = 3$. Da har vi at

$$
g'(y) = \dfrac{1}{f'(x)} \limplies g'(3) = \frac{1}{f'(4)}
$$

Vi bestemmer $f'(4)$:

$$
f'(x) = 2x - 4 \limplies f'(4) = 4
$$

Altså er

$$
g'(3) = \frac{1}{4}
$$


::::

:::::::::::::::


---



:::::::::::::::{exercise} Underveisoppgave 3
En funksjon $f$ er gitt ved

$$
f(x) = -x^2 + 2x + 8 \qder D_f = [2, \to\rangle.
$$


La $g = f^{-1}$ være den omvendte funksjonen til $f$.

Bestem $g'(0)$.


::::{answer}
$$
g'(0) = -\frac{1}{6}
$$
::::

::::{solution}
Siden vi skal regne ut $g'(0)$, så må vi vite $x$-verdien som tilsvarer $y = 0$. Vi løser derfor likningen

$$
f(x) = 0 \liff -x^2 + 2x + 8 = 0
$$

$$
x = -\dfrac{2 \pm \sqrt{2^2 - 4 \cdot (-1) \cdot 8}}{2 \cdot (-1)} = -\frac{2 \pm 6}{-2}
$$

$$
x = 4 \or x = -2
$$

Det er bare $x = 4 \in D_f$, så vi har at $f(4) = 0$. Da har vi at

$$
g'(y) = \dfrac{1}{f'(x)} \limplies g'(0) = \frac{1}{f'(4)}
$$

Vi bestemmer $f'(4)$:

$$
f'(x) = -2x + 2 \limplies f'(4) = -6
$$

Altså er

$$
g'(0) = -\frac{1}{6}
$$
::::

:::::::::::::::


---


Vi tar et eksempel til.


:::::::::::::::{example} Eksempel 4
En funksjon $f$ er gitt ved

$$
f(x) = x\ln x \qder D_f = \langle 1, \to\rangle.
$$


La $g = f^{-1}$. 


Bestem stigningstallet til tangenten til grafen til $g$ i punktet $(1, e)$.


::::{solution}
---
dropdown: 0
---
Punkter $(b, a)$ på grafen til $g$ vil tilsvare punkter $(a, b)$ på grafen til $f$. Det betyr at punktet $(1, e)$ på grafen til $g$ tilsvarer punktet $(e, 1)$ på grafen til $f$. Vi skal altså bestemme $g'(1)$, og det kan vi gjøre ved å finne $f'(e)$ først og så bruke

$$
g'(y) = \frac{1}{f'(x)} \limplies g'(1) = \frac{1}{f'(e)}
$$

Vi bestemmer $f'(e)$:

$$
f'(x) = \ln x + 1 \limplies f'(e) = 2
$$

Altså er

$$
g'(1) = \frac{1}{2}
$$

Dermed er stigningstallet til tangenten til grafen til $g$ i punktet $(1, e)$ lik $\dfrac{1}{2}$.
::::


:::::::::::::::



---


:::::::::::::::{exercise} Underveisoppgave 4
En funksjon $f$ er gitt ved

$$
f(x) = x^3 + x + 1 \qder D_f = \real.
$$


Bestem stigningstallet til tangenten til grafen til $f^{-1}$ i punktet $(3, 1)$.



::::{answer}
Stigningstallet er $\dfrac{1}{4}$
::::

::::{solution}
Vi skal bestemme stigningstallet til tangenten til grafen til $f^{-1}$ i punktet $(3, 1)$. Dette tilsvarer å bestemme $\left(f^{-1}\right)'(3)$.

Siden punktet $(3, 1)$ ligger på grafen til $f^{-1}$ så ligger det tilsvarende punktet $(3, 1)$ på grafen til $f$. Det betyr at

$$
\left(f^{-1}\right)'(3) = \frac{1}{f'(1)}
$$

Vi bestemmer $f'(1)$:

$$
f'(x) = 3x^2 + 1 \limplies f'(1) = 4
$$

Altså er

$$
\left(f^{-1}\right)'(3) = \frac{1}{4}
$$ 

Dette er stigningstallet til tangenten til grafen til $f^{-1}$ i punktet $(3, 1)$.

::::


:::::::::::::::




---



## Løsning med digitale verktøy 

Når vi skal bestemme den deriverte til den omvendte funksjonen i et punkt, er vi avhengig av å løse likningen $f(x) = y$, slik at vi vet hvilket punkt $(y, x)$ på grafen til $f^{-1}$ vi skal regne ut den deriverte i med formelen

$$
\left(f^{-1}\right)'(y) = \frac{1}{f'(x)}
$$

For en del funksjoner er det vanskelig å løse likningen $f(x) = y$ ved regning. I slike tilfeller kan vi bruke digitale hjelpemidler for å finne den tilhørende $x$-verdien slik at vi kan bestemme $\left(f^{-1}\right)'(y)$. 



:::::::::::::::{example} Eksempel 5
En funksjon $f$ er gitt ved

$$
f(x) = x^2 e^{-x} \qder D_f = [0, 2\rangle.
$$

Bestem $\left(f^{-1}\right)'(1)$.


::::{solution}
---
dropdown: 0
---

> Bruk CAS-vinduet til å følge regningen i eksempelet.

:::{cas-popup}
---
layout: sidebar
---
:::



Vi må først løse likningen $f(x) = 1$ slik at vi vet hvilken $x$-verdi som tilsvarer $y = 1$ på grafen til $f$ slik at vi kan bruke

$$
g'(y) = \frac{1}{f'(x)}
$$

I gif-en nedenfor viser vi hvordan vi kan gå frem for å gjøre dette med CAS.

:::{figure} ./gifer/derivasjon_omvendte_funksjoner.webp
---
class: no-click, adaptive-figure
width: 80%
---
:::

Vi får at $x \approx -0.7$ ved å løse likningen $f(x) = 1$ numerisk ved å bruke {ggb-icon}`mode_nsolve` i CAS. Så regner vi ut den deriverte til den omvendte funksjonen og får:

$$
g'(1) = \frac{1}{f'(-0.7)} \approx -0.26
$$


::::

:::::::::::::::
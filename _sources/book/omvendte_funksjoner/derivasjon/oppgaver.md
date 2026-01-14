# Oppgaver: Derivasjon og omvendte funksjoner


:::::::::::::::{exercise} Oppgave 1

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En funksjon $f$ er gitt ved

$$
f(x) = x^4 \qder D_f = \real.
$$

1. Avgjør om $f$ har en omvendt funksjon. 
2. Bestem definisjonsmengden til den omvendte funksjonen hvis den eksisterer.


::::{answer}
$f$ har ikke en omvendt funksjon.
::::


::::{solution}
Vi deriverer $f$ for å avgjøre hvor grafen til $f$ stiger og synker.

$$
f'(x) = 4x^3
$$

Vi løser $f'(x) = 0$ for å finne eventuelle ekstremalpunkter:


$$
f'(x) = 0 \limplies 4x^3 = 0 \liff x = 0
$$

Vi kan tegne en fortegnslinje for $f'(x)$:

:::{signchart-2}
width: 100%
function: 4 * x**3, f'(x)
fontsize: 24
:::

Her kan vi se at grafen til $f$ synker før $x = 0$ og stiger etterpå. Dermed er ikke $f$ monoton på hele sin definisjonsmengde, som betyr at $f$ ikke har en omvendt funksjon. 



::::

:::::::::::::



:::::::::::::{tab-item} b
En funksjon $g$ er gitt ved

$$
g(x) = -x^3 + 1 \qder D_g = [-1, 1\rangle.
$$

1. Avgjør om $g$ har en omvendt funksjon.
2. Bestem definisjonsmengden til den omvendte funksjonen hvis den eksisterer.

::::{answer}
1. $g$ har en omvendt funksjon.
2. $D_{g^{-1}} = \langle 0, 2]$.
::::


::::{solution}
Vi deriverer $g$ får å avgjøre hvor grafen til $g$ stiger og synker:

$$
g'(x) = (-x^3 + 1)' = -3x^2
$$

Så løser vi $g'(x) = 0$ for å undersøke om $g$ har noen ekstremalpunkter: 

$$
g'(x) = 0 \liff -3x^2 = 0 \liff x = 0
$$

Så tegner vi et fortegnsskjema for $g'(x)$:

:::{signchart-2}
width: 100%
function: -3*x**2, g'(x)
:::

Vi kan se at grafen til $g$ synker i hele sin definisjonsmengde, som betyr at $g$ må ha en omvendt funksjon. 

Definisjonsmengden til den omvendte funksjonen, er lik verdimengden til $g$. For å finne definisjonsmengden til den omvendte funksjonen holder det å regne ut funksjonsverdiene til $g$ i endepunktene av definisjonsmengden til $g$ (siden $g$ alltid synker!): 

$$
g(-1) = -(-1)^3 + 1 = 2
$$

Dette punktet er inkludert i verdimengden til $g$ siden $x = -1$ er inkludert i definisjonsmengden til $g$.

$$
g(1) = -(1)^3 + 1 = 0
$$

Dette punktet er ikke inkludert i verdimengden til $g$ siden $x = 1$ ikke er inkludert i definisjonsmengden til $g$. Dermed er definisjonsmengden til den omvendte funksjonen gitt ved

$$
D_{g^{-1}} = \langle 0, 2].
$$




::::



:::::::::::::



:::::::::::::{tab-item} c
En funksjon $h$ er gitt ved

$$
h(x) = x^3 + 6x - 21 \qder D_h = \langle -2, 1\rangle.
$$

1. Avgjør om $h$ har en omvendt funksjon.
2. Bestem $D_{h^{-1}}$ hvis den omvendte funksjonen eksisterer.

::::{answer}
1. $h$ har en omvendt funksjon.
2. $D_{h^{-1}} = \langle -41, -14\rangle$.
::::


::::{solution}
Vi starter med å undersøke hvor $h$ har eventuelle ekstremalpunkter:

$$
h'(x) = (x^3 + 6x - 21)' = 3x^2 + 6
$$

som gir

$$
h'(x) = 0 \liff 3x^2 + 6 = 0 \liff x^2 + 2 = 0
$$

Dette er det samme som 

$$
x^2 = -2
$$

som ikke har noen løsning siden vi ikke kan opphøye et tall i $2$ og få noe negativt. Dermed har ikke grafen til $h$ noen ekstremalpunkter. I såfall må den alltid *enten* stige eller synke. Dermed vet vi at $h$ har en omvendt funksjon.

Definisjonsmengden til $h^{-1}$ er lik verdimengden til $h$. For å finne denne regner vi ut funksjonsverdiene til $h$ i endepunktene av definisjonsmengden til $h$ (siden $h$ enten alltid stiger eller alltid synker!):

$$
h(-2) = (-2)^3 + 6 \cdot (-2) - 21 = -8 - 12 - 21 = -41
$$

$$
h(1) = (1)^3 + 6 \cdot 1 - 21 = 1 + 6 - 21 = -14
$$

Ingen av punktene er inkludert i verdimengden til $h$ siden ingen av endepunktene er inkludert i definisjonsmengden til $h$. Dermed er definisjonsmengden til den omvendte funksjonen gitt ved

$$
D_{h^{-1}} = \langle -41, -14\rangle.
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
En funksjon $p$ er gitt ved

$$
p(x) = e^{-(x - 2)^2} \qder D_p = [2, \to\rangle.
$$

1. Avgjør om $p$ har en omvendt funksjon. 
2. Bestem definisjonsmengden til den omvendte funksjonen hvis den eksisterer.

::::{answer}
1. $p$ har en omvendt funksjon.
2. $D_{p^{-1}} = \langle 0, 1]$.
::::


::::{solution}
Vi starter med å undersøke om grafen til $p$ har noen ekstremalpunkter. Vi deriverer først ved å bruke kjerneregelen med $u = -(x - 2)^2$ som kjerne:

$$
\begin{align*}
p'(x) &= \left(e^{-(x - 2)^2}\right)'\\
\\
&= e^{-(x - 2)^2} \cdot \left(-(x - 2)^2\right)' \\
\\
&= e^{-(x - 2)^2} \cdot (-2(x - 2)) \\
\\
&= -2(x - 2)e^{-(x - 2)^2}
\end{align*}
$$

Så løser vi $p'(x) = 0$:

$$
p'(x) = 0 \limplies -2(x - 2)e^{-(x - 2)^2} = 0
$$

som betyr at 

$$
x - 2 = 0 \or e^{-(x - 2)^2} = 0
$$

Bare den første likiningen kan bli null, så da får vi at 

$$
x = 2
$$

Punktet ligger akkurat på kanten av definisjonsmengden. Siden $p$ ikke kan snu fra å stige til å synke eller omvendt uten å ha et ekstremalpunkt i mellom, så må $p$ være monoton i hele sin definisjonsmengde. Dermed har $p$ en omvendt funksjon.

Definisjonsmengden til $p^{-1}$ er lik verdimengden til $p$. Vi bestemmer denne ved å regne ut funksjonsverdiene til $p$ i endepunktene av definisjonsmengden til $p$ (siden $p$ enten alltid stiger eller alltid synker!):

$$
p(2) = e^{-(2 - 2)^2} = e^0 = 1
$$

Dette punktet er inkludert i verdimengden til $p$ siden $x = 2$ er inkludert i definisjonsmengden til $p$.

Siden vi ikke har et endepunkt på andre siden, men $x \to \infty$, så må vi sjekke hva som skjer med $p(x)$ når $x \to \infty$:

$$
\lim_{x \to \infty} p(x) = \lim_{x \to \infty} e^{-(x - 2)^2} = e^{-\infty} = 0
$$

Altså vil verdimengden til $p$, og dermed definisjonsmengden til $p^{-1}$ være

$$
D_{p^{-1}} = \langle 0, 1].
$$
::::


:::::::::::::





::::::::::::::
:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 2
::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
En funksjon $f$ er gitt ved 

$$
f(x) = (x + 3)^2 - 9 \qder D_f = \langle a, \to\rangle.
$$


Bestem det minste tallet $a$ slik at $f$ har en omvendt funksjon.

::::{answer}
$$
a = -3
$$
::::


::::{solution}
For å bestemme det minste tallet $a$ slik at $f$ har en omvendt funksjon, må vi sjekke hvor grafen til $f$ har ekstremalpunkter. Dette kan vi gjøre ved å løse $f'(x) = 0$:

$$
\begin{align*}
f'(x) &= \left((x + 3)^2 - 9\right)' \\
\\
&= 2(x + 3)
\end{align*}
$$

Så løser vi $f'(x) = 0$:

$$
f'(x) = 0 \liff 2(x + 3) = 0 \liff x = -3
$$

Altså har grafen til $f$ muligens et ekstremalpunkt i $x = -3$. Vi sjekker ved å tegne et fortegnsskjema for $f'(x)$: 

:::{signchart-2}
width: 100%
function: 2 * (x + 3), f'(x)
:::

Her ser vi at grafen til $f$ synker før $x = -3$ og stiger etterpå. Dermed vil $f$ ha en omvendt funksjon dersom $a \geq -3$. Det minste tallet for $a$ vi kan velge er derfor 

$$
a = -3.
$$

::::


:::::::::::::


:::::::::::::{tab-item} b
En funksjon $g$ er gitt ved 

$$
g(x) = -2x^3 + 3x \qder D_g = \langle \gets, a].
$$

Bestem det største tallet $a$ slik at $g$ har en omvendt funksjon.


::::{answer}
$$
a = -\dfrac{1}{\sqrt{2}} = -\dfrac{\sqrt{2}}{2}
$$
::::


::::{solution}
Vi må avgjøre hvor grafen til $g$ har eventuelle ekstremalpunkter, så da løser vi først $g'(x) = 0$:

$$
g'(x) = (-2x^3 + 3x)' = -6x^2 + 3
$$

som betyr at 

$$
g'(x) = 0 \liff -6x^2 + 3 = 0 \liff 6x^2 = 3
$$

som vi kan skrive om til 

$$
x^2 = \dfrac{1}{2} \liff x = \pm \dfrac{1}{\sqrt{2}} = \pm \dfrac{\sqrt{2}}{2}
$$

Deretter tegner vi et fortegnsskjema for $g'(x)$:

:::{signchart-2}
width: 100%
function: -6 * x**2 + 3, g'(x)
:::

Vi ser at begge punktene svarer til ekstremalpunkter siden den deriverte skifter fortegn rundt begge punktene. Det betyr at grafen til $g$ skifter fra å synke til å stige når vi kommer forbi det første punktet. Dermed vil det største tallet for $a$ som gir en omvendt funksjon for $g$ være

$$
a = -\dfrac{1}{\sqrt{2}} = -\dfrac{\sqrt{2}}{2}
$$


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


::::{solution}
Funksjonen $h$ er en andregradsfunksjon der funksjonsuttrykket til $h$ er skrevet på ekstremalpunktsform som betyr at grafen til $h$ har et ekstremalpunkt i $(1, -4)$. 

Det betyr at det minste tallet $a$ vi kan velge slik at $h$ har en omvendt funksjon og at $D_h$ er størst mulig blir 

$$
a = 1
$$

Grafen til $h$ er konveks siden den ledende koeffisienten er positiv, så det betyr at grafen til $h$ har et bunnpunkt i $(1, -4)$. Dermed vil $y = -4$ være den laveste mulige verdien på grafen, så verdimengden til $h$ blir

$$
V_h = [-4, \to \rangle
$$ 

Verdimengden til $h$ er lik definisjonsmengden til $h^{-1}$, så da følger det at 

$$
D_{h^{-1}} = [-4, \to \rangle.
$$
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


::::{solution}
Vi må undersøke hvor grafen til $k$ har eventuelle ekstremalpunkter. Vi deriverer først ved å bruke produktregelen:

$$
\begin{align*}
k'(x) &= \left(x^2 e^{-x}\right)' \\
\\
&= (x^2)' \cdot e^{-x} + x^2 \cdot (e^{-x})' \\
\\
&= 2x e^{-x} + x^2 \cdot (-e^{-x}) \\
\\
&= e^{-x}(2x - x^2)
\end{align*}
$$

Så løser vi $k'(x) = 0$: 

$$
k'(x) = 0 \limplies e^{-x}(2x - x^2) = 0
$$

som gir oss at 

$$
e^{-x} = 0 \or 2x - x^2 = 0
$$

Den første av de to likningene har ingen løsning. Dermed vil $k'(x) = 0$ hvis og bare hvis

$$
2x - x^2 = 0 \liff x(2 - x) = 0 \liff x = 0 \or x = 2
$$

Vi tegner et fortegnsskjema for $k'(x)$:

:::{signchart-2}
width: 100%
function: exp(-x) * (2 * x - x**2), k'(x)
:::

Altså vil grafen til $k$ stige mellom $x = 0$ og $x = 2$, men synke etter at $x = 2$. Dermed vil det største tallet for $a$ som gir en omvendt funksjon for $k$ være

$$
a = 2.
$$

For å finne definisjonsmengden til den omvendte funksjonen, må vi finne verdimengden til $k$. Vi regner ut funksjonsverdiene til $k$ i endepunktene av definisjonsmengden til $k$ (siden $k$ stiger helt fra $x = 0$ til $x = 2$): 

$$
k(0) = 0^2 e^{-0} = 0
$$

$$
k(2) = 2^2 e^{-2} = \dfrac{4}{e^2}
$$

Dette er endepunktene til verdimengden til $k$, og dermed endepunktene til definisjonsmengden til $k^{-1}$. Dermed har vi at 

$$
D_{k^{-1}} = \left[0, \dfrac{4}{e^2}\right]
$$


::::

:::::::::::::
::::::::::::::
:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 3

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
3. $-1 \in D_g$.


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
h(x) = x^3 e^{-x^2 + 1} \qder D_h = [a, b].
$$

Bestem $a$ og $b$ slik at 

* $h^{-1}$ eksisterer
* $D_{h^{-1}}$ blir så stor som mulig.


::::{answer}
$$
a = -\dfrac{\sqrt{6}}{2} \and b = \dfrac{\sqrt{6}}{2}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d

:::{cas-popup}
---
layout: sidebar
---
:::



En funksjon $k$ er gitt ved

$$
k(x) = (\log_2 x)^2 - \log_2 x + 1 \qder D_k = \langle a, \to\rangle.
$$

1. Bestem det minste tallet $a$ slik at $k$ har en omvendt funksjon.
2. Bestem definisjonsmengden til den omvendte funksjonen for dette tallet $a$.


::::{answer}
1. $a = \sqrt{2}$.
2. $D_{k^{-1}} = \left\langle\dfrac{3}{4}, \to\right\rangle$
::::


:::::::::::::


::::::::::::::


:::::::::::::::



---





:::::::::::::::{exercise} Oppgave 4

> Notasjonen for den deriverte til den omvendte funksjonen er litt knotete, men vi bør prøve å bli vant til skrivemåten. Å skrive $(f^{-1})'(y)$ er det samme som å skrive $g'(y)$ dersom $g = f^{-1}$. Men ved å bruke denne notasjonen slipper vi å gi et nytt navn til den omvendte funksjonen. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En funksjon $f$ er gitt ved

$$
f(x) = 2x^2 + 3 \qder D_f = \langle 0, \to\rangle.
$$

Bestem $(f^{-1})'(5)$.


::::{answer}
$$
(f^{-1})'(5) = \dfrac{1}{4}
$$
::::


::::{solution}
Vi vet at

$$
(f^{-1})'(y) = \dfrac{1}{f'(x)}
$$

Vi vet at $y = 5$, så vi må finne den tilhørende $x$-verdien. Da løser vi likningen $f(x) = 5$:

$$
f(x) = 5 \limplies 2x^2 + 3 = 5
$$

som gir

$$
2x^2 = 2 \liff x = \pm 1 \limplies x = 1
$$

Dermed vil 

$$
(f^{-1})'(5) = \dfrac{1}{f'(1)}
$$

Da får vi

$$
f'(x) = (2x^2 + 3)' = 4x \limplies f'(1) = 4
$$

som betyr at

$$
(f^{-1})'(5) = \dfrac{1}{f'(1)} = \dfrac{1}{4}
$$

::::


:::::::::::::


:::::::::::::{tab-item} b
En funksjon $g$ er gitt ved

$$
g(x) = x^3 + 2x + 1 \qder D_g = \langle -1, 2\rangle.
$$

Bestem $(g^{-1})'(1)$.


::::{answer}
$$
\left(g^{-1}\right)'(1) = \dfrac{1}{2}
$$
::::


::::{solution}
Vi vet at

$$
(g^{-1})'(y) = \dfrac{1}{g'(x)}
$$

Vi vet også at $y = 1$, så vi må finne den tilhørende $x$-verdien. Da løser vi likningen $g(x) = 1$:

$$
g(x) = 1 \limplies x^3 + 2x + 1 = 1
$$

som gir

$$
x^3 + 2x = 0 \limplies x(x^2 + 2) = 0 \liff x = 0
$$

som betyr at

$$
(g^{-1})'(1) = \dfrac{1}{g'(0)}
$$


Vi har at 

$$
g'(x) = 3x^2 + 2 \limplies g'(0) = 2.
$$

Altså er 

$$
\left(g^{-1}\right)'(1) = \dfrac{1}{g'(0)} = \dfrac{1}{2}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
En funksjon $f$ er gitt ved

$$
h(x) = \sqrt{x^2 + 3} \qder D_h = \langle 0, \to\rangle.
$$

Bestem $(h^{-1})'(2)$.


::::{answer}
$$
(h^{-1})'(2) = 2
$$
::::

::::{solution}
Vi vet at

$$
(h^{-1})'(y) = \dfrac{1}{h'(x)}
$$

Vi vet også at $y = 2$, så vi må finne den tilhørende $x$-verdien. Da løser vi likningen $h(x) = 2$:

$$
h(x) = 2 \limplies \sqrt{x^2 + 3} = 2
$$

Vi kvadrerer begge sider og får

$$
(\sqrt{x^2 + 3})^2 = 2^2 \limplies x^2 + 3 = 4 \liff x^2 = 1 \limplies x = 1
$$

som betyr at

$$
(h^{-1})'(2) = \dfrac{1}{h'(1)}
$$

Vi deriverer $h(x)$ med kjerneregelen:

$$
h'(x) = \left(\sqrt{x^2 + 3}\right)' = \dfrac{2x}{2\sqrt{x^2 + 3}} = \dfrac{x}{\sqrt{x^2 + 3}}
$$

Da får vi

$$
h'(1) = \dfrac{1}{\sqrt{1^2 + 3}} = \dfrac{1}{2}
$$

Altså er


$$
(h^{-1})'(2) = \dfrac{1}{h'(1)} = \dfrac{1}{\frac{1}{2}} = 2
$$


::::

:::::::::::::


:::::::::::::{tab-item} d
En funksjon $p$ er gitt ved

$$
p(x) = \dfrac{\ln x}{x} \qder D_p = \langle 0, 2\rangle.
$$

Bestem $(p^{-1})'(0)$.


::::{answer}
$$
(p^{-1})'(0) = 1
$$
::::


::::{solution}
Vi vet at

$$
(p^{-1})'(y) = \dfrac{1}{p'(x)}
$$

Vi vet også at $y = 0$, så vi må finne den tilhørende $x$-verdien. Da løser vi likningen $p(x) = 0$:

$$
p(x) = 0 \limplies \dfrac{\ln x}{x} = 0 \limplies \ln x = 0 \liff x = 1
$$

som betyr at

$$
(p^{-1})'(0) = \dfrac{1}{p'(1)}
$$

Vi deriverer $p(x)$ med brøkregelen:

$$
p'(x) = \left(\dfrac{\ln x}{x}\right)' = \dfrac{\frac{1}{x} \cdot x - \ln x \cdot 1}{x^2} = \dfrac{1 - \ln x}{x^2}
$$

Da får vi

$$
p'(1) = \dfrac{1 - \ln 1}{1^2} = 1
$$

Altså er

$$
(p^{-1})'(0) = \dfrac{1}{p'(1)} = \dfrac{1}{1} = 1
$$
::::

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
En funksjon $f$ har en tangent i punktet $(1, 2)$ med stigningstall $4$.

Bestem stigningstallet til tangenten til grafen til $f^{-1}$ i $(2, 1)$.


::::{answer}
$$
\dfrac{1}{4}
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
En funksjon $g$ har nøyaktig én tangent med stigningstall $2$ som går gjennom punktet $(2, 5)$. 

Bestem koordinatene til punktet på grafen til $g^{-1}$ der $(g^{-1})'(y) = \dfrac{1}{2}$.

::::{answer}
$$
(5, 2)
$$
::::
:::::::::::::



:::::::::::::{tab-item} c
En funksjon $h$ har en tangent i punktet $(2, h(2))$ som har likningen

$$
y = -3x + 7.
$$

Bestem koordinatene til et punkt på grafen til $h^{-1}$ der en tangent har stigningstall $-\dfrac{1}{3}$.

::::{answer}
$$
\left(1, 2\right)
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
En tangent til grafen til $p^{-1}$ i punktet $(4, 1)$ har stigningstall $5$.

Bestem $p'(1)$


::::{answer}
$$
p'(1) = \dfrac{1}{5}
$$
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

:::{cas-popup}
---
layout: sidebar
---
:::


En funksjon $f$ er gitt ved

$$
f(x) = x \ln x \qder x \in \langle 0, \to\rangle. 
$$

La $g$ være den omvendte funksjonen til $f$.

Bestem $g'(4)$.


::::{answer}
$$
g'(4) \approx 0.45
$$
::::


:::::::::::::



:::::::::::::{tab-item} b


:::{cas-popup}
---
layout: sidebar
---
:::



En funksjon $f$ er gitt ved

$$
f(x) = x^3 + 3x - 2 \qder D_f = \real.
$$


La $g$ være den omvendte funksjonen til $f$.

Bestem $g'(12)$.

::::{answer}
$$
g'(12) = \dfrac{1}{435}
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


En funksjon $f$ er gitt ved

$$
f(x) = \dfrac{1}{3}x^3 - 2x^2 + 1
$$

og har definisjonsmengden $I = [a, b]$ der $a, b \in \real$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem det største intervallet $I$ slik at $f$ har en omvendt funksjon $g$ når $2 \in I$.


::::{answer}
$$
I = [0, 4]
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem stigningstallet til tangenten til grafen til $g$ i punktet $(-10, 3)$.


::::{answer}
$$
-\dfrac{1}{3}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Grafen til $g$ har en annen tangent med samme stigningstall som tangenten i punktet $(-10, 3)$. 

Bestem koordinatene til tangeringspunktet.


::::{answer}
$$
\left(-\dfrac{2}{3}, 1\right)
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
:::{cas-popup}
---
layout: sidebar
---
:::


En funksjon $f$ er gitt ved 

$$
f(x) = x e^{-ax} \qder D_f = \langle 0, 3\rangle.
$$

der $a > 0$.

For hvilke verdier av $a$ har $f$ en omvendt funksjon?


::::{answer}
$$
a \in \left[\dfrac{1}{3}, \to\right\rangle
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
g(x) = \dfrac{1}{3}x^3 + bx^2 - 6 \qder D_g = \langle 2, \to\rangle.
$$

For hvilke verdier av $b$ har $g$ en omvendt funksjon?


::::{answer}
$$
b \in \langle \gets, -1]
$$
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


Om en andregradsfunksjon $f$ får du vite at

* Den største definisjonsmengden som $f$ har en omvendt funksjon på er $D_f = [2, \to\rangle$.
* Punktet $(3, -8)$ ligger på grafen til $f$.
* $(f^{-1})'(-8) = \dfrac{1}{2}$

Bestem $f(x)$.


::::{answer}
$$
f(x) = x^2 - 4x - 5
$$
::::

:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::



Om en tredjegradsfunksjon $g$ får du vite at

* Det største lukkede intervallet $g$ har en omvendt funksjon på er $I = [-1, 3]$.
* Punktet $(2, 5)$ ligger på grafen til $g$.
* $(g^{-1})'(5) = \dfrac{1}{9}$

Bestem $g(x)$.


::::{answer}
$$
g(x) = -x^3 + 3x^2 + 9x - 17
$$
::::


:::::::::::::


::::::::::::::
:::::::::::::::


---




:::::::::::::::{exercise} Oppgave 10

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


::::{solution}
Vi må passe på at $f$ er monoton i hele sin definisjonsmengde for at det skal eksistere en omvendt funksjon $f^{-1}$. Vi deriverer $f$ og finner ut hvordan $f'(x)$ har eventuelle ekstremalpunkter:

$$
f'(x) = (x^4 - bx^3 + 2)' = 4x^3 - 3bx^2 = x^2(4x - 3b)
$$

Så løser vi $f'(x) = 0$ for å finne eventuelle ekstremalpunkter:

$$
f'(x) = 0 \limplies x^2(4x - 3b) = 0 \liff x = 0 \or x = \dfrac{3b}{4}
$$

Siden $f'(x)$ inneholder faktoren $x^2$, så vil ikke fortegnet til $f'(x)$ endre seg når vi passer gjennom $x = 0$. Det betyr at det er faktoren $(4x - 3b)$ som avgjør når fortegnet til $f'(x)$ endrer seg. Vi må derfor passe på at $x = \dfrac{3b}{4}$ ligger på kanten eller utenfor definisjonsmengden til $f$. For å sikre dette, så må vi kreve at 

$$
\dfrac{3b}{4} \leq -3 \liff b \leq -4.
$$

Altså vil $f$ har en omvendt funksjon dersom

$$
b \in \langle \gets, -4].
$$
::::



:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 11

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


::::{answer}
$$
k \in [-2, 2]
$$
::::



:::::{solution}
Vi lar 

$$
g(x) = -x^2 + (2 + k)x \qder x < k
$$

og

$$
h(x) = x^2 + (2 - k)x \qder x \geq k.
$$

Både $g$ og $h$ er andregradsfunksjoner som betyr at de er monotone på hver side av ekstremalpunktene sine. Vi har at

$$
g'(x) = (-x^2 + (2 + k)x)' = -2x + 2 + k = 0 \liff x = \dfrac{k + 2}{2}
$$

Ekstremalpunktet til $g$ vil derfor ligge midt mellom $x = k$ og $x = 2$ siden ekstremalpunktet er gjennomsnittet av de to punktene. Dersom vi velger $k = 2$, så ligger ekstremalpunktet akkurat på kanten av definisjonsmengden til $g$ i $x = k$. Dersom vi velger $k > 2$, så vil ekstremalpunktet havne en plass der $x < k$ og ligge innenfor definisjonsmengden til $g$. Da vil ikke $g$ være en monoton funksjon på sin definisjonsmengde. Det betyr at vi må minst kreve at $k \leq 2$.

:::{plot}
width: 50%
ymin: -16
ymax: 16
yticks: off
grid: off
function: -x**2 + (2 + 3) * x, (-10, 3), g, blue
function: x**2 + (2 - 3) * x, [3, 10), h, red 
function-endpoints: true

Grafen til $f$ når $k > 2$.
:::


På samme måte har vi at

$$
h'(x) = (x^2 + (2 - k)x)' = 2x + 2 - k = 0 \liff x = \dfrac{k - 2}{2}
$$

Ekstremalpunktet til $h$ vil derfor ligge midt mellom $x = k$ og $x = -2$ siden ekstremalpunktet er gjennomsnittet av de to punktene. Dersom vi velger $k = -2$, så ligger ekstremalpunktet akkurat på kanten av definisjonsmengden til $h$ i $x = k$. Dersom vi velger $k < -2$, så vil ekstremalpunktet havne en plass der $x > k$ og ligge innenfor definisjonsmengden til $h$. Da vil ikke $h$ være en monoton funksjon. Det betyr at vi må minst kreve at $k \geq -2$.

:::{plot}
width: 50%
ymin: -16
ymax: 16
yticks: off
grid: off
function: -x**2 + (2 - 4) * x, (-10, -4), g, blue
function: x**2 + (2 + 4) * x, [-4, 10), h, red 
function-endpoints: true

Grafen til $f$ når $k < -2$.
:::


Altså må 

$$
k \geq -2 \and k \leq 2 \liff k \in [-2, 2].
$$

Da vil $f$ være monoton på hele sin definisjonsmengde siden både $g$ og $h$ blir det. Dermed har $f$ en omvendt funksjon dersom 

$$
k \in [-2, 2].
$$


:::{plot}
width: 50%
ymin: -16
ymax: 16
yticks: off
grid: off
function: -x**2 + (2 + 1) * x, (-10, 1), g, blue
function: x**2 + (2 - 1) * x, [1, 10), h, red 
function-endpoints: true

Grafen til $f$ når $-2 \leq k \leq 2$.
:::



:::::


:::::::::::::::





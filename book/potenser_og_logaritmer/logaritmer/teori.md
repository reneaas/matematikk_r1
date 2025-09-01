# Logaritmer

:::{goals} Læringsmål
* Kunne beskrive sammenhengen mellom eksponentialfunksjoner og logaritmer
* Kunne bruke grafiske framstillinger av eksponentialfunksjoner til å bestemme verdien til logaritmer
* Kunne bruke potensregning til å bestemme verdien til logaritmer
:::


## Definisjon


:::::::::::::::{summary} Logaritmer
Logaritmen med grunntall $a$ skriver vi som 

$$
x = \log_{\displaystyle a}(y)
$$

Verdien til logaritmen er $x$-koordinaten til et punkt $(x, y)$ på grafen til $y = a^x$. 
:::::::::::::::


---


Det er sjeldent vi kan lese av den *eksakte* verdien til en logaritme fra grafen til en eksponentialfunksjon, men vi kan likevel lese av *tilnærmede* verdier. 

:::::::::::::::{example} Eksempel 1
Nedenfor vises grafen til $f(x) = 10^x$. 

Bestem $\log_{10}(2)$.


:::{plot}
width: 80%
function: 10^x, f(x) = 10^x
xmin: -0.1
xmax: 1.1
xstep: 0.1
ymin: -1
ymax: 11
ystep: 1
:::


::::{solution}
---
dropdown: 0
---

Vi tegner en horisontal linje $y = 2$ og sjekker når den treffer grafen. Deretter tegner vi en vertikal linje ned til $x$-aksen for å lese av $x$-koordinaten til skjæringspunktet:


:::{plot}
width: 80%
function: 10^x, f(x) = 10^x
xmin: -0.1
xmax: 1.1
xstep: 0.1
ymin: -1
ymax: 11
ystep: 1
hline: 2, 0, 0.3, dashed
vline: 0.3, 0, 2, dashed
point: (0.3, 2)
:::


Vi ser at når $y \approx 2$ på grafen til $f$, så er $x \approx 0.3$. Det betyr at 

$$
\log_{10}(2) \approx 0.3
$$
::::



:::::::::::::::



---




Fra Eksempel 1, kan vi forstå logaritmen som "hva må vi opphøye $a$ med for å få $y$?: 

$$
a^x = y
$$





:::::::::::::::{summary} Logaritmer
Logaritmen med grunntall $a$ er den verdien av $x$ vi må opphøye $a$ med for å få $y$:

$$
\log_{\displaystyle a}(y) = x \liff a^x = y
$$
:::::::::::::::


:::::::::::::::{example} Eksempel
Bestem $\log_5(125)$.


::::{solution}
---
dropdown: 0
---
:::{factor-tree}
n: 125
width: 60%
align: right
figsize: (3, 3)
:::

For å bestemme $\log_5(125)$, må vi finne hvilket tall vi må opphøye $5$ med for å få $125$. Vi kan lage et faktortre som vist til høyre. Da ser vi at 

$$
125 = 5^3
$$

Det betyr at 

$$
\log_5(125) = 3
$$


::::

:::::::::::::::



---



## Logaritmefunksjoner

Hvis vi ser på grafen til en eksponentialfunksjon, vil vi oppdage at for hver $y$-verdi, finnes det bare én $x$-verdi:



:::{plot}
width: 60%
function: 10^x, f(x) = a^x
xmin: -1
xmax: 2
ymin: -1
ymax: 100
ticks: off
hline: 50, 0, 1.7, dashed
vline: 1.7, 0, 50, dashed
point: (1.7, 50)
text: 1.7, 50, "$(x, y)$", center-right
:::


Det lar oss definere en **logaritmefunksjon** for hvert grunntall $a$ på formen $g(x) = \log_a(x)$. Tegner vi de to funksjonene i samme koordinatssystem, får vi grafen til $f(x) = a^x$ speilet om linja $y = x$. Se figuren nedenfor.


:::{plot}
width: 80%
function: 3^x, f(x) = a^x, (-10, 10), blue
function: log(x) / log(3), g(x) = \log_a(x), (0.000001, 6), red
line: 1, 0, epic
ticks: off
xmin: -6
xmax: 6
ymin: -6
ymax: 6
point: (0, 1)
point: (1, 0)
text: 0, 1, "$(0, 1)$", center-left
text: 1, 0, "$(1, 0)$", bottom-right
point: (3, 1)
point: (1, 3)
text: 3, 1, "$(a, 1)$", top-center
text: 1, 3, "$(1, a)$", center-right
:::

La oss spesielt legge merke til punktene som er markert på de to grafene. For eksponentialfunksjonen $f$, ser vi at den skjærer $y$-aksen i $(0, 1)$. Når $x = 1$, så vil vi få at $f(1) = a$ siden da har vi opphøyd grunntallet $a$ med $1$. Derfor går grafen gjennom punktet $(1, a)$. 

Logaritmefunksjonen på sin side skjærer i stedet $x$-aksen i $(1, 0)$. Når vi beveger oss til $x = a$ så går grafen gjennom punktet $(a, 1)$ som samsvarer med at logaritmen fås ved å stille spørsmålet "hvilket tall må vi opphøye grunntallet i for å få $a$?". Vel det er jo $1$ siden $a^1 = a$. 

Vi ser koordinatene til de to grafene bare har byttet plass som skyldes at vi kan lage grafen til logaritmefunksjonen ved å speile grafen til eksponentialfunksjonen om linja $y = x$.


:::::::::::::::{summary} Logaritmefunksjoner
Logaritmefunksjonen $g$ med grunntall $a$ skriver vi som

$$
g(x) = \log_a(x) \qder D_g = \langle 0, \to \rangle.
$$

Grafen til logaritmefunksjonen er grafen til eksponentialfunksjonen $y = a^x$ speilet om linja $y = x$.



:::::::::::::::


## Logaritmesetningene
Logaritmer har regneregler som er spesielt nyttig for å skrive om uttrykk med logaritmer – vi kommer til å trenge dem når vi jobber med logaritmelikninger og eksponentiallikninger. Reglene har en én-til-én sammenheng med potensreglene som vi skal se nedenfor.

:::::::::::::::{summary} Produktregelen for logaritmer
For alle tall $x, y \in \langle 0, \to \rangle$ gjelder:

$$
\log_a(xy) = \log_a(x) + \log_a(y)
$$


::::::::::::::{admonition} Bevis
---
class: theory, dropdown
---
Vi starter med å tenke oss at vi skriver $x$ og $y$ som potenser med grunntall $a$ slik at

$$
x = a^p \and y = a^q
$$

Siden $\log_a(x)$ er er hvilket tall vi må opphøye $a$ i for å få $x$, betyr det at $\log_a(x) = p$. På samme måte har vi at $\log_a(y) = q$. I tillegg gir potensreglene vi har sett på at

$$
x \cdot y = a^p \cdot a^q = a^{p+q}
$$

Dermed må 

$$
\log_a(xy) = p + q = \log_a(x) + \log_a(y)
$$


::::::::::::::



:::::::::::::::


---


:::::::::::::::{example} Eksempel 3
Grafen til eksponentialfunksjonen $f(x) = 5^x$ er vist i figuren nedenfor.

Bruk grafen til å bestemme en tilnærmet verdi for $\log_5(36)$

:::{plot}
width: 80%
function: 5^x, f
ymin: -1
ymax: 26
ystep: 2
xmin: -0.2
xmax: 2.5
xstep: 0.2
:::



::::{solution}
---
dropdown: 0
---
Vi kan ikke lese av hva verdien av $x$ må være for at $5^x = 36$ direkte fra grafen. Men vi kan faktorisere $36$ som

$$
36 = 2 \cdot 18
$$

som betyr at vi kan bruke produktregelen for logaritmer:

$$
\log_5(36) = \log_5(2 \cdot 18) = \log_5(2) + \log_5(18)
$$

Fra grafen til $f$, kan vi se at grafen omtrent går gjennom punktet $(0.4, 2)$ som betyr at $\log_5(2) \approx 0.4$.

Vi kan også se at grafen går gjennom punktet $(1.8, 18)$ som betyr at $\log_5(18) \approx 1.8$.

Dermed får vi at

$$
\log_5(36) \approx 0.4 + 1.8 = 2.2
$$
::::

:::::::::::::::


---


:::::::::::::::{summary} Kvotientregelen for logaritmer
For alle tall $x, y \in \langle 0, \to \rangle$ gjelder:

$$
\log_a\left(\frac{x}{y}\right) = \log_a(x) - \log_a(y)
$$


::::::::::::::{admonition} Bevis 
---
class: theory, dropdown
---
Vi starter med å tenke oss at vi skriver $x$ og $y$ som potenser med grunntall $a$ slik at

$$
x = a^p \and y = a^q
$$

Dette betyr at 

$$
\log_a(x) = p \and \log_a(y) = q
$$

Med potensregelen for brøker får vi:

$$
\dfrac{a^p}{a^q} = a^{p-q} \liff \log_a\left(\frac{x}{y}\right) = p - q = \log_a(x) - \log_a(y)
$$
::::::::::::::

:::::::::::::::


---


:::::::::::::::{example} Eksempel 4
I figuren nedenfor vises grafen til $f(x) = 3^x$. 

Bruk grafen til å bestemme $\log_3\left(\dfrac{3}{27}\right)$.

:::{plot}
width: 80%
function: 3^x
xmin: -1
xmax: 4
ymin: -3
ymax: 30
ystep: 3
:::


::::{solution}
---
dropdown: 0
---
Vi kan ikke lese av hva løsningen av likningen $3^x = \dfrac{1}{9}$ må være direkte fra grafen. Men vi kan skrive om uttrykket med kvotientregelen som

$$
\log_3\left(\dfrac{3}{27}\right) = \log_3(3) - \log_3(27)
$$

Deretter kan vi lese av grafen at $\log_3(3) = 1$ siden grafen går gjennom $(1, 3)$ og $\log_3(27) = 3$ siden grafen går gjennom $(3, 27)$. Dermed får vi at

$$
\log_3\left(\dfrac{3}{27}\right) = 1 - 3 = -2
$$

Vi ser at logaritmen blir negativ når vi tar logaritmen av et tall $x \in \langle 0, 1 \rangle$. Dette henger sammen med potensregelen $a^{-p} = \dfrac{1}{a^p}$. I dette tilfellet er det fordi

$$
\dfrac{3}{27} = \dfrac{3}{3^3} = 3^{1-3} = 3^{-2}
$$

Så for å få $\dfrac{3}{27}$, må vi opphøye $3$ med eksponenten $-2$ som forklarer hvorfor $\log_3\left(\dfrac{3}{27}\right) = -2$.
::::


:::::::::::::::


---



:::::::::::::::{summary} Potensregelen for logaritmer
For alle tall $x \in \langle 0, \to \rangle$ og $b \in \mathbb{R}$ gjelder:

$$
\log_a(x^b) = b \cdot \log_a(x)
$$


::::::::::::::{admonition} Bevis
---
class: theory, dropdown
---
Vi tenker oss at vi kan skrive $x$ som en potens med grunntall $a$ slik at

$$
x = a^p \liff \log_a(x) = p
$$

Videre kan vi bruke potensregelen $(a^p)^q = a^{p \cdot q}$, men tilpasset med variablene vi har med å gjøre:


$$
x^b = (a^p)^b = a^{p\cdot b} \liff \log_a(x^b) = p \cdot b = \log_a(x) \cdot b
$$

Dermed er 

$$
\log_a(x^b) = b \cdot \log_a(x)
$$

::::::::::::::

:::::::::::::::


---


:::::::::::::::{example} Eksempel 5
Regn ut

$$
\log_5(25^3)
$$


::::{solution}
---
dropdown: 0
---
Vi skriver om $25$ som en potens med grunntall $5$:

$$
25 = 5^2. 
$$

Deretter kan vi skrive

$$
\log_5(25^3) = \log_5((5^2)^3) = \log_5(5^{2 \cdot 3}) = \log_5(5^{6}) = 6 \cdot \log_5(5) = 6 \cdot 1 = 6.
$$

::::


:::::::::::::::


---


:::::::::::::::{example} Eksempel 6
Regn ut $\log_2\left(\dfrac{1}{128}\right)$.


::::{solution}
---
dropdown: 0
---

:::{factor-tree}
n: 128
width: 100%
align: right
figsize: 4, 8
nocache:
:::


Vi starter med å primtallsfaktorisere $128$ så vi kan skrive den som et produkt av potenser. Fra faktortreet til høyre ser vi at

$$
128 = 2^7
$$

Det betyr at 

\begin{align*}
\log_2\left(\dfrac{1}{128}\right) &= \log_2\left(\dfrac{1}{2^7}\right) \\
\\
&= \log_2\left(2^{-7}\right) \\
\\
&= -7 \cdot \log_2(2) \\
\\
&= -7 \cdot 1 = -7.
\end{align*}
::::



:::::::::::::::


4. **Logaritme av 1**: 

   $$
   \log_a(1) = 0
   $$

5. Bytte av grunntall: 

   $$
   \log_a(b) = \frac{\log_c(b)}{\log_c(a)}
   $$

6. Logaritme av grunntallet:

   $$
   \log_a(a) = 1
   $$

# Vektorer


:::{admonition} Læringsmål
---
class: tip
---
* Kunne forklare hva en vektor er geometrisk.
* Kunne forklare hva det vil si at to vektorer er like, og kunne avgjøre om to vektorer er like.
* Kunne bestemme lengden av en vektor.
* Kunne forklare og utføre skalarmultiplikasjon av vektorer.
* Kunne forklare og utføre addisjon og subtraksjon av vektorer.
* Kunne forklare hva det vil si at to vektorer er parallelle og avgjøre om to vektorer er parallelle.
:::


En **vektor** er en pil som har **retning** og **lengde**. Vektorer kan brukes til å beskrive posisjoner i et koordinatsystem, forflytninger, sidelengder i trekanter, linjer og mye mer. For nå skal vi forstå noen grunnleggende regneregler for vektorer og hva disse betyr geometrisk i et koordinatsystem.

For å beskrive en vektor gir vi den et navn og tegner en pil over navnet. For eksempel kan vi kalle en vektor for $\vec{a}~.$ Da leser vi dette som "$a$-vektor". 

Vi beskriver ofte vektorer matematisk med koordinater i et koordinatsystem, og da bruker vi hakeparenteser $[\cdot,\cdot]$ rundt koordinatene. Koordinatene til en vektor forteller oss hvor mye vektoren flytter seg i $x$- og $y$-retning.



:::::::::::::::{summary} Vektorkoordinater

:::{plot}
align: right
width: 100%
vector: 1, 2, 1, 2, blue
xmin: -0.5
xmax: 2.5
ymin: -0.5
ymax: 4.5
ticks: off
fontsize: 30
text: 1 + 0.5 * 1, 2 + 0.5 * 2, "$\vec{a}$", top-left
hline: 2, 1, 2, dashed, gray
vline: 2, 2, 4, dashed, gray
text: 1.5, 2, "$a_x$", bottom-center
text: 2, 3, "$a_y$", center-right
:::


En **vektor** $\vec{a}$ er en pil som har **retning** og **lengde**. 

Når vektoren $\vec{a}$ flytter seg $a_x$ enheter i $x$-retning og $a_y$ enheter i $y$-retning fra startpunktet sitt, skriver vi vektoren med koordinatene

$$
\vec{a} = [a_x, a_y]
$$


Vi kaller $a_x$ for **$x$-komponenten** til vektoren, og $a_y$ for **$y$-komponenten** til vektoren.

:::::::::::::::


---


:::::::::::::::{example} Eksempel 1

:::{plot}
align: right
width: 100%
vector: (1, 1), (4, 3), blue
text: 0.5 * (1 + 4), 0.5 * (1 + 3), "$\vec{a}$", top-left
xmin: -1
ymin: -1
xmax: 5
ymax: 4
fontsize: 30
:::



En vektor $\vec{a}$ er vist i koordinatsystemet til høyre.

Bestem $\vec{a}$. 


:::{clear}
:::

::::{solution}
---
dropdown: 0
---
Vi kan se at vektoren flytter seg $3$ enheter i $x$-retning og $2$ enheter i $y$-retning fra startpunktet sitt. Dermed er $a_x = 3$ og $a_y = 2$. Da kan vi skrive vektoren som:

$$
\vec{a} = [3, 2]
$$
::::
:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 1

:::{plot}
align: right
width: 100%
vector: (-3, 2), (-1, -4), blue
vector: (0, 0), (3, 1), red
text: -1.5, -2.5, "$\vec{a}$", bottom-left
text: 1.5, 0.5, "$\vec{b}$", top-right
xmin: -5
ymin: -5
xmax: 5
ymax: 5
fontsize: 30
:::



I koordinatsystemet til høyre er det tegnet inn to vektorer $\vec{a}$ og $\vec{b}$.

Bestem $\vec{a}$ og $\vec{b}$. 


:::{clear}
:::


::::{answer}
$$
\vec{a} = [2, -6] \qog \vec{b} = [3, 1]
$$
::::


::::{solution}
Vektoren $\vec{a}$ flytter seg $2$ enheter i $x$-retning fra startpunktet sitt som gir $a_x = 2$. Den flytter seg $-6$ enheter i $y$-retning fra startpunktet sitt som betyr at $a_y = -6$. Dermed er

$$
\vec{a} = [2, -6]
$$

Vektoren $\vec{b}$ flytter seg $3$ enheter i $x$-retning fra startpunktet sitt som betyr at $b_x = 3$. Vektoren flytter seg $1$ enhet i $y$-retning fra startpunktet sitt som betyr at $b_y = 1$. Dermed er

$$
\vec{b} = [3, 1]
$$
::::
:::::::::::::::


---


## Like vektorer
To vektorer er like dersom de har samme retning og lengde. Det betyr at to vektorer regnes som like dersom de forflytter seg like mye fra et startpunkt, men de trenger **ikke** å starte i samme punkt.


:::::::::::::::{summary} Like vektorer
To vektorer $\vec{a} = [a_x, a_y]$ og $\vec{b} = [b_x, b_y]$ er like hvis

$$
a_x = b_x \and a_y = b_y
$$

De to vektorene trenger ikke starte i samme punkt.


::::{multi-plot2}
---
rows: 1
cols: 2
fontsize: 30
---

:::{plot}
vector: -1, -2, 3, 1, blue
vector: 2, 1, 3, 1, red
text: 1, -2, "$\vec{a}$", bottom-right
text: 0.5 * (2 + 5), 0.5 * (1 + 2), "$\vec{b}$", top-left

Vektor $\vec{a}$ og $\vec{b}$ er like fordi de har samme lengde og retning. De flytter seg like mye i $x$- og $y$-retning fra startpunktene sine.
:::


:::{plot}
vector: -1, -2, 3, 1, blue
vector: 2, 1, 1, 3, red
text: 1, -2, "$\vec{a}$", bottom-right
text: 2.5, 2.5, "$\vec{b}$", bottom-right

Vektor $\vec{a}$ og $\vec{b}$ er ulike fordi de har forskjellig lengde og retning. De flytter seg ulikt i $x$- og $y$-retning fra startpunktene sine.
:::




::::





:::::::::::::::



## Lengden av en vektor
Lengden av en vektor er avstanden fra startpunktet til endpunktet til vektoren. Dette vil samsvare med hypotenusen i en rettvinklet trekant som er hva vi skal definere lengden av en vektor til å være.


:::::::::::::::{summary} Lengden av vektor

:::{plot}
figsize: (4, 3)
align: right
width: 100%
vector: 0, 0, 1, 2, blue
xmin: -0.1
xmax: 1.5
ymin: -0.2
ymax: 2.2
ticks: off
text: 0.5 * (1 + 0), 0.5 * (2 + 0), "$\vec{a}$", top-left
hline: 0, 0, 1, dashed, gray
vline: 1, 0, 2, dashed, gray
polygon: (1, 0), (0.9, 0), (0.9, 0.225), (1, 0.225)
axis: off
text: 0.5, 0, "$a_x$", bottom-center
text: 1, 1, "$a_y$", center-right
fontsize: 25
:::

For en vektor $\vec{a}$ skriver vi lengden av vektoren som $\len{a}$. 

Hvis vektoren $\vec{a}$ har vektorkoordinatene

$$
\vec{a} = [a_x, a_y]
$$

så er lengden av vektoren gitt ved Pytagoras' setning:

$$
\len{a} = \sqrt{a_x^2 + a_y^2}
$$




:::::::::::::::


---

Vi tar et eksempel.

:::::::::::::::{example} Eksempel 2

:::{plot}
align: right
width: 100%
vector: 1, 1, 3, 4, blue
xmin: -1
ymin: -1
xmax: 5
ymax: 6
text: 0.5 * (1 + 4), 0.5 * (1 + 5), "$\vec{a}$", top-left
hline: 1, 1, 4, dashed, gray
vline: 4, 1, 5, dashed, gray
text: 0.5 * (1 + 4), 1, "$3$", bottom-center
text: 4, 0.5 * (1 + 5), "$4$", center-right
fontsize: 30
:::



En vektor $\vec{a}$ er gitt ved

$$
\vec{a} = [3, 4]
$$

Bestem $\len{a}$.


:::{clear}
:::


::::{solution}
---
dropdown: 0
---

Lengden av vektoren får vi ved å bruke Pytagoras' setning der $x$-komponenten og $y$-komponenten er katetene:

$$
\len{a} = \sqrt{a_x^2 + a_y^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

::::


:::::::::::::::




---




:::::::::::::::{exercise} Underveisoppgave 2
To vektorer er gitt ved

$$
\vec{a} = [1, 3] \qog \vec{b} = [-2, 3]
$$

Bestem $\len{a}$ og $\len{b}$.


::::{answer}
$$
\len{a} = \sqrt{10} \qog \len{b} = \sqrt{13}
$$
::::


::::{solution}
Vi bruker Pytagoras' setning for å regne ut lengdene:

$$
\len{a} = \sqrt{1^2 + 3^2} = \sqrt{1 + 9} = \sqrt{10}
$$

og 

$$
\len{b} = \sqrt{(-2)^2 + 3^2} = \sqrt{4 + 9} = \sqrt{13}
$$

::::

:::::::::::::::






---



## Skalarmultiplikasjon med vektorer

:::{plot}
align: right
width: 100%
vector: (1, 1), (3, 3), red
vector: (3, 3), (5, 5), red
vector: (1, 0), (5, 4), blue
vector: (3, -1), (1, -3), purple
vector: (3, -4), (2, -5), purple
text: 0.5 * (1 + 3), 0.5 * (1 + 3), "$\vec{a}$", top-left
text: 0.5 * (3 + 5), 0.5 * (3 + 5), "$\vec{a}$", top-left
text: 0.5 * (1 + 5), 0.5 * (0 + 4), "$2 \cdot \vec{a}$", bottom-right
text: 0.5 * (3 + 1), 0.5 * (-1 + -3), "$-\vec{a}$", bottom-right
text: 0.5 * (3 + 2), 0.5 * (-4 + -5), "$-\displaystyle \frac{1}{2} \cdot \vec{a}$", bottom-right
xmin: -2
fontsize: 30
:::


Vi kan gange en vektor med et tall. Tallet kaller vi for en **skalar**. Når vi ganger en vektor med en skalar, kaller vi det for **skalarmultiplikasjon**. 

Når vi ganger en vektor med et tall, så kan vi tolke det som hvor mange ganger vi skal følge vektoren i en bestemt retning. Ganger vi vektoren med $2$, så følger vi vektoren to ganger så langt i samme retning, så da får vi en dobbelt så lang vektor.

Ganger vi en vektor med $-1$, skal vi følge vektoren i motsatt retning, så da får vi en vektor som er like lang som den opprinnelige vektoren, men som peker i motsatt retning.

Ganger vi vektoren med $-\dfrac{1}{2}$ så gjør vi vektoren halvparten så lang og følger den i motsatt retning.

:::{interactive-graph} 
interactive-var: k, -5, 5, 64
interactive-var-start: 1
vector: (0, 0), (k, 2*k), red
vector: (-4, 1), 1, 2, blue
text: 0.5 * (-4 - 3), 0.5 * (1 + 3), "$\vec{a}$", top-left
text: 0.5 * k, k, "{k:.2f} \cdot $\vec{a}$", bottom-right, bbox
align: right
width: 50%
fontsize: 25
:::



Når vi ganger en vektor $\vec{a}$ med en skalar $k$, så får vi en ny vektor $k \cdot \vec{a}$ slik at lengden av den nye vektoren er $\abs{k}$ ganger lengden av den opprinnelige vektoren. I tillegg vil komponentene være multiplisert med skalarverdien $k$.

Du kan utforske nærmere i den interaktive figuren til høyre ved å se på hva som skjer når du endrer på verdien til $k$.



:::{clear}
:::


:::::::::::::::{summary} Skalarmultiplikasjon av vektorer
Hvis vi ganger en vektor $\vec{a}$ med en skalar $k$, så får vi en ny vektor $k \cdot \vec{a}$ ved å gange hver av koordinatene til vektoren med skalarverdien:

$$
\vec{a} = [a_x, a_y] \limplies k \cdot \vec{a} = [k \cdot a_x, k \cdot a_y]
$$


Lengden til en vektor $k \cdot \vec{a}$ er gitt ved

$$
\abs{k \cdot \vec{a}} = \abs{k} \cdot \abs{\vec{a}}
$$


:::::::::::::::


---


:::::::::::::::{example} Eksempel 3
En vektor er gitt ved $\vec{a} = [3, -2]$.

En annen vektor $\vec{b}$ er gitt ved

$$
\vec{b} = -2 \cdot \vec{a}
$$


Bestem $\vec{b}$ og $\len{b}$.


::::{solution}
---
dropdown: 0
---
Vektoren $\vec{b}$ vil være gitt ved

$$
\vec{b} = -2 \cdot \vec{a} = -2 \cdot [3, -2] = [(-2) \cdot 3, (-2) \cdot (-2)] = [-6, 4]
$$

Lengden av vektoren kan vi finne å bruke koordinatene direkte:

$$
\len{b} = \sqrt{(-6)^2 + 4^2} = \sqrt{36 + 16} = \sqrt{52} = 2\sqrt{13} 
$$

Eller vi kan regne ut lengden av $\vec{a}$ først og deretter gange med $\abs{-2}$:

$$
\len{a} = \sqrt{3^2 + (-2)^2} = \sqrt{9 + 4} = \sqrt{13}
$$

Dermed får vi

$$
\len{b} = \abs{-2} \cdot \len{a} = 2 \cdot \sqrt{13} = 2\sqrt{13}
$$

::::
:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 3
En vektor er gitt ved $\vec{a} = [-2, 4]$.

En annen vektor $\vec{b}$ er gitt ved

$$
\vec{b} = \dfrac{1}{2} \cdot \vec{a}
$$


Bestem $\vec{b}$ og $\len{b}$.


::::{solution}
Vi regner ut vektoren $\vec{b}$:

$$
\vec{b} = \dfrac{1}{2} \cdot \vec{a} = \dfrac{1}{2} \cdot [-2, 4] = \v{\dfrac{1}{2} \cdot (-2)}{\dfrac{1}{2} \cdot 4} = \v{-1}{2}
$$

Da blir lengden:

$$
\len{b} = \sqrt{(-1)^2 + 2^2} = \sqrt{1 + 4} = \sqrt{5}
$$
::::

:::::::::::::::



## Addisjon av vektorer

:::{plot}
align: right
width: 100%
xmin: -0.5
xmax: 3.5
ymin: -0.5
ymax: 3.5
vector: 0, 0, 1, 2, blue
vector: 1, 2, 2, 1, red
vector: 0, 0, 3, 3, purple
vline: 0, 0, 2, dashed, gray
hline: 2, 0, 1, dashed, gray
vline: 1, 2, 3, dashed, gray
hline: 3, 1, 3, dashed, gray
hline: 0, 0, 3, dashed, gray
vline: 3, 0, 3, dashed, gray
text: 0.5 * 1, 0.5 * 2, "$\vec{a}$", top-left
text: 1 + 0.5 * 2, 2 + 0.5 * 1, "$\vec{b}$", top-left
text: 0.5 * 3, 0.5 * 3, "$\vec{a} + \vec{b}$", bottom-right
text: 0, 1, "$a_y$", center-left
text: 0.5, 2, "$a_x$", top-center
text: 1, 2.5, "$b_y$", center-left
text: 2, 3, "$b_x$", top-center
text: 0.5 * 3, 0, "$a_x + b_x$", bottom-center
text: 3, 0.5 * 3, "$a_y + b_y$", center-right
axis: off
fontsize: 30
:::


Når vi tar to vektorer $\vec{a}$ og $\vec{b}$ og legger dem sammen, så får vi en ny vektor $\vec{a}~+~\vec{b}$. Den nye vektoren får vi ved å starte i startpunktet til $\vec{a}$, flytte oss langs $\vec{a}$, og deretter flytte oss langs $\vec{b}$ fra endepunktet til $\vec{a}$. Den nye vektoren går da fra startpunktet til $\vec{a}$ til endepunktet til $\vec{b}$.

Fra figuren til høyre kan vi se at koordinatene til den nye vektoren blir summen av koordinatene til de to opprinnelige vektorene. 


:::{clear}
:::

:::::::::::::::{summary} Addisjon av vektorer

La $\vec{a} = [a_x, a_y]$ og $\vec{b} = [b_x, b_y]$. Da får vi vektoren $\vec{a} + \vec{b}$ ved å legge sammen koordinatene hver for seg:

$$
\vec{a} + \vec{b} = [a_x, a_y] + [b_x, b_y] = [a_x + b_x, a_y + b_y]
$$

::::





:::::::::::::::


---


La oss se på et eksempel.

:::::::::::::::{example} Eksempel 4
To vektorer $\vec{a}$ og $\vec{b}$ er gitt ved


$$
\vec{a} = [-1, 2] \qog \vec{b} = [3, 4]
$$

Bestem $\vec{a} + \vec{b}$.


::::{solution}
---
dropdown: 0
---
Vi legger sammen vektorene ved å legge sammen koordinatene hver for seg:


$$
\begin{align*}
\vec{a} + \vec{b} &= [-1, 2] + [3, 4] \\
\\
&= [-1 + 3] + [2 + 4] \\
\\
&= [2, 6]
\end{align*}
$$


::::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 4
To vektorer er gitt ved

$$
\vec{a} = [2, -1] \qog \vec{b} = [-3, 5]
$$

Bestem $\vec{a} + \vec{b}$.


::::{answer}
$$
\vec{a} + \vec{b} = [-1, 4]
$$
::::

::::{solution}
Vi legger sammen vektorene:

$$
\begin{align*}
\vec{a} + \vec{b} &= [2, -1] + [-3, 5] \\
\\
&= [2 + (-3), -1 + 5] \\
\\
&= [-1, 4]
\end{align*}
$$

::::
:::::::::::::::



## Subtraksjon av vektorer
Vi kan også trekke fra en vektor fra en annen. Hvis vi ønsker å regne ut $\vec{b} - \vec{a}$, så kan vi forstå dette
som å legge sammen $\vec{b}$ med vektoren $(-1) \cdot \vec{a}$. 


:::::::::::::::{summary} Subtraksjon av vektorer
Gitt en vektor $\vec{a} = [a_x, a_y]$ og en vektor $\vec{b} = [b_x, b_y]$, så er

$$
\vec{b} - \vec{a} = [b_x, b_y] - [a_x, a_y] = [b_x - a_x, b_y - a_y] 
$$

:::::::::::::::


---


:::::::::::::::{example} Eksempel 5
To vektorer er gitt ved

$$
\vec{a} = [4, 2] \qog \vec{b} = [1, 5]
$$

Bestem $\vec{b} - \vec{a}$.


::::{solution}
---
dropdown: 0
---
$$
\begin{align*}
\vec{b} - \vec{a} &= [1, 5] - [4, 2] \\
\\
&= [1 - 4, 5 - 2] \\
\\
&= [-3, 3]
\end{align*}
$$
::::
:::::::::::::::


---



:::::::::::::::{exercise} Underveisoppgave 5
To vektorer er gitt ved

$$
\vec{a} = [5, -2] \qog \vec{b} = [3, 4]
$$

Bestem $\vec{b} - \vec{a}$ og $\vec{a} - \vec{b}$.


::::{answer}
$$
\vec{b} - \vec{a} = [-2, 6] \qog \vec{a} - \vec{b} = [2, -6]
$$
::::

::::{solution}
$$
\begin{align*}
\vec{b} - \vec{a} &= [3, 4] - [5, -2] = [3 - 5, 4 - (-2)] = [-2, 6] \\
\end{align*}
$$

Videre vil vektoren $\vec{a} - \vec{b}$ være motsatt av $\vec{b} - \vec{a}$, altså

$$
\vec{a} - \vec{b} = [2, -6]
$$

Vi kan se dette ved å regne ut det direkte også:

$$
\begin{align*}
\vec{a} - \vec{b} &= [5, -2] - [3, 4] = [5 - 3, -2 - 4] = [2, -6]
\end{align*}
$$

::::


:::::::::::::::




## Parallelle vektorer

Når vi sier at to vektorer $\vec{a}$ og $\vec{b}$ er **parallelle**, så mener vi at de peker i samme retning, eller i motsatt retning. 
Hvor lange de er spiller ingen rolle og hvor de starter spiller heller ingen rolle – bare retningen. 

Vi har allerede sett at når vi ganger en vektor $\vec{a}$ med en skalar $k$, så får vi en ny vektor som
enten peker i samme retning som $\vec{a}$ (hvis $k > 0$), eller i motsatt retning (hvis $k < 0$). Dermed er den nye vektoren $k \cdot \vec{a}$ alltid parallell med $\vec{a}$.

Hvis to vektorer $\vec{a}$ og $\vec{b}$ er parallelle, skriver vi $\vec{a} \parallel \vec{b}$.


:::::::::::::::{summary} Parallelle vektorer
Hvis to vektorer $\vec{a}$ og $\vec{b}$ er parallelle skriver vi $\vec{a} \parallel \vec{b}$. Da finnes det en skalar $k \neq 0$ slik at

$$
\vec{a} = k \cdot \vec{b}
$$

Hvis $\vec{a} = [a_x, a_y]$ og $\vec{b} = [b_x, b_y]$, så betyr dette at

$$
[a_x, a_y] = [k \cdot b_x, k \cdot b_y]
$$

for en skalar $k \neq 0$. 

Det betyr at hvis forholdstallet mellom de tilsvarende komponentene er like, så må vektorene være parallelle siden

$$
a_x = k\cdot b_x \and a_y = k \cdot b_y \liff k = \dfrac{a_x}{b_x} \and k = \frac{a_y}{b_y}
$$

:::::::::::::::



---


:::::::::::::::{example} Eksempel 6
To vektorer er gitt ved

$$
\vec{a} = [6, 9] \qog \vec{b} = [2, 3]
$$


Avgjør om $\vec{a} \parallel \vec{b}$.


::::{solution}
---
dropdown: 0
---
Hvis $\vec{a} \parallel \vec{b}$, så må det finnes en skalar $k$ slik at

$$
\vec{a} = k \cdot \vec{b}
$$

Da får vi likningen

$$
[6, 9] = k \cdot [2, 3] = [2k, 3k]
$$

Altså må

$$
2k = 6 \and 3k = 9
$$

Disse likningene gir

$$
k = \dfrac{6}{2} \and k = \dfrac{9}{3}
$$

$$
k = 3 \and k = 3
$$

Siden vi fikk én verdi for $k$ fra begge likningene, så betyr det at vektorene er parallelle. Da vet vi at

$$
\vec{a} = 3 \cdot \vec{b} \liff \vec{a} \parallel \vec{b}
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 6
To vektorer er gitt ved 

$$
\vec{a} = [4, -8] \qog \vec{b} = [-1, 2]
$$

Avgjør om $\vec{a} \parallel \vec{b}$.

::::{answer}
Ja, $\vec{a} \parallel \vec{b}$ siden $\vec{a} = -4 \cdot \vec{b}$
::::

::::{solution}
Vi sjekker om det finnes en skalar $k$ slik at

$$
\vec{a} = k \cdot \vec{b}
$$

Da får vi likningen

$$
[4, -8] = k \cdot [-1, 2] = [-k, 2k]
$$

Altså må

$$
-k = 4 \and 2k = -8
$$

Disse likningene gir

$$
k = -4 \and k = -4
$$

Siden vi fikk én verdi for $k$ fra begge likningene, så betyr det at vektorene er parallelle. 

:::::::::::::::



## Basisvektorer og dekomponering av vektorer
Når vi beskriver vektorer, så setter vi opp et koordinatsystem ved å bruke **basisvektorer**. Vi skal oftest jobbe med basisvektorer har lengde $1$ og står vinkelrett på hverandre. Dette kaller vi for **enhetsvektorer**. 
De mest vanlige enhetsvektorene vi jobber med er $\vec{e}_x$ som peker langs $x$-aksen og $\vec{e}_y$ som peker langs $y$-aksen.

:::::::::::::::{summary} Standardbasis

:::{plot}
width: 100%
align: right
vector: (0, 0), (1, 0), blue
vector: (0, 0), (0, 1), red
text: 0.5, 0, "$\vec{e}_x$", bottom-center
text: 0, 0.5, "$\vec{e}_y$", center-left
xmin: -1
xmax: 3
ymin: -1
ymax: 2.5
fontsize: 30
:::


Standardbasisen består av enhetsvektorene $\vec{e}_x$ og $\vec{e}_y$. 

Disse er vektorer med lengde $1$ som peker langs $x$-aksen og $y$-aksen gitt ved:

$$
\vec{e}_x = [1, 0] \qog \vec{e}_y = [0, 1]
$$



:::::::::::::::


En vektor kan alltid dekomponeres langs to andre vektorer som ikke er parallelle. Dette betyr i praksis at vi skifter koordinatsystemet vårt til å bruke to nye vektorer som basisvektorer. 



:::::::::::::::{summary} Dekomponering av vektorer

:::{plot}
width: 100%
align: right
vector: (0, 0), (4, 2), blue
vector: (0, 0), (1, 2), red
vector: (1, 2), (2, 4), red
vector: (2, 4), (3, 3), red
vector: (3, 3), (4, 2), red
xmin: -1
xmax: 5
ymax: 5
ymin: -1
fontsize: 30
:::



Gitt to ikke-parallelle vektorer $\vec{u}$ og $\vec{v}$, kan vi alltid skrive en vektor $\vec{a}$ som

$$
\vec{a} = s \cdot \vec{u} + t \cdot \vec{v}
$$

der $s$ og $t$ er skalarer. 

:::::::::::::::



---


:::::::::::::::{example} Eksempel 7
To vektorer $\vec{u}$ og $\vec{v}$ er gitt ved

$$
\vec{u} = [1, 2] \qog \vec{v} = [-1, 1]
$$

En annen vektor $\vec{a}$ er gitt ved

$$
\vec{a} = [4, 2]
$$

Bestem $s$ og $t$ slik at

$$
\vec{a} = s\cdot \vec{u} + t \cdot \vec{v}
$$


:::::{solution}
---
dropdown: 0
---

:::{plot}
width: 100%
align: right
vector: (0, 0), (4, 2), blue
text: 0.5 * (0 + 4), 0.5 * (0 + 2), "$\vec{a}$", bottom-right
vector: (0, 0), (1, 2), red
text: 0.5 * (1 + 0), 0.5 * (2 + 0), "$\vec{u}$", top-left
vector: (0, 0), (-1, 1), purple
text: -1, 1, "$\vec{v}$", top-left
xmin: -2
xmax: 5
ymax: 3
ymin: -1
fontsize: 30
:::


Hvis vi tegner de tre vektorene i et koordinatsystem der alle starter i origo $O$, får vi figuren til høyre.


Å bestemme tallene $s$ og $t$ slik at 

$$
\vec{a} = s \cdot \vec{u} + t \cdot \vec{v}
$$


handler da å bestemme hvor mange enheter av $\vec{u}$ og $\vec{v}$ som vi må sette sammen for å få vektoren $\vec{a}~,$ som vist i figuren til høyre.


:::{plot}
width: 100%
align: right
vector: (0, 0), (4, 2), blue
text: 0.5 * (0 + 4), 0.5 * (0 + 2), "$\vec{a}$", bottom-right
vector: (0, 0), (2, 4), red
text: 0.5 * (0 + 2), 0.5 * (0 + 4), "$s \cdot \vec{u}$", top-left
vector: (2, 4), (4, 2), purple
text: 0.5 * (2 + 4), 0.5 * (4 + 2), "$t \cdot \vec{v}$", top-right
xmin: -1
xmax: 5
ymax: 5
ymin: -1
fontsize: 30
ticks: off
:::


For å løse dette, setter vi opp vektorlikningen uttrykt med koordinatene: 

$$
[4, 2] = s \cdot [1, 2] + t \cdot [-1, 1] \\
\\
[4, 2] = [s, 2s] + [-t, t] \\
\\
[4, 2] = [s - t, 2s + t]
$$

Her må $x$-kompontene og $y$-komponentene være like, så vi får likningssystemet:

$$
\begin{align*}
4 &= s - t \\
\\
2 &= 2s + t
\end{align*}
$$

Tar vi den første likningen og løser for $s$, får vi:

$$
s = 4 + t
$$

Deretter setter vi dette inn i den andre likningen for $s$:

$$
2 = 2(4 + t) + t \\
\\
2 = 8 + 2t + t \\
\\
2 = 8 + 3t \\
\\
3t = 2 - 8 \\
\\
3t = -6 \\
\\
t = -2
$$

Altså har vi funnet at $t = -2$. Setter vi dette inn i likningen for $s$, får vi:

$$
s = 4 + (-2) = 2
$$


$$
s = 2 \and t = -2
$$

som betyr at

$$
\vec{a} = 2 \cdot \vec{u} - 2 \cdot \vec{v}
$$

Grafisk betyr dette resultatet at hvis vi setter sammen $2$ enheter av $\vec{u}$ og $2$ enheter av $-\vec{v}$ i en kjede, så vil vi ende opp i endepunktet til $\vec{a}$ når vi starter kjeden i samme sted som $\vec{a}$ starter. De typiske to framstillingene blir da som vist i de to figurene nedenfor.



::::{multi-plot2}
---
rows: 1
cols: 2
xmin: -1
xmax: 5
ymax: 5
ymin: -4
fontsize: 30
---
:::{plot}
width: 100%
align: right
vector: (0, 0), (4, 2), blue
text: 0.5 * (0 + 4), 0.5 * (0 + 2), "$\vec{a}$", bottom-right
vector: (0, 0), (1, 2), red
vector: (1, 2), (2, 4), red
text: 0.5 * (0 + 2), 0.5 * (0 + 4), "$2 \cdot \vec{u}$", top-left
vector: (2, 4), (3, 3), purple
vector: (3, 3), (4, 2), purple
text: 0.5 * (2 + 4), 0.5 * (4 + 2), "$-2 \cdot \vec{v}$", top-right
xmin: -1
xmax: 5
ymax: 5
ymin: -1
fontsize: 30
:::


:::{plot}
width: 100%
align: right
vector: (0, 0), (4, 2), blue
text: 0.5 * (0 + 4), 0.5 * (0 + 2), "$\vec{a}$", top-left
vector: (0, 0), (1, -1), purple
vector: (1, -1), (2, -2), purple
text: 0.5 * (0 + 2), 0.5 * (0 + -2) - 0.5, "$-2 \cdot \vec{v}$", bottom-center
vector: (2, -2), (3, 0), red
vector: (3, 0), (4, 2), red
text: 0.5 * (2 + 4), 0.5 * (-2 + 1) - 0.5, "$2 \cdot \vec{u}$", bottom-center
ymax: 4
:::
::::



:::{plot}
width: 100%
align: right
vector: (0, 0), (1, 2), red
text: 0.5 * (0 + 1), 0.5 * (0 + 2), "$\vec{u}$", top-left
vector: (1, 2), (1 + 1, 2 - 1), purple
text: 1 + 0.5 * 1, 2 + 0.5 * -1, "$-\vec{v}$", top-center
vector: (1 + 1, 2 - 1), (1 + 1 + 1, 2 - 1 + 2), red
text: 1 + 1 + 0.5 * 1, 2 - 1 + 0.5 * 2, "$\vec{u}$", top-left
vector: (1 + 1 + 1, 2 - 1 + 2), (1 + 1 + 1 + 1, 2 - 1 + 2 - 1), purple
text: 1 + 1 + 1 + 0.5 * 1, 2 - 1 + 2 - 0.5 * 1, "$-\vec{v}$", top-center
vector: (0, 0), (4, 2), blue
text: 0.5 * (0 + 4), 0.5 * (0 + 2), "$\vec{a}$", bottom-right
xmin: -1
xmax: 5
ymax: 5
ymin: -1
fontsize: 30
:::


Vi tar en liten *risiko* og drar dette litt lenger for å illustrere at rekkefølgen på addisjonen av vektorene er uviktig. Det er nemlig ingenting som stopper oss fra å følge $\vec{u}$ og $-\vec{v}$ annenhver gang to ganger, som vist i figuren til høyre, siden:

$$
\begin{align*}
\vec{a} &= 2\vec{u} - 2\vec{v} \\
\\
&= \vec{u} - \vec{v} + \vec{u} - \vec{v}
\end{align*}
$$


:::{plot}
width: 100%
align: right
xmin: -1
xmax: 5
ymax: 5
ymin: -1
fontsize: 30
vector: (0, 0), (4, 2), blue
text: 0.5 * (2 + 4), 0.5 * (1 + 2), "$\vec{a}$", top-center
vector: (0, 0), (1, 2), red
vector: (1, 2), (2, 1), purple
text: 0.5 * (1 + 2), 0.5 * (2 + 1), "$-\vec{v}$", top-center
vector: (2, 1), (3, 0), purple
vector: (3, 0), (4, 2), red
text: 0.5 * (3 + 4), 0.5 * (0 + 2), "$\vec{u}$", bottom-right
:::

Hvorfor stoppe der? Vi kan vel av fri vilje velge å følge $\vec{u}$ etterfulgt av $-\vec{v}$ to ganger for deretter å følge $\vec{u}$ én siste gang siden:


$$
\begin{align*}
\vec{a} &= 2\vec{u} - 2\vec{v} \\
\\
&= \vec{u} - 2\vec{v} + \vec{u}
\end{align*}
$$


Du skjønner kanskje greia, vi får samme endepunkt uansett hvordan vi velger å sette vektorene etter hverandre. 


:::::



:::::::::::::::


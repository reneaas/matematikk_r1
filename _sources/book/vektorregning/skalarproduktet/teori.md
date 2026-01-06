# Skalarproduktet


:::{admonition} Læringsmål
---
class: tip
---
* Kunne regne ut skalarproduktet på komponentform og ved hjelp av geometriske egenskaper.
* Kunne beskrive sammenhengen mellom skalarproduktet og lengden av en vektor.
* Kunne bruke skalarproduktet til å bestemme vinkelen mellom to vektorer.
* Kunne bruke digitale verktøy til å regne med vektorer.
:::



## Definisjon

**Skalarproduktet** er én av mange måter vi kunne definert det å gange to vektorer med hverandre på. Det er ikke den eneste måten å gange sammen vektorer på, men denne definisjonen er spesielt nyttig fordi den gir samme svar uansett hvilket koordinatsystem vi bruker for å beskrive vektorene. Et tall som blir likt uansett hvilket koordinatsystem vi bruker, kaller vi for en **skalar**. Du har allerede møtt en skalar tidligere, som er lengden til en vektor.

Vi skal først se på definisjonen, før vi senere skal se hva det betyr geometrisk og hva det kan brukes til.



:::::::::::::::{summary} Skalarproduktet
For en vektor $\vec{a} = [a_x, a_y]$ og en vektor $\vec{b} = [b_x, b_y]$, er skalarproduktet mellom vektorene definert som

$$
\vec{a} \cdot \vec{b} = a_x\cdot b_x + a_y\cdot b_y
$$


Vi ganger altså $x$-komponentene og $y$-komponentene sammen, og legger sammen svarene.

:::::::::::::::


---

:::::::::::::::{example} Eksempel 1
La $\vec{a} = [2, 3]$ og $\vec{b} = [-4, 5]$. 

Bestem skalarproduktet $\vec{a} \cdot \vec{b}$.


::::{solution}
---
dropdown: 0
---

$$
\vec{a} \cdot \vec{b} = [2, 3] \cdot [-4, 5] = 2 \cdot (-4) + 3 \cdot 5 = -8 + 15 = 7
$$
::::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 1
Bestem skalarproduktet mellom vektorene

$$
\vec{a} = [-1, 3] \qog \vec{b} = [2, 1]
$$


::::{answer}
$$
\vec{a} \cdot \vec{b} = 1
$$
::::


::::{solution}
$$
\vec{a} \cdot \vec{b} = [-1, 3] \cdot [2, 1] = -1 \cdot 2 + 3 \cdot 1 = -2 + 3 = 1
$$
::::

:::::::::::::::


---



## Sammenheng mellom skalarprodukt og lengde

Det er en klar sammenheng mellom skalarproduktet av en vektor med seg selv og lengden av vektoren.



:::::::::::::::{summary} Skalarprodukt og lengde
For en vektor $\vec{a} = [a_x, a_y]$, så vil lengden $|\vec{a}|$ være gitt ved

$$
|\vec{a}| = \sqrt{\vec{a} \cdot \vec{a}}
$$


::::{admonition} Bevis
---
class: theory, dropdown
---
Vi regner ut lengden av vektoren ved hjelp av Pytagoras' setning:

$$
|\vec{a}| = \sqrt{a_x^2 + a_y^2}
$$

Bruker vi skalarproduktet, får vi:

$$
\vec{a} \cdot \vec{a} = [a_x, a_y] \cdot [a_x, a_y] = a_x \cdot a_x + a_y \cdot a_y = a_x^2 + a_y^2
$$

Tar vi kvadratroten av dette, får vi samme uttrykk som lengden til vektoren. Dermed har vi vist at

$$
|\vec{a}| = \sqrt{\vec{a} \cdot \vec{a}}
$$


::::


:::::::::::::::


---


:::::::::::::::{example} Eksempel 2
Bestem lengden av vektoren $\vec{a} = [3, 4]$ ved hjelp av skalarproduktet.

::::{solution}
---
dropdown: 0
---
Vi regner ut skalarproduktet først:

$$
\vec{a} \cdot \vec{a} = [3, 4] \cdot [3, 4] = 3 \cdot 3 + 4 \cdot 4 = 9 + 16 = 25
$$

Så tar vi kvadratroten for å finne lengden:

$$
|\vec{a}| = \sqrt{\vec{a} \cdot \vec{a}} = \sqrt{25} = 5
$$
::::
:::::::::::::::


---



:::::::::::::::{exercise} Underveisoppgave 2
Bruk skalarproduktet til å bestemme lengden av 

$$
\vec{b} = [-2, 1]
$$


::::{answer}
$$
\len{b} = \sqrt{5}
$$
::::


::::{solution}
Skalarproduktet er gitt ved

$$
\dot{b}{b} = [-2, 1] \cdot [-2, 1] = (-2) \cdot (-2) + 1 \cdot 1 = 4 + 1 = 5
$$

Så tar vi kvadratroten for å finne lengden:

$$
\len{b} = \sqrt{5}
$$

::::


:::::::::::::::





## Geometrisk formel for skalarproduktet

Det er ikke opplagt hva skalarproduktet egentlig betyr for noe. Så langt har vi bare definert hva vi mener med å gange to vektorer med hverandre. Nå skal vi se at det har en klar geometrisk betydning som vi skal utnytte videre.


:::::::::::::::{summary} Geometrisk formel for skalarproduktet


:::{plot}
figsize: (3, 3)
align: right
width: 100%
axis: off
vector: 0, 0, 1.5, 0, red
vector: 0, 0, 1, 1, blue
angle-arc: (0, 0), 0.3, 0, 45
xmin: -0.2
ymin: -0.5 
ymax: 1.3
xmax: 1.7
text: 0.45 * cos(pi/4), 0.1 * sin(pi/4), "$\varphi$", top-right
text: 0.75, 0, "$\vec{a}$", bottom-center
text: 0.5, 0.5, "$\vec{b}$", top-left
fontsize: 18
:::


For to vektorer $\vec{a}$ og $\vec{b}$ med en vinkel $\varphi$ mellom seg, er skalarproduktet gitt ved

$$
\dot{a}{b} = \len{a} \cdot \len{b} \cdot \cos \varphi
$$


Vi kan tolke dette som at vi plukker ut den delen av vektoren $\vec{b}$ som peker i samme retning som vektoren $\vec{a}$, og ganger denne med lengden av vektoren $\vec{a}$.


:::{clear}
:::


:::::{admonition} Bevis
---
class: theory, dropdown
---
Skalarproduktet skal gi en skalar, som betyr at svaret vi får ikke er avhengig av koordinatsystemet vi bruker for å beskrive vektorene. Vi kan derfor velge et koordinatssystem som gjør regningen enklest mulig. 


:::{plot}
figsize: (3, 3)
align: right
width: 100%
axis: off
vector: 0, 0, 1, 1, blue
vector: 0, 0, 1, 0, red
vector: 1, 0, 0, 1, red
angle-arc: (0, 0), 0.3, 0, 45
xmin: -0.2
ymin: -0.5 
ymax: 1.3
xmax: 1.7
text: 0.45 * cos(pi/4), 0.1 * sin(pi/4), "$\varphi$", top-right
text: 0.5, 0, "$b_x$", bottom-center
text: 1, 0.5, "$b_y$", center-right
text: 0.5, 0.5, "$\vec{b}$", top-left
fontsize: 18
polygon: (1, 0), (0.9, 0), (0.9, 0.1), (1, 0.1)
:::

Hvis vi velger koordinatsystemet slik at $\vec{a}$ ligger langs $x$-aksen, får vi at

$$
\vec{a} = \v{\len{a}}{0}
$$

For å beskrive $\vec{b} = \v{b_x}{b_y}$ i det samme koordinatsystemet, kan vi bruke definisjonen av sinus og cosinus:


$$
\cos \varphi = \dfrac{b_x}{\len{b}} \qog \sin \varphi = \dfrac{b_y}{\len{b}}
$$

Løser vi disse likningene for $b_x$ og $b_y$, får vi:

$$
b_x = \len{b} \cdot \cos \varphi \qog b_y = \len{b} \cdot \sin \varphi
$$

Dermed kan vi skrive vektoren $\vec{b}$ som

$$
\vec{b} = \v{\len{b} \cdot \cos \varphi}{\len{b} \cdot \sin \varphi}
$$


Hvis vi nå regner ut skalarproduktet mellom $\vec{a}$ og $\vec{b}$, får vi:

$$
\begin{align*}
\dot{a}{b} &= \v{\len{a}}{0} \cdot \v{\len{b} \cdot \cos \varphi}{\len{b} \cdot \sin \varphi} \\
\\
&= \len{a} \cdot \len{b} \cdot \cos \varphi + 0 \cdot \len{b} \cdot \sin \varphi \\
\\
&= \len{a} \cdot \len{b} \cdot \cos \varphi
\end{align*}
$$

som var det vi skulle vise. 

:::::





:::::::::::::::


---


:::::::::::::::{example} Eksempel 3
Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $\len{a} = 4$
* $\len{b} = 3$
* Vinkelen mellom de to vektorene er $60\degree$. 


Bestem $\dot{a}{b}$.


::::{solution}
---
dropdown: 0
---
Vi bruker den geometriske formelen for skalarproduktet

$$
\dot{a}{b} = \len{a} \cdot \len{b} \cdot \cos \varphi
$$

der 

$$
\len{a} = 4 \and \len{b} = 3 \and \varphi = 60\degree
$$

Vi minner om at $\cos 60\degree = \dfrac{1}{2}$. Vi får da:

$$
\dot{a}{b} = \len{a} \cdot \len{b} \cdot \cos \varphi = 4 \cdot 3 \cdot \dfrac{1}{2} = 12 \cdot \dfrac{1}{2} = 6
$$
::::


:::::::::::::::


---

Før vi går videre minner vi om noen kjente vinkler og deres cosinusverdier:

| $\varphi$ | $0\degree$ | $30\degree$ | $45\degree$ | $60\degree$ | $90\degree$ | $120\degree$ | $135\degree$ | $150\degree$ | $180\degree$ | 
|:-----------:|:------------:|:-------------:|:-------------:|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|:--------------:|
| $\cos \varphi$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-\dfrac{1}{2}$ | $-\dfrac{\sqrt{2}}{2}$ | $-\dfrac{\sqrt{3}}{2}$ | $-1$ |


:::::::::::::::{exercise} Underveisoppgave 3
Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $\len{a} = 5$
* $\dot{a}{b} = 10\sqrt{3}$
* Vinkelen mellom de to vektorene er $30\degree$.


Bestem $\len{b}$.


::::{answer}
$$
\len{b} = 4
$$
::::


::::{solution}
Vi bruker den geometriske formelen for skalarproduktet

$$
\dot{a}{b} = \len{a} \cdot \len{b} \cdot \cos \varphi
$$

der vi vet at

$$
\dot{a}{b} = 10\sqrt{3} \and \len{a} = 5 \and \varphi = 30\degree \implies \cos \varphi = \dfrac{\sqrt{3}}{2}
$$

Så setter vi inn og løser likningen for $\len{b}$:

$$
10 \sqrt{3} = 5 \cdot \len{b} \cdot \dfrac{\sqrt{3}}{2}
$$

Vi kan dele med $\sqrt{3}$ og gange med $2$ på hver side som gir:

$$
20 = 5 \len{b} \liff \len{b} = \dfrac{20}{5} = 4
$$

Altså er $\len{b} = 4$.
::::


:::::::::::::::

## Generelle regneregler for skalarproduktet

:::::::::::::::{summary} Regneregler for skalarproduktet
La $\vec{a}$, $\vec{b}$ og $\vec{c}$ være vektorer, og la $k$ være en skalar. Da gjelder følgende regneregler for skalarproduktet:

1. $\dot{a}{b} = \dot{b}{a}$
2. $(\vec{a} + \vec{b}) \cdot \vec{c} = \vec{a} \cdot \vec{c} + \vec{b} \cdot \vec{c}$
3. $(k \vec{a}) \cdot \vec{b} = k (\vec{a} \cdot \vec{b})$
4. $\vec{a} \cdot \vec{a} = \len{a}^2 = \vec{a}^2$
5. $(\vec{a} + \vec{b}) \cdot (\vec{c} + \vec{d}) = \vec{a} \cdot \vec{c} + \vec{a} \cdot \vec{d} + \vec{b} \cdot \vec{c} + \vec{b} \cdot \vec{d}$


:::::::::::::::


La oss ta et eksempel. 


:::::::::::::::{example} Eksempel 4
Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $\len{a} = 3$ og $\len{b} = 4$
* $\dot{a}{b} = 3$

To andre vektorer $\vec{p}$ og $\vec{q}$ er gitt ved

$$
\vec{p} = 2\vec{a} + \vec{b} \qog \vec{q} = \vec{a} - 3\vec{b}
$$

Bestem $\dot{p}{q}$.


::::{solution}
---
dropdown: 0
---
Vi regner ut ved å bruke regnereglene for skalarproduktet:

$$
\begin{align*}
\vec{p} \cdot \vec{q} &= (2 \vec{a} + \vec{b}) \cdot (\vec{a} - 3 \vec{b}) \\
\\
&= (2 \vec{a}) \cdot \vec{a} + (2 \vec{a}) \cdot (-3 \vec{b}) + \vec{b} \cdot \vec{a} + \vec{b} \cdot (-3 \vec{b}) \\
\\
&= 2 \len{a}^2 - 6 \dot{a}{b} + \dot{b}{a} - 3 \len{b}^2 \\
\\
&= 2 \len{a}^2 - 6 \dot{a}{b} + \dot{a}{b} - 3 \len{b}^2 \\
\\
&= 2 \len{a}^2  - 5 \dot{a}{b} - 3 \len{b}^2 \\
\\
&= 2 \cdot 3^2 - 5 \cdot 3 - 3 \cdot 4^2 \\
\\
&= 18 - 15 - 48 \\
\\
&= -45
\end{align*}
$$

::::

:::::::::::::::


---



:::::::::::::::{exercise} Underveisoppgave 4
Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $\len{a} = 2$ og $\len{b} = 1$
* $\dot{a}{b} = 1$

To vektorer $\vec{p}$ og $\vec{q}$ er gitt ved

$$
\vec{p} = 3\vec{a} - 2\vec{b} \qog \vec{q} = -\vec{a} + 4\vec{b}
$$

Bestem $\dot{p}{q}$.


::::{answer}
$$
\dot{p}{q} = -6
$$
::::


::::{solution}
Vi regner ut ved å bruke regnereglene for skalarproduktet:


$$
\begin{align*}
\dot{p}{q} &= (3 \vec{a} - 2 \vec{b}) \cdot (-\vec{a} + 4 \vec{b}) \\
\\
&= (3 \vec{a}) \cdot (-\vec{a}) + (3 \vec{a}) \cdot (4 \vec{b}) + (-2 \vec{b}) \cdot (-\vec{a}) + (-2 \vec{b}) \cdot (4 \vec{b}) \\
\\
&= -3 \len{a}^2 + 12 \dot{a}{b} + 2 \dot{b}{a} - 8 \len{b}^2 \\
\\
&= -3 \len{a}^2 + 12 \dot{a}{b} + 2 \dot{a}{b} - 8 \len{b}^2 \\
\\
&= -3 \len{a}^2 + 14 \dot{a}{b} - 8 \len{b}^2 \\
\\
&= -3 \cdot 2^2 + 14 \cdot 1 - 8 \cdot 1^2 \\
\\
&= -12 + 14 - 8 \\
\\
&= -6
\end{align*}
$$

::::

:::::::::::::::




## Vinkler mellom vektorer

Vi har så langt tatt for gitt hva det vil si at to vektorer har en vinkel mellom seg. Siden $\cos \varphi$ inngår i den geometriske formelen for skalarproduktet, vil skalarproduktet fortelle oss noe om vinkelen mellom to vektorer. Vi skal nå presisere hva vi mener med vinkelen mellom to vektorer.


:::::::::::::::{summary} Vinkelen mellom to vektorer
La $\vec{a}$ og $\vec{b}$ være to vektorer med en vinkel $\varphi$ mellom seg. Da vil $\varphi$ være den *minste* vinkelen vi kan tegne mellom retningene til de to vektorene:


::::{multi-plot2}
---
rows: 1
cols: 2
---

:::{plot}
figsize: (5, 4)
width: 100%
vector: 0, 0, 1, 0, blue
vector: 0, 0, -0.8, 1, red
angle-arc: (0, 0), 0.3, 0, 128.66
text: 0.35 * cos(64.33 * pi/180), 0.35 * sin(64.33 * pi/180), "$\varphi$", top-right
xmin: -1.5
xmax: 1.5
ymin: -0.5
ymax: 1.5
fontsize: 25
ticks: off
axis: off
text: 0, 1, "Riktig vinkelmål", top-center
text: 0.5, 0, "$\vec{a}$", bottom-center
text: -0.4, 0.5, "$\vec{b}$", bottom-left
:::


:::{plot}
figsize: (5, 4)
width: 100%
vector: 0, 0, 1, 0, blue
vector: 0, 0, -0.8, 1, red
angle-arc: (0, 0), 0.2, 0, -(360 - 128.66)
text: -0.25 * cos(64.33 * pi/180), -0.25 * sin(64.33 * pi/180), "$\varphi$", bottom-left
xmin: -1.5
xmax: 1.5
ymin: -0.5
ymax: 1.5
fontsize: 25
ticks: off
axis: off
text: 0, 1, "Feil vinkelmål", top-center
text: 0.5, 0, "$\vec{a}$", bottom-center
text: -0.4, 0.5, "$\vec{b}$", bottom-left
:::

Vinkelen $\varphi$ vil altså alltid være $\varphi \in [0\degree, 180\degree]$.

::::



:::::::::::::::


---

Fra den geometriske formelen for skalarproduktet så vil fortegnet til skalarproduktet fortelle oss noe om hvilken retning vektorene peker i forhold til hverandre. Vi kan også i utgangspunktet regne ut vinkelen, men det skal vi spare til vi jobber med digitale verktøy nedenfor. For nå, kan vi få oversikt over hva fortegnet til skalarproduktet forteller oss om vinkelen mellom to vektorer:



:::::::::::::::{summary} Fortegn på skalarproduktet
La $\vec{a}$ og $\vec{b}$ være to vektorer med en vinkel $\varphi$ mellom seg. Regner vi ut skalarproduktet med den geometriske formelen

$$
\vec{a} \cdot \vec{b} = \len{a} \cdot \len{b} \cdot \cos \varphi
$$

får vi følgende fortegn som er bestemt av vinkelen mellom vektorene:



:::::{grid} 1 1 2 3
---
gutter: 2
---

::::{grid-item-card}
$$
\begin{align*}
\vec{a} \cdot \vec{b} &> 0 \\
\\
\varphi &\in [0^\circ, 90^\circ \rangle
\end{align*}
$$
^^^
:::{plot}
figsize: (3, 2)
vector: 0, 0, 1, 0, blue
vector: 0, 0, cos(pi/3), sin(pi/3), red
angle-arc: (0, 0), 0.3, 0, 60
text: 0.25, 0.15, "$\varphi$", top-right
xmin: -0.1
xmax: 1.2
ymin: -0.2
ymax: 0.9
ticks: off
axis: off
text: 0.5, 0, "$\vec{a}$", bottom-center
text: 0.2, 0.4, "$\vec{b}$", top-left
fontsize: 30
:::
::::

::::{grid-item-card}
$$
\begin{align*}
\vec{a} \cdot \vec{b} &= 0 \\
\\
\varphi &= 90^\circ
\end{align*}
$$
^^^

:::{plot}
figsize: (3, 3)
vector: 0, 0, 1, 0, blue
vector: 0, 0, 0, 1, red
polygon: (0, 0), (0.2, 0), (0.2, 0.2), (0, 0.2)
text: 0.4 * cos(pi/4), 0.4 * sin(pi/4), "$\varphi$", center-center
xmin: -0.2
xmax: 1.2
ymin: -0.2
ymax: 1.2
ticks: off
axis: off
text: 0.5, 0, "$\vec{a}$", bottom-center
text: -0.05, 0.5, "$\vec{b}$", center-left
fontsize: 30
:::
::::

::::{grid-item-card}
$$
\begin{align*}
\vec{a} \cdot \vec{b} &< 0 \\
\\
\varphi &\in \langle 90^\circ, 180^\circ]
\end{align*}
$$
^^^
:::{plot}
figsize: (3, 2)
vector: 0, 0, 1, 0, blue
vector: 0, 0, -0.8, 1, red
angle-arc: (0, 0), 0.3, 0, 128.66
text: 0.35 * cos(64.33 * pi/180), 0.35 * sin(64.33 * pi/180), "$\varphi$", top-right
xmin: -1.1
xmax: 1.1
ymin: -0.2
ymax: 1.2
ticks: off
axis: off
text: 0.5, 0, "$\vec{a}$", bottom-center
text: -0.45, 0.5, "$\vec{b}$", bottom-left
fontsize: 30
:::

::::

:::::



| $\varphi$ | $\cos \varphi$ | $\vec{a} \cdot \vec{b}$ |
|:-----------:|:------------:|:-------------:|
| $0\degree \leq \varphi < 90\degree$ (spiss vinkel) | $\cos \varphi > 0$ (Positiv) | Positiv |
| $\varphi = 90\degree$ (rett vinkel) | $\cos\varphi = 0$  | $0$ |
| $90\degree < \varphi \leq 180\degree$ (stump vinkel) | $\cos \varphi < 0$ (Negativ) | Negativ |  


Vi forutsetter at ingen av vektorene er nullvektoren, altså at $\len{a} > 0$ og $\len{b} > 0$.


:::::::::::::::



---


:::::::::::::::{example} Eksempel 5
En vektor $\vec{a} = [1, 2]$ og en annen vektor $\vec{b} = [-2, 1]$.

Bestem om vinkelen mellom vektorene er spiss, rett eller stump.


::::{solution}
---
dropdown: 0
---
Vi regner ut skalarproduktet mellom vektorene og sjekker fortegnet:

$$
\dot{a}{b} = [1, 2] \cdot [-2, 1] = 1 \cdot (-2) + 2 \cdot 1 = -2 + 2 = 0
$$

Siden skalarproduktet er lik $0$, så er vinkelen $\varphi = 90\degree$, er det en *rett* vinkel mellom vektorene.
::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 5
Nedenfor vises tre vektorer

$$
\vec{a} = [1, -3] \qog \vec{b} = [4, 2] \qog \vec{c} = [-2, 6]
$$

Bestem om vinklene mellom parvise vektorer er spisse, rette eller stumpe.


::::{answer}
* Stumpe vinkler mellom $\vec{a}$ og $\vec{b}$, og mellom $\vec{a}$ og $\vec{c}$.
* Spiss vinkel mellom $\vec{b}$ og $\vec{c}$.
::::


::::{solution}
Vi regner ut skalarproduktet mellom vektorene parvis og sjekker fortegnet:


$$
\vec{a} \cdot \vec{b} = [1, -3] \cdot [4, 2] = 1 \cdot 4 + (-3) \cdot 2 = 4 - 6 = -2 \liff \text{Stump vinkel}
$$


$$
\vec{a} \cdot \vec{c} = [1, -3] \cdot [-2, 6] = 1 \cdot (-2) + (-3) \cdot 6 = -2 - 18 = -20 \liff \text{Stump vinkel}
$$

$$
\vec{b} \cdot \vec{c} = [4, 2] \cdot [-2, 6] = 4 \cdot (-2) + 2 \cdot 6 = -8 + 12 = 4 \liff \text{Spiss vinkel}
$$


::::

:::::::::::::::


### Ortogonale vektorer


Når vi skal anvende skalarproduktet, så vil vi ofte gå veien om å kreve at to vektorer er **ortogonale**. Dette betyr at vektorene står vinkelrett på hverandre, altså at vinkelen mellom dem er $90^\circ$. Da skriver vi at $\vec{a} \perp \vec{b}$. Vi har allerede vært innom dette, men vi skal formelt knytte dette sammen med skalarproduktet.


:::::::::::::::{summary} Setning: Ortogonale vektorer og skalarproduktet
To vektorer $\vec{a}$ og $\vec{b}$ er **ortogonale** hvis og bare hvis skalarproduktet mellom dem er null:

$$
\vec{a} \cdot \vec{b} = 0 \liff \vec{a} \perp \vec{b}
$$



::::{admonition} Bevis
---
class: theory, dropdown
---
Den geometriske formelen for skalarproduktet sier at

$$
\dot{a}{b} = \len{a} \cdot \len{b} \cdot \cos \varphi
$$

Hvis skalarproduktet skal bli $0$, så må enten

$$
\len{a} = 0 \or \len{b} = 0 \or \cos \varphi = 0
$$

Siden vi forutsetter her at vektorene ikke er nullvektorer, så må det bety at det er $\cos \varphi = 0$. Dette skjer bare når $\varphi = 90^\circ$, altså når vektorene er ortogonale. Dermed har vi vist setningen. 

::::



:::::::::::::::


---


:::::::::::::::{example} Eksempel 6
To vektorer er gitt ved 

$$
\vec{a} = [1, 2] \qog \vec{b} = [-2, 1]
$$

Vis at $\vec{a} \perp \vec{b}$ (de er ortogonale). 



::::{solution}
---
dropdown: 0
---
Vi regner ut skalarproduktet mellom vektorene og sjekker om svaret blir $0$:

$$
\dot{a}{b} = [1, 2] \cdot [-2, 1] = 1 \cdot (-2) + 2 \cdot 1 = -2 + 2 = 0
$$

Altså har vi 

$$
\dot{a}{b} = 0 \liff \vec{a} \perp \vec{b}
$$

Altså er vektorene ortogonale.

::::


:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 6
Nedenfor vises tre vektorer.

$$
\vec{a} = [-1, 3] \qog \vec{b} = [6, 2] \qog \vec{c} = [1, -3]
$$

Bestem hvilke av vektorene som er ortogonale (parvis!).


::::{answer}
$$
\vec{a} \perp \vec{b} \and \vec{b} \perp \vec{c}
$$
::::

:::::::::::::::


---



## Skalarproduktet med digitale verktøy

Vi skal utvide verktøykassen vår slik at vi kan regne med skalarproduktet ved hjelp av CAS. Vi skal både se på hvordan vi kan regne ut skalarproduktet mellom to vektorer, og hvordan vi kan bestemme vinkelen mellom to vektorer ved hjelp av skalarproduktet i CAS.


:::::::::::::::{explore} Utforsk 1
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


I gif-en nedenfor viser vi hvordan vi kan regne ut skalarproduktet mellom vektorene

$$
\vec{a} = [2, 3] \qog \vec{b} = [-1, 18]
$$

Bruk CAS-vinduet og regn ut skalarproduktet som vist nedenfor. 

:::{figure} ./gifer/skalarproduktet.webp
---
class: no-click, adaptive-figure
width: 60%
---
:::



:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::


I gif-en nedenfor viser vi hvordan vi kan bruke skalarproduktet til å regne ut vinkelen mellom to vektorer gitt ved

$$
\vec{a} = [3, 4] \qog \vec{b} = [1, 5]
$$

Da bruker vi den geometriske formelen for skalarproduktet og løser den for vinkelen. 


Bruk CAS-vinduet til å bestemme vinkelen mellom vektorene som vist nedenfor.


:::{figure} ./gifer/skalarproduktet_vinkel.webp
---
class: no-click, adaptive-figure
width: 60%
---
:::


:::::::::::::
::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 7
:::{cas-popup}
---
layout: sidebar
---
:::

To vektorer er gitt ved

$$
\vec{a} = [-2, 1] \qog \vec{b} = [4, 3]
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\dot{a}{b}$ med CAS.


:::::::::::::


:::::::::::::{tab-item} b
Bestem vinkelen mellom vektorene med CAS.


:::::::::::::
::::::::::::::

:::::::::::::::















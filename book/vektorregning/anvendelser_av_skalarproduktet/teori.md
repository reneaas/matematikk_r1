# Anvendelser av skalarproduktet

:::{admonition} Læringsmål
---
class: tip
---
* Kunne lage en tverrvektor til en gitt vektor.
* Kunne bruke skalarproduktet til å bestemme avstanden fra et punkt til en linje.
* Kunne bruke skalarproduktet til å bestemme arealet av en trekant.
:::


> I dette kapittelet vil du finne at det er ganske mange formler, men de er alle logisk utledet med å tenke med vektorer. Det er derfor viktig at du prøver å forstå hvordan formlene er bygget opp så de ikke bare er *black-box*-formler (✈) du pugger utenat. Vi formulerer dem med formler her så vi har gjort det én gang for alle, men skulle du glemme en formel kan du alltid gå gjennom resonnementet på nytt og finne fram til den igjen! 

## Tverrvektorer


Når vi jobber med geometriske problemer i vektorregning, vil vi i blant trenge å lage oss en vektor som er vinkelrett på en gitt vektor med samme lengde som før. En slik vektor kaller vi for en **tverrvektor**. Denne typen vektor blir en gjenganger vi trenger igjen og igjen.


:::::::::::::::{summary} Tverrvektor
La $\vec{a}$ være en vektor. Da vil $\vec{a}_\perp$ være en **tverrvektor** til $\vec{a}$ hvis

$$
\vec{a} \perp \vec{a}_\perp \qog \len{a} = \abs{\vec{a}_\perp}
$$


Hvis $\vec{a} = [x, y]$, så er en tverrvektor til $\vec{a}$ gitt ved

$$
\vec{a}_\perp = [-y, x] \qeller \vec{a}_\perp = [y, -x]
$$

:::::::::::::::



---




:::::::::::::::{example} Eksempel 1
La $\vec{a} = [2, -1]$. 

Bestem en tverrvektor til $\vec{a}$.


::::{solution}
---
dropdown: 0
---
Vi bytter rekkefølge på komponentene til $\vec{a}$ og endrer fortegnet på én av dem for å lage en tverrvektor. Da får vi

$$
\vec{a}_\perp = [1, 2] \qeller \vec{a}_\perp = [-1, -2]
$$

Vi kan sjekke at $\vec{a} \perp \vec{a}_\perp$: 

$$
\vec{a} \cdot \vec{a}_\perp = [2, -1] \cdot [1, 2] = 2 \cdot 1 + (-1) \cdot 2 = 2 - 2 = 0
$$

Du kan få sjekke den andre. La oss også bekrefte at $\len{a} = \abs{\vec{a}_\perp}$:

$$
\len{a} = \sqrt{2^2 + (-1)^2} = \sqrt{4 + 1} = \sqrt{5}
$$

og 

$$
\abs{\vec{a}_\perp} = \sqrt{1^2 + 2^2} = \sqrt{1 + 4} = \sqrt{5}
$$

Altså er begge kriteriene for en tverrvektor oppfylt.

::::
:::::::::::::::


---



:::::::::::::::{exercise} Underveisoppgave 1
La $\vec{a} = [3, 1]$. 

1. Bestem en tverrvektor til $\vec{a}$. 
2. Sjekk at vektoren du finner tilfredsstiller $\vec{a} \perp \vec{a}_\perp$ og $\len{a} = \abs{\vec{a}_\perp}$.


::::{answer}
$$
\vec{a}_\perp = [-1, 3] \qeller \vec{a}_\perp = [1, -3]
$$
::::


:::::::::::::::









## Arealet av en trekant

Vi kan bruke vektorregning til å bestemme arealet av trekanter der vi kjenner to vektorer som utspenner trekanten.


:::::::::::::::{summary} Setning: Arealet av en trekant

:::{plot}
align: right
width: 100%
figsize: (4, 4)
point: (0, 0)
point: (3, 0)
point: (2, 1)
vector: 0, 0, 3, 0, blue
vector: 0, 0, 2, 1, red
line-segment: (3, 0), (2, 1), dashed, gray 
xmin: -0.5
xmax: 3.5
ymin: -0.5
ymax: 1.5
ticks: off
axis: off
text: 1.5, 0, "$\vec{a}$", bottom-center
text: 1, 0.5, "$\vec{b}$", top-left
fontsize: 20
text: 0, 0, "$A$", bottom-left
text: 3, 0, "$B$", bottom-right
text: 2, 1, "$C$", top-right
:::



En trekant $\triangle ABC$ utspent av vektorene $\vec{a}$ og $\vec{b}$ har et areal $T$ gitt ved

$$
T = \dfrac{1}{2} \abs{\vec{a} \cdot \vec{b}_\perp}
$$


der $\vec{b}_\perp$ er en **tverrvektor** til $\vec{b}$. 



:::{clear}
:::

:::::{admonition} Forklaring av formelen
---
class: theory, dropdown
---
Vi lager en hjelpefigur og tegner inn en høyde $h$ i trekanten og en tverrvektor $\vec{b}_\perp$ til vektoren $\vec{b}$:

:::{plot}
figsize: (4, 4)
width: 70%
point: (0, 0)
point: (3, 0)
point: (2, 1)
vector: 0, 0, 3, 0, blue
vector: 0, 0, 2, 1, red
line-segment: (3, 0), (2, 1), dashed, gray 
xmin: -0.5
xmax: 3.5
ymin: -3
ymax: 1.5
ticks: off
axis: off
text: 1.5, 0, "$\vec{a}$", bottom-center
text: 1, 0.5, "$\vec{b}$", top-left
fontsize: 20
text: 0, 0, "$A$", bottom-left
text: 3, 0, "$B$", bottom-right
text: 2, 1, "$C$", top-right
vector: 0, 0, 1, -2, red
text: 0.5, -1, "$\vec{b}_\perp$", bottom-left
angle-arc: (0, 0), 0.5, 0, 26.565
text: 0.6, 0.05, "$\varphi$", top-right
vline: 2, 0, 1, dashed, gray
angle-arc: (0, 0), 0.35, 0, 26.565 - 90
text: 0.3, -0.15, "$90^\circ - \varphi$", bottom-right
text: 2, 0.5, "$h$", center-left
fontsize: 18
:::

Vi vet at arealet $T$ til en trekant bare er gitt ved grunnlinje ganger høyde delt på to. Her er grunnlinjen $\len{a}$ og høyden er $h$ slik at

$$
T = \dfrac{1}{2} \cdot \len{a} \cdot h
$$

Vi kan uttrykke høyden $h$ ved hjelp av $\len{b}$ og vinkelen $\varphi$ mellom vektorene $\vec{a}$ og $\vec{b}$. Vi kan først se at

$$
\sin \varphi = \dfrac{h}{\len{b}} \liff h = \len{b} \cdot \sin \varphi
$$

Altså kan vi skrive om arealet til

$$
T = \dfrac{1}{2} \cdot \len{a} \cdot \len{b} \cdot \sin \varphi
$$

Vi vet lengdene til en vektor og dens tverrvektor er den samme slik at $\len{b} = \abs{\vec{b}_\perp}$. I såfall må det bety at arealet også kan skrives om til


$$
T = \dfrac{1}{2} \cdot \len{a} \cdot \abs{\vec{b}_\perp} \cdot \sin \varphi
$$

Arealformelen ligner skrekkelig mye på den geometriske formelen for skalarproduktet, bortsett fra $\sin \varphi$ inngår i uttrykket og ikke $\cos \varphi$. Men så er jo vinkelen mellom $\vec{a}$ og $\vec{b}_\perp$ gitt ved $90^\circ - \varphi$ og ikke $\varphi$. Kanskje vi kan se om det er en sammenheng til skalarproduktet mellom $\vec{a}$ og $\vec{b}_\perp$? Da får vi:

$$
\vec{a} \cdot \vec{b}_\perp = \len{a} \cdot \abs{\vec{b}_\perp} \cdot \cos(90\degree - \varphi)
$$

:::{plot}
align: right
width: 100%
figsize: (4, 3)
polygon: (0, 0), (cos(pi/6), 0), (cos(pi/6), sin(pi/6))
polygon: (cos(pi/6), 0), (cos(pi/6) - 0.1, 0), (cos(pi/6) - 0.1, 0.1), (cos(pi/6), 0.1)
axis: equal
angle-arc: (0, 0), 0.2, 0, 30
text: 0.2, 0.025, "$\varphi$", top-right
angle-arc: (cos(pi/6), sin(pi/6)), 0.15, -90, -90-60
text: cos(pi/6), sin(pi/6) - 0.15, "$90^\circ - \varphi$", bottom-left
axis: off
text: 0, 0, "$A$", bottom-left
text: cos(pi/6), 0, "$B$", bottom-right
text: cos(pi/6), sin(pi/6), "$C$", top-right
:::

Uttrykket ligner en del på uttrykket vi har kommet fram til for arealet, men vi må undersøke om det er en sammenheng mellom $\sin \varphi$ og $\cos(90\degree - \varphi)$ vi kan bruke. La oss tegne oss en trekant $\triangle ABC$ og lete etter en slik sammenheng:

Ved å bruke definisjonen av sinus og cosinus på de to vinklene i trekanten, får vi 

$$
\sin \varphi = \dfrac{BC}{AC} \and \cos (90\degree - \varphi) = \dfrac{BC}{AC}
$$

Men de to uttrykkene må jo da være like, så vi får at

$$
\sin \varphi = \cos(90\degree - \varphi)
$$

Dermed har vi at 

$$
\vec{a} \cdot \vec{b}_\perp = \len{a} \cdot \abs{\vec{b}_\perp} \cdot \cos(90\degree - \varphi) = \len{a} \cdot \abs{\vec{b}_\perp} \cdot \sin \varphi
$$

Og siden arealet av trekanten kunne skrives som

$$
T = \dfrac{1}{2} \cdot \len{a} \cdot \abs{\vec{b}_\perp} \cdot \sin \varphi
$$

må dette betyr at 

$$
T = \dfrac{1}{2} \cdot \vec{a} \cdot \vec{b}_\perp
$$

Vi har en siste floke å løsne opp i. Siden det finnes to tverrvektorer til $\vec{b}$ som er motsatt rettet av hverandre, vil skalarproduktet i formelen ovenfor kunne bli negativt. For å fikse dette, tar vi bare absoluttverdien av svaret slik at det alltid blir positivt: 

$$
T = \dfrac{1}{2} \abs{\vec{a} \cdot \vec{b}_\perp}
$$

Dette var formelen vi skulle begrunne.


:::::


:::::::::::::::



Vi tar et eksempel.


:::::::::::::::{example} Eksempel 2

:::{plot}
figsize: (4, 4)
align: right
width: 100%
point: (-2, -1)
point: (3, 2)
point: (-1, 3)
polygon: (-2, -1), (3, 2), (-1, 3)
text: -2, -1, "$A(-2, -1)$", bottom-left
text: 3, 2, "$B(3, 2)$", bottom-right
text: -1, 3, "$C(-1, 3)$", top-left
ticks: off
xmin: -3
xmax: 4
ymin: -1.5
ymax: 3.5
:::



En trekant $\triangle ABC$ har hjørnene $A(-2, -1)$, $B(3, 2)$ og $C(-1, 3)$.

Bestem arealet av trekanten. 



:::{clear}
:::

::::{solution}
---
dropdown: 0
---
Vi trenger to vektorer som spenner ut trekanten. Vi velger å bruke $\lvec{AB}$ og $\lvec{AC}$. Da får vi

$$
\lvec{AB} = [3, 2] - [-2, -1] = [5, 3] \qog \lvec{AC} = [-1, 3] - [-2, -1] = [1, 4]
$$

Så må vi lage en tverrvektor til én av de to. Vi velger å lage en tverrvektor til $\vec{AC}$. Da bytter vi om rekkefølgen på koordinatene og endrer fortegnet på én av dem:

$$
\lvec{AC}_\perp = [-4, 1]
$$

Så regner vi ut skalarproduktet mellom $\lvec{AB}$ og $\lvec{AC}_\perp$:

$$
\lvec{AB} \cdot \lvec{AC}_\perp = [5, 3] \cdot [-4, 1] = 5 \cdot (-4) + 3 \cdot 1 = -20 + 3 = -17
$$

Så bruker vi formelen for arealet av trekanten:

$$
T = \dfrac{1}{2} |\lvec{AB} \cdot \lvec{AC}_\perp| = \dfrac{1}{2} \cdot |-17| = \dfrac{17}{2}
$$

::::


:::::::::::::::




---


:::::::::::::::{exercise} Underveisoppgave 2

:::{plot}
figsize: (4, 4)
align: right
width: 100%
point: (-3, 1)
point: (2, -1)
point: (1, 3)
polygon: (-3, 1), (2, -1), (1, 3)
text: -3, 1, "$A(-3, 1)$", bottom-left
text: 2, -1, "$B(2, -1)$", bottom-right
text: 1, 3, "$C(1, 3)$", top-right
ticks: off
xmin: -3.5
xmax: 4.5
ymin: -1.5
ymax: 4
:::


En trekant $\triangle ABC$ har hjørnene $A(-3, 1)$, $B(2, -1)$ og $C(1, 3)$. 

Bestem arealet av trekanten.


:::{clear}
:::


::::{answer}
$$
T = 9
$$
::::


::::{solution}
Vi lager oss to vektorer som spenner ut trekanten. Vi velger $\lvec{AB}$ og $\lvec{AC}$. Da får vi

$$
\lvec{AB} = [2, -1] - [-3, 1] = [5, -2] \qog \lvec{AC} = [1, 3] - [-3, 1] = [4, 2]
$$

Så lager vi en tverrvektor til $\lvec{AC}$. Da bytter vi om rekkefølgen på koordinatene og endrer fortegnet på én av dem:

$$
\lvec{AC}_\perp = [-2, 4]
$$

Så regner vi ut skalarproduktet mellom $\lvec{AB}$ og $\lvec{AC}_\perp$:

$$
\lvec{AB} \cdot \lvec{AC}_\perp = [5, -2] \cdot [-2, 4] = 5 \cdot (-2) + (-2) \cdot 4 = -10 - 8 = -18
$$

Så bruker vi formelen for arealet av trekanten:

$$
T = \dfrac{1}{2} |\lvec{AB} \cdot \lvec{AC}_\perp| = \dfrac{1}{2} \cdot |-18| = 9
$$
::::



:::::::::::::::


---


## Arealet av et parallellogram

Et parallellogram kan vi få ved å ta en trekant, og speile den om én av sidene. Da får vi en firkant som parvis har to parallelle sider. Siden denne består av to like store trekanter, blir arealet dobbelt så stort som arealet av en trekant som utgjør halvparten. Det betyr at vi kan gjenbruke formelen vi fant for arealet av en trekant for å bestemme arealet av et parallellogram.


:::::::::::::::{summary} Setning: Arealet av et parallellogram

:::{plot}
align: right
width: 100%
figsize: (4, 4)
point: (0, 0)
point: (3, 0)
point: (2, 1)
vector: 0, 0, 3, 0, blue
vector: 0, 0, 2, 1, red
line-segment: (3, 0), (2, 1), dashed, gray 
xmin: -0.5
xmax: 5.5
ymin: -0.5
ymax: 1.5
ticks: off
axis: off
text: 1.5, 0, "$\vec{a}$", bottom-center
text: 1, 0.5, "$\vec{b}$", top-left
fontsize: 20
text: 0, 0, "$A$", bottom-left
text: 3, 0, "$B$", bottom-right
text: 2, 1, "$C$", top-left
point: (5, 1)
line-segment: (3, 0), (5, 1), dashed, red
line-segment: (2, 1), (5, 1), dashed, blue
text: 5, 1, "$D$", top-right
:::



Et parallellogram $ABCD$ utspent av vektorene $\vec{a}$ og $\vec{b}$ har et areal $T$ gitt ved

$$
T = |\vec{a} \cdot \vec{b}_\perp|
$$


der $\vec{b}_\perp$ er en **tverrvektor** til $\vec{b}$. 

:::::::::::::::



---




:::::::::::::::{example} Eksempel 3
Et parallellogram har hjørnene $A(-2, -1)$, $B(3, 2)$, $C(-1, 3)$ og $D(4, 6)$.

Bestem arealet av parallellogrammet.

::::{solution}
---
dropdown: 0
---
Vi trenger to vektorer som spenner ut parallellogrammet. Vi velger å bruke $\lvec{AB}$ og $\lvec{AD}$. Da får vi

$$
\lvec{AB} = [3, 2] - [-2, -1] = [5, 3] \qog \lvec{AD} = [4, 6] - [-2, -1] = [6, 7]
$$

Så må vi lage en tverrvektor til én av de to. Vi velger å lage en tverrvektor til $\lvec{AD}$. Da bytter vi om rekkefølgen på koordinatene og endrer fortegnet på én av dem:

$$
\lvec{AD}_\perp = [-7, 6]
$$

Så regner vi ut skalarproduktet mellom $\lvec{AB}$ og $\lvec{AD}_\perp$:

$$
\lvec{AB} \cdot \lvec{AD}_\perp = [5, 3] \cdot [-7, 6] = 5 \cdot (-7) + 3 \cdot 6 = -35 + 18 = -17
$$

Så bruker vi formelen for arealet av parallellogrammet:

$$
T = |\lvec{AB} \cdot \lvec{AD}_\perp| = |-17| = 17
$$

Altså er arealet av parallellogrammet lik $17$.
::::
:::::::::::::::



---


:::::::::::::::{exercise} Underveisoppgave 3
Et parallellogram har hjørner i punktene $A(-3, 1)$, $B(2, -1)$, $C(1, 3)$ og $D(6, 1)$.

Bestem arealet av parallellogrammet.


::::{answer}
Arealet er $18$. 
::::


::::{solution}
Vi trenger to vektorer som spenner ut parallellogrammet. Vi velger å bruke $\lvec{AB}$ og $\lvec{AD}$. Da får vi

$$
\lvec{AB} = [2, -1] - [-3, 1] = [5, -2] \qog \lvec{AD} = [6, 1] - [-3, 1] = [9, 0]
$$

Så må vi lage en tverrvektor til én av de to. Vi velger å lage en tverrvektor til $\lvec{AD}$. Da bytter vi om rekkefølgen på koordinatene og endrer fortegnet på én av dem:

$$
\lvec{AD}_\perp = [-0, 9] = [0, 9]
$$

Så regner vi ut skalarproduktet mellom $\lvec{AB}$ og $\lvec{AD}_\perp$:

$$
\lvec{AB} \cdot \lvec{AD}_\perp = [5, -2] \cdot [0, 9] = 5 \cdot 0 + (-2) \cdot 9 = 0 - 18 = -18
$$


Så bruker vi formelen for arealet av parallellogrammet:

$$
T = |\lvec{AB} \cdot \lvec{AD}_\perp| = |-18| = 18
$$

Altså er arealet av parallellogrammet lik $18$.
::::


:::::::::::::::



## Avstanden fra et punkt til en linje


:::{plot}
figsize: (4, 3)
align: right
width: 100%
line: 1, -2, solid, blue
point: (1, 3)
text: 1, 3, "$R$", top-left
text: 0.5 * (1 + 3), 0.5 * (1 + 3), "$h$", top-right
line-segment: (1, 3), (3, 1), dashed, gray
axis: equal
xmin: -1
xmax: 5
ymin: -1
ymax: 5
polygon: (2.6, 0.6), (3, 1), (2.6, 1.4), (2.2, 1)
axis: off
fontsize: 20
text: 5, 3, "$\ell$", top-right
:::

Arealformelen for en trekant gir oss en måte å bestemme avstanden fra et punkt $R$ til en linje $\ell$ ved hjelp av skalarproduktet. 

Når vi snakker om avstanden fra et punkt til en linje, så mener vi den **korteste avstanden** fra punktet til linjen som vil være et linjestykke som står vinkelrett på linja. Dette kan vi tolke som høyden i en trekant som har grunnlinje langs linjen $\ell$.


:::{clear}
:::

:::::::::::::::{summary} Avstand fra et punkt til en linje

:::{plot}
figsize: (4, 3)
align: right
width: 100%
line: 1, -2, solid, blue
point: (1, 3)
text: 1, 3, "$R$", top-left
text: 0.5 * (1 + 3), 0.5 * (1 + 3), "$h$", top-right
line-segment: (1, 3), (3, 1), dashed, gray
axis: equal
xmin: -1
xmax: 5
ymin: -1
ymax: 5
polygon: (2.6, 0.6), (3, 1), (2.6, 1.4), (2.2, 1)
axis: off
fontsize: 20
text: 5, 3, "$\ell$", top-right
point: (0, -2)
text: -0.15, -2, "$Q$", center-left
vector: (0, -2), (1.75, -0.25), red
text: 0.5 * (0 + 1.75), 0.5 * (-2 + -0.25), "$\vec{v}$", bottom-right
vector: (0, -2), (1, 3), red
text: 0.5 * (0 + 1), 0.5 * (-2 + 3), "$\overrightarrow{QR}$", top-left
:::

La en linje $\ell$ ha retningsvektor $\vec{v}$ og et punkt $Q$ som ligger på linja. La $R$ være et punkt utenfor linja.

Avstanden $h$ fra $R$ til linja $\ell$ er gitt ved

$$
h = \dfrac{|\lvec{QR} \cdot \vec{v}_\perp|}{\abs{\vec{v}}}
$$

der $\vec{v}_\perp$ er en tverrvektor til retningsvektoren $\vec{v}$, og $\lvec{QR}$ er vektoren fra punktet $Q$ til punktet $R$.


:::{clear}
:::


:::::{admonition} Forklaring av formelen
---
class: theory, dropdown
---


:::{plot}
align: right
width: 100%
hline: 0, -3, 3, dashed, blue
text: 3, 0, "$\ell$", center-right
point: (-2, 0)
point: (1, 3)
text: -2, 0, "$Q$", bottom-left
text: 1, 3, "$R$", top-right
vline: 1, 0, 3, dashed, gray
xmin: -3.5
xmax: 3.5
ymin: -0.5
ymax: 3.5
vector: -2, 0, 4, 0, red
vector: -2, 0, 3, 3, red
line-segment: (2, 0), (1, 3), dashed, gray
axis: off
fontsize: 30
text: 0, 0, "$\vec{v}$", bottom-center
text: 1, 1.5, "$h$", center-left
:::



La $\vec{v}$ være en retningsvektor på en linje $\ell$ og $Q$ være et vilkårlig punkt på linja. Da spenner $\vec{v}$ og $\lvec{QR}$ ut en trekant som vist i figuren til høyre.

Da kan vi skrive arealet på to måter. Først ved hjelp av høyden $h$ og grunnlinja $\len{v}$:

$$
T = \dfrac{1}{2} \len{v} \cdot h 
$$

Deretter ved å bruke skalarproduktet mellom vektorene $\vec{v}_\perp$ (tverrvektoren til $\vec{v}$) og $\lvec{QR}$:

$$
T = \dfrac{1}{2} |\lvec{QR} \cdot \vec{v}_\perp|
$$


Disse to uttrykkene for arealet må være like, som betyr at vi kan si at


$$
\dfrac{1}{2} \len{v} \cdot h = \dfrac{1}{2} |\lvec{QR} \cdot \vec{v}_\perp|
$$

Så løser vi denne likningen for $h$ for å finne hvor langt unna punktet $R$ er fra linja $\ell$:

$$
h = \dfrac{|\lvec{QR} \cdot \vec{v}_\perp|}{\len{v}}
$$

som var det vi skulle vise.

:::::







:::::::::::::::


Vi ser på et eksempel.


:::::::::::::::{example} Eksempel 4

:::{plot}
figsize: (4, 4)
align: right
width: 100%
line: 1, -2, solid, blue
point: (1, 3)
text: 1, 3, "$R(1, 3)$", top-right
xmin: -1
xmax: 5
ymin: -4
ymax: 4
:::


En linje $\ell$ er gitt ved likningen $y = x - 2$. 

Bestem avstanden fra punktet $R(1, 3)$ til linja. 



:::{clear}
:::


::::{solution}
---
dropdown: 0
---

Vi trenger ett punkt på linja $\ell$ og en retningsvektor $\vec{v}$ slik at vi kan definere vektorene som skal spenne ut en trekant. Setter vi inn $x = 0$ i likningen for linja, får vi $y = -2$ slik at punktet $Q(0, -2)$ ligger på linja. Da får vi vektoren

$$
\lvec{QR} = \lvec{OR} - \lvec{OQ} = [1, 3] - [0, -2] = [1, 5]
$$

En retningsvektor for linja kan vi finne ved å observere at stigningstallet til linja er $1$. Når vi beveger oss langs linja vil vi derfor øke $y$ med $1$ hver gang vi øker $x$ med $1$. En retningsvektor for linja er derfor

$$
\vec{v} = [1, 1]
$$

En tverrvektor til $\vec{v}$ får vi ved å bytte om rekkefølgen på koordinatene og endre fortegnet på én av dem:

$$
\vec{v}_\perp = [1, -1]
$$

Nå kan vi regne ut skalarproduktet mellom $\lvec{QR}$ og $\vec{v}_\perp$:

$$
\lvec{QR} \cdot \vec{v}_\perp = [1, 5] \cdot [1, -1] = 1 \cdot 1 + 5 \cdot (-1) = 1 - 5 = -4
$$

Så kan vi bruke formelen for avstanden fra punktet til linja:

$$
h = \dfrac{|\lvec{QR} \cdot \vec{v}_\perp|}{|\vec{v}|} = \dfrac{|-4|}{\sqrt{1^2 + 1^2}} = \dfrac{4}{\sqrt{2}} = 2\sqrt{2}
$$

Altså er avstanden fra punktet $R$ til linja $\ell$ lik $2\sqrt{2}$.

::::


:::::::::::::::


---



:::::::::::::::{exercise} Underveisoppgave 4

:::{plot}
figsize: (4, 4)
align: right
width: 100%
line: 2, -3, solid, blue
point: (-2, 3)
text: -2, 3, "$R(-2, 3)$", center-left
point: (2, 1)
point: (4, 5)
text: 2, 1, "$A(2, 1)$", bottom-right
text: 4, 5, "$B(4, 5)$", bottom-right
ymin: -2
ticks: off
:::


En linje $\ell$ går gjennom punktene $A(2, 1)$ og $B(4, 5)$.

Bestem avstanden fra punktet $R(-2, 3)$ til linja $\ell$.


:::{clear}
:::


::::{answer}
$$
2\sqrt{5}
$$
::::

::::{solution}
Vi kjenner til to punkter på linja, så vi kan regne ut en retningsvektor 

$$
\vec{v} = \lvec{AB} = [4, 5] - [2, 1] = [2, 4]
$$

En tverrvektor til $\vec{v}$ får vi ved å bytte om rekkefølgen på koordinatene og endre fortegnet på én av dem:

$$
\vec{v}_\perp = [4, -2]
$$

Vi trenger også vektoren fra ett punkt på linja til punktet utenfor linja. Vi velger $\lvec{AR}$:

$$
\lvec{AR} = [-2, 3] - [2, 1] = [-4, 2]
$$


Nå kan vi regne ut skalarproduktet mellom $\lvec{AR}$ og $\vec{v}_\perp$:

$$
\lvec{AR} \cdot \vec{v}_\perp = [-4, 2] \cdot [4, -2] = (-4) \cdot 4 + 2 \cdot (-2) = -16 - 4 = -20
$$

Så kan vi bruke formelen for avstanden fra punktet til linja:

$$
h = \dfrac{|\lvec{AR} \cdot \vec{v}_\perp|}{|\vec{v}|} = \dfrac{|-20|}{\sqrt{2^2 + 4^2}} = \dfrac{20}{\sqrt{4 + 16}} = \dfrac{20}{\sqrt{20}} = 2\sqrt{5}
$$

Altså er avstanden fra punktet $R$ til linja $\ell$ lik $2\sqrt{5}$.

::::

:::::::::::::::



---


## Dekomponering relativ til en linje
Når vi arbeidet med vektorer i planet, så er det nyttig å kunne dele opp en vektor i to komponenter: Én som peker langs en linje og én som står ortogonalt på linja. Dette kalles å **dekomponere** en vektor langs en linje. Vi skal se at dette er naturlige utvidelser av det vi allerede har jobbet med.


:::{plot}
figsize: (4, 3)
align: right
width: 100%
line: 1, -2, solid, blue
point: (1, 3)
text: 1, 3, "$R$", top-left
vector: (3, 1), (1, 3), red
text: 0.5 * (1 + 3), 0.5 * (1 + 3), "$\vec{h}$", top-right
axis: equal
xmin: -1
xmax: 5
ymin: -1
ymax: 5
polygon: (2.6, 0.6), (3, 1), (2.6, 1.4), (2.2, 1)
axis: off
fontsize: 20
text: 5, 3, "$\ell$", top-right
point: (0, -2)
text: -0.15, -2, "$Q$", center-left
vector: (0, -2), (1, 3), red
text: 0.5 * (0 + 1), 0.5 * (-2 + 3), "$\overrightarrow{QR}$", top-left
vector: (0, -2), (3, 1), red
text: 0.5 * (0 + 3), 0.5 * (-2 + 1), "$\vec{p}$", bottom-right
:::


Hvis vi lar et punkt $Q$ ligge på en linje $\ell$ med retningsvektor $\vec{v}$, og et punkt $R$ ligger utenfor linja, så kan vi dele opp vektoren $\lvec{QR}$ i to komponenter: Én som peker langs linja og én som står vinkelrett på linja.




$$
\lvec{QR} = \underbrace{\vec{p}}_{\mstack{\text{langs} \\ \text{linja}}} + \underbrace{\vec{h}}_{\mstack{\text{vinkelrett} \\ \text{på} \\ \text{linja}}}
$$


Vi vet allerede hvordan vi finner $\abs{\vec{h}}$ fra da vi så på hvordan vi fant avstanden fra et punkt til en linje. Nå skal vi se hvordan vi kan si noe om vektorene $\vec{p}$ og $\vec{h}$ hver for seg.



### Parallellkomponenten (komponenten langs linja)


Den delen av en vektor som er parallell med en linje, kalles gjerne for **projeksjonen** av vektoren ned på linja. 

Vi har allerede gjort mesteparten av forarbeidet for å finne projeksjonen. Formelen for projeksjonen er skremmende lik formelen for avstanden fra et punkt til en linje. Dette vil være en gjenganger – som vi snart skal se.

:::{clear}
:::


:::::::::::::::{summary} Parallellkomponenten langs en linje (projeksjonen)

:::{plot}
figsize: (4, 3)
align: right
width: 100%
line: 1, -2, solid, blue
point: (1, 3)
text: 1, 3, "$R$", top-left
vector: (3, 1), (1, 3), red
text: 0.5 * (1 + 3), 0.5 * (1 + 3), "$\vec{h}$", top-right
axis: equal
xmin: -1
xmax: 5
ymin: -1
ymax: 5
polygon: (2.6, 0.6), (3, 1), (2.6, 1.4), (2.2, 1)
axis: off
fontsize: 20
text: 5, 3, "$\ell$", top-right
point: (0, -2)
text: -0.15, -2, "$Q$", center-left
vector: (0, -2), (1, 3), red
text: 0.5 * (0 + 1), 0.5 * (-2 + 3), "$\overrightarrow{QR}$", top-left
vector: (0, -2), (3, 1), red
text: 0.5 * (0 + 3), 0.5 * (-2 + 1), "$\vec{p}$", bottom-right
:::


Parallellkomponenten (projeksjonen) $\vec{p}$ av en vektor $\lvec{QR}$ ned på en linje $\ell$ med retningsvektor $\vec{v}$ er gitt ved

$$
\vec{p} = \dfrac{\lvec{QR} \cdot \vec{v}}{\abs{\vec{v}}^2} \vec{v}
$$

:::{clear}
:::

::::::::::::::{admonition} Forklaring av formelen
---
class: theory, dropdown
---

:::{plot}
figsize: (4, 3)
align: right
width: 100%
line: 1, -2, solid, blue
point: (1, 3)
text: 1, 3, "$R$", top-left
vector: (3, 1), (1, 3), red
text: 0.5 * (1 + 3), 0.5 * (1 + 3), "$\vec{h}$", top-right
axis: equal
xmin: -1
xmax: 5
ymin: -1
ymax: 5
polygon: (2.6, 0.6), (3, 1), (2.6, 1.4), (2.2, 1)
axis: off
fontsize: 20
text: 5, 3, "$\ell$", top-right
point: (0, -2)
text: -0.15, -2, "$Q$", center-left
vector: (0, -2), (1, 3), red
text: 0.5 * (0 + 1), 0.5 * (-2 + 3), "$\overrightarrow{QR}$", top-left
vector: (0, -2), (3, 1), red
text: 0.5 * (0 + 3), 0.5 * (-2 + 1), "$\vec{p} = t\vec{v}$", bottom-right
:::

Projeksjonen $\vec{p}$ (vektoren som ligger langs linja) må være parallell med retningsvektoren $\vec{v}$ til linja. Derfor kan vi skrive projeksjonen som et skalarmultiplum av retningsvektoren:

$$
\vec{p} = t\vec{v}
$$

Vi vet at vektoren $\vec{h}$ (den vinkelrette komponenten) må stå ortogonalt på linja. Da er skalarproduktet mellom $\vec{h}$ og retningsvektoren $\vec{v}$ lik null:

$$
\vec{h} \cdot \vec{v} = 0
$$

Videre kan vi se at 

$$
\lvec{QR} = \vec{p} + \vec{h} \liff \vec{h} = \lvec{QR} - \vec{p}
$$

Så erstatter vi med at $\vec{p} = t \vec{v}$ i uttrykket ovenfor:

$$
\vec{h} = \lvec{QR} - t \vec{v}
$$

Så tar vi skalarproduktet som vi vet må bli null:

$$
\vec{h} \cdot \vec{v} = 0
$$

$$
(\lvec{QR} - t \vec{v}) \cdot \vec{v} = 0
$$

$$
\lvec{QR} \cdot \vec{v} - t (\vec{v} \cdot \vec{v}) = 0
$$

$$
\lvec{QR} \cdot \vec{v} - t \abs{\vec{v}}^2 = 0
$$

Løser vi denne likningen for $t$, får vi

$$
t = \dfrac{\lvec{QR} \cdot \vec{v}}{\abs{\vec{v}}^2}
$$

Altså må projeksjonen være

$$
\vec{p} = \dfrac{\lvec{QR} \cdot \vec{v}}{\abs{\vec{v}}^2} \vec{v}
$$

Denne vektoren har en ganske naturlig tolkning som vi kan se hvis vi skriver den om litt:

$$
\vec{p} = \left(\dfrac{\lvec{QR} \cdot \vec{v}}{\abs{\vec{v}}}\right) \cdot \left(\dfrac{\vec{v}}{\abs{\vec{v}}}\right)
$$

Den første faktoren forteller hvor lang delen av vektoren $\lvec{QR}$ som peker langs linja er, mens den andre faktoren er en enhetsvektor som peker langs linja. Hvordan kan vi se det? Vel, vi tenker oss at det er en vinkel $\varphi$ mellom vektorene $\lvec{QR}$ og $\vec{v}$. Da gir den geometriske formelen for skalarproduktet oss at

$$
\lvec{QR} \cdot \vec{v} = \abs{\lvec{QR}} \cdot \abs{\vec{v}} \cdot \cos \varphi
$$

Setter vi det inn i uttrykket for $\vec{p}$ får vi:

$$
\vec{p} = \left(\dfrac{\abs{\lvec{QR}} \cdot \abs{\vec{v}} \cdot \cos \varphi}{\abs{\vec{v}}}\right) \cdot \left(\dfrac{\vec{v}}{\abs{\vec{v}}}\right) = \left(\abs{\lvec{QR}} \cdot \cos \varphi\right) \cdot \left(\dfrac{\vec{v}}{\abs{\vec{v}}}\right)
$$

Den første faktoren vil være lengden langs linja (men *med* fortegn siden $\cos \varphi$ kan være negativ), mens den andre faktoren er en enhetsvektor som peker langs linja.

::::::::::::::


:::::::::::::::


---


:::::::::::::::{example} Eksempel 5

En linje $\ell$ går gjennom punktet $Q(0, -2)$ og har en retningsvektor $\vec{v} = [1, 2]$. 

Et punkt $R(4, 1)$ ligger utenfor linja.

Bestem koordinatene til punktet $P$ på linja som ligger nærmest punktet $R$.


:::{clear}
:::

::::{solution}
---
dropdown: 0
---

:::{plot}
width: 100%
align: right
figsize: (4, 3)
fontsize: 20
point: (0, -2)
text: -0.15, -2, "$Q(0, -2)$", center-left
vector: (0, -2), 2, 4, red
text: 0.5 * (0 + 2), 0.5 * (-2 + (-2 + 4)), "$\vec{p}$", top-left
line: 2, -2, solid, blue
text: 3.5, 4, "$\ell$", top-right
point: (4, 1)
text: 4, 1, "$R(4, 1)$", top-right
ticks: off
axis: off
xmin: -1
xmax: 4
ymin: -1
ymax: 4
axis: equal
line-segment: (2, 2), (4, 1), dashed, gray
point: (2, 2)
text: 2, 2, "$P$", top-left
vector: (0, -2), (4, 1), red
text: 0.5 * (0 + 4), 0.5 * (-2 + 1), "$\overrightarrow{QR}$", bottom-right
:::

Som alltid, bør vi starte med å lage oss en hjelpefigur så vi får oversikt over problemstillingen og systematisert opplysningene vi har. 

For å bestemme koordinatene til punktet $P$ på linja som ligger nærmest punktet $R$, kan vi følge projeksjonsvektoren $\vec{p}$ fra punktet $Q$ på linja. Altså vil

$$
\lvec{OP} = \lvec{OQ} + \vec{p}
$$

For å finne projeksjonsvektoren $\vec{p}$, trenger vi først vektoren $\lvec{QR}$:

$$
\lvec{QR} = \lvec{OR} - \lvec{OQ} = [4, 1] - [0, -2] = [4, 3]
$$

Nå kan vi bruke formelen for projeksjonsvektoren:

$$
\vec{p} = \dfrac{\lvec{QR} \cdot \vec{v}}{\abs{\vec{v}}^2} \vec{v}
$$

Først regner vi ut skalarproduktet i telleren:

$$
\lvec{QR} \cdot \vec{v} = [4, 3] \cdot [1, 2] = 4 \cdot 1 + 3 \cdot 2 = 4 + 6 = 10
$$

Så regner vi ut nevneren:

$$
\abs{\vec{v}}^2 = 1^2 + 2^2 = 1 + 4 = 5
$$

Nå kan vi sette det sammen for å finne projeksjonsvektoren:

$$
\vec{p} = \dfrac{10}{5} \cdot [1, 2] = 2 \cdot [1, 2] = [2, 4]
$$

Nå som vi har projeksjonsvektoren, kan vi finne koordinatene til punktet $P$:

$$
\lvec{OP} = \lvec{OQ} + \vec{p} = [0, -2] + [2, 4] = [2, 2]
$$

Altså har punktet $P$ (som ligger nærmest $R$) koordinatene $(2, 2)$.



::::


:::::::::::::::



### Normalkomponenten (komponenten vinkelrett på linja)

Nå som vi har funnet projeksjonen av vektoren ned på linja, så er det enkelt å finne den delen av vektoren som står vinkelrett på linja. Dette er bare resten av vektoren når vi har tatt bort projeksjonen. Vi bare gjentar argumentet på nytt, men nå langs tverrvektoren til retningsvektoren. 

:::::::::::::::{summary} Normalkomponenten til en vektor på en linje
:::{plot}
figsize: (4, 3)
align: right
width: 100%
line: 1, -2, solid, blue
point: (1, 3)
text: 1, 3, "$R$", top-left
vector: (3, 1), (1, 3), red
text: 0.5 * (1 + 3), 0.5 * (1 + 3), "$\vec{h}$", top-right
axis: equal
xmin: -1
xmax: 5
ymin: -1
ymax: 5
polygon: (2.6, 0.6), (3, 1), (2.6, 1.4), (2.2, 1)
axis: off
fontsize: 20
text: 5, 3, "$\ell$", top-right
point: (0, -2)
text: -0.15, -2, "$Q$", center-left
vector: (0, -2), (1, 3), red
text: 0.5 * (0 + 1), 0.5 * (-2 + 3), "$\overrightarrow{QR}$", top-left
vector: (0, -2), (3, 1), red
text: 0.5 * (0 + 3), 0.5 * (-2 + 1), "$\vec{p}$", bottom-right
:::

La et punkt $Q$ ligge på en linje $\ell$ med retningsvektor $\vec{v}$, og la et punkt $R$ ligge utenfor linja. Da er normalkomponenten $\vec{h}$ til vektoren $\lvec{QR}$ gitt ved

$$
\vec{h} = \dfrac{\lvec{QR} \cdot \vec{v}_\perp}{\abs{\vec{v}_\perp}^2} \vec{v}_\perp
$$

der $\vec{v}_\perp$ er en tverrvektor til retningsvektoren $\vec{v}$.


::::::::::::::{admonition} Forklaring av formelen
---
class: theory, dropdown
---

:::{plot}
figsize: (4, 3)
align: right
width: 100%
line: 1, -2, solid, blue
point: (1, 3)
text: 1, 3, "$R$", top-left
vector: (3, 1), (1, 3), red
text: 0.5 * (1 + 5), 0.5 * (1 + 4), "$\vec{h} = s \cdot \vec{v}_\perp$", top-center
axis: equal
xmin: -1
xmax: 5
ymin: -1
ymax: 5
polygon: (2.6, 0.6), (3, 1), (2.6, 1.4), (2.2, 1)
axis: off
fontsize: 20
text: 5, 3, "$\ell$", top-right
point: (0, -2)
text: -0.15, -2, "$Q$", center-left
vector: (0, -2), (1, 3), red
text: 0.5 * (0 + 1), 0.5 * (-2 + 3), "$\overrightarrow{QR}$", top-left
vector: (0, -2), (3, 1), red
text: 0.5 * (0 + 3), 0.5 * (-2 + 1), "$\vec{p}$", bottom-right
:::

Vi gjør et tilsvarende argument som for projeksjonsvektoren. Normalkomponenten $\vec{h}$ må være parallell med tverrvektoren $\vec{v}_\perp$ til retningsvektoren $\vec{v}$. Derfor kan vi skrive normalkomponenten som et skalarmultiplum av tverrvektoren:

$$
\vec{h} = s\vec{v}_\perp
$$

Videre vet vi at vi kan skrive $\lvec{QR}$ som summen av projeksjonsvektoren og normalkomponenten:

$$
\lvec{QR} = \vec{p} + \vec{h} \liff \vec{p} = \lvec{QR} - \vec{h}
$$

Nå, siden projeksjonsvektoren $\vec{p}$ må ligge langs linja, så må skalarproduktet mellom $\vec{p}$ og tverrvektoren $\vec{v}_\perp$ være lik null (siden de står normalt på hverandre):

$$
\vec{p} \cdot \vec{v}_\perp = 0
$$

$$
(\lvec{QR} - \vec{h}) \cdot \vec{v}_\perp = 0
$$

Så erstatter vi $\vec{h} = s \vec{v}_\perp$ i uttrykket over så vi kan bestemme $s$:

$$
(\lvec{QR} - s \vec{v}_\perp) \cdot \vec{v}_\perp = 0
$$

$$
\lvec{QR} \cdot \vec{v}_\perp - s (\vec{v}_\perp \cdot \vec{v}_\perp) = 0
$$

$$
\lvec{QR} \cdot \vec{v}_\perp - s \abs{\vec{v}_\perp}^2 = 0
$$

Løser vi denne likningen for $s$, får vi

$$
s = \dfrac{\lvec{QR} \cdot \vec{v}_\perp}{\abs{\vec{v}_\perp}^2}
$$

Dermed er normalkomponenten til vektoren gitt ved:

$$
\vec{h} = \dfrac{\lvec{QR} \cdot \vec{v}_\perp}{\abs{\vec{v}_\perp}^2} \vec{v}_\perp
$$

som var det vi skulle vise.

::::::::::::::

:::::::::::::::

Det er altså en ganske fin symmetri her, der projeksjonen ned på linja involverer $\vec{v}$, mens normalkomponenten har en lik formel som involverer $\vec{v}_\perp$ som står normalt på $\vec{v}$. Det er kanskje ikke *så* overraskende! Men dette gir en helt ny betydning til skalarproduktet. Så lenge vi bruker basisvektorer som står normalt på hverandre, så vil skalarproduktet fungere som en måte å hente ut komponentene langs hver retning – med *noen ekstra steg*, selvfølgelig.



:::::::::::::::{example} Eksempel 6
En linje $\ell$ går gjennom et punkt $Q(1, -1)$ og har retningsvektor $\vec{v} = [-1, 2]$.

Et punkt $R(3, 5)$ ligger utenfor linja.

Bestem koordinatene til punktet $R'$ som er speilbildet av punktet $R$ om linja $\ell$.


::::{solution}
---
dropdown: 0
---

:::{plot}
width: 100%
align: right
figsize: (3, 3)
fontsize: 16
xmin: -3
xmax: 3
ymin: -3
ymax: 3
axis: equal
axis: off
point: (1, -1)
text: 1, -1, "$Q(1, -1)$", bottom-left
point: (3, 5)
text: 3, 5, "$R(3, 5)$", top-right
line: (0, 1), (1, -1), solid, blue
point: (-5, 1)
text: -5, 1, "$R'$", top-left
vector: (1, -1), (3, 5), red
text: 0.5 * (1 + 3), 0.5 * (-1 + 5), "$\overrightarrow{QR}$", bottom-right
vector: (-1, 3), (3, 5), red
text: 0.5 * (-1 + 3), 0.5 * (3 + 5), "$\vec{h}$", top-center
:::



Vi starter med å lage oss en hjelpefigur for å systematisere opplysningene og få oversikt.

For å bestemme koordinatene til punktet $R'$ som er speilbildet av punktet $R$ om linja $\ell$, kan vi bruke normalkomponenten $\vec{h}$ til vektoren $\lvec{QR}$. Hvis vi følger denne vektorer to ganger i motsatt retning fra punktet $R$, så lander vi på punktet $R'$:

$$
\lvec{OR'} = \lvec{OR} - 2\vec{h}
$$


For å bestemme normalkomponenten $\vec{h}$, trenger vi først vektoren $\lvec{QR}$:

$$
\lvec{QR} = \lvec{OR} - \lvec{OQ} = [3, 5] - [1, -1] = [2, 6]
$$

Nå trenger vi en tverrvektor til retningsvektoren $\vec{v} = [-1, 2]$. En tverrvektor får vi ved å bytte om rekkefølgen på koordinatene og endre fortegnet på én av dem:

$$
\vec{v}_\perp = [2, 1]
$$

Nå kan vi bruke formelen for normalkomponenten:

$$
\vec{h} = \dfrac{\lvec{QR} \cdot \vec{v}_\perp}{\abs{\vec{v}_\perp}^2} \vec{v}_\perp
$$

Først regner vi ut skalarproduktet i telleren:

$$
\lvec{QR} \cdot \vec{v}_\perp = [2, 6] \cdot [2, 1] = 2 \cdot 2 + 6 \cdot 1 = 4 + 6 = 10
$$

Så regner vi ut nevneren:

$$
\abs{\vec{v}_\perp}^2 = 2^2 + 1^2 = 4 + 1 = 5
$$

Nå kan vi sette det sammen for å finne normalkomponenten:

$$
\vec{h} = \dfrac{10}{5} \cdot [2, 1] = 2 \cdot [2, 1] = [4, 2]
$$

Nå som vi har normalkomponenten, kan vi finne koordinatene til punktet $R'$:

$$
\lvec{OR'} = \lvec{OR} - 2\vec{h} = [3, 5] - 2 \cdot [4, 2] = [3, 5] - [8, 4] = [-5, 1]
$$

Altså har punktet $R'$ (som er speilbildet av punktet $R$ om linja $\ell$) koordinatene $(-5, 1)$.


::::


:::::::::::::::


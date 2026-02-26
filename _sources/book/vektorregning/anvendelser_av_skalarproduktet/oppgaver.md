# Oppgaver: Anvendelser av skalarproduktet

> Du vil finne hint til mange av oppgavene, men prøv å *huske* strategien selv først! Dersom du ikke klarer å komme fram til fremgangsmåten etter litt tid, kan du se på hintet. Det er helt okei å se på hintet, men øv på å prøve og tenke deg fram til løsningen uten! Figurer og hint vil gradvis strippes bort når du kommer lenger ut i oppgavesettet slik at du må øve på å jobbe selvstendig.

:::::::::::::::{exercise} Oppgave 1

::::{hints} Hvordan fant man en tverrvektor igjen?
La $\vec{a}$ være en vektor. Da vil $\vec{a}_\perp$ være en **tverrvektor** til $\vec{a}$ hvis

$$
\vec{a} \perp \vec{a}_\perp \qog \len{a} = \abs{\vec{a}_\perp}
$$


Hvis $\vec{a} = [x, y]$, så er en tverrvektor til $\vec{a}$ gitt ved

$$
\vec{a}_\perp = [-y, x] \qeller \vec{a}_\perp = [y, -x]
$$
::::


Bestem en tverrvektor til vektorene.

1. Sjekk at $\vec{a} \perp \vec{a}_\perp$
2. Sjekk at $\len{a} = \abs{\vec{a}_\perp}$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\vec{a} = [3, 1]
$$


::::{answer}
$$
\vec{a}_\perp = [-1, 3] \qeller \vec{a}_\perp = [1, -3]
$$
::::


::::{solution}
For å lage en tverrvektor til $\vec{a}$, bytter vi rekkefølgen på koordinatene og endrer fortegnet på én av dem. For eksempel kan vi velge:

$$
\vec{a}_\perp = [-1, 3]
$$

Vi sjekker at vektorene er ortogonale ved å regne ut skalarproduktet:

$$
\vec{a} \cdot \vec{a}_\perp = 3 \cdot (-1) + 1 \cdot 3 = -3 + 3 = 0
$$

Så det stemmer. Vektorene må også ha samme lengde:

$$
\abs{\vec{a}} = \sqrt{3^2 + 1^2} = \sqrt{9 + 1} = \sqrt{10}
$$

$$
\abs{\vec{a}_\perp} = \sqrt{(-1)^2 + 3^2} = \sqrt{1 + 9} = \sqrt{10}
$$

Dette stemmer også.
::::

:::::::::::::



:::::::::::::{tab-item} b
$$
\vec{b} = [-2, 4]
$$


::::{answer}
$$
\vec{b}_\perp = [-4, -2] \qeller \vec{b}_\perp = [4, 2]
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\vec{c} = [1, -5]
$$


::::{answer}
$$
\vec{c}_\perp = [5, 1] \qeller \vec{c}_\perp = [-5, -1]
$$
::::

:::::::::::::



:::::::::::::{tab-item} d
$$
\vec{d} = [0, 3]
$$


::::{answer}
$$
\vec{d}_\perp = [-3, 0] \qeller \vec{d}_\perp = [3, 0]
$$

::::

:::::::::::::


::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 2


::::{hints} Hvordan fant man arealet av en trekant igjen?
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

::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{plot}
width: 100%
align: right
fontsize: 30
vector: (0, 0), (2, -1), blue
vector: (0, 0), (1, 3), red
line-segment: (2, -1), (1, 3), dashed, gray
point: (0, 0)
text: 0, 0, "$O$", bottom-left
point: (2, -1)
text: 2, -1, "$A$", bottom-right
point: (1, 3)
text: 1, 3, "$B$", top-left
ymin: -2
ymax: 5
xmin: -1
xmax: 3
fill-polygon: (0, 0), (2, -1), (1, 3)
:::


En trekant $\triangle OAB$ er spent ut av vektorene $\vec{a}$ og $\vec{b}$ gitt ved

$$
\vec{a} = [2, -1] \qog \vec{b} = [1, 3]
$$

Bestem arealet av trekanten.



:::{clear}
:::

::::{answer}
$$
T = \dfrac{7}{2}
$$
::::

::::{solution}
Arealet $T$ av en trekant som er spent ut av to vektorer $\vec{a}$ og $\vec{b}$ er gitt ved

$$
T = \dfrac{1}{2} \abs{\vec{a} \cdot \vec{b}_\perp}
$$

Vi bestemmer en tverrvektor til $\vec{b}$ ved å bytte om på rekkefølgen til koordinatene og endre fortegn på én av dem:

$$
\vec{b}_\perp = [-3, 1]
$$

Nå kan vi regne ut skalarproduktet:

$$
\vec{a} \cdot \vec{b}_\perp = [2, -1] \cdot [-3, 1] = 2 \cdot (-3) + (-1) \cdot 1 = -6 - 1 = -7
$$

Dermed blir arealet av trekanten

$$
T = \dfrac{1}{2} \abs{-7} = \dfrac{7}{2}
$$
::::


:::::::::::::



:::::::::::::{tab-item} b


:::{plot}
width: 100%
align: right
fontsize: 30
vector: (1, 2), (4, 3), blue
vector: (1, 2), (2, 6), red
line-segment: (4, 3), (2, 6), dashed, gray
point: (1, 2)
text: 1, 2, "$A$", bottom-left
point: (4, 3)
text: 4, 3, "$B$", bottom-right
point: (2, 6)
text: 2, 6, "$C$", top-left
ymin: 0
ymax: 7
xmin: 0
xmax: 5
fill-polygon: (1, 2), (4, 3), (2, 6)
:::



En trekant $\triangle ABC$ er spent ut av to vektorer $\vec{a}$ og $\vec{b}$ gitt ved

$$
\vec{a} = [4, 2] \qog \vec{b} = [-1, 5]
$$

Bestem arealet av trekanten.


:::{clear}
:::


::::{answer}
$$
T = 11
$$
::::

::::{solution}
Arealet er gitt ved

$$
T = \dfrac{1}{2} \abs{\vec{a} \cdot \vec{b}_\perp}
$$

En tverrvektor til $\vec{b}$ er

$$
\vec{b}_\perp = [-5, -1]
$$

Nå kan vi regne ut skalarproduktet:

$$
\vec{a} \cdot \vec{b}_\perp = 4 \cdot (-5) + 2 \cdot (-1) = -20 - 2 = -22
$$

Dermed blir arealet av trekanten

$$
T = \dfrac{1}{2} \abs{-22} = 11
$$
::::


:::::::::::::



:::::::::::::{tab-item} c


:::{plot}
width: 100%
align: right
fontsize: 30
vector: (-3, 1), (1, 4), blue
vector: (-3, 1), (2, -2), red
line-segment: (1, 4), (2, -2), dashed, gray
point: (-3, 1)
text: -3, 1, "$A$", top-left
point: (1, 4)
text: 1, 4, "$B$", top-right
point: (2, -2)
text: 2, -2, "$C$", bottom-right
ymin: -3
ymax: 5
xmin: -4
xmax: 3
fill-polygon: (-3, 1), (1, 4), (2, -2)
:::



En trekant $\triangle PQR$ er spent ut av vektorene $\vec{p}$ og $\vec{q}$ gitt ved

$$
\vec{p} = [3, 4] \qog \vec{q} = [2, -1]
$$

Bestem arealet av trekanten.




:::{clear}
:::

::::{answer}
$$
T = \dfrac{11}{2}
$$
::::

::::{solution}
Arealet av trekanten er gitt ved

$$
T = \dfrac{1}{2} \abs{\vec{p} \cdot \vec{q}_\perp}
$$

En tverrvektor til $\vec{q}$ er

$$
\vec{q}_\perp = [1, 2]
$$

Nå kan vi regne ut skalarproduktet:

$$
\vec{p} \cdot \vec{q}_\perp = 3 \cdot 1 + 4 \cdot 2 = 3 + 8 = 11
$$

Dermed blir arealet av trekanten

$$
T = \dfrac{1}{2} \abs{11} = \dfrac{11}{2}
$$
::::


:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3

::::{hints} Hvordan finner jeg vektorer som spenner ut trekanten?
Velg deg **ett** hjørne i trekanten og lag to vektorer fra dette hjørnet til de to andre hjørnene. Da har du to vektorer som spenner ut trekanten! Deretter kan du bruke formelen for arealet av trekanten som i oppgave 2.
::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{plot}
width: 100%
align: right
fontsize: 30
point: (1, 2)
text: 1, 2, "$A$", bottom-left
point: (4, 5)
text: 4, 5, "$B$", bottom-right
point: (2, 6)
text: 2, 6, "$C$", top-left
polygon: (1, 2), (4, 5), (2, 6)
ymin: 0
ymax: 7
xmin: 0
xmax: 5
fill-polygon: (1, 2), (4, 5), (2, 6)
:::


En trekant $\triangle ABC$ har hjørnene $A(1, 2)$, $B(4, 5)$ og $C(2, 6)$.

Bestem arealet av trekanten.


:::{clear}
:::


::::{answer}
Arealet er $\dfrac{9}{2}$
::::


::::{solution}
Vi trenger to vektorer som spenner ut trekanten. Vi velger oss et hjørne og lager to vektorer fra dette hjørnet til de to andre hjørnene. La oss velge hjørnet $A$. Da får vi:

$$
\lvec{AB} = [4 - 1, 5 - 2] = [3, 3]
$$

og

$$
\lvec{AC} = [2 - 1, 6 - 2] = [1, 4]
$$

Så lager vi en tverrvektor til én av de to. Vi velger å lage en tverrvektor til $\lvec{AC}$:

$$
\lvec{AC}_\perp = [-4, 1]
$$

Nå kan vi regne ut skalarproduktet:

$$
\lvec{AB} \cdot \lvec{AC}_\perp = 3 \cdot (-4) + 3 \cdot 1 = -12 + 3 = -9
$$

Dermed blir arealet av trekanten

$$
T = \dfrac{1}{2} |\lvec{AB} \cdot \lvec{AC}_\perp| = \dfrac{1}{2} \abs{-9} = \dfrac{9}{2}
$$

::::


:::::::::::::


:::::::::::::{tab-item} b

:::{plot}
width: 100%
align: right
fontsize: 30
point: (-2, 1)
text: -2, 1, "$P$", bottom-left
point: (1, 4)
text: 1, 4, "$R$", top-right
point: (3, 0)
text: 3, 0, "$Q$", top-right
polygon: (-2, 1), (1, 4), (3, 0)
ymin: -1
ymax: 5
xmin: -3
xmax: 4
fill-polygon: (-2, 1), (1, 4), (3, 0)
:::


En trekant $\triangle PQR$ har hjørnene $P(-2, 1)$, $Q(3, 0)$ og $R(1, 4)$.

Bestem arealet av trekanten.



:::{clear}
:::

::::{answer}
Arealet er $9$.
::::

::::{solution}
Vi velger oss et hjørne i trekanten og lager to vektorer som spenner ut trekanten:

$$
\lvec{PQ} = [3 - (-2), 0 - 1] = [5, -1]
$$

$$
\lvec{PR} = [1 - (-2), 4 - 1] = [3, 3]
$$


En tverrvektor til $\lvec{PR}$ er

$$
\lvec{PR}_\perp = [-3, 3]
$$

Nå kan vi regne ut skalarproduktet:

$$
\lvec{PQ} \cdot \lvec{PR}_\perp = 5 \cdot (-3) + (-1) \cdot 3 = -15 - 3 = -18
$$

Dermed blir arealet av trekanten

$$
T = \dfrac{1}{2} |\lvec{PQ} \cdot \lvec{PR}_\perp| = \dfrac{1}{2} \abs{-18} = 9
$$


::::


:::::::::::::


:::::::::::::{tab-item} c

:::{plot}
width: 100%
align: right
fontsize: 30
point: (0, 0)
text: 0, 0, "$S$", bottom-left
point: (3, 5)
text: 3, 5, "$T$", top-right
point: (5, 2)
text: 5, 2, "$R$", bottom-right
polygon: (0, 0), (3, 5), (5, 2)
ymin: -1
ymax: 6
xmin: -1
xmax: 6
fill-polygon: (0, 0), (3, 5), (5, 2)
:::


En trekant $\triangle SRT$ har hjørnene $S(0, 0)$, $R(5, 2)$ og $T(3, 5)$.

Bestem arealet av trekanten.



:::{clear}
:::

::::{answer}
Arealet er $\dfrac{19}{2}$.
::::

::::{solution}
Vi lager to vektorer som spenner ut trekanten:

$$
\lvec{SR} = [5 - 0, 2 - 0] = [5, 2]
$$

$$
\lvec{ST} = [3 - 0, 5 - 0] = [3, 5]
$$

En tverrvektor til $\lvec{ST}$ er

$$
\lvec{ST}_\perp = [-5, 3]
$$

Nå kan vi regne ut skalarproduktet:

$$
\lvec{SR} \cdot \lvec{ST}_\perp = 5 \cdot (-5) + 2 \cdot 3 = -25 + 6 = -19
$$

Dermed blir arealet av trekanten

$$
T = \dfrac{1}{2} |\lvec{SR} \cdot \lvec{ST}_\perp| = \dfrac{1}{2} \abs{-19} = \dfrac{19}{2}
$$
::::


:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4


::::{hints} Hvordan finner jeg avstanden fra et punkt til en linje?
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
::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a


:::{plot}
width: 100%
align: right
fontsize: 30
line: (1, 2), (1 + 3, 2 + 1), solid, blue
ymin: 0
point: (1, 2)
text: 1, 2, "$Q(1, 2)$", bottom-right
vector: (-2, 1), 3, 1, red
text: -2 + 0.5 * 3, 1 + 0.5 * 1, "$\vec{v}$", top-left
point: (5, 1)
text: 5, 1, "$R(5, 1)$", bottom-left
ticks: off
ymax: 3
:::



En linje $\ell$ har et punkt $Q(1, 2)$ på linja og en retningsvektor $\vec{v} = [3, 1]$.

Et punkt $R(5, 1)$ ligger utenfor linja.

Bestem avstanden fra $R$ til $\ell$.


:::{clear}
:::

::::{answer}
Avstanden er $\dfrac{7}{\sqrt{10}}$.
::::



:::::::::::::



:::::::::::::{tab-item} b

:::{plot}
width: 100%
align: right
fontsize: 30
line: (-1, 0), (2, 4), solid, blue
point: (-1, 0)
text: -1, 0, "$A(-1, 0)$", top-left
point: (2, 4)
text: 2, 4, "$B(2, 4)$", bottom-right
point: (3, 1)
text: 3, 1, "$C(3, 1)$", center-right
ticks: off
ymin: -1
:::



En linje $m$ går gjennom punktene $A(-1, 0)$ og $B(2, 4)$.

Et punkt $C(3, 1)$ ligger utenfor linja.

Bestem avstanden fra $C$ til $m$.


:::{clear}
:::

::::{answer}
Avstanden er $\dfrac{13}{5}$. 
::::


:::::::::::::


:::::::::::::{tab-item} c

:::{plot}
width: 100%
align: right
fontsize: 30
line: (-2, 3), (1, 1), solid, blue
point: (-2, 3)
text: -2, 3, "$P(-2, 3)$", bottom-left
point: (1, 1)
text: 1, 1, "$Q(1, 1)$", top-right
point: (0, 5)
text: 0, 5, "$R(0, 5)$", center-right
ticks: off
ymax: 6
ymin: -2
:::


En linje $n$ går gjennom punktene $P(-2, 3)$ og $Q(1, 1)$. 

Et punkt $R(0, 5)$ ligger utenfor linja.

Bestem avstanden fra $R$ til $n$.


:::{clear}
:::

::::{answer}
Avstanden er $\dfrac{10}{\sqrt{13}}$.
::::


:::::::::::::



::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 5
:::{plot}
width: 60%
ticks: off
let: x = 2.5
point: (0, 4)
point: (8, 0)
point: (0, x)
point: (x, 0)
point: (4, 2)
line-segment: (0, 4), (8, 0), solid, black
polygon: (x, 0), (0, x), (4, 2), blue, 0.2
text: 0, x, "$P(0, t)$", center-left
text: x, 0, "$Q(t, 0)$", bottom-center
text: 0, 0, "$O$", bottom-left
text: 8, 0, "$B(8, 0)$", bottom-center
text: 0, 4, "$A(0, 4)$", center-left
text: 4, 2, "$M(4, 2)$", top-right
xmin: -1
xmax: 9
ymin: -1
ymax: 5 
:::

En trekant har hjørnene $P(0, t)$, $Q(t, 0)$ og $M(4, 2)$ der $t \in \langle 0, 4 \rangle$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk vektorregning til å finne en uttrykk for arealet av $\triangle PQM$ uttrykt ved $t$.

::::{answer}
$$
T(t) = -\dfrac{1}{2}t^2 + 3t
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem det største mulige arealet en slik trekant kan ha.

::::{answer}
$$
\dfrac{9}{2}
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
En firkant $ABCD$ har hjørnene $A(1, 1)$, $B(4, 2)$, $C(3, 5)$ og $D(0, 7)$.

Bestem arealet av firkanten.


::::{answer}
Arealet er $13$. 
::::


:::::::::::::


:::::::::::::{tab-item} b
En firkant har hjørnene $A(2, -1)$, $B(5, -2)$, $C(7, 6)$ og $D(1, t)$ der $t > 0$.

Bestem $t$ slik at arealet av firkanten er $20$. 


::::{answer}
$$
t = \dfrac{2}{5}
$$
::::



:::::::::::::


:::::::::::::{tab-item} c
En linje $\ell$ går gjennom punktene $A(2, 1)$ og $B(8, 4)$.

Et annen punkt $C(3, 9)$ ligger utenfor linja. Dersom vi speiler $C$ om linja $\ell$, får vi punktet $D$.

Bestem arealet av firkanten $ADBC$.


::::{answer}
Arealet er $45$.
::::


:::::::::::::


::::::::::::::
:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 7


::::{hints} Dekomponering relativ til en linje
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

$$
\vec{p} = \dfrac{\lvec{QR} \cdot \vec{v}}{\abs{\vec{v}}^2} \vec{v} \qog \vec{h} = \dfrac{\lvec{QR} \cdot \vec{v}_\perp}{\abs{\vec{v}}^2} \vec{v}_\perp
$$

::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En linje $\ell$ går gjennom punktene $A(2, 3)$ og $B(5, 7)$.

Et punkt $C(1, 10)$ ligger utenfor linja.

Bestem koordinatene til punktet $P$ på linja $\ell$ som ligger nærmest punktet $C$.

::::{answer}
$$
P(5, 7)
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
En linje $m$ går gjennom punktene $D(-2, 4)$ og $E(1, -2)$.

Et punkt $F(4, 3)$ ligger utenfor linja.

Bestem koordinatene til punktet $Q$ på linja $m$ som ligger nærmest punktet $F$.

::::{answer}
$$
Q\left(-\dfrac{2}{5}, \dfrac{4}{5}\right)
$$
::::
:::::::::::::


:::::::::::::{tab-item} c
En linje $n$ går gjennom punktene $Q(-1, 5)$ og $R(1, 7)$. 

Et punkt $S(3, 2)$ ligger utenfor linja.

Bestem koordinatene til punktet $T$ på linja $n$ som ligger nærmest punktet $S$.


::::{answer}
$$
T\left(-\dfrac{1}{2}, \dfrac{11}{2}\right)
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
En linje $\ell$ går gjennom et punkt $Q(2, 1)$ og har retningsvektor $\vec{v} = [-2, 1]$.

Et punkt $R(4, 5)$ ligger utenfor linja.

Bestem koordinatene til punktet $R'$ som fås ved å speile $R$ om linja $\ell$.


::::{answer}
$$
R'(0, -3)
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
En linje $m$ går gjennom to punkter $A(1, 4)$ og $B(4, 1)$.

Et punkt $C(1, 8)$ ligger utenfor linja.

Bestem koordinatene til punktet $C'$ som fås ved å speile $C$ om linja $m$.


::::{answer}
$$
C'(-3, 4)
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
En linje $n$ går gjennom to punkter $P(-2, 3)$ og $Q(4, -3)$.

Et punkt $R(0, 5)$ ligger utenfor linja.

Bestem koordinatene til punktet $R'$ som fås ved å speile $R$ om linja $n$.


::::{answer}
$$
R'(-4, 1)
$$
::::
:::::::::::::


::::::::::::::

:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 9
En sirkel har sentrum i $S(4, -2)$. En linje $\ell$ tangerer sirkelen i punktet $T(8, 2)$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem sirkelens radius.


::::{answer}
$$
r = 4\sqrt{2}
$$
::::
:::::::::::::



:::::::::::::{tab-item} b
En annen linje $m$ er parallell med $\ell$ og tangerer også sirkelen.

Bestem koordinatene til punktet $m$ tangerer sirkelen.

::::{answer}
$$
(0, -6)
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
En tredje linje $n$ står ortogonalt på $\ell$ og $m$. 

Bestem koordinatene til de to punktene der linja $n$ kan tangere sirkelen.


::::{answer}
$$
(0, 2) \qog (8, -6)
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::

---




:::::::::::::::{exercise} Oppgave 10

::::::::::::::{tab-set}
---
class: tabs-parts
---

:::::::::::::{tab-item} a
En linje $\ell$ går gjennom punktene $A(-2, 1)$ og $B(4, 3)$.

En sirkel har sentrum i $S(1, 0)$ og tangerer $\ell$. 

Bestem radiusen til sirkelen.


::::{answer}
$$
r = \dfrac{3 \sqrt{10}}{5}
$$
::::


:::::::::::::



:::::::::::::{tab-item} b
En linje $\ell$ går gjennom punktet $A(3, 2)$ og tangerer to sirkler i $B(7, 5)$ med radius $10$. 

Bestem koordinatene til sentrum i de to sirklene.


::::{answer}
$$
S_1(1, 13) \qog S_2(13, -3)
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
En sirkel har sentrum i $S(1, -1)$.

En linje $\ell$ skjærer sirkelen i punktene $A(-2, 1)$ og $B(4, 1)$.

To andre linjer er parallelle med $\ell$ og tangerer sirkelen.

Bestem koordinatene til punktene der linjene tangerer sirkelen.


::::{answer}
$$
(1, \sqrt{13} - 1) \qog (1, -\sqrt{13} - 1)
$$
::::
:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 11

:::{cas-popup}
---
layout: sidebar
---
:::


Tre punkter er gitt ved $A(0, 0)$, $B(9, 1)$ og $C(24, 10)$. En stråle $\ell$ er gitt ved 

$$
\ell: \begin{cases}
x = 12t \\
\\
y = 5t
\end{cases} \qfor t > 0.
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Vis at $C$ ligger på $\ell$.

:::::::::::::


:::::::::::::{tab-item} b
Bestem $\angle BAC$


::::{answer}
$$
\angle BAC = 155.38\degree
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Et annet punkt $D$ ligger på $\ell$ slik at $\angle ADB = 120\degree$.

Bestem koordinatene til $D$.


::::{answer}
$$
D\left(\dfrac{-132 \sqrt{3} + 1356}{169}, \dfrac{-55 \sqrt{3} + 565}{169}\right) \approx D(6.67, 2.78)
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
Et punkt $E$ ligger på $\ell$ slik at arealet av $\triangle ABE$ er $11$.

Bestem de eksakte koordinatene til $E$.


::::{answer}
$$
E\left(8, \dfrac{10}{3}\right).
$$
::::


:::::::::::::


::::::::::::::


:::::::::::::::




---


:::::::::::::::{exercise} Oppgave 12
Grafen til en funksjonen $f$ gitt ved $f(x) = \ln x$ er vist i figuren nedenfor.

Et punkt $B$ på grafen til $f$ er plassert slik at tangenten til grafen i punktet $B$ går gjennom $A(0, 0)$.

Punktet $C$ er plassert på linja $y = x$ slik at $\angle ACB = 90\degree$.



:::{plot}
width: 55%
xmin: -1
ymin: -1
xmax: 3.5
ymax: 3.5
figsize: (5, 5)
let: ds = 0.15
let: c = (exp(1) + 1) / 2
function: log(x + 1e-6), (0, 10), f, blue
point: (0, 0)
text: 0, 0, "$A$", top-left
point: (exp(1), 1)
text: exp(1), 1, "$B$", top-right
tangent: exp(1), f, solid, red
point: ((exp(1) + 1) / 2, (exp(1) + 1) / 2)
text: (exp(1) + 1) / 2, (exp(1) + 1) / 2, "$C$", top-left
line: 1, 0, dashed, gray
polygon: (0, 0), (exp(1), 1), ((exp(1) + 1) / 2, (exp(1) + 1) / 2)
fill-polygon: (0, 0), (exp(1), 1), ((exp(1) + 1) / 2, (exp(1) + 1) / 2)
line-segment: (c - ds, c - ds), (c, c - 2 * ds), solid, black
line-segment: (c, c - 2 * ds), (c + ds, c - ds), solid, black
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
&= \dfrac{e + 1}{2} \cdot ( -e + 1) = \dfrac{-(e^2 - 1)}{2}
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
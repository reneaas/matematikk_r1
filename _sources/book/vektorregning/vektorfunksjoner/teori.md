# Vektorfunksjoner


## Kurver og partikkelbevegelse

Den vanligste naturvitenskapelige anvendelsen av vektorfunksjoner er å beskrive posisjonen, farten og akselerasjonen til en partikkel over tid. En partikkel her er et generelt ord for en gjenstand som beveger seg. Det kan for eksempel være et elektron, en bil, et fly, en måne, en sol eller en galakse – til og med Usain Bolt som løper 100 m. Begrepet er ganske bredt!

Når vi sporer bevegelsen til en partikkel, kan partikkelen følge en ganske komplisert **kurve** som ikke lar seg beskrive av en vanlig funksjon. For å beskrive kurven partikkelen beveger seg på kan vi i stedet bruke en **vektorfunksjon**. En vektorfunksjon er en funksjon som sporer posisjonsvektoren til en partikkel. I naturvitenskapen vil dette ofte være over tid $t$.

Nedenfor vises noen interaktive grafer som sporer en "partikkel" (et punkt) som følger en kurve over tid i planet. De viser et lite utvalg av hvor forskjellig og kompliserte kurver kan være, som likevel være mulig å beskrive med matematikk. De gir håp for at det er mulig å beskrive komplekse fenomener i naturen som beveger seg på svært kompliserte måter. 

::::{multi-plot2}
---
rows: 2
cols: 2
---
:::{interactive-graph} 
parallel: true
figsize: (6, 6)
interactive-var: t, 0, 18 * pi, 1028
interactive-var-start: 0
curve: t * cos(t), t * sin(t), (0, t), blue
point: (t * cos(t), t * sin(t))
xmin: -60
xmax: 60
ymin: -60
ymax: 60
ticks: off
fontsize: 30
:::

:::{interactive-graph} 
parallel: true
figsize: (6, 6)
interactive-var: t, 0, 4 * pi, 1028
interactive-var-start: 0
curve: 16 * sin(t)**3, 13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t), (0, t), red
point: (16 * sin(t)**3, 13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t))
xmin: -30
xmax: 30
ymin: -20
ymax: 20
ticks: off
fontsize: 30
:::

:::{interactive-graph} 
parallel: true
interactive-var: t, 0, 18 * pi, 1028
interactive-var-start: 0
curve: 2 * (t - sin(t)), 2 * exp(-0.05 * t) *  (1 - cos(t)), (0, t), blue
point: (2 * (t - sin(t)), 2 * exp(-0.05 * t) *  (1 - cos(t)))
xmin: -1
xmax: 120
ymin: -1
ymax: 5
ticks: off
fontsize: 30
:::

:::{interactive-graph} 
interactive-var: t, 0, 20 * pi, 512
interactive-var-start: 0
curve: sin(t) * (exp(cos(t)) - 2 * cos(4 * t) - sin(t/12)**5), cos(t) * (exp(cos(t)) - 2 * cos(4 * t) - sin(t/12)**5), (0, t), red
point: (sin(t) * (exp(cos(t)) - 2 * cos(4 * t) - sin(t/12)**5), cos(t) * (exp(cos(t)) - 2 * cos(4 * t) - sin(t/12)**5))
xmin: -4
xmax: 4
ymin: -4
ymax: 4
ticks: off
fontsize: 30
:::
::::



---


Som de interaktive figurene ovenfor viser, kan vi beskrive ganske varierte bevegelser med matematikk når vi bruker vektorfunksjoner. Vi skal bruke resten av dette kapittelet på å se på hvordan det er mulig. 


## Posisjonsvektorer
Vi tenker oss at en partikkel beveger seg i planet. Dersom vi sporer alle punktene partikkelen er innom i løpet av et tidsintervall, så får vi en **kurve** $C$. 

**Posisjonsvektoren** $\vec{r}(t)$ over tid vil fortelle oss *hvor* på kurven partikkelen befinner seg på et tidspunkt $t$. Denne vektoren peker fra origo ut til punktet på kurven der partikkelen er på det tidspunktet. 

I de interaktive figurene nedenfor kan du se hvordan posisjonsvektoren $\vec{r}(t)$ endrer seg mens vi sporer posisjonen til en partikkel over tid på to forskjellige kurver.


::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{interactive-graph} 
parallel: true
width: 100%
interactive-var: t, 0, 2 * pi, 256
interactive-var-start: 0
curve: t**2 * cos(3*t), 4 * sin(2*t), (0, t), blue
point: (t**2 * cos(3*t), 4 * sin(2*t))
vector: (0, 0), (t**2 * cos(3*t), 4 * sin(2*t)), red
ticks: off
xmin: -40
xmax: 60
ymin: -6
ymax: 6
fontsize: 30
:::

:::{interactive-graph} 
parallel: true
width: 100%
interactive-var: t, 0, 2*pi, 512
interactive-var-start: 0
curve: cos(2*t) * cos(t), cos(2*t) * sin(t), (0, t), blue
point: (cos(2*t) * cos(t), cos(2*t) * sin(t))
vector: (0, 0), (cos(2*t) * cos(t), cos(2*t) * sin(t)), red
ticks: off
xmin: -1.5
xmax: 1.5
ymin: -1.2
ymax: 1.2
fontsize: 30
:::

::::





:::::::::::::::{summary} Posisjonsvektorer
Bevegelsen til en partikkel på en kurve $C$ kan beskrives med en posisjonsvektor $\vec{r}(t)$ som forteller oss *hvor* på kurven partikkelen er på et tidspunkt $t$. Posisjonsvektoren peker fra origo ut til punktet på kurven der partikkelen er på det tidspunktet. 

På komponentform, kan vi skrive 

$$
\vec{r}(t) = [x(t), y(t)]
$$

der $x(t)$ gir oss $x$-koordinaten til partikkelen på tidspunkt $t$, og $y(t)$ gir oss $y$-koordinaten til partikkelen på tidspunkt $t$.
:::::::::::::::


## Fartsvektorer og banefart
Når en partikkel er i en posisjon $\vec{r}(t)$ på en kurve $C$, så har partikkelen en **fartsvektor** $\vec{v}(t)$ som forteller oss *hvor fort* og i *hvilken retning* partikkelen beveger seg på et tidspunkt $t$. Fartsvektoren er alltid en tangent til kurven i punktet partikkelen befinner seg. Lengden til vektoren forteller oss hvor raskt partikkelen beveger seg i retningen.

Et tidspunkt $\Delta t$ senere så vil partikkelen være i en ny posisjon $\vec{r}(t + \Delta t)$ på kurven. Fartsvektoren $\vec{v}(t)$ er da definert som:

$$
\vec{v}(t) = \lim_{\Delta t \to 0} \dfrac{\vec{r}(t + \Delta t) - \vec{r}(t)}{\Delta t} = \vec{r}'(t)
$$

På komponentform betyr dette at 

$$
\vec{v}(t) = [x'(t), y'(t)]
$$


**Banefarten** $v(t)$, eller bare **farten**, til partikkelen er lengden til fartsvektoren, 

$$
v(t) = |\vec{v}(t)|
$$

Denne forteller oss hvor fort partikkelen beveger seg på et tidspunkt $t$.


Se den interaktive figuren nedenfor.

::::{multi-plot2}
---
rows: 1
cols: 2
---
:::{interactive-graph} 
parallel: true
width: 100%
interactive-var: t, 0, 2 * pi, 256
interactive-var-start: 0
let: n = 10
curve: t**2 * cos(3*t), 4 * sin(2*t), (0, 2*pi), blue
point: (t**2 * cos(3*t), 4 * sin(2*t))
vector: (t**2 * cos(3*t), 4 * sin(2*t)), (t**2 * cos(3*t) + (2 * t * cos(3 * t) - 3 * t**2 * sin(3 * t)) / 3, 4 * sin(2*t) + 8 * cos(2 * t) / 3), red
ticks: off
xmin: -40
xmax: 60
ymin: -6
ymax: 6
fontsize: 30
:::

:::{interactive-graph} 
parallel: true
width: 100%
interactive-var: t, 0, 2*pi, 512
interactive-var-start: 0
curve: cos(2*t) * cos(t), cos(2*t) * sin(t), (0, 2*pi), blue
point: (cos(2*t) * cos(t), cos(2*t) * sin(t))
vector: (cos(2*t) * cos(t),  cos(2*t) * sin(t)), (cos(2*t) * cos(t) + (-2*cos(t) * sin(2*t) - cos(2*t)*sin(t))/2, cos(2*t) * sin(t) + (cos(t)*cos(2*t) - 2*sin(t)*sin(2*t))/2), red
ticks: off
xmin: -1.8
xmax: 1.8
ymin: -1.6
ymax: 1.6
fontsize: 30
:::
::::



## Akselerasjonsvektorer og baneakselerasjon
**Akselerasjonsvektoren** $\vec{a}(t)$ til en partikkel forteller oss både i hvilke retningen vi fartsvektoren vil endre seg, og hvor mye lengden til fartsvektoren vil endre seg på et tidspunkt $t$. Akselerasjonsvektoren er definert som:

$$
\vec{a}(t) = \lim_{\Delta t \to 0} \dfrac{\vec{v}(t + \Delta t) - \vec{v}(t)}{\Delta t} = \vec{v}'(t) = \vec{r}''(t)
$$

På komponentform betyr dette at

$$
\vec{a}(t) = [v_x'(t), v_y'(t)] = [x''(t), y''(t)]
$$

Vi kan også definere **baneakselerasjonen** $a(t)$, eller bare **akselerasjonen**, til å være den deriverte av banefarten:

$$
a(t) = v'(t)
$$

Det betyr at akselerasjonen forteller oss hvor mye farten til partikkelen endrer seg på et tidspunkt $t$.




## Oversikt over størrelser for partikkelbevegelse

:::::::::::::::{summary} Parameterframstillinger av kurver
For partikkel som følger en kurve $C$, så har partikkelen følgende egenskaper:


:::{table}
labels: Størrelse, Symbol, Beskrivelse
Posisjonsvektor, $\vec{r}(t)$, Forteller oss hvor på kurven partikkelen er på et tidspunkt $t$.
Fartsvektor, $\vec{v}(t)$, Forteller oss hvor fort og i hvilken retning partikkelen beveger seg på et tidspunkt $t$. Fartsvektoren er $\vec{v}(t) = \vec{r}'(t)$.
(Bane)fart, $v(t)$, Forteller oss hvor fort partikkelen beveger seg på et tidspunkt $t$. Farten er $v(t) = |\vec{v}(t)|$.
Akselerasjonsvektor, $\vec{a}(t)$, Forteller oss hvor fort og i hvilken retning partikkelen akselererer på et tidspunkt $t$. Akselerasjonsvektoren er $$\vec{a}(t) = \vec{v}'(t) = \vec{r}''(t)$$
(Bane)akselerasjon, $a(t)$, Forteller oss hvor fort partikkelen akselererer på et tidspunkt $t$. Bane akselerasjonen er $$a(t) = v'(t)$$
:::

:::::::::::::::



## Vektorfunksjoner for rette linjer
La oss forestille oss at en partikkel beveger seg med konstant fart $v$ langs en rett linje. Dersom dette er langs $x$-aksen, kunne vi beskrevet posisjonen $s$ på $x$-aksen til partikkelen på et tidspunkt $t$ som

$$
s(t) = s_0 + v \cdot t
$$

der $s_0$ er startposisjonen til partikkelen på $x$-aksen.


Dersom partikkelen beveger seg langs en rett linje i planet med en konstant fartsvektor $\vec{v}$, så kan posisjonsvektoren til partikkelen uttrykkes som 

$$
\vec{r}(t) = \vec{r}_0 + \vec{v} \cdot t
$$

der $\vec{r}_0 = \lvec{OA}$ er startposisjonen. 

I den interaktive figuren nedenfor viser vi et eksempel på en partikkel som starter i et punkt $A$ og beveger seg med en konstant fartsvektor $\vec{v}$ langs en rett linje. Den røde vektoren viser posisjonsvektoren $\vec{r}(t)$, og den grønne vektoren viser fartsvektoren $\vec{v}$, og punktet vises posisjonen til partikkelen på kurven (den blå rette linjen) på et tidspunkt $t$.

:::{interactive-graph} 
parallel: true
width: 70%
interactive-var: t, 0, 6, 512
interactive-var-start: 0
curve: -8 + 3*t, 3 + t, (0, t), blue
point: (-8 + 3*t, 3 + t)
vector: (0, 0), (-8 + 3*t, 3 + t), red
vector: (-8 + 3*t, 3 + t), (-8 + 3*t + 3, 3 + t + 1), teal
point: (-8, 3)
text: -8, 3, "$A$", top-left
ticks: off
xmin: -15
xmax: 15
ymin: -1
ymax: 15
fontsize: 26
:::


:::::::::::::::{summary} Vektorfunksjoner for rette linjer
En partikkel som beveger seg langs en rett linje i planet med en konstant fartsvektor $\vec{v}$, kan beskrives med en posisjonsvektor $\vec{r}(t)$ som uttrykkes som

$$
\vec{r}(t) = \vec{r}_0 + \vec{v} \cdot t
$$

der $\vec{r}_0 = \lvec{OA}$ er startposisjonen.

:::::::::::::::
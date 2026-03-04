# Vektorregning


:::{goals} Læringsmål
* Kunne bestemme vektorer og vektorer mellom punkter med CAS.
* Kunne bestemme lengden av en vektor med CAS.
* Kunne regne ut skalarproduktet mellom vektorer med CAS.
* Kunne bestemme vinkelen mellom to vektorer med CAS.
:::

## Vektorer 

:::::::::::::::{example} Eksempel 1
I gif-en nedenfor vises hvordan man
1. definerer en vektor $\vec{u}$ direkte.
2. definerer en vektor $\lvec{AB}$ mellom to punkter $A$ og $B$.


:::{figure} ./videoer/eksempel/1/definere_vektorer.webp
---
class: no-click, adaptive-figure
width: 70%
---
:::

> Når vi skriver liten bokstav for navnet på vektoren, så får vi en søylevektor $\mqty(3 \\ 2)$. Når vi gir vektoren et navn med store bokstaver, så får vi et punkt $(5, 3)$. Men dette er bare en visuell sak og regningen vil fungere likt uansett. Under overflaten behandler Geogebra de to likt.

:::::::::::::::



---


:::::::::::::::{exercise} Underveisoppgave 1

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

Bestem vektoren mellom punktene $A(1, 2)$ og $B(4, 6)$.


:::::::::::::


:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::


Bestem vektoren mellom punktene $P(2, 3)$ og $Q(5, 1)$.



:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::


Bestem vektoren mellom punktene $M(1, 4)$ og $N(3, 2)$.
:::::::::::::


::::::::::::::


:::::::::::::::


## Lengden av vektorer

:::::::::::::::{example} Eksempel 2
For å regne ut lengden av en vektor $\vec{a}$, kan vi enten skrive `|a|` eller `lengde(a)` i CAS. I gif-en nedenfor viser vi hvordan:


:::{figure} ./videoer/eksempel/2/lengde.webp
---
class: no-click, adaptive-figure
width: 70%
---
:::



:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 2
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


Bestem lengden av vektorene 

$$
\vec{a} = [3, 5] \qog \vec{b} = [-1, 3] \qog \vec{c} = [2, -7]
$$

:::::::::::::


:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::


Bestem avstanden mellom punktene $A(-3, 4)$ og $B(2, -1)$.



:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::


Bestem omkretsen av trekanten $\triangle PQR$ som har hjørnene

$$
P(1, 2), \qog Q(4, 6) \qog R(5, 3)
$$
:::::::::::::


::::::::::::::
:::::::::::::::



## Skalarproduktet

:::::::::::::::{example} Eksempel 3
Vi regner ut skalarproduktet mellom to vektorer $\vec{a}$ og $\vec{b}$ ved å skrive `a * b` i CAS. I gif-en nedenfor viser vi hvordan:


:::{figure} ./videoer/eksempel/3/skalarprodukt.webp
---
class: no-click, adaptive-figure
width: 70%
---
:::


:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 3
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


To vektorer er gitt ved 

$$
\vec{a} = [3, 5] \qog \vec{b} = [-1, 3]
$$

Regn ut $\vec{a} \cdot \vec{b}$.
:::::::::::::


:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::

To vektorer er gitt ved

$$
\vec{u} = [2, -1] \qog \vec{v} = [4, 3]
$$

Regn ut $\vec{u} \cdot \vec{v}$.
:::::::::::::



:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

To vektorer er gitt ved

$$
\vec{p} = [1, 2] \qog \vec{q} = [5, 4]
$$

Regn ut $\vec{p} \cdot \vec{q}$.
:::::::::::::

::::::::::::::
:::::::::::::::




## Vinkelen mellom vektorer 

:::::::::::::::{example} Eksempel 4 
For å finne vinkelen mellom to vektorer $\vec{a}$ og $\vec{b}$, bruker vi den geometriske formelen for skalarproduktet:


$$
\vec{a} \cdot \vec{b} = \abs{\vec{a}} \cdot \abs{\vec{b}} \cdot \cos(x\degree)
$$

og så løser vi likningen for $x$. I gif-en nedenfor viser vi hvordan:


:::{figure} ./videoer/eksempel/4/vinkel.webp
---
class: no-click, adaptive-figure
width: 70%
---
:::

> 1. Vi passer på å avgrense vinkelen $x \in [0, 180]$. 
> 2. Vi må skrive $\cos (x\degree)$ slik at $x$ blir i grader. 


:::::::::::::::



---


:::::::::::::::{exercise} Underveisoppgave 4
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


Bestem vinkelen mellom vektorene


$$
\vec{a} = [3, 5] \qog \vec{b} = [-1, 3]
$$





:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::



Bestem vinkelen mellom vektorene

$$
\vec{u} = [2, -1] \qog \vec{v] = [4, 3]
$$



:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

Bestem vinkelen mellom vektorene

$$
\vec{p} = [1, 2] \qog \vec{q] = [5, 4]
$$


:::::::::::::



::::::::::::::

:::::::::::::::

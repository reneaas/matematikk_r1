# Løsning med digitale verktøy


:::::::::::::::{exercise} Oppgave 1
I gif-en nedenfor vises hvordan vi kan løse en logaritmelikning med CAS i GeoGebra. Vi bruker {ggb-icon}`mode_solve` for å løse likningen **eksakt**.

:::{figure} ./videoer/lg_likning.webp
---
class: no-click, adaptive-figure
width: 80%
---
:::


Løs likningene nedenfor med CAS.

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


$$
\lg(x) + \lg(x - 3) = 1
$$
:::::::::::::


:::::::::::::{tab-item} b

:::{cas-popup}
---
layout: sidebar
---
:::


$$
\lg(x + 2) - \lg(x - 2) = 2
$$
:::::::::::::


:::::::::::::{tab-item} c

> For å bruke den naturlige logaritmen, skriver vi bare `ln(x)` i stedet for `lg(x)` i CAS. 

<br>

:::{cas-popup}
---
layout: sidebar
---
:::


$$
\ln(x^2 + 1) - \ln(x + 3) = 0
$$


:::::::::::::


:::::::::::::{tab-item} d
:::{cas-popup}
---
layout: sidebar
---
:::

$$
(\ln x)^2 - 3\ln x + 2 = 0
$$


:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2
Mange likninger kan *ikke* løses eksakt fordi det er umulig å få $x$ alene. Bruker vi {ggb-icon}`mode_solve` får vi bare `{?}` som utskrift fordi det går ikke løse den eksakt.

Da må i stedet løse likningen **numerisk** – da finner vi bare en tilnærmet tallverdi for løsningen av likningen. Det kan vi gjøre ved å bruke {ggb-icon}`mode_nsolve` i CAS. 

Se gif-en nedenfor.

:::{figure} ./videoer/numerisk_1.webp
---
class: no-click, adaptive-figure
width: 80%
---
:::


Løs likningene nedenfor numerisk med CAS.


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


$$
x \ln x - 2 = 0
$$

:::::::::::::



:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::

$$
x^2 \ln x - 3\cdot (\ln x)^2 = 10
$$

:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

$$
(\ln x)^2 + \ln(x - 1) = 1
$$

:::::::::::::



::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
Vi må være litt forsiktige når vi løser likninger numerisk, for det er mulig å miste løsninger dersom vi ikke er oppmerksomme på hvordan vi gjør det. 

I gif-en nedenfor løser vi likningen ved å først bruke {ggb-icon}`mode_nsolve` direkte uten å "registrere" likningen først. Da får vi bare én løsning. Hvis vi derimot registrerer den først og deretter bruker {ggb-icon}`mode_nsolve`, får vi alle løsningene.

:::{figure} ./videoer/numerisk_2.webp
---
class: no-click, adaptive-figure
width: 80%
---
:::


Løs likningene nedenfor numerisk med CAS.


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

$$
x^2 \ln \dfrac{1}{x^2} + x^2 - \dfrac{1}{2x} = 0
$$

:::::::::::::



:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::

$$
x^2 \ln x - 2^x = 0
$$

:::::::::::::



:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::

$$
(x^2 - 2) \ln x = 4
$$

:::::::::::::


::::::::::::::









:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
En annen vanlig skrivemåte for $e^x$ i matematikken er $e^x = \exp (x)$. I CAS, så må vi bruke denne skrivemåten for å bruke $e^x$. Se gif-en nedenfor for et eksempel:


:::{figure} ./videoer/exp_1.webp
---
class: no-click, adaptive-figure
width: 80%
---
:::


Løs likningene nedenfor eksakt.


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


$$
e^x - 2 = 0
$$
:::::::::::::



:::::::::::::{tab-item} b
:::{cas-popup}
---
layout: sidebar
---
:::



$$
e^{2x} - e^x - 2 = 0
$$
:::::::::::::


:::::::::::::{tab-item} c
:::{cas-popup}
---
layout: sidebar
---
:::


$$
e^x + 3e^{-x} = 4
$$


:::::::::::::


::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 5
Ifølge Newtons avkjølingslov vil temperaturen $T$ til en gjenstand etter $t$ minutter være gitt ved 

$$
\ln (T - T_0) = -k\cdot t + r
$$

der $k$ og $t$ er konstander og $T_0$ er romtemperaturen.


I et rom er temperaturen $22 \, \degree \mathrm{C}$. Vi setter en kopp med kaffe som har temperaturen $82 \, \degree \mathrm{C}$ inn i rommet. Etter $2$ minutter er temperaturen på kaffen $66 \, \degree \mathrm{C}$.


Hvor lang tid tar det før kaffen har en temperatur som er mindre enn $40 \, \degree \mathrm{C}$?


:::{cas-popup}
:::




:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6
**Momentmagnitudeskalaen** (ruller ikke av tunga for å si det sånn!) er en skala for å måle størrelsen på jordskjelv. 

Sammenhengen mellom momentmagnituden $M$ og energien $E$ som frigjøres ved et jordskjelv er gitt ved 

$$
M = \dfrac{2}{3} \lg E - 3.2
$$


**Energien** $E$ måles med enheten Joule, J. 


:::{cas-popup}
---
layout: sidebar
---
:::


:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem et uttrykk for energien $E$ som løses ut i et jordskjelv. 


:::::::::::::

:::::::::::::{tab-item} b
Bestem hvor mye energi som utløses når et jordskjelv måles til å ha $4.7$ på momentmagnitudeskalaen.



:::::::::::::


:::::::::::::{tab-item} c
Hvor mange ganger så stor er energien som frigjøres av et jordskjelv dersom $M$ øker med $1$?


:::::::::::::

::::::::::::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 7
Sammenhengen mellom lydstyrken $L$ (målt i desibel, dB) og lydintensiteten $I$ (målt i watt per kvadratmeter, $\mathrm{W/m^2}$) er gitt ved

$$
L = 120 + 10 \lg I
$$

Menneskets øre har en smertegrense for lydstyrke som ligger omkring 130 dB.


:::{cas-popup}
---
layout: sidebar
---
:::

:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem lydintensiteten når lydstyrken er $130$ dB.


:::::::::::::


:::::::::::::{tab-item} b
Hvor mange prosent øker lydintensiteten når lydstyrken øker med 2 dB?


:::::::::::::


:::::::::::::{tab-item} c
Dersom effekten til lyden som sendes ut fra en lydkilde er $E$, vil lydintensiteten $I$ avta med kvadratet av avstanden $r$ fra lydkilden, altså

$$
I = \dfrac{E}{4\pi r^2}
$$

Lydstyrken fra et fly er 140 dB dersom du er 50 m fra flyet.

Bestem den minste avstanden til dette flyet der lydstyrken er lavere enn smertegrensen for mennesker.

:::::::::::::




::::::::::::::


:::::::::::::::
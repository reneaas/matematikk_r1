# Sirkler


## Sirkellikningen

En sirkel er en kurve med et punkt $S$ som kalles for **sentrum** og en **radius** $r$ som er avstanden ut til alle punktene som ligger på kurven. 

:::{plot}
width: 70%
fontsize: 25
curve: 5 + 3*cos(t), 4 + 3*sin(t), (0, 2*pi), solid, blue
nocache:
xmin: -1
ymin: -1
axis: equal
point: (5, 4)
text: 5, 4, "$S(x_0, y_0)$", bottom-right
point: (5 + 3*cos(pi/3), 4 + 3*sin(pi/3))
text: 5 + 3*cos(pi/3), 4 + 3*sin(pi/3), "$P(x, y)$", top-right
vector: (0, 0), (5, 4), red
text: 0.5 * 5, 0.5 * 4, "$\overrightarrow{OS}$", bottom-right
vector: (5, 4), (5 + 3*cos(pi/3), 4 + 3*sin(pi/3)), red
text: 0.5 * (5 + 5 + 3*cos(pi/3)), 0.5 * (4 + 4 + 3*sin(pi/3)), "$\overrightarrow{SP}$", bottom-right
vector: (0, 0), (5 + 3*cos(pi/3), 4 + 3*sin(pi/3)), red
text: 0.5 * (5 + 3*cos(pi/3)), 0.5 * (4 + 3*sin(pi/3)), "$\overrightarrow{OP}$", top-left
ticks: off
:::

Hvis vi lar sentrum i sirkelene være $S(x_0, y_0)$ og et punkt på sirkelen være $P(x, y)$, så skal avstanden mellom $S$ og $P$ være lik radiusen $r$. Det betyr at

$$
\abs{\overrightarrow{SP}} = r \limplies \abs{\lvec{SP}}^2 = r^2
$$

Men vi har også at

$$
\lvec{SP} = \lvec{OP} - \lvec{OS} = [x - x_0, y - y_0] \limplies \abs{\lvec{SP}}^2 = (x - x_0)^2 + (y - y_0)^2
$$

Altså får vi at alle punktene på sirkelen må tilfredsstille likningen

$$
(x - x_0)^2 + (y - y_0)^2 = r^2
$$

:::::::::::::::{summary} Sirkellikningen

:::{plot}
width: 100%
align: right
fontsize: 27
curve: 5 + 3*cos(t), 4 + 3*sin(t), (0, 2*pi), solid, blue
nocache:
xmin: -1
ymin: -1
axis: equal
point: (5, 4)
text: 5, 4, "$S(x_0, y_0)$", bottom-right
point: (5 + 3*cos(pi/3), 4 + 3*sin(pi/3))
text: 5 + 3*cos(pi/3), 4 + 3*sin(pi/3), "$P(x, y)$", top-right
line-segment: (5, 4), (5 + 3*cos(pi/3), 4 + 3*sin(pi/3)), dashed, red
text: 0.5 * (5 + 5 + 3*cos(pi/3)), 0.5 * (4 + 4 + 3*sin(pi/3)), "$r$", bottom-right
ticks: off
:::

Alle punkter $P(x, y)$ som ligger på en sirkel med sentrum i $S(x_0, y_0)$ og radius $r$ oppfyller likningen

$$
(x - x_0)^2 + (y - y_0)^2 = r^2
$$




:::::::::::::::


---


:::::::::::::::{example} Eksempel 1
En sirkel har sentrum i punktet $S(2, -1)$ og radius $4$. 

Bestem likningen til sirkelen.

::::{solution}
---
dropdown: 0
---

:::{plot}
width: 100%
align: right
fontsize: 28
curve: 2 + 4*cos(t), -1 + 4*sin(t), (0, 2*pi), solid, blue
ticks: off
point: (2, -1)
text: 2, -1, "$S(2, -1)$", bottom-right
point: (2 + 4*cos(pi/4), -1 + 4*sin(pi/4))
text: 2 + 4*cos(pi/4), -1 + 4*sin(pi/4), "$P(x, y)$", top-right
line-segment: (2, -1), (2 + 4*cos(pi/4), -1 + 4*sin(pi/4)), dashed, red
text: 0.5 * (2 + 2 + 4*cos(pi/4)), 0.5 * (-1 -1 + 4*sin(pi/4)), "$4$", top-left
axis: equal
:::

Vi bruker sirkellikningen 

$$
(x - x_0)^2 + (y - y_0)^2 = r^2
$$

der $S(x_0, y_0) = S(2, -1)$ og $r = 4$. Vi får da

$$
(x - 2)^2 + (y - (-1))^2 = 4^2 \\
\\
(x - 2)^2 + (y + 1)^2 = 16
$$

::::

:::::::::::::::


---

I noen tilfeller kan likningen til en sirkel være skrevet på en litt annen form, og da må vi omforme likningen så vi kan lese av sentrum og radius.

:::::::::::::::{example} Eksempel 2
En sirkel er gitt ved likningen

$$
x^2 - 2x + y^2 + 6y = -6
$$


Bestem sentrum og radius til sirkelen.


::::{solution}
---
dropdown: 0
---
Vi må fullføre kvadratene for både $x$ og $y$. Vi starter med $x$-leddene:

$$
x^2 - 2x = x^2 - 2x + 1 - 1 = (x - 1)^2 - 1
$$

For $y$-leddene gjør vi det samme:

$$
y^2 + 6y = y^2 + 6y + 9 - 9 = (y + 3)^2 - 9
$$

Setter vi dette inn i likningen får vi

$$
(x - 1)^2 - 1 + (y + 3)^2 - 9 = -6 \\
\\
(x - 1)^2 + (y + 3)^2 - 10 = -6 \\
\\
(x - 1)^2 + (y + 3)^2 = 4 \\
\\
(x - 1)^2 + (y - (-3))^2 = 2^2
$$


Altså har sirkelen sentrum i punktet $S(1, -3)$ og radius $r = 2$.

::::




:::::::::::::::


## Tangenter til sirkler

:::{plot}
width: 100%
align: right
fontsize: 30
curve: 5 + 3*cos(t), 4 + 3*sin(t), (0, 2*pi), solid, blue
nocache:
xmin: -1
ymin: -1
axis: equal
point: (5, 4)
text: 5, 4, "$S$", bottom-right
point: (5 + 3*cos(pi/3), 4 + 3*sin(pi/3))
text: 5 + 3*cos(pi/3), 4 + 3*sin(pi/3), "$P$", top-center
vector: (5, 4), (5 + 3*cos(pi/3), 4 + 3*sin(pi/3)), red
text: 0.5 * (5 + 5 + 3*cos(pi/3)), 0.5 * (4 + 4 + 3*sin(pi/3)), "$\overrightarrow{SP}$", top-left
ticks: off
curve: (3 * t * sqrt(3) + 13) / 2, (-3 * t + 3*sqrt(3) + 8) / 2, (-2, 2), solid, red
vector: (5 + 3*cos(pi/3), 4 + 3*sin(pi/3)), 3*sin(pi/3), -3*cos(pi/3), blue
text: 5 + 3*cos(pi/3) + 0.5 * 3*sin(pi/3), 4 + 3*sin(pi/3) + 0.5 * (-3*cos(pi/3)), "$\vec{v}$", top-right
:::



En tangent til en sirkel er en linje $\ell$ som berører sirkelen i et punkt $P~.$ Hvis vi lar $\lvec{SP}$ være vektoren fra sentrum $S$ ut til punktet $P$, så må tangenten ha en retningsvektor $\vec{v}$ som er ortogonal med $\lvec{SP}$. Altså må vi ha at

$$
\lvec{SP} \cdot \vec{v} = 0
$$

Vi er fri til å velge størrelsen på retningsvektoren, så det enkleste er å bruke tverrvektoren til $\lvec{SP}$ som retningsvektor for tangenten slik at $\vec{v} = \lvec{SP}_\perp$. Siden linja $\ell$ går gjennom punktet $P$, betyr det at tangenten kan beskrives som

$$
\vec{r}(t) = \lvec{OP} + \lvec{SP}_\perp \cdot t
$$



:::::::::::::::{summary} Tangent til en sirkel
En tangent $\ell$ i et punkt $P$ på en sirkel med sentrum $S$ er gitt ved

$$
\vec{r}(t) = \lvec{OP} + \lvec{SP}_\perp \cdot t
$$

der $\lvec{SP}_\perp$ er tverrvektoren til vektoren fra sentrum $S$ til punktet $P$.
:::::::::::::::


---


:::::::::::::::{example} Eksempel 3
En sirkel har sentrum i punktet $S(3, 2)$ og radius $4$.

En punkt $P$ på sirkelen har koordinatene $(\sqrt{3} + 3, 3)$.

Bestem likningen til tangenten til sirkelen i punktet $P$.


::::{solution}
---
dropdown: 0
---

::::


:::::::::::::::





## Normaler til sirkler


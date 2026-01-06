# Oppgaver: Vektorer i koordinatsystemet



:::::::::::::::{exercise} Oppgave 1


:::{plot}
align: right
width: 100%
point: (-2, 3)
text: -2, 3, "$A$", top-left
point: (3, 4)
text: 3, 4, "$B$", top-right
fontsize: 30
xmin: -4
xmax: 5
ymin: -1
vector: (0, 0), (-2, 3), red
vector: (0, 0), (3, 4), red
vector: (-2, 3), (3, 4), blue
text: 0.5 * 3, 0.5 * 4, "$\overrightarrow{OB}$", bottom-right
text: 0.5 * -2, 0.5 * 3, "$\overrightarrow{OA}$", bottom-left
text: 1, 3.5, "$\overrightarrow{AB}$", top-center
:::



I koordinatsystemet til høyre vises to punkter $A$ og $B$.

:::{clear}
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\lvec{OA}$ og $\lvec{OB}$.

::::{answer}
$$
\lvec{OA} = [-2, 3] \qog \lvec{OB} = [3, 4]
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $\lvec{AB}$ og $\lvec{BA}$.


::::{answer}
$$
\lvec{AB} = [5, 1] \qog \lvec{BA} = -\lvec{BA} = [-5, -1]
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Bestem avstanden mellom punktene $A$ og $B$.


::::{answer}
$$
\abs{\lvec{AB}} = \sqrt{26}
$$
::::


:::::::::::::


::::::::::::::
:::::::::::::::


:::::::::::::::{exercise} Oppgave 2
Gitt punktene $A(2, 3)$ og $B(-2, 2)$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\lvec{OA}$ og $\lvec{OB}$


::::{answer}
$$
\lvec{OA} = [2, 3] \qog \lvec{OB} = [-2, 2]
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $\lvec{AB}$ og $\lvec{BA}$


::::{answer}
$$
\lvec{AB} = [-4, -1] \qog \lvec{BA} = -\lvec{AB} = [4, 1]
$$
::::


:::::::::::::

:::::::::::::{tab-item} c
Bestem avstanden mellom punktene $A$ og $B$.


::::{answer}
$$
\abs{\lvec{AB}} = \sqrt{17}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
Sjekk ved regning at

$$
\lvec{OB} = \lvec{OA} + \lvec{AB}
$$
:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
En linje $\ell$ går gjennom punktet $A(2, -1)$ og har retningsvektoren $\vec{v} = [2, 3]$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem posisjonsvektoren $\vec{r}(t)$ for linja.


::::{answer}
$$
\vec{r}(t) = [2 + 2t, -1 + 3t]
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem koordinatene til punktet $B$ på linja gitt ved posisjonsvektoren $\lvec{OB} = \vec{r}(2)$.


::::{answer}
$$
\lvec{OB} = \vec{r}(2) = [6, 5]
$$

Så punktet $B$ har koordinatene $(6, 5)$.
::::


:::::::::::::


:::::::::::::{tab-item} c
Et annet punkt $C(0, -4)$ ligger på linja $\ell$.

Bestem hvilken verdi for $t$ som gir posisjonsvektoren til punktet $C$.


::::{answer}
$$
t = -1
$$
::::
:::::::::::::


:::::::::::::{tab-item} d
En annet punkt er gitt ved $D(3, 2)$.

Avgjør om punktet $D$ ligger på linja $\ell$.


::::{hints} Hvor starter jeg for å avgjøre dette?
Hvis punktet $D$ ligger på linja, så må det finnes én verdi for $t$ slik at

$$
\vec{r}(t) = \lvec{OD}
$$

Hvis du får mer enn én verdi for $t$ når du løser likningen, så ligger ikke punktet på linja.

::::

::::{answer}
Punktet ligger ikke på linja siden vi får at $t = \dfrac{1}{2}$ for at $x$-komponentene skal være like, og $t = 1$ for at $y$-kompontenene skal være like.
::::
::::


:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
En linje $\ell$ går gjennom punktene $A(-2, 3)$ og $B(1, -1)$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en retningsvektor for linja.


::::{answer}
$$
\vec{v} = \lvec{OB} - \lvec{OA} = [3, -4]
$$
::::
:::::::::::::


:::::::::::::{tab-item} b
Bestem en posisjonsvektor $\vec{r}(t)$. 


::::{answer}
$$
\vec{r}(t) = \lvec{OA} + \vec{v} \cdot t = [-2 + 3t, 3 - 4t]
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Avgjør om punktet $C(4, -5)$ ligger på linja $\ell$.

::::{answer}
Punktet ligger på linja siden $x$-kompontenene er like når $t = 2$ og $y$-kompontene er like når $t = 2$. 
::::

:::::::::::::

::::::::::::::
:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 5
En linje $\ell$ har likningen $y = x - 4$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en retningsvektor for $\ell$.

:::::::::::::


:::::::::::::{tab-item} b
Bestem en posisjonsvektor $\vec{r}(t)$ for linja.

:::::::::::::


:::::::::::::{tab-item} c
En annen linje $m$ er gitt ved 

$$
m: \begin{cases}
x = 2s + 1 \\
\\
y = -s + 2
\end{cases}
$$


Bestem koordinatene til skjæringspunktet mellom linjene $\ell$ og $m$.

:::::::::::::


::::::::::::::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 6
Et punkt er gitt ved $A(3, 2)$. To vektorer $\vec{u}$ og $\vec{v}$ er gitt ved

$$
\vec{u} = [4, 3] \qog \vec{v} = [2t, 5t]
$$

Et parallellogram $ABCD$ er bestemt ved at $\lvec{AB} = \vec{u}$ og $\lvec{AD} = \vec{v}$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til $B$.

Bestem koordinatene til $C$ og $D$ uttrykt ved $t$.
:::::::::::::


:::::::::::::{tab-item} b
Bestem $t$ slik at skjæringspunktet mellom diagonalene i parallellogrammet er $P(8, 11)$.
:::::::::::::


::::::::::::::


:::::::::::::::
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

::::{solution}
Posisjonsvektorene har de samme koordinatene som punktene har. Vi kan lese av fra figuren at punktene er gitt ved $A(-2, 3)$ og $B(3, 4)$.  Med andre ord er

$$
\lvec{OA} = [-2, 3] \qog \lvec{OB} = [3, 4]
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $\lvec{AB}$ og $\lvec{BA}$.


::::{answer}
$$
\lvec{AB} = [5, 1] \qog \lvec{BA} = -\lvec{AB} = [-5, -1]
$$
::::


::::{solution}
Vi har at $\lvec{OA} = [-2, 3]$ og $\lvec{OB} = [3, 4]$. Da er

$$
\lvec{AB} = \lvec{OB} - \lvec{OA} = [3 - (-2), 4 - 3] = [5, 1]
$$

og

$$
\lvec{BA} = \lvec{OA} - \lvec{OB} = [-2 - 3, 3 - 4] = [-5, -1]
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


::::{solution}
Vi har at $\lvec{AB} = [5, 1]$. Da er avstanden mellom punktene $A$ og $B$ gitt ved

$$
\abs{\lvec{AB}} = \sqrt{5^2 + 1^2} = \sqrt{26}
$$
::::

:::::::::::::


::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2

:::{plot}
width: 100%
align: right
point: (1, 4)
text: 1, 4, "$C$", top-right
point: (-4, -3)
text: -4, -3, "$A$", bottom-left
point: (4, 2)
text: 4, 2, "$B$", top-right
fontsize: 30
:::



Gitt punktene $A$, $B$ og $C$ i koordinatsystemet til høyre.


:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem posisjonsvektorene $\lvec{OA}$, $\lvec{OB}$ og $\lvec{OC}$.


::::{answer}
$$
\lvec{OA} = [-4, -3] \qog \lvec{OB} = [4, 2] \qog \lvec{OC} = [1, 4]
$$
::::

::::{solution}
Punktet $A$ har koordinatene $(-4, -3)$ som betyr at 

$$
\lvec{OA} = [-4, -3]
$$

Punktet $B$ har koordinatene $(4, 2)$ som betyr at

$$
\lvec{OB} = [4, 2]
$$

Punktet $C$ har koordinatene $(1, 4)$ som betyr at 

$$
\lvec{OC} = [1, 4]
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $\lvec{AB}$, $\lvec{AC}$ og $\lvec{BC}$.


::::{answer}
$$
\lvec{AB} = [8, 5] \qog \lvec{AC} = [5, 7] \qog \lvec{BC} = [-3, 2]
$$
::::


::::{solution}
Vi kan lese av fra figuren at $A(-4, -3)$ og $B(4, 2)$. Da har vi

$$
\lvec{AB} = \lvec{OB} - \lvec{OA} = [4, 2] - [-4, -3] = [4 - (-4), 2 - (-3)] = [8, 5]
$$

Vi kan også lese av fra figuren at $C(1, 4)$. Da har vi

$$
\lvec{AC} = \lvec{OC} - \lvec{OA} = [1, 4] - [-4, -3] = [1 - (-4), 4 - (-3)] = [5, 7]
$$


Vi kan finne $\lvec{BC}$ ved å bruke at

$$
\lvec{BC} = \lvec{AC} - \lvec{AB} = [5, 7] - [8, 5] = [5 - 8, 7 - 5] = [-3, 2]
$$

::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem omkretsen til trekanten $\triangle ABC$.


::::{answer}
$$
\mathcal{O} = \sqrt{89} + \sqrt{74} + \sqrt{13}
$$
::::

::::{solution}
Vi har at

$$
\begin{align*}
\abs{\lvec{AB}} &= \sqrt{8^2 + 5^2} = \sqrt{64 + 25} = \sqrt{89} \\
\\
\abs{\lvec{AC}} &= \sqrt{5^2 + 7^2} = \sqrt{25 + 49} = \sqrt{74} \\
\\
\abs{\lvec{BC}} &= \sqrt{(-3)^2 + 2^2} = \sqrt{9 + 4} = \sqrt{13}
\end{align*}
$$

Altså er omkretsen til trekanten gitt ved

$$
\mathcal{O} = \abs{\lvec{AB}} + \abs{\lvec{AC}} + \abs{\lvec{BC}} = \sqrt{89} + \sqrt{74} + \sqrt{13}
$$
::::


:::::::::::::





::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
Gitt punktene $A(2, 3)$ og $B(-2, 2)$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\lvec{OA}$ og $\lvec{OB}$.


::::{answer}
$$
\lvec{OA} = [2, 3] \qog \lvec{OB} = [-2, 2]
$$
::::

::::{solution}
Posisjonsvektorene til punktene vil ha samme vektorkoordinater som koordinatene til punktene i seg selv. Altså er:

$$
\lvec{OA} = [2, 3] \qog \lvec{OB} = [-2, 2]
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $\lvec{AB}$ og $\lvec{BA}$.


::::{answer}
$$
\lvec{AB} = [-4, -1] \qog \lvec{BA} = -\lvec{AB} = [4, 1]
$$
::::


::::{solution}
Vi har at $\lvec{OA} = [2, 3]$ og $\lvec{OB} = [-2, 2]$. Da er

$$
\lvec{AB} = \lvec{OB} - \lvec{OA} = [-2 - 2, 2 - 3] = [-4, -1]
$$

og

$$
\lvec{BA} = -\lvec{AB} = (-1) \cdot [-4, -1] = [4, 1]
$$
::::


:::::::::::::

:::::::::::::{tab-item} c
Bestem lengden av linjestykket $AB$.


::::{answer}
$$
\abs{\lvec{AB}} = \sqrt{17}
$$
::::

::::{solution}
Vi har allerede funnet at $\lvec{AB} = [-4, -1]$. Da er lengden av linjestykket $AB$ gitt ved

$$
\abs{\lvec{AB}} = \sqrt{(-4)^2 + (-1)^2} = \sqrt{17}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
Bestem koordinatene til midtpunktet $M$ på linjestykket $AB$.


::::{answer}
$M\left(0, \dfrac{5}{2}\right)$
::::


::::{solution}
Midtpunktet $M$ ligger midt mellom punktene $A(2, 3)$ og $B(-2, 2)$. Vi kan derfor finne dette punktet ved å først gå veien om $A$, deretter følger vi $\lvec{AB}$ halve veien. Posisjonsvektoren til punktet er derfor

$$
\begin{align*}
\lvec{OM} &= \lvec{OA} + \frac{1}{2} \cdot \lvec{AB} \\
\\
&= [2, 3] + \frac{1}{2} \cdot [-4, -1] \\
\\
&= [2, 3] + \left[-2, -\dfrac{1}{2}\right] \\
\\
&= \left[2 - 2, 3 - \dfrac{1}{2}\right] \\
\\
&= \left[0, \dfrac{5}{2}\right]
\end{align*}
$$

Altså er koordinatene til punktet $M\left(0, \dfrac{5}{2}\right)$.

::::

:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
Tre punkter er gitt ved $A(-2, 1)$, $B(1, 5)$ og $C(7, -3)$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\lvec{OA}$, $\lvec{OB}$ og $\lvec{OC}$.


::::{answer}
$$
\begin{align*}
\lvec{OA} &= [-2, 1] \\
\\
\lvec{OB} &= [1, 5] \\
\\
\lvec{OC} &= [7, -3]
\end{align*}
$$
::::


::::{solution}
Posisjonsvektorene til punktene vil ha samme vektorkoordinater som koordinatene til punktene i seg selv. Altså er:
 
$$
\begin{align*}
    \lvec{OA} &= [-2, 1] \\
    \\
    \lvec{OB} &= [1, 5] \\
    \\
    \lvec{OC} &= [7, -3]
\end{align*}
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $\lvec{AB}$, $\lvec{BC}$ og $\lvec{CA}$.


::::{answer}
$$
\begin{align*}
\lvec{AB} &= [3, 4] \\
\\
\lvec{BC} &= [6, -8] \\
\\
\lvec{CA} &= [-9, 4]
\end{align*}
$$
::::


::::{solution}
Vi har at $\lvec{OA} = [-2, 1]$, $\lvec{OB} = [1, 5]$ og $\lvec{OC} = [7, -3]$. Da er

$$
\begin{align*}
\lvec{AB} &= \lvec{OB} - \lvec{OA} = [1 - (-2), 5 - 1] = [3, 4] \\
\\ 
\lvec{BC} &= \lvec{OC} - \lvec{OB} = [7 - 1, -3 - 5] = [6, -8] \\
\\
\lvec{CA} &= \lvec{OA} - \lvec{OC} = [-2 - 7, 1 - (-3)] = [-9, 4]
\end{align*}
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Punktene $A$, $B$ og $C$ utgjør en trekant $\triangle ABC$.

Bestem hvilken sidelengde som er lengst i trekanten, og hvilken lengde denne sidelengden har.

::::{answer}
$$
|\lvec{BC}| = 10
$$
::::


::::{solution}
Vi regner ut lengden til hver av sidene i trekanten:

$$
\begin{align*}
\abs{\lvec{AB}} &= \sqrt{3^2 + 4^2} = \sqrt{25} = 5 \\
\\
\abs{\lvec{BC}} &= \sqrt{6^2 + (-8)^2} = \sqrt{36 + 64} = \sqrt{100} = 10 \\
\\
\abs{\lvec{CA}} &= \sqrt{(-9)^2 + 4^2} = \sqrt{81 + 16} = \sqrt{97}
\end{align*}
$$

Altså er $BC$ den lengste siden i trekanten med lengde $10$.
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5

:::{plot}
fontsize: 30
width: 100%
align: right
xmin: -1
xmax: 9
ymin: -1
ymax: 9
ticks: off
point: (1, 2)
text: 1, 2, "$A(1, 2)$", bottom-right
point: (5, 4)
text: 5, 4, "$B(5, 4)$", bottom-right
point: (7, 8)
text: 7, 8, "$C(7, 8)$", top-right
point: (3, 6)
text: 3, 6, "$D$", top-left
line-segment: (1, 2), (5, 4), dashed, gray
line-segment: (5, 4), (7, 8), dashed, gray
line-segment: (7, 8), (3, 6), dashed, gray
line-segment: (3, 6), (1, 2), dashed, gray
:::




Et parallellogram $ABCD$ har hjørnene

$$
A(1, 2), \, B(5, 4), \, C(7, 8) \qog D(a, b)
$$


:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til punktet $D$.



::::{hints} Hint: Hva er egentlig et parallellogram?
I et parallellogram så vil to og to sider være parallelle og like lange.
::::



::::{answer}
$$
D(3, 6)
$$
::::

::::{solution}
Sidene $AD$ og $BC$ er parallelle og like lange som betyr at 

$$
\begin{align*}
\lvec{AD} &= \lvec{BC} \\
\\
&= \lvec{OC} - \lvec{OB}
\\
\\&= [7, 8] - [5, 4] \\
\\
&= [2, 4]
\end{align*}
$$

For å finne koordinatene til punktet $D$, kan vi da gå veien om $A$ først og så følge vektoren $\lvec{AD}$:

$$
\begin{align*}
\lvec{OD} &= \lvec{OA} + \lvec{AD} \\
\\
&= [1, 2] + [2, 4] \\
\\
&= [3, 6]
\end{align*}
$$

Dermed er punktet $D$ gitt ved $D(3, 6)$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem koordinatene til skjæringspunktet $P$ mellom diagonalene $AC$ og $BD$. 


::::{hints} Hint
Når du deler opp parallellogrammet med diagonalene $AC$ og $BD$, hvor havner skjæringspunktet i forhold til $A$ og $C$, og $B$ og $D$? 
::::


::::{answer}
$$
P(4, 5)
$$
::::

::::{solution}

:::{plot}
fontsize: 30
width: 100%
align: right
xmin: -1
xmax: 9
ymin: -1
ymax: 9
ticks: off
point: (1, 2)
text: 1, 2, "$A(1, 2)$", bottom-right
point: (5, 4)
text: 5, 4, "$B(5, 4)$", bottom-right
point: (7, 8)
text: 7, 8, "$C(7, 8)$", top-right
point: (3, 6)
text: 3, 6, "$D$", top-left
line-segment: (1, 2), (5, 4), dashed, gray
line-segment: (5, 4), (7, 8), dashed, gray
line-segment: (7, 8), (3, 6), dashed, gray
line-segment: (3, 6), (1, 2), dashed, gray
line-segment: (1, 2), (7, 8), solid, blue
line-segment: (5, 4), (3, 6), solid, red
point: (4, 5)
text: 4, 5, "$P$", top-right
:::


Vi lager en hjelpefigur som vist til høyre.
Fordi linjestykkene $AC$ deler parallellogrammet i to like store trekanter, må skjæringspunktet $P$ ligge midt mellom $B$ og $D$, altså er det midtpunktet på linjestykket $BD$. Vi kan også snu dette rundt og si at $P$ er midtpunktet på linjestykket $AC$ fordi linjestykket $BD$ også deler parallellogrammet i to like store trekanter. 

Vi kan altså bestemme koordinatene til $P$ ved å først gå veien om punktet $A$, og så følge vektoren $\lvec{AC}$ halve veien. Vi har at

$$
\lvec{AC} = \lvec{OC} - \lvec{OA} = [7, 8] - [1, 2] = [6, 6]
$$

Altså er posisjonsvektoren til punktet $P$ gitt ved

$$
\begin{align*}
\lvec{OP} &= \lvec{OA} + \frac{1}{2} \cdot \lvec{AC} \\
\\
&= [1, 2] + \frac{1}{2} \cdot [6, 6] \\
\\
&= [1, 2] + [3, 3] \\
\\
&= [4, 5]
\end{align*}
$$

Altså er skjæringspunktet $P(4, 5)$.



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
En linje $\ell$ har et punkt $A(2, 0)$ som ligger på linja og en retningsvektor $\vec{v} = [1, 2]$.

Bestem posisjonsvektoren $\vec{r}(t)$ til punktene på linja.


::::{answer}
$$
\vec{r}(t) = [2 + t, 2t]
$$
::::


::::{solution}
Posisjonsvektorene til punktene på linja $\ell$ er generelt gitt ved 

$$
\vec{r}(t) = \lvec{OA} + \vec{v} \cdot t
$$

Vi har at 

$$
\lvec{OA} = [2, 0] \qog \vec{v} = [1, 2]
$$

Da får vi

$$
\vec{r}(t) = [2, 0] + [1, 2] \cdot t = [2 + 1 \cdot t, 0 + 2 \cdot t] = [2 + t, 2t]
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
En linje $m$ har et punkt $B(4, -3)$ som ligger på linja og en retningsvektor $\vec{v} = [-2, 1]$.

Bestem posisjonsvektoren $\vec{r}(t)$ til punktene på linja.

::::{answer}
$$
\vec{r}(t) = [4 - 2t, -3 + t]
$$
::::

::::{solution}
Posisjonsvektorene til punktene på linja $m$ er generelt gitt ved

$$
\vec{r}(t) = \lvec{OB} + \vec{v} \cdot t
$$

Vi har at

$$
\lvec{OB} = [4, -3] \qog \vec{v} = [-2, 1]
$$

Da får vi

$$
\vec{r}(t) = [4, -3] + [-2, 1] \cdot t = [4 - 2t, -3 + t]
$$
::::
:::::::::::::


:::::::::::::{tab-item} c
Punktene $A(2, -1)$ og $B(5, 3)$ ligger på en linje $n$.

Bestem en parameterframstilling $\vec{r}(t)$ for linja.


::::{answer}
$$
\vec{r}(t) = [2 + 3t, -1 + 4t]
$$
::::

::::{solution}
Vi har at

$$
\lvec{OA} = [2, -1] \qog \lvec{OB} = [5, 3]
$$

En retningsvektor for linja er da gitt ved 

$$
\vec{v} = \lvec{AB} = \lvec{OB} - \lvec{OA} = [5 - 2, 3 - (-1)] = [3, 4]
$$

Da er en posisjonsvektoren for punktene på linja gitt ved

$$
\begin{align*}
\vec{r}(t) &= \lvec{OA} + \vec{v} \cdot t \\
\\
&= [2, -1] + [3, 4] \cdot t \\
\\
&= [2 + 3t, -1 + 4t]
\end{align*}
$$ 
::::
:::::::::::::


:::::::::::::{tab-item} d
Punktene $C(-1, 4)$ og $D(3, -2)$ ligger på en linje $p$.

Bestem en parameterframstilling $\vec{r}(t)$ for linja.


::::{answer}
$$
\vec{r}(t) = [-1 + 4t, 4 - 6t]
$$
::::

::::{solution}
Vi har at

$$
\lvec{OC} = [-1, 4] \qog \lvec{OD} = [3, -2]
$$

En retningsvektor for linja er da gitt ved

$$
\vec{v} = \lvec{CD} = \lvec{OD} - \lvec{OC} = [3 - (-1), -2 - 4] = [4, -6]
$$

Da er en posisjonsvektoren for punktene på linja gitt ved

$$
\begin{align*}
\vec{r}(t) &= \lvec{OC} + \vec{v} \cdot t \\
\\
&= [-1, 4] + [4, -6] \cdot t \\
\\
&= [-1 + 4t, 4 - 6t]
\end{align*}
$$
::::


:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 7
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Punktet $A(1, 2)$ ligger på en linje $\ell$ som har stigningstall $-2$.

Bestem en parameterframstilling $\vec{r}(t)$ for linja.


::::{answer}
$$
\vec{r}(t) = [1 + t, 2 - 2t]
$$
::::

::::{solution}
En retningsvektor for en linje med stigningstall $a$ er $\vec{v} = [1, a]$. Dermed er en retningsvektor for linja $\ell$ gitt ved

$$
\vec{v} = [1, -2]
$$

Posisjonsvektoren til punktene på linja er da gitt ved

$$
\begin{align*}
\vec{r}(t) &= \lvec{OA} + \vec{v} \cdot t \\
\\
&= [1, 2] + [1, -2] \cdot t \\
\\
&= [1 + t, 2 - 2t]
\end{align*}
$$
::::
:::::::::::::


:::::::::::::{tab-item} b
Punktet $B(3, -1)$ ligger på en linje $m$ som har stigningstall $4$.

Bestem en parameterframstilling $\vec{r}(t)$ for linja.


::::{answer}
$$
\vec{r}(t) = [3 + t, -1 + 4t]
$$
::::

::::{solution}
En retningsvektor for en linje med stigningstall $a$ er $\vec{v} = [1, a]$. Dermed er en retningsvektor for linja $m$ gitt ved

$$
\vec{v} = [1, 4]
$$

Posisjonsvektoren til punktene på linja er da gitt ved

$$
\begin{align*}
\vec{r}(t) &= \lvec{OB} + \vec{v} \cdot t \\
\\
&= [3, -1] + [1, 4] \cdot t \\
\\
&= [3 + t, -1 + 4t]
\end{align*}
$$
::::


:::::::::::::



:::::::::::::{tab-item} c
En linje har likningen 

$$
y = 2x - 4
$$

Bestem en parameterframstilling $\vec{r}(t)$ for linja.

::::{answer}
$$
\vec{r}(t) = [t, -4 + 2t]
$$
::::

::::{solution}
Stigningstallet til linja er $2$ som betyr at en retningsvektor for linja er gitt ved

$$
\vec{v} = [1, 2]
$$

Et punkt på linja får vi ved å sette $x = 0$ i likningen til linja:

$$
y = 2 \cdot 0 - 4 = -4
$$

Dermed er $A(0, -4)$ et punkt på linja, og posisjonsvektoren til punktene på linja er da gitt ved

$$
\begin{align*}
\vec{r}(t) &= \lvec{OA} + \vec{v} \cdot t \\
\\
&= [0, -4] + [1, 2] \cdot t \\
\\
&= [0 + t, -4 + 2t] \\
\\
&= [t, -4 + 2t]
\end{align*}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
En linje har likningen

$$
y = -x + 3
$$

Bestem en parameterframstilling $\vec{r}(t)$ for linja.

::::{answer}
$$
\vec{r}(t) = [t, 3 - t]
$$
::::

::::{solution}
Stigningstallet til linja er $-1$ som betyr at en retningsvektor for linja er gitt ved

$$
\vec{v} = [1, -1]
$$

Et punkt på linja får vi ved å sette $x = 0$ i likningen til linja:

$$
y = -0 + 3 = 3
$$

Dermed er $A(0, 3)$ et punkt på linja, og posisjonsvektoren til punktene på linja er da gitt ved

$$
\begin{align*}
\vec{r}(t) &= \lvec{OA} + \vec{v} \cdot t \\
\\
&= [0, 3] + [1, -1] \cdot t \\
\\
&= [0 + t, 3 - t] \\
\\
&= [t, 3 - t]
\end{align*}
$$
::::
:::::::::::::

::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8
En linje $\ell$ er beskrevet av parameterframstillingen

$$
\vec{r}(t) = [1 + 2t, 3 - t]
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til skjæringspunktet mellom $\ell$ og $x$-aksen.


::::{answer}
$$
(7, 0)
$$
::::

::::{solution}
For å finne skjæringspunktet mellom linja og $x$-aksen, setter vi $y = 0$ i parameterframstillingen til linja:

$$
3 - t = 0 \liff t = 3
$$

Når vi setter inn $t = 3$ i parameterframstillingen, får vi:

$$
\vec{r}(3) = [1 + 2 \cdot 3, 3 - 3] = [7, 0]
$$

Altså er skjæringspunktet mellom linja og $x$-aksen i punktet $(7, 0)$.
::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem koordinatene til skjæringspunktet mellom $\ell$ og $y$-aksen.

::::{answer}
$$
\left(0, \dfrac{7}{2}\right)
$$
::::

::::{solution}
For å finne skjæringspunktet mellom linja og $y$-aksen, setter vi $x = 0$ i parameterframstillingen til linja:

$$
1 + 2t = 0 \liff t = -\dfrac{1}{2}
$$

Når vi setter inn $t = -\dfrac{1}{2}$ i parameterframstillingen, får vi:

$$
\vec{r}\left(-\dfrac{1}{2}\right) = \left[1 + 2 \cdot \left(-\dfrac{1}{2}\right), 3 - \left(-\dfrac{1}{2}\right)\right] = \left[0, \dfrac{7}{2}\right]
$$

Altså er skjæringspunktet mellom linja og $y$-aksen i punktet $\left(0, \dfrac{7}{2}\right)$.
::::
:::::::::::::


:::::::::::::{tab-item} c
Avgjør om punktet $A(5, -2)$ ligger på linja $\ell$.


::::{answer}
Punktet ligger **ikke** på linja.
::::

::::{solution}
For at punktet $A(5, -2)$ skal ligge på linja, må det finnes en verdi for $t$ slik at

$$
\vec{r}(t) = \lvec{OA}
$$

som vi kan skrive som

$$
[1 + 2t, 3 - t] = [5, -2]
$$

Her må $x$-komponentene og $y$-komponentene være like, så vi får to likninger:

$$
1 + 2t = 5 \and 3 - t = -2
$$

Vi løser den første likningen:

$$
1 + 2t = 5 \liff 2t = 4 \liff t = 2
$$

Så løser vi den andre likningen

$$
3 - t = -2 \liff -t = -5 \liff t = 5
$$

Vi får to forskjellige verdier for $t$ som betyr at $A(5, -2)$ **ikke** ligger på linja.
::::

:::::::::::::


::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 9
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


::::{solution}
Posisjonsvektorene til punktene på linja $\ell$ er generelt gitt ved

$$
\vec{r}(t) = \lvec{OA} + \vec{v} \cdot t
$$

Vi har at

$$
\lvec{OA} = [2, -1] \qog \vec{v} = [2, 3]
$$

Da får vi

$$
\vec{r}(t) = [2, -1] + [2, 3] \cdot t = [2 + 2t, -1 + 3t]
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

::::{solution}
Vi har at

$$
\vec{r}(t) = [2 + 2t, -1 + 3t]
$$

Når vi setter inn $t = 2$, får vi posisjonsvektoren til punktet $B$:

$$
\begin{align*}
\lvec{OB} = \vec{r}(2) &= [2 + 2 \cdot 2, -1 + 3 \cdot 2] \\
\\
&= [2 + 4, -1 + 6] \\
\\
&= [6, 5]
\end{align*}
$$
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


::::{solution}
For at punktet $C(0, -4)$ skal ligge på linja, må det finnes en verdi for $t$ slik at

$$
\vec{r}(t) = \lvec{OC}
$$

som vi kan skrive som

$$
[2 + 2t, -1 + 3t] = [0, -4]
$$

Her må $x$-komponentene og $y$-komponentene være like, så vi får to likninger som må være tilfredsstilt samtidig:

$$
2 + 2t = 0 \and -1 + 3t = -4
$$

Vi løser den første likningen:

$$
2 + 2t = 0 \liff 2t = -2 \liff t = -1
$$

Så løser vi den andre likningen:

$$
-1 + 3t = -4 \liff 3t = -3 \liff t = -1
$$

Vi får $t = -1$ for begge likninger, som betyr at posisjonsvektoren til $C(0, -4)$ er 

$$
\vec{r}(-1) = [0, -4]
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
En annet punkt er gitt ved $D(3, 2)$.

Avgjør om punktet $D$ ligger på linja $\ell$.

::::{answer}
Punktet ligger ikke på linja siden vi får at $t = \dfrac{1}{2}$ for at $x$-komponentene skal være like, og $t = 1$ for at $y$-komponentene skal være like.
::::


::::{solution}
For at punktet $D(3, 2)$ skal ligge på linja, må det finnes en verdi for $t$ slik at

$$
\vec{r}(t) = \lvec{OD}
$$

som vi kan skrive som

$$
[2 + 2t, -1 + 3t] = [3, 2]
$$

Her må $x$-komponentene og $y$-komponentene være like, så vi får to likninger som må være tilfredsstilt samtidig:

$$
2 + 2t = 3 \and -1 + 3t = 2
$$

Vi løser den første likningen:

$$
2 + 2t = 3 \liff 2t = 1 \liff t = \dfrac{1}{2}
$$

Så løser vi den andre likningen:

$$
-1 + 3t = 2 \liff 3t = 3 \liff t = 1
$$

Vi får to forskjellige verdier for $t$ som betyr at $D(3, 2)$ ikke ligger på linja.
::::


:::::::::::::


::::::::::::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 10
En linje $\ell$ er beskrevet av parameterframstillingen

$$
\ell: \begin{cases}
x = 3t + 1 \\
\\
y = -2t + 4
\end{cases}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem retningsvektoren til parameterframstillingen.

::::{answer}
$$
\vec{v} = [3, -2]
$$
::::

::::{solution}
Retningsvektoren til parameterframstillingen er gitt ved koeffisientene til $t$ i likningene for $x$ og $y$. Altså er retningsvektoren

$$
\vec{v} = [3, -2]
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem koordinatene til skjæringspunktene mellom $\ell$ og koordinataksene.

::::{answer}
* Linja skjærer $x$-aksen i $(7, 0)$
* Linja skjærer $y$-aksen i $\left(0, \dfrac{14}{3}\right)$
::::

::::{solution}
Vi har at $x(t) = 3t + 1$. Når linja $\ell$ skjærer $y$-aksen vil $x(t) = 0$: 

$$
x(t) = 0 \liff 3t + 1 = 0 \liff t = -\dfrac{1}{3}
$$

Vi har at $y(t) = -2t + 4$, så da blir $y$-koordinaten til skjæringspunktet

$$
y\left(-\dfrac{1}{3}\right) = -2 \cdot \left(-\dfrac{1}{3}\right) + 4 = \dfrac{2}{3} + 4 = \dfrac{14}{3}
$$

Altså skjærer linja $y$-aksen i $\left(0, \dfrac{14}{3}\right)$.

For å finne skjæringspunktet mellom linja og $x$-aksen, setter vi $y(t) = 0$:

$$
y(t) = 0 \liff -2t + 4 = 0 \liff -2t = -4 \liff t = 2
$$

Når vi setter inn $t = 2$ i $x(t)$, får vi:

$$
x(2) = 3 \cdot 2 + 1 = 6 + 1 = 7
$$

Altså skjærer linja $x$-aksen i punktet $(7, 0)$.
::::

:::::::::::::


::::::::::::::

:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 11
En linje $\ell$ har likningen $y = x - 4$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en retningsvektor for $\ell$.

::::{answer}
$$
\vec{v} = [1, 1]
$$
::::

::::{solution}
En retningsvektor for en linje med stigningstall $a$ er $\vec{v} = [1, a]$. Siden stigningstallet til linja er $1$, er en retningsvektor for linja gitt ved

$$
\vec{v} = [1, 1]
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem en posisjonsvektor $\vec{r}(t)$ for linja.


::::{answer}
$$
\vec{r}(t) = [t, -4 + t]
$$
::::

::::{solution}
En posisjonsvektor for punktene på linja er gitt ved

$$
\begin{align*}
\vec{r}(t) &= \lvec{OA} + \vec{v} \cdot t \\
\\
&= [0, -4] + [1, 1] \cdot t \\
\\
&= [t, -4 + t]
\end{align*}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
En annen linje $m$ er gitt ved 

$$
m: \begin{cases}
x = 2s + 1 \\
\\
y = -s + 3
\end{cases}
$$


Bestem koordinatene til skjæringspunktet mellom linjene $\ell$ og $m$.


::::{answer}
$$
(5, 1)
$$
::::

::::{solution}
Vi kaller posisjonsvektoren til $\ell$ for $\vec{r}_\ell(t)$ og posisjonsvektoren til $m$ for $\vec{r}_m(s)$. For å bestemme koordinagtene til skjæringspunktet mellom de to linjene, må vi finne verdier for $t$ og $s$ slik at

$$
\vec{r}_\ell(t) = \vec{r}_m(s)
$$

som vi kan skrive som

$$
[t, -4 + t] = [2s + 1, -s + 3]
$$

Her må $x$-komponentene og $y$-komponentene være like, så vi får to likninger som må være tilfredsstilt samtidig:

$$
t = 2s + 1 \and -4 + t = -s + 3
$$

Den første likningen er allerede løst for $t$, så vi setter inn dette i den andre likningen:

$$
-4 + (2s + 1) = -s + 3
$$

$$
-3 + 2s = -s + 3
$$

$$
3s = 6 \liff s = 2
$$

Når vi setter inn $s = 2$ i den første likningen, får vi:

$$
t = 2 \cdot 2 + 1 = 5
$$

Når vi setter inn $t = 5$ i posisjonsvektoren til linja $\ell$, får vi skjæringspunktet mellom de to linjene:

$$
\vec{r}_\ell(5) = [5, -4 + 5] = [5, 1]
$$

Altså er koordinatene til skjæringspunktet mellom linjene $\ell$ og $m$ gitt ved $(5, 1)$.
::::

:::::::::::::


::::::::::::::
:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 12
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
En linje $\ell$ går gjennom punktene $A(-6, 1)$ og $B(3, -2)$.

En annen linje $m$ er gitt ved parameterframstillingen

$$
m: \begin{cases}
x = 2s + 1 \\
\\
y = 3s - 5
\end{cases}
$$

Bestem koordinatene til skjæringspunktet mellom $\ell$ og $m$.

::::{answer}
$$
(3, -2)
$$
::::


::::{solution}
Vi starter med å finne en retningsvektor $\vec{v}_\ell$ for linja $\ell$. En retningsvektor for linja er gitt ved

$$
\vec{v}_\ell = \lvec{AB} = \lvec{OB} - \lvec{OA} = [3 - (-6), -2 - 1] = [9, -3]
$$

Et punkt på linja kan vi velge å være $A(-6, 1)$, og posisjonsvektoren til punktene på linja er da gitt ved

$$
\vec{r}_\ell(t) = \lvec{OA} + \vec{v}_\ell \cdot t = [-6, 1] + [9, -3] \cdot t = [-6 + 9t, 1 - 3t]
$$

For å finne skjæringspunktet mellom de to linjene, må vi finne verdier for $t$ og $s$ slik at

$$
\vec{r}_\ell(t) = \vec{r}_m(s)
$$

som vi kan skrive som

$$
[-6 + 9t, 1 - 3t] = [2s + 1, 3s - 5]
$$

Her må $x$-komponentene og $y$-komponentene være like, så vi får to likninger som må være tilfredsstilt samtidig:

$$
-6 + 9t = 2s + 1 \and 1 - 3t = 3s - 5
$$

Den første likningen kan vi skrive om til

$$
9t - 2s = 7 \liff 9t = 2s + 7 \liff t = \dfrac{2s + 7}{9}
$$

Deretter setter vi dette inn i den andre likningen:

$$
1 - 3\left(\dfrac{2s + 7}{9}\right) = 3s - 5
$$

$$
1 - \dfrac{2s + 7}{3} = 3s - 5
$$

Så ganger vi med $3$ på begge sider for å kvitte oss med brøken:

$$
3 - (2s + 7) = 9s - 15
$$

Så forenkler vi slik at vi får $s$ alene:

$$
-2s - 4 = 9s - 15
$$

$$
-4 + 15 = 9s + 2s
$$

$$
11 = 11s \liff s = 1
$$

Setter vi inn $s = 1$ i $\vec{r}_m(s)$ for å finne koordinatene til skjæringspunktet mellom de to linjene:

$$
\vec{r}_m(1) = [2 \cdot 1 + 1, 3 \cdot 1 - 5] = [3, -2]
$$

Altså skjærer linjene hverandre i punktet $(3, -2)$.
::::


:::::::::::::


:::::::::::::{tab-item} b
En linje $\ell$ har likningen $y = -2x + 4$.

Posisjonsvektoren til punktene på en annen linje $m$ er gitt ved 

$$
\vec{r}_m(s) = [1 + s, 1 - s]
$$

Bestem koordinatene til skjæringspunktet mellom $\ell$ og $m$.


::::{answer}
$$
(2, 0)
$$
::::

::::{solution}
Vi har at likningen til linja $\ell$ er

$$
y = -2x + 4
$$

Siden linja har stigningstall $-2$, kan vi skrive en retningsvektor for linja som

$$
\vec{v}_\ell = [1, -2]
$$

Vi kan finne et punkt $A$ på linja $\ell$ ved å sette $x = 0$ i likningen til linja:

$$
y = -2 \cdot 0 + 4 = 4
$$

Altså er $A(0, 4)$ et punkt på linja, og posisjonsvektoren til punktene på linja er da gitt ved

$$
\vec{r}_\ell(t) = \lvec{OA} + \vec{v}_\ell \cdot t = [0, 4] + [1, -2] \cdot t = [t, 4 - 2t]
$$

For å finne skjæringspunktet mellom de to linjene, må vi finne verdier for $t$ og $s$ slik at

$$
\vec{r}_\ell(t) = \vec{r}_m(s)
$$

som vi kan skrive som

$$
[t, 4 - 2t] = [1 + s, 1 - s]
$$

Her må $x$-komponentene og $y$-komponentene være like, så vi får to likninger som må være tilfredsstilt samtidig:

$$
t = 1 + s \and 4 - 2t = 1 - s
$$

Den første likningen er allerede løst for $t$, så vi setter inn dette i den andre likningen:

$$
4 - 2(1 + s) = 1 - s
$$

$$
4 - 2 - 2s = 1 - s
$$

$$
2 - 2s = 1 - s
$$

$$
-s = -1 \liff s = 1
$$

Vi setter inn $s = 1$ i $\vec{r}_m(s)$ for å finne koordinatene til skjæringspunktet mellom de to linjene:

$$
\vec{r}_m(1) = [1 + 1, 1 - 1] = [2, 0]
$$

Altså skjærer linjene hverandre i punktet $(2, 0)$.
::::
:::::::::::::


:::::::::::::{tab-item} c
En linje $\ell$ har stigningstall $2$ og har et punkt $A(0, 2)$ som ligger på linja.

En annen linje $m$ har stigningstall $-1$ og har et punkt $B(-1, 6)$ som ligger på linja.

Besten koordinatene til skjæringspunktet mellom linjene $\ell$ og $m$.


::::{answer}
$$
(1, 4)
$$
::::

::::{solution}
Linja $\ell$ har stigningstall $2$ som betyr at en retningsvektor for linja er 

$$
\vec{v}_\ell = [1, 2]
$$

Punktet $A(0, 2)$ ligger på linja, og posisjonsvektoren til punktene på linja er da gitt ved

$$
\vec{r}_\ell(t) = \lvec{OA} + \vec{v}_\ell \cdot t = [0, 2] + [1, 2] \cdot t = [t, 2 + 2t]
$$

Linja $m$ har stigningstall $-1$ som betyr at en retningsvektor for linja er

$$
\vec{v}_m = [1, -1]
$$

Punktet $B(-1, 6)$ ligger på linja, og posisjonsvektoren til punktene på linja er da gitt ved

$$
\vec{r}_m(s) = \lvec{OB} + \vec{v}_m \cdot s = [-1, 6] + [1, -1] \cdot s = [-1 + s, 6 - s]
$$

For å finne skjæringspunktet mellom de to linjene, må vi finne verdier for $t$ og $s$ slik at

$$
\vec{r}_\ell(t) = \vec{r}_m(s)
$$

som vi kan skrive som

$$
[t, 2 + 2t] = [-1 + s, 6 - s]
$$

Her må $x$-komponentene og $y$-komponentene være like, så vi får to likninger som må være tilfredsstilt samtidig:

$$
t = -1 + s \and 2 + 2t = 6 - s
$$

Den første likningen er allerede løst for $t$, så vi setter inn dette i den andre likningen:

$$
2 + 2(-1 + s) = 6 - s
$$

$$
2 - 2 + 2s = 6 - s
$$

$$
3s = 6 \liff s = 2
$$

Vi setter inn $s = 2$ i $\vec{r}_m(s)$ for å finne koordinatene til skjæringspunktet mellom de to linjene:

$$
\vec{r}_m(2) = [-1 + 2, 6 - 2] = [1, 4]
$$

Altså er koordinatene til skjæringspunktet mellom $\ell$ og $m$ gitt ved $(1, 4)$.
::::


:::::::::::::


::::::::::::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 13
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


::::{answer}
* $B(7, 5)$
* $C(7 + 2t, 5 + 5t)$
* $D(3 + 2t, 2 + 5t)$
::::

::::{solution}

:::{plot}
fontsize: 25
width: 100%
align: right
xmin: -1
xmax: 12
ymin: -1
ymax: 12
ticks: off
point: (3, 2)
text: 3, 2, "$A(3, 2)$", bottom-right
point: (7, 5)
text: 7, 5, "$B$", bottom-right
point: (7 + 2, 5 + 5)
text: 7 + 2, 5 + 5, "$C$", top-right
point: (3 + 2, 2 + 5)
text: 3 + 2, 2 + 5, "$D$", top-left
line-segment: (3, 2), (7, 5), dashed, gray
line-segment: (7, 5), (7 + 2, 5 + 5), dashed, gray
line-segment: (7 + 2, 5 + 5), (3 + 2, 2 + 5), dashed, gray
line-segment: (3 + 2, 2 + 5), (3, 2), dashed, gray
vector: (0, 0), (3, 2), blue
text: 0.5 * 3, 0.5 * 2, "$\overrightarrow{OA}$", top-left
vector: (3, 2), (7, 5), red
text: 0.5 * (3 + 7), 0.5 * (2 + 5), "$\overrightarrow{AB}$", bottom-right
vector: (7, 5), (7 + 2, 5 + 5), red
text: 0.5 * (7 + (7 + 2)), 0.5 * (5 + (5 + 5)), "$\overrightarrow{BC} = \overrightarrow{AD}$", bottom-right
vector: (3, 2), (3 + 2, 2 + 5), red
text: 0.5 * (3 + (3 + 2)), 0.5 * (2 + (2 + 5)), "$\overrightarrow{AD}$", top-left
:::


Vi lager oss en hjelpefigur som vist til høyre.

For å komme til punktet $B$, går vi via punktet $A$ og så følger vi $\lvec{AB}$ for å ende opp i punktet $B$. Altså:

$$
\begin{align*}
\lvec{OB} &= \lvec{OA} + \lvec{AB} \\
\\
&= [3, 2] + [4, 3] \\
\\
&= [3 + 4, 2 + 3] \\
\\
&= [7, 5]
\end{align*}
$$

Altså er koordinatene til punktet $B$ gitt ved $(7, 5)$.

For å komme til punktet $D$, kan vi gå via punktet $A$ og så følge $\lvec{AD}$ for å ende opp i punktet $D$. Altså:

$$
\begin{align*}
\lvec{OD} &= \lvec{OA} + \lvec{AD} \\
\\
&= [3, 2] + [2t, 5t] \\
\\
&= [3 + 2t, 2 + 5t] \\
\end{align*}
$$

Altså er koordinatene til punktet $D$ gitt ved $(3 + 2t, 2 + 5t)$.

For å komme til punktet $C$, kan vi gå via punktet $B$ og så følge $\lvec{AD} = \lvec{BC}$ for å ende opp i punktet $C$. Altså:

$$
\begin{align*}
\lvec{OC} &= \lvec{OB} + \lvec{AD} \\
\\
&= [7, 5] + [2t, 5t] \\
\\
&= [7 + 2t, 5 + 5t] \\
\end{align*}
$$

Dermed er koordinatene til punktet $C$ gitt ved $(7 + 2t, 5 + 5t)$.
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $t$ slik at skjæringspunktet mellom diagonalene i parallellogrammet er $P(8, 11)$.



::::{answer}
$$
t = 3
$$
::::


::::{solution}

:::{plot}
fontsize: 25
width: 100%
align: right
xmin: -1
xmax: 12
ymin: -1
ymax: 12
ticks: off
point: (3, 2)
text: 3, 2, "$A$", bottom-right
point: (7, 5)
text: 7, 5, "$B$", center-right
point: (7 + 2, 5 + 5)
text: 7 + 2, 5 + 5, "$C$", center-right
point: (3 + 2, 2 + 5)
text: 3 + 2, 2 + 5, "$D$", top-center
point: (6, 6)
text: 6, 6, "$P$", top-center
line-segment: (3, 2), (7, 5), dashed, gray
line-segment: (7, 5), (7 + 2, 5 + 5), dashed, gray
line-segment: (7 + 2, 5 + 5), (3 + 2, 2 + 5), dashed, gray
line-segment: (3 + 2, 2 + 5), (3, 2), dashed, gray
line: (3, 2), (7 + 2, 5 + 5), solid, blue
line: (7,5), (3 + 2, 2 + 5), solid, red
text: 0.5 * 3, 0.5 * 2, "$\ell$", top-center
text: 0.5 * 3, 10, "$m$", bottom-center
:::

Vi lager oss en hjelpefigur først. Vi kan tenke oss at vi har to linjer $\ell$ (blå) og $m$ (rød), der linja $\ell$ går gjennom punktene $A$ og $C$, og linja $m$ går gjennom punktene $B$ og $D$. Skjæringspunktet til de to linjene er da skjæringspunktet $P$ mellom diagonalene i parallellogrammet.

Både linja $\ell$ og linja $m$ deler parallellogrammet i to like store deler som er speilet om linjene, som betyr at skjæringspunktet $P$ må ligge midt mellom $A$ og $C$, og midt mellom $B$ og $D$. 

Det betyr at vi kan komme oss til punktet $P$, ved å først gå til punktet $A$ og deretter følge vektorer $\lvec{AC}$ halvveis. Vi har at

$$
\lvec{AC} = \lvec{OC} - \lvec{OA} = [7 + 2t, 5 + 5t] - [3, 2] = [4 + 2t, 3 + 5t]
$$

Altså er posisjonsvektoren til punktet $P$ gitt ved

$$
\begin{align*}
\lvec{OP} &= \lvec{OA} + \dfrac{1}{2} \cdot \lvec{AC} \\
\\
&= [3, 2] + \dfrac{1}{2} \cdot [4 + 2t, 3 + 5t] \\
\\
&= [3, 2] + \left[2 + t, \dfrac{3 + 5t}{2}\right] \\
\\
&= \left[5 + t, 2 + \dfrac{3 + 5t}{2}\right] \\
\end{align*}
$$

Vi skal kreve at $\lvec{OP} = [8, 11]$, som gir oss likningene

$$
5 + t = 8 \and 2 + \dfrac{3 + 5t}{2} = 11
$$

Vi løser den første likningen:

$$
5 + t = 8 \liff t = 3
$$

Så løser vi den andre likningen for å sjekke at vi får samme verdi for $t$:

$$
2 + \dfrac{3 + 5t}{2} = 11  \liff 4 + (3 + 5t) = 22
$$

$$
7 + 5t = 22 \liff 5t = 15 \liff t = 3
$$

Altså vil koordinatene til skjæringspunktet $P$ mellom diagonalene være $(8, 11)$ når

$$
t = 3
$$

::::

:::::::::::::


::::::::::::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 14
Om et parallellogram $ABCD$ får du vite at 

* $A(0, 1)$.
* $\lvec{AB} = [4, 2]$.
* $\lvec{AD} = [t, 3]$ for et tall $t \in \real$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem koordinatene til $B$, $C$ og $D$.


::::{answer}
* $B(4, 3)$
* $C(4 + t, 6)$
* $D(t, 4)$
::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem $t$ slik at skjæringspunktet mellom diagonalene ligger på linja $y = 2x + 1$.

::::{answer}
$$
t = -\dfrac{3}{2}
$$
::::

:::::::::::::



::::::::::::::

:::::::::::::::





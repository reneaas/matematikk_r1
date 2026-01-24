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
\lvec{AB} = [5, 1] \qog \lvec{BA} = -\lvec{BA} = [-5, -1]
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

::::{solution}
Posisjonsvektorene til punktene vil ha samme vektorkoordinater som koordinatene til punktene i seg selv. Altså er:

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
Bestem avstanden mellom punktene $A$ og $B$.


::::{answer}
$$
\abs{\lvec{AB}} = \sqrt{17}
$$
::::

::::{solution}
Vi har allerede funnet at $\lvec{AB} = [-4, -1]$. Da er avstanden mellom punktene $A$ og $B$ gitt ved

$$
\abs{\lvec{AB}} = \sqrt{(-4)^2 + (-1)^2} = \sqrt{17}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
Sjekk ved regning at

$$
\lvec{OB} = \lvec{OA} + \lvec{AB}
$$


::::{solution}
Vi har at

$$
\lvec{OA} + \lvec{AB} = [2, 3] + [-4, -1] = [2 - 4, 3 - 1] = [-2, 2] = \lvec{OB}
$$
::::
:::::::::::::


::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
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



:::::::::::::::{exercise} Oppgave 4
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
\vec{v} = \lvec{CD} = \lvec{CD} = \lvec{OD} - \lvec{OC} = [3 - (-1), -2 - 4] = [4, -6]
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



:::::::::::::::{exercise} Oppgave 5
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


:::::::::::::::{exercise} Oppgave 6
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


:::::::::::::::{exercise} Oppgave 7
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
Punktet ligger ikke på linja siden vi får at $t = \dfrac{1}{2}$ for at $x$-komponentene skal være like, og $t = 1$ for at $y$-kompontenene skal være like.
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


:::::::::::::::{exercise} Oppgave 8
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
Bestem startpunktet til parameterframstillingen.

::::{answer}
$$
(1, 4)
$$
::::

::::{solution}
Startpunktet til parameterframstillingen får vi ved å sette $t = 0$ i likningene for $x$ og $y$:

$$
\begin{align*}
x &= 3 \cdot 0 + 1 = 1 \\
\\
y &= -2 \cdot 0 + 4 = 4
\end{align*}
$$

Altså er startpunktet til parameterframstillingen $(1, 4)$.
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 9

En linje $\ell$ er gitt ved 

$$
\vec{r}(t) = [4 - t, 2 + 2t]
$$

Hvilken av linjene nedenfor viser grafen til $\ell$? 


::::{multi-plot2}
---
rows: 2
cols: 2
xmin: -12
xmax: 12
ymin: -12
ymax: 12
xstep: 2
ystep: 2
fontsize: 25
---
:::{plot}
function: -2*x + 10 
text: 8, 8, "A", center-center, bbox
:::

:::{plot}
function: 2*x - 10
text: 8, 8, "B", center-center, bbox
:::

:::{plot}
function: -2*x + 4 
text: 8, 8, "C", center-center, bbox
:::

:::{plot}
function: 2*x + 4
text: 8, 8, "D", center-center, bbox
:::

::::


::::{answer}
Graf A.
::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 10
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


:::::::::::::::{exercise} Oppgave 11
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
:::::::::::::


::::::::::::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 12
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
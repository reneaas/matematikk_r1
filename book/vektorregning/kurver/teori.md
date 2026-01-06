# Naturvitenskapelige anvendelser av kurver


:::{admonition} Læringsmål
---
class: tip
---
* Kunne beskrive linjer og kurver med parameterframstillinger.
* Kunne finne fartsvektor og akselerasjonsvektor for en partikkel som beveger seg langs en kurve.
* Kunne finne banefart og baneakselerasjon for en partikkel som beveger seg langs en kurve.
:::

Vi skal bruke ordet **partikkel** litt løst og tenke på det som et punkt som beveger seg langs en kurve. Partikkelen kan representere alt fra en bil som kjører langs en vei, en planet som beveger seg i bane rundt en stjerne eller et elektron som forflytter seg i et elektrisk felt. Anvendelsene er mange, og teorien vi skal jobbe med her ble i hovedsak utviklet for å beskrive bevegelsen til fysiske objekter i naturen. 


## Partikler på linjer




## Partikler på kurver



:::{plot}
align: right
width: 100%
curve: 2*t, -1/2 * 9.81 * t**2 + 20*t + 1, (0, 4.13), solid, blue
ymax: 30
ymin: -1
xmin: -0.5
xmax: 9
ticks: off
point: (3, 15971/800)
vector: (0, 0), (3, 15971/800), red
text: 0.5 * 3, 0.5 * 15971/800, "$\vec{r}(t)$", bottom-right
vector: (3, 15971/800), 2, 1057/200, red
text: 3 + 0.5 * 2 , 15971/800 + 0.5 * 1057/200, "$\vec{v}(t)$", top-left
fontsize: 30
:::



En kurve i planet kan beskrives ved hjelp av en parameterframstilling $\vec{r}(t)$. 

I naturvitenskapelige anvendelser tenker vi på $\vec{r}(t)$ som posisjonsvektoren til en partikkel som beveger seg langs kurven over tid $t$. Partikkelen vil da bevege seg med en fartsvektor $\vec{v}(t)$ som beskriver hvor fort og hvilken retning partikkelen forflytter seg langs kurven. 



:::::::::::::::{summary} Parameterframstilling for kurver
En kurve $C$ i planet kan beskrives med en parameterframstilling

$$
\vec{r}(t) = [x(t), y(t)]
$$

hvor $x(t)$ og $y(t)$ er funksjoner som beskriver koordinatene til punktene på kurven som funksjoner av parameteren $t$.

En partikkel som beveger seg langs kurven har da posisjonsvektor $\vec{r}(t)$ og fartsvektor gitt ved

$$
\vec{v}(t) = \vec{r}'(t) = \left[ x'(t), y'(t) \right]
$$
:::::::::::::::




----



:::::::::::::::{exercise} Oppgave 1
Ta quizen nedenfor.


::::::::{quiz-2}
:::::::{quiz-question}
Grafen til en funksjon $f$ er vist i figuren nedenfor.

:::{plot}
width: 50%
function: (x - 1)**2 + 1, f
fontsize: 30
:::

Hvilket alternativ viser $f(x)$? 

::::::{quiz-answer}
$$
f(x) = -(x - 1)^2 + 1
$$
::::::


::::::{quiz-answer}
---
correct: true
---
$$
f(x) = (x - 1)^2 + 1
$$
::::::


::::::{quiz-answer}
$$
f(x) = -(x + 1)^2 + 1
$$
::::::


::::::{quiz-answer}
$$
f(x) = (x + 1)^2 + 1
$$
::::::





:::::::




:::::::{quiz-question}
I programmet nedenfor er en funksjon $f$ definert


:::{code-block} python
def f(x):
    return (x - 2)**2 - 3

y = f(4)
print(y)
:::


Hva er det som skrives ut av programmet?


::::::{quiz-answer}
---
correct: true
---
$$1$$
::::::

::::::{quiz-answer}
$$0$$
::::::


::::::{quiz-answer}
$$
-2
$$
::::::


::::::{quiz-answer}
$$
15
$$
::::::

:::::::



::::::::


:::::::::::::::



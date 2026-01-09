# Omvendte funksjoner



::::{admonition} Læringsmål
---
class: tip
---
* Kunne forklare hva en omvendt funksjon er og beskrive sammenhengen mellom en funksjon og dens omvendte funksjon algebraisk og grafisk.
* Kunne bestemme den omvendte funksjonen til en gitt funksjon.
* Kunne avgjøre om en funksjon har en omvendt funksjon.
::::


Hvis $f$ er en funksjon som gjør noe med et tall $x$, får vi et nytt tall $y$ ved å regne ut $y = f(x)$. Dersom $g$ er en **omvendt funksjon** til $f$, så vil $g$ fungere som en **angreknapp** som tar $y$ tilbake til utgangspunktet vårt igjen ved å regne ut $x = g(y)$. Vi kan illustrere sammenhengen med et diagram som vist i figuren nedenfor.


:::{plot}
width: 50%
figsize: (5, 3)
ellipse: (-2, 0), 1, 0.6, solid, blue
ellipse: (2, 0), 1, 0.6, solid, red
point: (-2, 0.2)
point: (2.5, -0.3)
annotate: (-2, 0.2), (2.5, -0.3), "", -0.5
annotate: (2.5, -0.3), (-2, 0.2), "", -0.5
text: -2, 0.2, "$x$", center-left
text: 2.5, -0.3, "$y$", top-right
text: 0.3, 1.3, "$y = f(x)$", top-center
text: 0.3, -1.35, "$x = g(y)$", bottom-center
fontsize: 25
xmin: -3.2
xmax: 3.2
ymin: -2.2
ymax: 2.2
axis: off
:::

Mer presist kan vi definere sammenhengen mellom en funksjon $f$ og dens omvendte funksjon $g$ som følger:


:::::::::::::::{summary} Omvendte funksjoner
La $f$ være en funksjon og $g$ være den omvendte funksjon til $f$. Da har vi at

$$
g(f(x)) = x
$$

Det vil si at dersom vi først bruker funksjonen $f$ på et tall $x$, og deretter bruker den omvendte funksjonen $g$ på svaret $f(x)$ vi får, så ender vi opp med det opprinnelige tallet $x$ igjen.

Dette vil være symmetrisk (vi kan gå begge veier), så vi har også at $f$ er den omvendte funksjonen til $g$, slik at

$$
f(g(x)) = x
$$

> Noen ganger skriver vi den omvendte funksjonen til $f$ som $f^{-1}$ i stedet for å gi den et eget navn som $g$. Dette er bare en skrivemåte og svarer ikke til at vi skal bruke potensregler. 

:::::::::::::::


La oss konkretisere dette med noen eksempler:


:::::::::::::::{example} Eksempel 1
Vi lar funksjonen $f$ være gitt ved 

$$
f(x) = x + 2
$$


Det vil si, $f$ er funksjonen som tar et tall $x$ og legger til $2$. 

Bestem den omvendte funksjonen $g$ til $f$.



::::{solution}
---
dropdown: 0
---
Den omvendte funksjonen må "angre" handlingen $f$ gjør med et tall $x$. Hvis $f(x)$ tar tallet $x$ og legger til $2$, så må $g(x)$ gjøre det motsatte, altså ta tallet vi får fra $f(x)$ og trekke fra $2$. Det vil si at 

$$
g(x) = x - 2.
$$


Vi kan se at dette stemmer ved å regne ut $g(f(x))$ og sjekke at vi får $x$ som svar:


$$
g(f(x)) = f(x) - 2 = \underbrace{x + 2}_{\displaystyle f(x)} - 2 = x
$$

Altså har vi funnet den omvendte funksjonen til $f$.

::::



:::::::::::::::



---


:::::::::::::::{exercise} Underveisoppgave 1
En funksjon $f$ er gitt ved 


$$
f(x) = 3x
$$


1. Forklar hva funksjonen $f$ gjør med et tall $x$.
2. Bestem den omvendte funksjonen $g$ som "angrer" handlingen til $f$.


::::{answer}
$$
g(x) = \dfrac{x}{3}
$$
::::


::::{solution}
1. Funksjonen $f$ ganger tallet $x$ med $3$. 
2. Den omvendte funksjonen $g$ vil være en som "angrer" handlingen til $f$. Det motsatte av å gange med $3$ er å dele med $3$, så derfor vil den omvendte funksjonen være

$$
g(x) = \dfrac{x}{3}
$$

Det kan vi se stemmer ved å regne ut $g(f(x))$:

$$
g(f(x)) = \dfrac{f(x)}{3} = \dfrac{\overbrace{3x}^{\displaystyle f(x)}}{3} = x
$$
::::


:::::::::::::::



---


Vi har allerede jobbet med funksjoner som har omvendte funksjoner uten at vi har brukt dette begrepet bevisst. Eksponentialfunksjoner og logaritmer er et slikt eksempel.


:::::::::::::::{example} Eksempel 2
La $f$ være gitt ved $f(x) = e^x$ og $g$ være gitt ved $g(x) = \ln(x)$. Da er $f$ og $g$ omvendte funksjoner. Det kan vi se fordi

$$
g(f(x)) = \ln(e^x) = x
$$

og 

$$
f(g(x)) = e^{\ln(x)} = x.
$$


Altså vil eksponentialfunksjonen og logaritmefunksjonen "angre" hverandres handlinger. Dermed er de omvendte funksjoner.


:::::::::::::::

Vi har vært borti mange flere omvendte funksjoner tidligere, og nedenfor er en liten liste: 

| Funksjon $f(x)$         | Omvendt funksjon $g(x)$        |
|----------------------|------------------------------|
| $x + a$       | $x - a$                |
| $ax$           | $\dfrac{x}{a}$                |
| $x^2$ (for $x \geq 0$) | $\sqrt{x}$                |
| $x^n$ (for $x \geq 0$) | $\sqrt[n]{x}$                |
| $e^x$          | $\ln(x)$                |
| $a^x$          | $\log_a(x)$                |



---



## Bestemme omvendte funksjoner
Gitt en funksjon $f$, så kan vi bestemme den omvendte funksjonen $g$ ved å sette opp likningen 

$$
y = f(x) 
$$

og løse likningen for $x$ slik at vi får $x$ uttrykt som en funksjon av $y$. Den funksjonen vi da får for $x$ er den omvendte funksjonen $g(y)$. For å kunne tenke på grafen til $g$ som vanlig, så bytter vi ofte navnet på variabelen $y \to x$ igjen etterpå.


:::::::::::::::{example} Eksempel 3
Bestem den omvendte funksjonen til $f$ gitt ved

$$
f(x) = \ln (2x - 3)
$$


::::{solution}
---
dropdown: 0
---
Vi setter opp likningen

$$
y = f(x) \limplies y = \ln(2x - 3)
$$

For å løse likningen for $x$, begynner vi med å bruke definisjonen av den naturlige logaritmen til å omskrive likningen:

$$
e^y = 2x - 3
$$

Deretter isolerer vi $x$:

$$
2x = e^y + 3 \limplies x = \dfrac{e^y + 3}{2}
$$

Dermed vil 

$$
g(y) = \dfrac{e^y + 3}{2}
$$

Så bytter vi om $y \to x$ igjen så vi kan tenke på $g$ som en vanlig funksjon. Da får vi at den omvendte funksjonen til $f$ er gitt ved

$$
g(x) = \dfrac{e^x + 3}{2}
$$

::::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2
En funksjon $f$ er gitt ved

$$
f(x) = e^{3x - 1}
$$

Bestem den omvendte funksjonen $g$ til $f$.

Sjekk svaret ditt ved å verifisere at $g(f(x)) = x$ og $f(g(x)) = x$. 


::::{answer}
$$
g(x) = \dfrac{\ln x + 1}{3}
$$
::::

:::::::::::::::


## Grafisk sammenheng mellom funksjoner og deres omvendte funksjoner

Vi har så langt sett at $g$ er den omvendte funksjonen til $f$, så vil $g$ "angre" handlingen til $f$ og omvendt. Funksjonen $f$ tar et tall $x$ fra sin definsjonsmengde $D_f$ og gir oss et nytt tall $y = f(x)$ som ligger i sin verdimengden $V_f$. Den omvendte funksjonen $g$ tar derimot et tall $y$ fra sin definisjonsmengde $D_g$ (som tilsvarer verdimengden til $f$) og gir oss tilbake tallet $x = g(y)$ som ligger i sin verdimengde $V_g$ (som tilsvarer definisjonsmengden til $f$). Dette kan vi illustrere som vist i figuren nedenfor.

:::{plot}
width: 50%
figsize: (5, 3)
ellipse: (-2, 0), 1, 0.6, solid, blue
ellipse: (2, 0), 1, 0.6, solid, red
point: (-2, 0.2)
point: (2.5, -0.3)
annotate: (-2, 0.2), (2.5, -0.3), "", -0.5
annotate: (2.5, -0.3), (-2, 0.2), "", -0.5
text: -2, 0.2, "$a$", center-left
text: 2.5, -0.3, "$b$", top-right
text: 0.3, 1.3, "$b = f(a)$", top-center
text: 0.3, -1.35, "$a = g(b)$", bottom-center
fontsize: 25
xmin: -3.2
xmax: 3.2
ymin: -2.2
ymax: 2.2
axis: off
text: 2, 0.5, "$V_f = D_g$", top-right
text: -2, -0.5, "$D_f = V_g$", bottom-left
:::


Dette betyr at et punkt $(a, b)$ på grafen til $f$, svarer til et punkt $(b, a)$ på grafen til $g$. Altså byttes $x$- og $y$-verdiene om når vi går fra grafen til $f$ til grafen til $g$. 

:::::::::::::::{summary} Grafisk sammenheng mellom funksjoner og deres omvendte funksjoner
La $f$ og $g$ være omvendte funksjoner til hverandre. Da er 

* $D_f = V_g$
* $V_f = D_g$
* Punktet $(a, b)$ på grafen til $f$ tilsvarer punktet $(b, a)$ på grafen til $g$.


:::{plot}
width: 70%
function: x**3 + 1, f, (-2, 2], blue
function: (abs(x - 1))**(1/3) * (x - 1) / abs(x - 1), g, (-7, 9], red
line: 1, 0, dashed, gray
xmin: -11.5
xmax: 11.5
ymin: -11.5
ymax: 11.5
point: (g(f(1.5)), f(1.5))
point: (f(1.5), g(f(1.5)))
function-endpoints: true
ticks: off
text: g(f(1.5)), f(1.5), "$(a, b)$", top-right
text: f(1.5), g(f(1.5)), "$(b, a)$", top-right
fontsize: 25
:::

Siden et punkt $(a, b)$ på grafen til $f$ tilsvarer et punkt $(b, a)$ på grafen til $g$, så vil grafen til $g$ være et speilbilde av grafen til $f$ om linjen $y = x$. 


:::::::::::::::


Vi kan se noen helt konkrete eksempler på grafen til $f$ og dens omvendte funksjon $g$ nedenfor.


:::::::::::::::{example} Eksempel 4
Når du ser på figurene nedenfor kan du legge merke til følgende:
1. Grafen til $f$ og grafen til den omvendte funksjon $g$ er speilbilder av hverandre rundt linjen $y = x$
2. Et punkt $(a, b)$ på grafen til $f$ tilsvarer et punkt $(b, a)$ på grafen til $g$
3. Definisjonsmengden til $f$ er lik verdimengden til $g$, og verdimengden til $f$ er lik definisjonsmengden til $g$

::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
---

:::{plot}
function: exp(x), f
function: ln(x), g, (0, 20)
line: 1, 0, dashed, gray

Viser grafen til $f(x) = e^x$ og den omvendte funksjonen $g(x) = \ln(x)$
:::

:::{plot}
function: x**2, f, (0, 20), blue
function: sqrt(x), g, (0, 20), red
function-endpoints: true
line: 1, 0, dashed, gray
xmin: -3
ymin: -2
point: (2, 4)
point: (4, 2)
text: 2, 4, "$(2, 4)$", top-left
text: 4, 2, "$(4, 2)$", bottom-right

Viser grafen til $f(x) = x^2$ med $D_f = \langle 0, \to\rangle$ og den omvendte funksjonen $g(x) = \sqrt{x}$
:::


:::{plot}
function: (x - 1)**2 + 2, f, [1, 3), blue
function: (x - 2)**(1/2) + 1, g, [2, 6), red
line: 1, 0, dashed, gray
xmin: -3
xmax: 7
ymin: -2
point: (2, 3)
point: (3, 2)
function-endpoints: true
ymax: 7
text: 2, 3, "$(2, 3)$", top-left
text: 3, 2, "$(3, 2)$", bottom-right

Viser grafen til $f(x) = (x - 1)^2 + 2$ med $D_f = [1, 3\rangle$ og den omvendte funksjonen $g(x) = \sqrt{x - 2} + 1$ med $D_g = [2, 6\rangle$. Merk at $D_f = V_g$ og $V_f = D_g$.
:::


:::{plot}
function: x**3 + 1, f, (-2, 2], blue
function: (abs(x - 1))**(1/3) * (x - 1) / abs(x - 1), g, (-7, 9], red
function-endpoints: true
line: 1, 0, dashed, gray
xmin: -10
xmax: 10
xstep: 2
ymin: -10
ymax: 10
ystep: 2

Viser grafen til $f(x) = x^3 + 1$ for $x \in \langle -2, 2]$ og den omvendte funksjonen $g(x) = \sqrt[3]{x - 1}$
:::





::::


:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 3

:::{plot}
align: right
width: 320
function: x**3, f, (-2, 2], blue
function-endpoints: true
xmin: -3
xmax: 3
ymin: -10
ymax: 10
ystep: 2
fontsize: 25
:::


Grafen til en funksjon $f$ er vist i figuren til høyre.

Én av grafene nedenfor viser $f$ som omvendte funksjon. Avgjør hvilken.


::::{multi-plot2}
---
rows: 2
cols: 2
fontsize: 25
---

:::{plot}
function: -cbrt(abs(x)) * sign(x), A, (-8, 8], blue
xmin: -10
xmax: 10
ymin: -3
ymax: 3
xstep: 2
ystep: 1
function-endpoints: true
:::


:::{plot}
function: cbrt(abs(x)) * sign(x), B, (-8, 8], blue
xmin: -10
xmax: 10
ymin: -3
ymax: 3
xstep: 2
ystep: 1
function-endpoints: true
:::

:::{plot}
function: -cbrt(abs(x)) * sign(x), C, [-8, 8), blue
xmin: -10
xmax: 10
ymin: -3
ymax: 3
xstep: 2
ystep: 1
function-endpoints: true
:::

:::{plot}
function: cbrt(abs(x)) * sign(x), D, [-8, 8), blue
xmin: -10
xmax: 10
ymin: -3
ymax: 3
xstep: 2
ystep: 1
function-endpoints: true
:::

::::


::::{answer}
Graf B.
::::


::::{solution}
Grafen til $f$ skal speiles over linja $y = x$ for å få grafen til den omvendte funksjonen. Vi kan for eksempel se at endepunktet $(2, 8)$ da må bli $(8, 2)$ som kun graf B har. Graf D har samme form, men her er dette endepunktet ekskludert. 

Dermed er graf B den riktige grafen for den omvendte funksjonen til $f$.
::::



:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 4

:::{plot}
align: right
width: 100%
fontsize: 25
function: x**3, f, (-2, 2], blue
function-endpoints: true
xmin: -3
xmax: 3
ymin: -10
ymax: 10
ystep: 2
:::

Grafen til en funksjon $f$ er vist i figuren til høyre.

Bestem definisjonsmengden og verdimengden til den omvendte funksjonen $g$.


:::{clear}
:::

::::{answer}
$$
D_g = \langle -8, 8] \qog V_g = \langle -2, 2]
$$
::::


:::::::::::::::




## Eksistens av omvendte funksjoner

Når vet vi egentlig om en funksjon har en omvendt funksjon? Hva skal til for at vi skal kunne "angre" handlingen til en funksjon $f$?
Når vi regner ut $y = f(x)$, kan det hende at flere forskjellige verdier for $x$ "lander" på samme verdi for $y$. Da vil ikke $y$-verdien kunne fortelle oss nøyaktig hvilken $x$-verdi vi startet med, og da kan vi ikke "angre" handlingen til $f$.

Figuren til venstre nedenfor viser et eksempel på en funksjon $f$ som har en omvendt funksjon, mens figuren nedenfor til høyre viser et eksempel på en funksjon $f$ som ikke har en omvendt funksjon.



::::{multi-plot2}
---
rows: 1
cols: 2
---


:::{plot}
figsize: (5, 3.5)
ellipse: (-2, 0), 0.5, 1, solid, blue
ellipse: (2, 0), 0.5, 1, solid, red
axis: equal
axis: off 
text: -2, 1, "$D_f$", top-center
text: 2, 1, "$V_f$", top-center
fontsize: 25
text: -2, 0.6, "$1$", center-center
text: -2, 0, "$2$", center-center
text: -2, -0.6, "$3$", center-center
text: 2, 0.6, "$1$", center-center
text: 2, 0, "$4$", center-center
text: 2, -0.6, "$9$", center-center
annotate: (-2, 1), (2, 1), "", -0.3
text: 0, 1.5, "$y = f(x)$", top-center
annotate: (-2, 0.6), (1.95, -0.6), "", 0
annotate: (-2, 0), (1.95, 0.6), "", 0
annotate: (-2, -0.6), (1.95, 0), "", 0


Definisjonsmengden til $f$ er $D_f = \{1, 2, 3\}$. Når vi regner ut $y = f(x)$, så er det bare én verdi for $x$ for hver verdi for $y$ i $V_f = \{1, 4, 9\}$. Da har $f$ en omvendt funksjon $g$ som "angrer" handlingen til $f$.


:::


:::{plot}
figsize: (5, 3.5)
ellipse: (-2, 0), 0.5, 1, solid, blue
ellipse: (2, 0), 0.5, 1, solid, red
axis: equal
axis: off 
text: -2, 1, "$D_f$", top-center
text: 2, 1, "$V_f$", top-center
fontsize: 25
annotate: (-2, 1), (2, 1), "", -0.3
text: 0, 1.5, "$y = f(x)$", top-center
text: -2, 0.6, "$1$", center-center
text: -2, 0, "$2$", center-center
text: -2, -0.6, "$3$", center-center
text: 2, 0.5, "$4$", center-center
text: 2, -0.5, "$9$", center-center
annotate: (-2, 0.6), (1.95, -0.5), "", 0
annotate: (-2, 0), (1.95, -0.5), "", 0
annotate: (-2, -0.6), (1.95, 0.5), "", 0

Definisjonsmengden til $f$ er $D_f = \{1, 2, 3\}$. Når vi regner ut $y = f(x)$, så er det to forskjellige verdier for $x$ som gir samme verdi $y = 9$ i $V_f = \{4, 9\}$. Da kan vi ikke "angre" handlingen til $f$ fordi vi vet ikke hvilken verdi for $x$ som ga oss $y = 9$.
:::


::::



---


### Monotone funksjoner

> I neste kapittel skal vi se hvordan vi kan bruke den deriverte til å avgjøre om en funksjon har en omvendt funksjon ved å undersøke om funksjonen er monoton. Her ser vi på det grafiske kjennetegnet.

Så lenge en funksjon $f$ stiger eller synker i hele sin definisjonsmengde, så kan vi være sikre på at den bare har én verdi for $x$ for hver verdi for $y = f(x)$. Dermed kan vi "angre" handlingen til $f$ og funksjonen har en omvendt funksjon. Slike funksjoner kalles gjerne for **monotone funksjoner**. Mer presist har vi at:

:::::::::::::::{summary} Monotone funksjoner
En funksjon $f$ er en **monoton funksjon** dersom den er enten strengt voksende eller strengt avtakende i hele sin definisjonsmengde.

Strengt voksende
: Hvis $x_1 < x_2 \limplies f(x_1) < f(x_2)$ for alle $x_1, x_2$ i definisjonsmengden til $f$.

Stengt avtakende
: Hvis $x_1 < x_2 \limplies f(x_1) > f(x_2)$ for alle $x_1, x_2$ i definisjonsmengden til $f$.



::::{multi-plot2}
---
rows: 1
cols: 2
fontsize: 30
---
:::{plot}
width: 100%
function: (x - 1) * (x**2 - x + 1), (-1, 3], blue
function-endpoints: true
ticks: off
ymax: 18
ymin: -10
xmax: 4
xmin: -2
text: 0.5 * (4 + 0), 16, "Strengt voksende", top-center, bbox
:::

:::{plot}
width: 100%
function: -(x - 1) * (x**2 - x + 1), (-1, 3], blue
function-endpoints: true
ticks: off
ymax: 12
ymin: -16
xmax: 4
xmin: -2
text: 0.5 * (4 + 0), 10, "Strengt avtakende", top-center, bbox
:::


::::

:::::::::::::::


---


:::::::::::::::{example} Eksempel 5
Nedenfor vises grafene til to funksjoner.

1. Avgjør hvilke av funksjonene som har en omvendt funksjon.
2. Bestem definisjonsmengden til den omvendte funksjonen hvis den eksisterer.


::::{multi-plot2}
---
rows: 1
cols: 2
fontsize: 28
---
:::{plot}
width: 100%
function: (x + 1) * (1/30 * x**2 + 4/15 * x + 2), [-3, 2), f, blue
function-endpoints: true
xmin: -4
xmax: 3
ymax: 9
ymin: -5
:::

:::{plot}
width: 100%
function: -1/10 * x**3 + 2/3 * x**2 + 17/30 * x - 3, (-3, 3], g, blue
function-endpoints: true
xmin: -4
xmax: 4
ymax: 5
ymin: -4
:::

::::


::::{solution}
---
dropdown: 0
---

Grafen til $f$ stiger i hele sin definisjonsmengde slik at den bare vil skjære enhver horisontal linje én gang. Derfor vil $f$ ha en omvendt funksjon $f^{-1}$. 

Definisjonsmengden til $f^{-1}$ vil svare til verdimengden til $f$ som er gitt ved $V_f = [-3, 8\rangle$. Dermed er definisjonsmengden til den omvendte funksjonen til $f$ gitt ved

$$
D_{f^{-1}} = [-3, 8\rangle.
$$


Grafen til $g$ synker først og deretter stiger innenfor definisjonsmengden sin. Dermed vil den skjære minst én horisontal linje mer enn én gang. Da kan ikke $g$ ha en omvendt funksjon.
::::


:::::::::::::::



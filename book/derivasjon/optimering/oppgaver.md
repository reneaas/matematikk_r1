# Størst og minst verdi

> Å løse oppgavene nedenfor uten hjelpemidler kan være tidkrevende. Det er derfor lurt å jobbe seg gjennom oppgavene og løse dem med CAS først, og deretter gå tilbake å prøve og løse dem uten hjelpemidler for å trene på å anvende derivasjonsregler og løse likningene for hånd.

:::::::::::::::{exercise} Oppgave 1

:::{cas-popup}
---
layout: sidebar
---
:::


Anna og Bjørn har materiale nok til å lage et gjerde som er 64 m langt.

De skal gjerde inn et område som skal ha form som et rektangel, og de ønsker at området skal få størst mulig areal. Se figuren nedenfor.

Bestem det største mulige arealet de kan gjerde inn.

:::{plot}
width: 60%
axis: off
polygon: (0, 0), (44, 0), (44, 20), (0, 20)
xmin: -5
xmax: 45
ymax: 22
ymin: -2
text: 22, 0, "$x$", bottom-center
text: 44, 10, "$y$", center-right
figsize: (4, 2)
:::


::::{answer}
$$
A_\text{størst} = 256 \, \mathrm{m}^2
$$
::::


::::{solution}
Omkretsen til området kan beskrives som:

$$
2x + 2y = 64 \liff x + y = 32
$$

Arealet til området vil være $A = x \cdot y$. Vi kan løse likningen ovenfor for $y$:

$$
x + y = 32 \liff y = 32 - x
$$

Da kan vi lage en funksjon $A(x)$ for arealet som blir:

$$
A(x) = x\cdot y(x) = x\cdot(32 - x) = -x^2 + 32x
$$

````{tab-set}
```{tab-item} Med CAS
For å bestemme den verdien av $x$ som gir størst areal, så må vi se etter ekstremalpunktene til $A$. Deretter må vi sjekke at $A''(x) < 0$ i punktet for å sikre at det er et toppunkt. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgave_1/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $A'(x) = 0$ når $x = 16$. Vi ser også at $A''(16) < 0$ som betyr at $A$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $x = 16$ et toppunkt. Vi ser at da er $A(16) = 256$ som betyr at det største mulige arealet er $256 \, \mathrm{m}^2$.



```

```{tab-item} Uten hjelpemidler

For å bestemme den verdien av $x$ som gir størst areal, så må vi se etter ekstremalpunktene til $A$. Da løser vi $A'(x) = 0$. Vi deriverer funksjonen først:

$$
A'(x) = -2x + 32
$$

Deretter løser vi likningen:

$$
A'(x) = 0 \liff -2x + 32 = 0
$$

som gir

$$
2x = 32 \liff x = 16
$$

Vi må begrunne at dette er et toppunkt. Det vil det være siden $A(x)$ er en konkav andregradsfunksjon {polyicon}`frown` fordi den ledende koeffisienten er negativ.

Det største arealet blir da

$$
A(16) = 16 \cdot (32 - 16) = 16^2 = 256
$$

Det største mulige arealet er dermed $256 \, \mathrm{m}^2$. 
```

````


::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2

:::{cas-popup}
---
layout: sidebar
---
:::


Anna og Bjørn skal slå opp telt ved en elvebredde. De skal sette opp et tau rundt teltet for å holde dyr unna. 

De har 80 m med tau og fire pinner. Området de skal gjerde inn skal ha form som et rektangel og de tenker å bruke elvebredden som en av sidene i rektangelet slik at de kan gjerde inn et større område. Målet deres er å få et størst mulig areal innenfor gjerdet. Se figuren nedenfor.

Bestem det største mulige arealet de kan gjerde inn.


:::{plot}
width: 70%
axis: off
figsize: (5, 3)
hline: 0, -10, 10, solid, blue
line-segment: (0, 0), (8, 0), black, solid
line-segment: (-4, 0), (-4, 5), black, solid
line-segment: (-4, 5), (4, 5), black, solid
line-segment: (4, 5), (4, 0), black, solid
text: 0, 0, "Elvebredde", bottom-center
annotate: (5, 5), (0, 5), "Gjerde", 0.5
:::


::::{answer}
$$
A_\mathrm{størst} = 800 \, \mathrm{m}^2
$$
::::

::::{solution}
Vi setter opp et uttrykk for "omkretsen" av gjerde:

$$
x + 2y = 80
$$

Dette kan vi løse for $y$:

$$
x + 2y = 80 \liff y = 40 - \dfrac{1}{2}x
$$

Nå kan vi lage en funksjon $A(x)$ for arealet som blir:

$$
A(x) = x \cdot y(x) = x \cdot \left(40 - \dfrac{1}{2}x\right) = -\dfrac{1}{2}x^2 + 40x
$$

````{tab-set}
```{tab-item} Med CAS
For å bestemme ekstremalpunktene til $A$, så må vi løse $A'(x) = 0$ og sjekke at $A''(x) < 0$ i punktet for å sikre at det er et toppunkt. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgave_2/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at $x = 40$ er et ekstremalpunkt siden $A'(40) = 0$. Videre er punktet et toppunkt siden $A''(40) < 0$. Dermed gir $x = 40$ et toppunkt. Vi ser også at $A(40) = 800$ som betyr at det største mulige arealet er $800 \, \mathrm{m}^2$.

```
```{tab-item} Uten hjelpemidler
For å bestemme ekstremalpunktene til $A$, så må vi løse $A'(x) = 0$. Vi deriverer funksjonen først:

$$
A'(x) = -x + 40
$$

Så løser vi likningen:

$$
A'(x) = 0 \liff -x + 40 = 0
$$

som betyr at $x = 40$. 

Vi må begrunne at dette svarer til et toppunkt. Det gjør det fordi $A(x)$ er en konkav andregradsfunksjon {polyicon}`frown` siden den ledende koeffisienten er negativ. Dermed blir det største mulige arealet:

$$
A(40) = 40 \cdot \left(40 - \dfrac{1}{2} \cdot 40\right) = 40 \cdot 20 = 800
$$

Det største mulige arealet de kan gjerde inn er dermed $800 \, \mathrm{m}^2$.
```
````
::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 3

:::{cas-popup}
---
layout: sidebar
---
:::



En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -x^2 + 9 \qder x \in [0, 3].
$$

En trekant har hjørner i $(0, 0)$, $(k, 0)$ og $(k, f(k))$. Se figuren nedenfor.


Bestem $k$ slik at arealet av trekanten er størst mulig.


:::{plot}
width: 70%
function: -x**2 + 9, (0, 3), f
xmin: -1
xmax: 4
ymax: 10
ymin: -1
ticks: off
polygon: (0, 0), (2, 0), (2, 5)
point: (0, 0)
point: (2, 0)
point: (2, 5)
text: 0, 0, "$(0, 0)$", bottom-left
text: 2, 0, "$(k, 0)$", bottom-center
text: 2, 5, "$(k, f(k))$", top-right
:::


::::{answer}
$$
k = \sqrt{3}
$$
::::


::::{solution}
Vi setter opp et funksjon $A(k)$ for arealet av trekanten: 

$$
A(k) = \dfrac{k \cdot f(k)}{2} = \dfrac{-k^3 + 9k}{2} = -\dfrac{1}{2}k^3 + \dfrac{9}{2}k
$$

````{tab-set}
```{tab-item} Med CAS
For å bestemme ekstremalpunktene til arealfunksjonen, så må vi løse $A'(k) = 0$ og sjekke at $A''(k) < 0$ i punktet for å sikre at det er et toppunkt. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgave_3/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi får to løsninger til likningen $A'(k) = 0$, men det er bare $k = \sqrt{3}$ som er en del av definisjonsmengden. Vi ser også at $A''(\sqrt{3}) < 0$ som betyr at $A$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $k = \sqrt{3}$ et toppunkt. Dermed blir arealet av trekanten størst mulig dersom

$$
k = \sqrt{3}
$$


```
```{tab-item} Uten hjelpemidler
For å bestemme ekstremalpunktene til arealfunksjonen, så må vi løse $A'(k) = 0$. Vi deriverer først:

$$
A'(k) = -\dfrac{3}{2}k^2 + \dfrac{9}{2}
$$

Så løser vi likningen

$$
A'(k) = 0 \liff -\dfrac{3}{2}k^2 + \dfrac{9}{2} = 0
$$

Vi ganger med $2$ i alle ledd for å forenkle likningen: 

$$
-3k^2 + 9 = 0
$$

Så deler vi med $-3$ i alle ledd for å forenkle den ytterliggere:

$$
k^2 - 3 = 0
$$

Da får vi 

$$
k = \pm \sqrt{3}
$$

Vi må forkaste den negative løsningen siden denne ikke er en del av definisjonsmengden. Det betyr at $k = \sqrt{3}$ er en kandidat for den verdien som gjør arealet størst mulig. 

Vi må sjekke at dette er et toppunkt og at det er en den største verdien. Arealet er opplagt null når $k = 0$ eller $k = 3$, så endepunktene i definisjonsmengden gir ikke størst mulig arealet. For å bestemme om $k = \sqrt{3}$ er et toppunkt, tegner vi et fortegnsskjema for $A'(k)$ for å sjekke: 

:::{signchart}
width: 100%
function: -3/2 * k**2 + 9/2, $A'(k)$
:::

Vi ser at $A'(k) > 0$ rett før $k = \sqrt{3}$ og $A'(k) < 0$ rett etter. Det betyr at grafen til $A(k)$ stiger rett før punktet og synker rett etter. Men da gir $k = \sqrt{3}$ et toppunkt. Dermed vil $k = \sqrt{3}$ gi det største arealet av trekanten.
```
````

::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4

:::{cas-popup}
---
layout: sidebar
---
:::



Nedenfor ser du grafen til en funksjon $f$ gitt ved

$$
f(x) = \dfrac{8}{x^2 + 20} \qder D_f = [0, \to \rangle
$$

Et rektangel har hjørnene $(0, 0)$, $(r, 0)$, $(r, f(r))$ og $(0, f(r))$. Se figuren nedenfor.

Bestem $r$ slik at arealet av rektangelet er størst mulig.

:::{plot}
width: 70%
function: 8/(x**2 + 20), (0, 20), f
xmin: -1
xmax: 15
ymin: -0.1
ymax: 0.5
ystep: 0.1
point: (5, f(5))
point: (0, 0)
point: (0, f(5))
point: (5, 0)
polygon: (0, 0), (5, 0), (5, f(5)), (0, f(5))
text: 0, 0, "$(0, 0)$", bottom-left
text: 5, 0, "$(r, 0)$", bottom-center
text: 5, f(5), "$(r, f(r))$", top-right
text: 0, f(5), "$(0, f(r))$", top-left
ticks: off
:::


::::{answer}
$$
r = 2\sqrt{5}
$$
::::

::::{solution}
Vi bestemmer en funksjon $A(r)$ for arealet av rektangelet:

$$
A(r) = r\cdot f(r) = r \cdot \dfrac{8}{r^2 + 20} = \dfrac{8r}{r^2 + 20}
$$

````{tab-set}
```{tab-item} Med CAS
For å bestemme ekstremalpunktene til $A$, må vi løse $A'(r) = 0$ og sjekke at $A''(r) < 0$ i punktet for å sikre at det er et toppunkt. Vi bruker CAS til å utføre selve regningen:


:::{figure} ./figurer/oppgave_4/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften er vi at $A'(r) = 0$ når $r = 2\sqrt{5}$ (som er den eneste løsningen som er innenfor definisjonsmengden). Vi ser også at $A''(2\sqrt{5}) < 0$ som betyr at $A$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $r = 2\sqrt{5}$ et toppunkt. Derfor vil $r = 2\sqrt{5}$ gi det største arealet av rektangelet.

```
```{tab-item} Uten hjelpemidler

For å bestemme ekstremalpunktene til $A$, må vi løse $A'(r) = 0$. Vi deriverer funksjonen først:

\begin{align*}
    A'(r) &= \dfrac{(8r)' \cdot (r^2 + 20) - 8r \cdot (r^2 + 20)'}{(r^2 + 20)^2} \\
    \\
    &= \dfrac{8(r^2 + 20) - 8r \cdot 2r}{(r^2 + 20)^2} \\
    \\
    &= \dfrac{8r^2 + 160 - 16r^2}{(r^2 + 20)^2} = \dfrac{-8r^2 + 160}{(r^2 + 20)^2}
\end{align*}

Deretter løser vi likningen:

$$
A'(r) = 0 \liff \dfrac{-8r^2 + 160}{(r^2 + 20)^2} = 0
$$

Det er bare telleren som kan medføre av brøken blir null, så vi setter telleren lik null:

$$
-8r^2 + 160 = 0 \liff 8r^2 = 160 \liff r^2 = 20 \liff r = \pm\sqrt{20}
$$

Vi kan faktorisere $20 = 4 \cdot 5$ som betyr at vi kan forenkle kvadratroten til 

$$
r = \pm \sqrt{20} = \pm \sqrt{4 \cdot 5} = \pm \sqrt{4} \cdot \sqrt{5} = \pm 2\sqrt{5}
$$

Det er bare den positive løsningen som er en del av definisjonsmengden. Vi må sjekke at dette er et toppunkt. Vi tegner et fortegnsskjema for $A'(r)$ for å sjekke:


:::{signchart}
width: 100%
function: (-8 * r**2 + 160) / (r**2 + 20)**2, $A'(r)$
:::

Vi ser at $A'(r) > 0$ rett før punktet og $A'(r) < 0$ rett etter punktet. Det betyr at grafen til $A$ stiger rett før og synker rett etter. Det betyr at $r = 2\sqrt{5}$ er et toppunkt. Dermed vil $r = 2\sqrt{5}$ gi det største arealet av rektangelet – eller?


Vi burde også argumentere for at arealet i endepunktene av definisjonsmengden er mindre enn arealet i dette toppunktet. Når $r = 0$ så er arealet $A(0) = 0$. Når $r \to \infty$ så vil $f(r) \to 0$ og dermed vil også arealet $A(r) \to 0$. Dermed er arealet i "endepunktene" mindre enn arealet i toppunktet. 

Så ja – $r = 2\sqrt{5}$ gir det største arealet av rektangelet.
```
````

::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 5

:::{cas-popup}
---
layout: sidebar
---
:::



Punktene på en halvsirkel oppfyller likningen

$$
x^2 + y^2 = 4 \qder y \geq 0.
$$

Et rektangel har hjørnene $(-x, 0)$, $(x, 0)$, $(x, f(x))$ og $(-x, f(-x))$ der $f$ er grafen til halvsirkelen.

Se figuren nedenfor.


Bestem $x$ slik at arealet av rektangelet er størst mulig.


:::{plot}
width: 70%
ticks: off 
xmin: -2.5
xmax: 2.5
ymin: -0.1
ymax: 2.5
function: sqrt(4 - x**2), (-2, 2), f
polygon: (-1.5, 0), (1.5, 0), (1.5, f(1.5)), (-1.5, f(-1.5))
point: (-1.5, 0)
point: (1.5, 0)
point: (1.5, f(1.5))
point: (-1.5, f(-1.5))
axis: equal
text: -1.5, 0, "$(-x, 0)$", bottom-center
text: 1.5, 0, "$(x, 0)$", bottom-center
text: 1.5, f(1.5), "$(x, f(x))$", top-right
text: -1.5, f(-1.5), "$(-x, f(-x))$", top-left
:::

::::{answer}
$$
x = \sqrt{2}
$$
::::


::::{solution}
Vi starter med å bestemme en funksjon $A(x)$ som gir arealet av rektangelet. Denne vil være gitt ved:

$$
A(x) = 2x \cdot f(x)
$$

Vi trenger et uttrykk for $f(x)$ som vi kan bestemme ved å løse likningen for halvsirkelen for $y$:

$$
x^2 + y^2 = 4 \liff y^2 = 4 - x^2 \limplies y = \sqrt{4 - x^2}
$$

Dermed vil $y(x) = \sqrt{4 - x^2}$. Vi kan dermed skrive arealfunksjonen som:

$$
A(x) = 2xy(x) = 2x \cdot \sqrt{4 - x^2}
$$


````{tab-set}
```{tab-item} Med CAS
For å bestemme ekstremalpunktene til $A$, må vi løse $A'(x) = 0$ og sjekke at $A''(x) < 0$ i punktet for å sikre at det er et toppunkt. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgave_5/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $A'(x) = 0$ når $x = \sqrt{2}$. Videre er $A''(\sqrt{2}) < 0$ som betyr at $A$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $x = \sqrt{2}$ et toppunkt. Derfor vil $x = \sqrt{2}$ gi det største arealet av rektangelet.

```
```{tab-item} Uten hjelpemidler

For å bestemme ekstremalpunktene til $A$, må vi løse $A'(x) = 0$. Vi deriverer funksjonen først:

\begin{align*}
    A'(x) &= 2 \cdot \sqrt{4 - x^2} + 2x \cdot \dfrac{(4 - x^2)'}{2\sqrt{4 - x^2}} \\
    \\
    &= 2 \cdot \sqrt{4 - x^2} + 2x \cdot \dfrac{-2x}{2\sqrt{4 - x^2}} \\
    \\
    &= 2 \cdot \sqrt{4 - x^2} - \dfrac{2x^2}{\sqrt{4 - x^2}} \\
    \\
    &= \dfrac{2(4 - x^2) - 2x^2}{\sqrt{4 - x^2}} = \dfrac{8 - 4x^2}{\sqrt{4 - x^2}}
\end{align*}

Så løser vi likningen $A'(x) = 0$. Brøken kan bare bli null dersom telleren er null, så vi setter telleren lik null:

$$
8 - 4x^2 = 0 \liff 4x^2 = 8 \liff x^2 = 2 \liff x = \pm \sqrt{2}
$$

Det er bare den positive løsningen som gir mening i denne sammenhengen. Vi må sjekke at dette er et toppunkt. Vi tegner et fortegnsskjema for $A'(x)$. Nevneren er positiv for alle $x$ i definisjonsmengden, så det holder å tegne et fortegnsskjema for telleren:

:::{signchart}
width: 100%
function: (8 - 4 * x**2), A'(x)
xmin: -2
xmax: 2
:::

```
````

::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 6

:::{cas-popup}
---
layout: sidebar
---
:::



Anna skal reise fra en holme som ligger $8$ km fra strandkanten. $12$ km fra det punktet på stranden som ligger nærmest holmen, ligger det en hytte. 
Anna kan ro med en fart på $2$ km/t og gå med en fart på $6$ km/t. Anna kan gå i land i hvilket som helst punkt $\ell$ på veien.

Se figuren nedenfor. 

:::{plot}
width: 70%
axis: off
xmin: -1
xmax: 13
ymax: 10
ymin: -2
point: (0, 8)
point: (4, 0)
point: (12, 0)
line-segment: (0, 8), (4, 0), blue, solid
hline: 0, -1, 13, solid, gray
vline: 0, 0, 8, dashed, gray
hline: 0, 4, 12, solid, red
text: 0, 8, "Holme", top-center
text: 12, 0, "Hytte", top-center
text: 4, 0, "$\ell$", top-right
bar: (-0.5, 0), 8, vertical
text: -0.5, 4, "8 km", center-left
bar: (0, -0.5), 4, horizontal
text: 2, -0.5, "$x$ km", bottom-center
bar: (0, -1.4), 12, horizontal
text: 6, -1.4, "12 km", bottom-center
text: 2, 4, "I vann", top-right
text: 8, -0.2, "På land", bottom-center
:::



::::{answer}
$$
x = 2\sqrt{2} \, \mathrm{km}
$$
::::

::::{solution}
Tiden Anna bruker vil være gitt ved strekningen $s$ hun reiser delt på farten $v$ hun har. Strekningen hun må ro før hun går i land er 

$$
s_\mathrm{vann}(x) = \sqrt{x^2 + 8^2} = \sqrt{x^2 + 64}
$$

Strekningen Anna må gå når hun er i land er 

$$
s_\mathrm{land}(x) = 12 - x
$$

Tiden Anna vil bruke på hver del av turen blir dermed: 

$$
T_\mathrm{vann}(x) = \dfrac{s_\mathrm{vann}}{v_\mathrm{vann}} = \dfrac{\sqrt{x^2 + 64}}{2} \and T_\mathrm{land}(x) = \dfrac{s_\mathrm{land}}{v_\mathrm{land}} = \dfrac{12 - x}{6}
$$

Den samlede tiden kan derfor beskrives av funksjonen

$$
T(x) = T_\mathrm{vann}(x) + T_\mathrm{land}(x) = \dfrac{\sqrt{x^2 + 64}}{2} + \dfrac{12 - x}{6}
$$


`````{tab-set}
````{tab-item} Med CAS
For å få kortest mulig tid, må vi bestemme ekstremalpunktene til $T$. Da løser vi $T'(x) = 0$ og sjekker at $T''(x) > 0$ i punktet:

:::{figure} ./figurer/oppgave_6/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $T'(x) = 0$ når $x = 2\sqrt{2}$. Vi ser også at $T''(2\sqrt{2}) > 0$ som betyr at punktet gir et bunnpunkt. Derfor må Anna gå i land $2\sqrt{2}$ km fra det punktet på stranden som ligger nærmest holmen for å få kortest mulig reisetid.

````

````{tab-item} Uten hjelpemidler
For å få kortest mulig tid, må vi finne ekstremalpunktene til $T$. Vi deriverer først funksjonen:

\begin{align*}
    T'(x) &= \left(\dfrac{\sqrt{x^2 + 64}}{2}\right)' + \left(\dfrac{12 - x}{6}\right)' \\
    \\
    &= \dfrac{1}{2} \cdot \dfrac{1}{2\sqrt{x^2 + 64}} \cdot (x^2 + 64)' + \dfrac{-1}{6} \\
    \\
    &= \dfrac{1}{2} \cdot \dfrac{2x}{2\sqrt{x^2 + 64}} - \dfrac{1}{6} \\
    \\
    &= \dfrac{x}{2\sqrt{x^2 + 64}} - \dfrac{1}{6} \\
    \\
    &= \dfrac{3x - \sqrt{x^2 + 64}}{6\sqrt{x^2 + 64}}
\end{align*}


Så løser vi likningen $T'(x) = 0$. Brøken kan bare bli null dersom telleren er null, så vi setter telleren lik null:

$$
3x - \sqrt{x^2 + 64} = 0 \liff 3x = \sqrt{x^2 + 64}
$$

Så kvadrarer vi begge sider:

$$
9x^2 = x^2 + 64 \liff 8x^2 = 64 \liff x^2 = 8 \liff x = \pm \sqrt{8}
$$

Det vil bare være den positive løsningen som gjør den opprinnelige likningen lik 0 (og det er også den eneste som er praktisk relevant). Vi kan skrive den enklere:

$$
x = \sqrt{8} = \sqrt{4 \cdot 2} = \sqrt{4} \cdot \sqrt{2} = 2\sqrt{2}
$$

Så tegner vi et fortegnsskjema for å sjekke at dette svarer til et bunnpunkt: 

:::{signchart}
width: 100%
function: (3 * x - sqrt(x**2 + 64)) / (6 * sqrt(x**2 + 64)), T'(x)
:::

Fra fortegnsskjema ser vi at $T'(x)$ er negativ før punktet og positiv etter, som betyr at grafen synker rett før og stiger rett etter. Dermed gir $x = 2\sqrt{2}$ et bunnpunkt, og Anna bør gå i land $2\sqrt{2}$ km fra det punktet på stranden som ligger nærmest holmen for å få kortest mulig reisetid.
````
`````


::::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 7

:::{cas-popup}
---
layout: sidebar
---
:::


En takrenne skal lages i form av et åpent trapes ved å brette to sidekanter fra et flatt rektangel slik at alle sidelengder i takrenna er $10$ cm og takrennen har en høyde på $x$ cm. Se figuren nedenfor.


Bestem høyden $x$ slik at mest mulig vann kan strømme gjennom takrenna.

:::{plot}
width: 70%
axis: off
xmin: -8.5
xmax: 18.5
ymin: -2
ymax: 8
line-segment: (0, 0), (10, 0), black, solid
line-segment: (0, 0), (-8, 6), black, solid
line-segment: (10, 0), (18, 6), black, solid
text: 5, 0, "10 cm", bottom-center
text: -4, 3, "10 cm", center-left
text: 14.2, 3, "10 cm", center-right
hline: 6, -8, 18, dashed, gray
vline: 0, 0, 6, dashed, gray
vline: 10, 0, 6, dashed, gray
text: 0, 3, "$x$ cm", center-right
lw: 1.5
figsize: (6, 4)
:::


::::{answer}
$$
5 \sqrt{3} \, \mathrm{cm}
$$
::::

::::{solution}
For at mest mulig vann skal strømme gjennom, må arealet av tverrsnittet til takrenna være størst mulig. Vi bestememr en funksjon for arealet:

$$
A(x) = 10x + x\sqrt{10^2 - x^2} = 10x + x\sqrt{100 - x^2}
$$

Vi må finne ekstremalpunktene til $A$. Da må vi løse $A'(x) = 0$ og sjekke om løsningen gir et toppunkt. 
Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgave_7/sol.png
---
class: no-click, adaptive-figure
width: 70%
---
:::

Fra utskriften ser vi at $A'(x) = 0$ når

$$
x = \pm 5 \sqrt{3}
$$

Det er bare den positive løsningen som gir mening. I tillegg så er $A''(5\sqrt{3}) < 0$ som betyr at $A$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $x = 5\sqrt{3}$ et toppunkt for $A$. Derfor vil det strømme mest vann gjennom takrenna dersom høyden er $5 \sqrt{3} \, \mathrm{cm}$.


::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8

:::{cas-popup}
---
layout: sidebar
---
:::



:::{plot}
width: 80%
ellipse: (0, 5), 3, 0.5, black, solid
ellipse: (0, 0), 3, 0.5, black, solid
line-segment: (-3, 0), (-3, 5), black, solid
line-segment: (3, 0), (3, 5), black, solid
figsize: (3, 4)
ymin: -1
axis: off
align: right
bar: (3.8, 0), 5, v
text: 3.8, 2.5, "$h$", center-right
bar: (0, 6), 3, h
text: 1.5, 6, "$r$", top-center
hline: 5, 0, 3, dashed, gray
:::

En sylinder har overflateareal $A = 32\pi$. 

Bestem hvilken høyde $h$ og radius $r$ som gir sylinderen størst mulig volum.


:::{clear}
:::



::::{answer}
$$
r = \dfrac{4\sqrt{3}}{3} \and h = \dfrac{8\sqrt{3}}{3}
$$
::::


::::{solution}
Overflatearealet $A$ kan uttrykkes som

$$
A = 2\pi r^2 + 2\pi rh = 32\pi
$$

Volumet er gitt ved 

$$
V = \pi r^2 h
$$

Vi kan bestemme en funksjon $V(r)$ eller en funksjon $V(h)$ ved å bruke likningen for overflatearealet. 
Siden $r^2$ opptrer i begge uttrykk, er det enklere å løse likningen for overflatearealet for $h$ og erstatte dette i uttrykket for volumet $V$:

$$
2\pi r^2 + 2\pi r h = 32\pi
$$

$$
r^2 + rh = 16
$$

$$
rh = 16 - r^2 \liff h(r) = \dfrac{16 - r^2}{r}
$$


Så setter vi uttrykket for $h$ inn i uttrykket for volumet: 

$$
V(r) = \pi r^2 h(r) = \pi r^2 \cdot \dfrac{16 - r^2}{r} = \pi r(16 - r^2) = \pi(16r - r^3)
$$

````{tab-set}
```{tab-item} Med CAS
For å bestemme ekstremalpunktene til $V$, må vi løse $V'(r) = 0$ og sjekke at $V''(r) < 0$ i punktet for å sikre at det er et toppunkt. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgave_8/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $V'(r) = 0$ når $x = \dfrac{4\sqrt{3}}{3}$. Vi ser også at $V''\left(\dfrac{4\sqrt{3}}{3}\right) < 0$ som betyr at $V$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $r = \dfrac{4\sqrt{3}}{3}$ et toppunkt. Vi trenger også høyden ved denne radien, så vi også kan regne ut med CAS: 

:::{figure} ./figurer/oppgave_8/sol_2.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Dermed er volumet størst mulig hvis 

$$
r = \dfrac{4\sqrt{3}}{3} \and h = \dfrac{8\sqrt{3}}{3}
$$

```
```{tab-item} Uten hjelpemidler

Vi må finne ekstremalpunktene til $V(r)$. Vi deriverer først funksjonen:

$$
V'(r) = \pi(16 - 3r^2)
$$

Så løser vi likningen $V'(r) = 0$:

$$
V'(r) = 0 \liff \pi(16 - 3r^2) = 0
$$

$$
16 - 3r^2 = 0 \liff 3r^2 = 16 \liff r^2 = \dfrac{16}{3}
$$

som gir at

$$
r = \sqrt{\dfrac{16}{3}} = \dfrac{4}{\sqrt{3}} = \dfrac{4\sqrt{3}}{3}
$$

Vi må sjekke at dette gir et toppunkt for $V(r)$. Vi tegner et fortegnsskjema for $V'(r)$. Da er det først hensiktsmessig å faktorisere $V'(r)$:

$$
V'(r) = \pi(16 - 3r^2) = -3\pi(r^2 - \dfrac{16}{3}) = -3\pi(r - \dfrac{4\sqrt{3}}{3})(r + \dfrac{4\sqrt{3}}{3})
$$

Så tegner vi skjemaet:

:::{signchart}
width: 100%
function: pi * (16 - 3 * r**2), $V'(r)$
:::

Vi ser at $V'(r) > 0$ rett før punktet og $V'(r) < 0$ rett etter punktet. Det betyr at grafen til $V$ stiger rett før og synker rett etter. Dermed betyr at $r = \dfrac{4\sqrt{3}}{3}$ svarer til toppunkt.


Høyden til sylinderen er da 

\begin{align*}
    h\left(\dfrac{4\sqrt{3}}{3}\right) &= \dfrac{16 - \left(\dfrac{4\sqrt{3}}{3}\right)^2}{\dfrac{4\sqrt{3}}{3}} = \dfrac{16 - \dfrac{16}{3}}{\dfrac{4\sqrt{3}}{3}} \\
    \\
    &= \dfrac{\dfrac{48}{3} - \dfrac{16}{3}}{\dfrac{4\sqrt{3}}{3}} = \dfrac{\dfrac{32}{3}}{\dfrac{4\sqrt{3}}{3}} = \dfrac{32}{4\sqrt{3}} = \dfrac{8}{\sqrt{3}} = \dfrac{8\sqrt{3}}{3}
\end{align*}

Altså er volumet størst mulig hvis

$$
r = \dfrac{4\sqrt{3}}{3} \and h = \dfrac{8\sqrt{3}}{3}
$$
```
````

::::

:::::::::::::::






---








:::::::::::::::{exercise} Oppgave 9


:::{cas-popup}
---
layout: sidebar
---
:::



En kurve er gitt ved grafen til funksjonen $f(x) = x^2$. I samme figur er et punkt $P(6, 3)$. 
Et linjestykke $\ell$ går fra punktet $P$ til et punkt på grafen.

Bestem koordinatene til punktet på grafen som gjør at $\ell$ blir kortest mulig. Bestem et eksakt uttrykk for lengden av $\ell$ i dette tilfellet.

:::{plot}
width: 70%
function: x**2, f
point: (5, 3)
text: 5, 3, "$P(6, 3)$", top-right
ymin: -1 
ymax: 8
xmin: -3
hline: 3, 2.5, 5, dashed, gray
vline: 2.5, 3, f(2.5), dashed, gray
point: (2.5, f(2.5))
text: 2.5, f(2.5), "$(x, f(x))$", top-right
line-segment: (5, 3), (2.5, f(2.5)), red, solid
text: 3.7, 4.5, "$\ell$", top-right
ticks: off
polygon: (2.5, 3), (2.8, 3), (2.8, 3.4), (2.5, 3.4)
:::

::::{answer}
* Koordinatene til punktet på grafen er $(2, 4)$
* Lengden til linjestykket er da $\sqrt{17}$
::::


::::{solution}
Avstanden fra punktet $P(6, 3)$ til et punkt på grafen $(x, f(x))$ kan vi uttrykke ved hjelp av Pytagoras' setning:

$$
d(x) = \sqrt{(x - 6)^2 + (f(x) - 3)^2} = \sqrt{(x - 6)^2 + (x^2 - 3)^2}
$$

````{tab-set}
```{tab-item} Med CAS
For å bestemme ekstremalpunktene til $d$, må vi løse $d'(x) = 0$ og sjekke at $d''(x) > 0 i punktet for å sikre at det er et bunnpunkt. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgave_9/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $d'(x) = 0$ når $x = 2$. Vi ser også at $d''(2) > 0$ som betyr at $d$ er konveks {polyicon}`smile` i nabolaget til punktet. Dermed gir $x = 2$ et bunnpunkt. Derfor vil linjestykket $\ell$ bli kortest mulig når det går fra $P(6, 3)$ til punktet $(2, f(2)) = (2, 4)$ på grafen. Vi ser også at $d(2) = \sqrt{17}$ som er lengden av linjestykket i dette tilfellet.

```

```{tab-item} Uten hjelpemidler (*at your own risk* ☢️)
For å bestemme ekstremalpunktene til $d$, må vi løse $d'(x) = 0$. Men det er ganske slitsomt å derivere $d(x)$ direkte fordi det er en kvadratrotfunksjon med en sum av polynomer inni. I tilfeller som dette, kan vi lage en ny funksjon $D(x)$ som er $d(x)$ opphøyd i andre: 

$$
D(x) = d(x)^2
$$

Den deriverte av $D(x)$ vil da etter kjerneregelen være:

$$
D'(x) = 2d(x) \cdot d'(x)
$$

Setter vi $D'(x) = 0$ så får vi

$$
D'(x) = 0 \liff 2d(x) \cdot d'(x) = 0
$$

Men etter produktregelen for likninger får vi da 

$$
D'(x) = 0 \liff d(x) = 0 \or d'(x) = 0
$$

Vi vet allerede at det ikke finnes noen løsning for $d(x) = 0$ siden lengden på linjestykket kan ikke bli null når punktet ligger utenfor grafen. Dermed vil 

$$
D'(x) = 0 \liff d'(x) = 0
$$

Vi deriverer derfor $D(x)$:

\begin{align*}
    D'(x) &= \left((x - 6)^2 + (x^2 - 3)^2\right)' = 2(x - 6) + 2(x^2 - 3) \cdot 2x \\
    \\
    &= 2(x - 6) + 4x(x^2 - 3) = 2x - 12 + 4x^3 - 12x \\
    \\
    &= 4x^3 - 10x - 12
\end{align*}

Vi får en tredjegradslikning som ikke er så enkel å angripe direkte. Men vi kan merke oss at tredjegradslikningen *kan* være null for alle heltall som deler konstandleddet. Da har vi kandidatene:

$$
x \in \{\pm 1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 12\}
$$

Vi prøver oss frem systematisk:

:::{horner}
---
p: 4x^3 - 10x - 12
x: 1
width: 50% 
---
:::

Resten er ikke 0, så vi går videre til neste mulighet:

:::{horner}
---
p: 4x^3 - 10x - 12
x: -1
width: 50%
---
:::

Resten er fortsatt ikke 0, så vi går videre:

:::{horner}
---
p: 4x^3 - 10x - 12
x: 2
width: 50%
---
:::

Her ble resten null. Vi kan også lese av at kvotienten er $4x^2 + 8x + 6$. Dermed kan vi faktorisere tredjegradspolynomet som:

$$
4x^3 - 10x - 12 = (x - 2)(4x^2 + 8x + 6)
$$

Vi kan forsøke å faktorisere andregradspolynomet, men først kan vi sjekke verdien til diskriminanten for å se om det finnes noen nullpunkter:

$$
b^2 - 4ac = 8^2 - 4 \cdot 4 \cdot 6 = 64 - 96 = -32
$$

Diskriminanten er negativ, så da kan vi ikke faktorisere andregradspolynomet. Det betyr at det er kun $x = 2$ som gir $D'(x) = 0$, og dermed også $d'(x) = 0$. Vi må bekrefte at dette er et bunnpunkt: 

$$
D''(x) = (4x^3 - 10x - 12)' = 12x^2 - 10
$$

Men vi må vite hvordan $D''(x)$ henger sammen med $d''(x)$ siden det er $d(x)$ som beskriver avstanden vi er interessert i. Vi deriverer $D'(x)$ en gang til:

$$
D''(x) = (2d'(x) \cdot d(x))' = 2d''(x) \cdot d(x) + 2(d'(x))^2
$$

I ekstremalpunktet $x = m$ vil $d'(m) = 0$, slik at 

$$
D''(m) = 2d''(m) \cdot d(m)
$$

Vi vet at $d(m) > 0$, så da vil $D''(m)$ og $d''(m)$ ha samme fortegn. Dermed kan vi undersøke fortegnet til $D''(x)$ for å avgjøre om vi har et bunnpunkt eller toppunkt for $d(x)$.

Vi setter inn $x = 2$:

$$
D''(2) = 12 \cdot 2^2 - 10 = 48 - 10 = 38 > 0
$$

Siden $D''(2) > 0$, betyr det at $D$ er konveks {polyicon}`smile` i nabolaget til punktet. Dermed gir $x = 2$ et bunnpunkt for $D$, og dermed også for $d$. Derfor vil linjestykket $\ell$ bli kortest mulig når det går fra $P(6, 3)$ til punktet $(2, f(2)) = (2, 4)$ på grafen. Vi kan også regne ut lengden av linjestykket i dette tilfellet:

$$
D(2) = (2 - 6)^2 + (f(2) - 3)^2 = (-4)^2 + (4 - 3)^2 = 16 + 1 = 17
$$

Avstanden er da 

$$
d(2) = \sqrt{D(2)} = \sqrt{17}
$$


```
````


::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 10
:::{cas-popup}
---
layout: sidebar
---
:::


Punktene på en parabel tilfredsstiller likningen

$$
x = (y - 1)^2 - 2.
$$ 

Kurven til parabelen er vist i figuren nedenfor.

Bestem en eksakt verdi for den korteste avstanden fra punktet $P(-2, 4)$ til kurven.

:::{plot}
width: 70%
curve: (t - 1)**2 - 2, t, (-10, 10), solid, blue
point: (-2, 4)
text: -2, 4, "$P(-2, 4)$", top-left
ticks: off
:::


::::{answer}
$$
\sqrt{5}
$$
::::

::::{solution}

Avstanden fra punktet $P(-2, 4)$ til et punkt på parabelen $(x, y)$ kan vi uttrykke ved hjelp av Pytagoras' setning:

\begin{align*}
    d &= \sqrt{(x + 2)^2 + (y - 4)^2} = \sqrt{\left((y - 1)^2 - 2 + 2\right)^2 + (y - 4)^2} \\
    \\
    &= \sqrt{(y - 1)^4 + (y - 4)^2}
\end{align*}

Vi har derfor en funksjon $d(y)$ for avstanden fra punktet $P$ til et punkt på parabelen. Vi må finne ekstremalpunktene til $d$. Da må vi løse $d'(y) = 0$ og sjekke at løsningen gir et bunnpunkt for at vi skal få kortest mulig avstand. Vi gjør dette med CAS:


:::{figure} ./figurer/oppgave_10/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Fra utskriften ser vi at $d'(y) = 0$ når $y = 2$. Da er $d''(2) > 0$ som betyr at $d$ er konveks {polyicon}`smile` i nabolaget til punktet. Dermed gir $y = 2$ et bunnpunkt. Derfor vil den korteste avstanden fra punktet $P(-2, 4)$ til kurven være når vi går til punktet på kurven der $y = 2$. Fra utskriften ser vi at $d(2) = \sqrt{5}$ som er den korteste avstanden.






::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 11

:::{cas-popup}
---
layout: sidebar
---
:::


Et punkt $A$ ligger en avstand $2$ fra en linje $\ell$. Et annet punkt $C$ ligger en avstand $4$ fra linjen $\ell$.

Et punkt $B$ skal plasseres på $\ell$ slik at summen av linjestykkene $AB + BC$ blir minst mulig.

Se figuren nedenfor.

Bestem den minste verdien for summen av linjestykkene $AB + BC$. 


:::{plot}
width: 70%
axis: off
xmin: -1
xmax: 10
ymax: 5
ymin: -2
hline: 0, -1, 10, solid
vline: 0, 0, 2, dashed, gray
vline: 9, 0, 4, dashed, gray
point: (0, 2)
point: (4, 0)
point: (9, 4)
line-segment: (0, 2), (4, 0), black, solid
line-segment: (4, 0), (9, 4), black, solid
vline: 0.65, 0, 0.4, solid, black
hline: 0.4, 0, 0.65, solid, black
vline: 8.35, 0, 0.4, solid, black
hline: 0.4, 9, 8.35, solid, black
text: 4, 0, "$B$", top-center
text: 0, 2, "$A$", top-left
text: 9, 4, "$C$", top-right
lw: 1.5
point: (0, 0)
text: 10, 0, "$\ell$", center-right
bar: (0, -0.4), 9, horizontal
text: 4.5, -0.4, "$9$", bottom-center
bar: (-0.5, 0), 2, vertical
text: -0.5, 1, "$2$", center-left
bar: (9.5, 0), 4, vertical
text: 9.5, 2, "$4$", center-right
:::


::::{answer}
$$
3\sqrt{13}
$$
::::


::::{solution}
Vi lar $x$ være avstanden fra det punktet på linja $\ell$ som ligger nærmest $A$ bort til punktet $B$. Da vil avstanden fra $B$ bort til det punktet på $\ell$ som ligger nærmest $C$ være $9 - x$. Bruker vi Pytagoras' setning, får vi da at linjestykket $AB$ er:

$$
AB = \sqrt{x^2 + 2^2} = \sqrt{x^2 + 4}
$$

På tilsvarende vis vil linjestykket $BC$ være

$$
BC = \sqrt{(9 - x)^2 + 4^2} = \sqrt{(x - 9)^2 + 16}
$$

Vi kan lage en funksjon $L(x)$ som gir summen av de to linjestykkene:

$$
L(x) = AB + BC = \sqrt{x^2 + 4} + \sqrt{(x - 9)^2 + 16}
$$

````{tab-set}
```{tab-item} Med CAS
For å bestemme ekstremalpunktene til $L$, må vi løse $L'(x) = 0$ og sjekke at $L''(x) > 0 i punktet for å sikre at det er et bunnpunkt. Vi bruker CAS til å utføre selve regningen:

:::{figure} ./figurer/oppgave_11/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $L'(x) = 0$ når $x = 3$. Vi ser også at $L''(3) > 0$ som betyr at $L$ er konveks {polyicon}`smile` i nabolaget til punktet. Dermed gir $x = 3$ et bunnpunkt. Derfor vil summen av linjestykkene $AB + BC$ bli minst mulig når $B$ ligger $3$ enheter fra punktet på linja $\ell$ som ligger nærmest $A$. Vi kan også regne ut den minste verdien for summen av linjestykkene i dette tilfellet (med CAS):

:::{figure} ./figurer/oppgave_11/sol_2.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Altså er den minste verdien for summen av linjestykkene $AB + BC$ lik $3\sqrt{13}$.

```
```{tab-item} Uten hjelpemidler ☣️

For å bestemme $x$ slik at summen blir så liten som mulig, må vi lete etter ekstremalpunktene til $L$. Da løser vi $L'(x) = 0$. Men først deriverer vi:

\begin{align*}
    L'(x) &= \left(\sqrt{x^2 + 4}\right)' + \left(\sqrt{(x - 9)^2 + 16}\right)' \\
    \\
    &= \dfrac{1}{2 \sqrt{x^2 + 4}} \cdot (x^2 + 4)' + \dfrac{1}{2 \sqrt{(x - 9)^2 + 16}} \cdot ((x - 9)^2 + 16)' \\
    \\
    &= \dfrac{2x}{2 \sqrt{x^2 + 4}} + \dfrac{2(x - 9)}{2 \sqrt{(x - 9)^2 + 16}} \\
    \\
    &= \dfrac{x}{\sqrt{x^2 + 4}} + \dfrac{x - 9}{\sqrt{(x - 9)^2 + 16}} \\
    \\
    &= \dfrac{x \sqrt{(x - 9)^2 + 16} + (x - 9)\sqrt{x^2 + 4}}{\sqrt{x^2 + 4} \cdot \sqrt{(x - 9)^2 + 16}}
\end{align*}

Deretter setter vi $L'(x) = 0$. Det vil bare være telleren som kan medføre at brøken blir null, så vi setter telleren lik null:

$$
x \sqrt{(x - 9)^2 + 16} + (x - 9)\sqrt{x^2 + 4} = 0
$$

Vi skriver det om til:

$$
x \sqrt{(x - 9)^2 + 16} = - (x - 9)\sqrt{x^2 + 4}
$$

Så kvadrerer vi begge sider:

$$
x^2 \left((x - 9)^2 + 16\right) = (x - 9)^2 (x^2 + 4)
$$

Utvider vi begge sider, får vi:

$$
x^2 (x^2 - 18x + 81 + 16) = (x^2 - 18x + 81)(x^2 + 4)
$$

$$
x^4 - 18x^3 + 97x^2 = x^4 - 18x^3 + 81x^2 + 4x^2 - 72x + 324
$$

Vi forenkler likningen ved å stryke bort alle ledd som er felles på hver side:

$$
97x^2 = 85x^2 - 72x + 324
$$

Så skriver vi om likningen til standardform:

$$
-12x^2 - 72x + 324 = 0
$$

Vi har at $72 = 6 \cdot 12$ og $324 = 27 \cdot 12$, så vi kan dele likningen med $-12$ i alle ledd for å forenkle den:

$$
x^2 + 6x - 27 = 0
$$

Så bruker vi $abc$-formelen:

\begin{align*}
    x &= \dfrac{-6 \pm \sqrt{6^2 - 4 \cdot 1 \cdot (-27)}}{2 \cdot 1} = \dfrac{-6 \pm \sqrt{36 + 108}}{2}\\
    \\
    x &= \dfrac{-6 \pm \sqrt{144}}{2} = \dfrac{-6 \pm 12}{2}
\end{align*}

Vi får da to løsninger:

$$
x = \dfrac{-6 + 12}{2} = 3 \or x = \dfrac{-6 - 12}{2} = -9
$$

Å sjekke om $L''(x) > 0$ i punktet er et *mareritt*. Men vi uten hjelpemidler får vi bite i det sure eplet.

Vi har at 

$$
L'(x) = \dfrac{x}{\sqrt{x^2 + 4}} + \dfrac{x - 9}{\sqrt{(x - 9)^2 + 16}}
$$

Vi deriverer hvert ledd for ryddighetens skyld:

\begin{align*}
    \left(\dfrac{x}{\sqrt{x^2 + 4}}\right)' &= \dfrac{(x)' \cdot \sqrt{x^2 + 4} - x \cdot \left(\sqrt{x^2 + 4}\right)'}{(\sqrt{x^2 + 4})^2} \\
    \\
    &= \dfrac{\sqrt{x^2 + 4} - x \cdot \dfrac{1}{2\sqrt{x^2 + 4}} \cdot (x^2 + 4)'}{x^2 + 4} \\
    \\
    &= \dfrac{\sqrt{x^2 + 4} - x \cdot \dfrac{1}{2\sqrt{x^2 + 4}} \cdot 2x}{x^2 + 4} \\
    \\
    &= \dfrac{\sqrt{x^2 + 4} - \dfrac{x^2}{\sqrt{x^2 + 4}}}{x^2 + 4} = \dfrac{\dfrac{x^2 + 4 - x^2}{\sqrt{x^2 + 4}}}{x^2 + 4} \\
    \\
    &= \dfrac{4}{(x^2 + 4)^{3/2}}
\end{align*}

Så deriverer vi det andre leddet:

\begin{align*} 
    &\left(\dfrac{x - 9}{\sqrt{(x - 9)^2 + 16}}\right)'\\
    \\
    &= \dfrac{(x - 9)' \cdot \sqrt{(x - 9)^2 + 16} - (x - 9) \cdot \left(\sqrt{(x - 9)^2 + 16}\right)'}{(\sqrt{(x - 9)^2 + 16})^2} \\
    \\
    &= \dfrac{\sqrt{(x - 9)^2 + 16} - (x - 9) \cdot \dfrac{1}{2\sqrt{(x - 9)^2 + 16}} \cdot ((x - 9)^2 + 16)'}{(x - 9)^2 + 16} \\
    \\
    &= \dfrac{\sqrt{(x - 9)^2 + 16} - (x - 9) \cdot \dfrac{1}{2\sqrt{(x - 9)^2 + 16}} \cdot 2(x - 9)}{(x - 9)^2 + 16} \\
    \\
    &= \dfrac{\sqrt{(x - 9)^2 + 16} - \dfrac{(x - 9)^2}{\sqrt{(x - 9)^2 + 16}}}{(x - 9)^2 + 16} \\
    \\
    &= \dfrac{\dfrac{(x - 9)^2 + 16 - (x - 9)^2}{\sqrt{(x - 9)^2 + 16}}}{(x - 9)^2 + 16} \\
    \\
    &= \dfrac{16}{((x - 9)^2 + 16)^{3/2}}
\end{align*}

Den andrederiverte er derfor:

$$
L''(x) = \dfrac{4}{(x^2 + 4)^{3/2}} + \dfrac{16}{((x - 9)^2 + 16)^{3/2}}
$$

Både telleren og nevneren i begge ledd er positive for alle $x \in \langle 0, 9\rangle$. Derfor er $L''(x) > 0$ for alle $x \in \langle 0, 9\rangle$.

Altså er $L''(3) > 0$, som betyr at $L$ er konveks {polyicon}`smile` i nabolaget til punktet. Dermed gir $x = 3$ et bunnpunkt for $L$. Derfor vil summen av linjestykkene $AB + BC$ bli minst mulig når $B$ ligger $3$ enheter fra punktet på linja $\ell$ som ligger nærmest $A$. Da kan vi regne ut den minste verdien for summen av linjestykkene i dette tilfellet:

\begin{align*}
    L(3) &= \sqrt{3^2 + 4} + \sqrt{(3 - 9)^2 + 16} \\
    \\
    &= \sqrt{9 + 4} + \sqrt{36 + 16} = \sqrt{13} + \sqrt{52} = \sqrt{13} + 2\sqrt{13} = 3\sqrt{13}
\end{align*}

```
````


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 12
:::{cas-popup}
---
layout: sidebar
---
:::


En likebeint trekant skal innskrives i en sirkel med radius $1$. 

Bestem en eksakt verdi for det største arealet en slik trekant kan ha.


:::{plot}
width: 50%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
polygon: (0, 1), (cos(-pi/4), sin(-pi/4)), (cos(pi + pi/4), sin(pi + pi/4))
fontsize: 30
:::


::::{hints} Vanskelig å komme i gang? Her er en hjelpefigur!
Nedenfor vises en mindre rettvinklet trekant som er tegnet inn som du kan bruke for å hjelpe deg å finne et uttrykk for arealet av den store trekanten.

:::{plot}
width: 55%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
polygon: (0, 1), (cos(-pi/4), sin(-pi/4)), (cos(pi + pi/4), sin(pi + pi/4))
line-segment: (0, 0), (0, sin(-pi/4)), black, dashed
line-segment: (0, 0), (cos(pi + pi/4), sin(pi + pi/4)), black, dashed
text: 0.5 * (cos(pi + pi/4)), 0.5 * (sin(pi + pi/4)) + 0.15, "$1$", center-center
text: 0 + 0.1, 0.5 * sin(-pi/4), "$x$", center-center
text: 0.5 * cos(pi + pi/4), sin(pi + pi/4) - 0.1, "$\ell$", center-center
fontsize: 30
polygon: (0, sin(-pi/4)), (-0.15, sin(-pi/4)), (-0.15, sin(-pi/4) + 0.15), (0, sin(-pi/4) + 0.15)
:::
::::


::::{answer}
$$
\dfrac{3\sqrt{3}}{4}
$$
::::


::::{solution}
:::{plot}
align: right
width: 100%
curve: cos(t), sin(t), (0, 2*pi), solid, blue
axis: equal
axis: off
polygon: (0, 1), (cos(-pi/4), sin(-pi/4)), (cos(pi + pi/4), sin(pi + pi/4))
line-segment: (0, 0), (0, sin(-pi/4)), black, dashed
line-segment: (0, 0), (cos(pi + pi/4), sin(pi + pi/4)), black, dashed
text: 0.5 * (cos(pi + pi/4)), 0.5 * (sin(pi + pi/4)) + 0.15, "$1$", center-center
text: 0 + 0.1, 0.5 * sin(-pi/4), "$x$", center-center
text: 0.5 * cos(pi + pi/4), sin(pi + pi/4) - 0.1, "$\ell$", center-center
fontsize: 30
polygon: (0, sin(-pi/4)), (-0.15, sin(-pi/4)), (-0.15, sin(-pi/4) + 0.15), (0, sin(-pi/4) + 0.15)
:::
Vi lager en hjelpefigur der vi lager en mindre rettvinklet som vi kan bruke til å finne et uttrykk for arealet av den store trekanten som vist til høyre.

Vi trenger å et uttrykk for grunnlinja og høyden til trekanten for å kunne finne et uttrykk for arealet.

Fra Pytagoras' setning har vi at 

$$
\ell^2 + x^2 = 1^2
$$

Vi kan løse denne likningen for $\ell$:

$$
\ell = \sqrt{1 - x^2}
$$

:::{clear}
:::

Grunnlinjen $g$ til den store trekanten er da $g = 2\ell$. 

Høyden til trekanten vil være $h = x + 1$. 

Arealet $A$ av trekanten kan da skrives som:

$$
A = \dfrac{g \cdot h}{2} = \dfrac{2\ell \cdot h}{2} = \ell \cdot h
$$

Setter vi inn uttrykket for $\ell$ og $h$, får vi funksjonen

$$
A(x) = \ell \cdot h = \sqrt{1 - x^2} \cdot (x + 1) = (x + 1)\sqrt{1 - x^2}
$$

````{tab-set}
```{tab-item} Med CAS
For å bestemme det største arealet $A$ vi kan få, så løser vi $A'(x) = 0$ og sjekker at $A''(x) < 0$ i punktet for å sikre at det er et toppunkt. Vi bruker CAS til å utføre selve regningen:


:::{figure} ./figurer/oppgave_12/sol.png
---
class: no-click, adaptive-figure
width: 60%
---
:::

Vi ser at $x = \dfrac{1}{2}$ er et ekstremalpunkt og vi ser at $A''\left(\dfrac{1}{2}\right) < 0$ som betyr at $A$ er konkav {polyicon}`frown` i nabolaget til punktet. Dermed gir $x = \dfrac{1}{2}$ et toppunkt. Derfor vil arealet $A$ bli størst mulig når $x = \dfrac{1}{2}$. Fra utskriften kan vi da også konkludere at det eksakte største arealet er

$$
A\left(\dfrac{1}{2}\right) = \dfrac{3\sqrt{3}}{4}
$$


```
```{tab-item} Uten hjelpemidler
For å bestemme mulige ekstremalpunkter for $A(x)$, må vi løse $A'(x) = 0$. Vi deriverer derfor $A(x)$ først: 

\begin{align*}
    A'(x) &= \left((x + 1)\sqrt{1 - x^2}\right)' \\
    \\
    &= (x + 1)' \cdot \sqrt{1 - x^2} + (x + 1) \cdot \left(\sqrt{1 - x^2}\right)' \\
    \\
    &= 1 \cdot \sqrt{1 - x^2} + (x + 1) \cdot \dfrac{1}{2\sqrt{1 - x^2}} \cdot (1 - x^2)' \\
    \\
    &= \sqrt{1 - x^2} + (x + 1) \cdot \dfrac{1}{2\sqrt{1 - x^2}} \cdot (-2x) \\
    \\
    &= \sqrt{1 - x^2} - \dfrac{x(x + 1)}{\sqrt{1 - x^2}} \\
    \\
    &= \dfrac{(1 - x^2) - x(x + 1)}{\sqrt{1 - x^2}} = \dfrac{1 - x^2 - x^2 - x}{\sqrt{1 - x^2}} \\
    \\
    &= \dfrac{1 - 2x^2 - x}{\sqrt{1 - x^2}} \\
    \\
    &= -\dfrac{2x^2 + x - 1}{\sqrt{1 - x^2}}
\end{align*}

For å løse $A'(x) = 0$ setter vi telleren lik null:

$$
2x^2 + x - 1 = 0
$$

Vi løser likningen med $abc$-formelen:

$$
x = \dfrac{-1 \pm \sqrt{1^2 - 4 \cdot 2 \cdot (-1)}}{2 \cdot 2} = \dfrac{-1 \pm \sqrt{1 + 8}}{4} = \dfrac{-1 \pm 3}{4}
$$

Vi får da to løsninger:

$$
x = \dfrac{-1 + 3}{4} = \dfrac{1}{2} \or x = \dfrac{-1 - 3}{4} = -1
$$

Den negative løsningen gir ikke praktisk mening og vil også medføre at nevneren blir lik 0, så vi må forkaste den. Vi må derfor undersøke om $x = \dfrac{1}{2}$ gir et toppunkt. Vi tegner et fortegnsskjema for å oppnå dette. Nevneren vil være positiv for alle $x \in \langle -1, 1\rangle$, så det holder å tegne et fortegnsskjema med faktorene i telleren for å bestemme fortegnslinja til $A'(x)$:

:::{signchart}
width: 100%
function: -(2*x**2 + x - 1), A'(x)
:::

Vi ser at $A'(x)$ skifter fra positiv til negativ når vi passerer $x = \dfrac{1}{2}$ fra venstre mot høyre. Derfor har vi et toppunkt når $x = \dfrac{1}{2}$. Vi kan da regne ut det største arealet:

\begin{align*}
    A\left(\dfrac{1}{2}\right) &= \left(\dfrac{1}{2} + 1\right) \sqrt{1 - \left(\dfrac{1}{2}\right)^2} \\
    \\
    &= \dfrac{3}{2} \cdot \sqrt{1 - \dfrac{1}{4}}\\
    \\
    &= \dfrac{3}{2} \cdot \sqrt{\dfrac{3}{4}} \\
    \\
    &= \dfrac{3}{2} \cdot \dfrac{\sqrt{3}}{2} \\
    \\
    &= \dfrac{3\sqrt{3}}{4}
\end{align*}

Altså er det eksakte største arealet en slik trekant kan ha lik $\dfrac{3\sqrt{3}}{4}$.

```
````
::::


:::::::::::::::
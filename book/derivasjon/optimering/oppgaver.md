# Størst og minst verdi


> Oppgaver 


:::::::::::::::{exercise} Oppgave 1
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
::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2

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
::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 3


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
nocache:
:::

Vi ser at $A'(k) > 0$ rett før $k = \sqrt{3}$ og $A'(k) < 0$ rett etter. Det betyr at grafen til $A(k)$ stiger rett før punktet og synker rett etter. Men da gir $k = \sqrt{3}$ et toppunkt. Dermed vil $k = \sqrt{3}$ gi det største arealet av trekanten.

::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4


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
nocache:
:::

Vi ser at $A'(r) > 0$ rett før punktet og $A'(r) < 0$ rett etter punktet. Det betyr at grafen til $A$ stiger rett før og synker rett etter. Det betyr at $r = 2\sqrt{5}$ er et toppunkt. Dermed vil $r = 2\sqrt{5}$ gi det største arealet av rektangelet – eller?


Vi burde også argumentere for at arealet i endepunktene av definisjonsmengden er mindre enn arealet i dette toppunktet. Når $r = 0$ så er arealet $A(0) = 0$. Når $r \to \infty$ så vil $f(r) \to 0$ og dermed vil også arealet $A(r) \to 0$. Dermed er arealet i "endepunktene" mindre enn arealet i toppunktet. 

Så ja – $r = 2\sqrt{5}$ gir det største arealet av rektangelet.

::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 5
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

Dermed vil $f(x) = \sqrt{4 - x^2}$. Vi kan dermed skrive arealfunksjonen som:

$$
A(x) = 2x \cdot \sqrt{4 - x^2}
$$

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
nocache:
:::

::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 6
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

::::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 9

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

:::{figure} ./figurer/oppgave_9/sol.png
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


:::::::::::::::{exercise} Oppgave 10

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

::::

:::::::::::::::






---








:::::::::::::::{exercise} Oppgave 11
En kurve er gitt ved grafen til funksjonen $f(x) = x^2$. I samme figur er et punkt $P(5, 3)$. 
Et linjestykke $\ell$ går fra punktet $P$ til et punkt på grafen.

Bestem koordinatene til punktet på grafen som gjør at $\ell$ blir kortest mulig.

:::{plot}
width: 70%
function: x**2, f
point: (5, 3)
text: 5, 3, "$P(5, 3)$", top-right
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


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 12
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

Bestem den korteste avstanden fra punktet $P(-2, 4)$ til kurven.

:::{plot}
width: 70%
curve: (t - 1)**2 - 2, t, (-10, 10), solid, blue
point: (-2, 4)
text: -2, 4, "$P(-2, 4)$", top-left
ticks: off
:::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave X

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

$$
x = \dfrac{-6 \pm \sqrt{6^2 - 4 \cdot 1 \cdot (-27)}}{2 \cdot 1} = \dfrac{-6 \pm \sqrt{36 + 108}}{2} = \dfrac{-6 \pm \sqrt{144}}{2} = \dfrac{-6 \pm 12}{2}
$$

Vi får da to løsninger:

$$
x = \dfrac{-6 + 12}{2} = 3 \or x = \dfrac{-6 - 12}{2} = -9
$$

Det er bare den positive løsningen som gir mening, så kandidaten vår for å få minst mulig sum av linjestykkene er $x = 3$. Ut ifra den praktiske problemstillingen, så vet vi at hvis vi setter $x = 0$ eller $x = 9$, så vil summen av linjestykkene være større enn for alle $x \in \langle 0, 9\rangle$. Dermed vil $x = 3$ gi den minste summen av linjestykkene.


:::::::::::::::
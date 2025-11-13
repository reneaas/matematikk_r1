# Størst og minst verdi



:::::::::::::::{exercise} Oppgave 1
Anna og Bjørn har materiale nok til å lage et gjerde som er 64 m langt.

De skal gjerde inn et område som skal ha form som et rektangel, og de ønsker at området skal få størst mulig areal. Se figuren nedenfor.

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
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2
Anna og Bjørn skal slå opp telt ved en elvebredde. De skal sette opp et tau rundt teltet for å holde dyr unna. 

De har 80 m med tau og fire pinner. Området de skal gjerde inn skal ha form som et rektangel og de tenker å bruke elvebredden som en av sidene i rektangelet slik at de kan gjerde inn et større område. Målet deres er å få et størst mulig areal innenfor gjerdet. Se figuren nedenfor.


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


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 3
En andregradsfunksjon $f$ er gitt ved

$$
f(x) = -x^2 + 9 \qder x \in [0, 3].
$$

En trekant har hjørner i $(0, 0)$, $(k, 0)$ og $(k, f(k))$. Se figuren nedenfor.


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

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
Nedenfor ser du grafen til en funksjon $f$ gitt ved

$$
f(x) = \dfrac{8}{x^2 + 20} \qder D_f = [0, \to \rangle
$$

Et rektangel har hjørnene $(0, 0)$, $(r, 0)$, $(r, f(r))$ og $(0, f(r))$. Se figuren nedenfor.

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


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
En båt skal reise fra en øy $A$ til en øy $C$. <br>
Båten skal kjøre innom land på en kystlinje på et punkt $B$ for å hente ferskvann. Punktet kan være hvor som helst langs kystlinjen. Båten skal reise en så kort som mulig avstand for å spare drivstoff.

Kystlinjen er $9$ km lang. Øy $A$ ligger $2$ km fra land og øy $C$ ligger $4$ km fra land. En strandkiosk $S$ er plassert på starten av kystlinja.

Se figuren nedenfor.


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
text: 0, -0.2, "$S$", bottom-left
bar: (0, -0.3), 4, horizontal
text: 2, -0.3, "$x$ km", bottom-center
bar: (0, -0.8), 9, horizontal
text: 4.5, -0.8, "9 km", bottom-center
bar: (-0.5, 0), 2, vertical
text: -0.5, 1, "2 km", center-left
bar: (9.5, 0), 4, vertical
text: 9.5, 2, "4 km", center-right
:::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 7
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



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8
En halvsirkel er gitt ved

$$
x^2 + y^2 = 4 \qder y \geq 0.
$$

Et rektangel har hjørnene $(-a, 0)$, $(a, 0)$, $(a, f(a))$ og $(-a, f(-a))$ der $f$ er funksjonen som beskriver halvsirkelen. 

Se figuren nedenfor.


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
text: -1.5, 0, "$(-a, 0)$", bottom-center
text: 1.5, 0, "$(a, 0)$", bottom-center
text: 1.5, f(1.5), "$(a, f(a))$", top-right
text: -1.5, f(-1.5), "$(-a, f(-a))$", top-left
:::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 9

En takrenne skal lages i form av et åpent trapes ved å brette to sidekanter fra et flatt rektangel slik at alle sidelengder i takrenna er $10$ cm og takrennen har en høyde på $x$ cm. Se figuren nedenfor.


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

:::::::::::::::






---








:::::::::::::::{exercise} Oppgave 11
En kurve er gitt ved grafen til funksjonen $f(x) = x^2$. I samme figur er et punkt $P(4, 5)$. 

Bestem punkt på grafen som ligger nærmest punktet $P$.

:::{plot}
width: 70%
function: x**2
point: (4, 5)
text: 4, 5, "$P(4, 5)$", top-right
ymin: -1 
ymax: 7
xmin: -3
:::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 12
En kurve er gitt ved parabelen $x = (y - 1)^2 - 2$. Kurven er vist i figuren nedenfor.

Bestem den korteste avstanden fra punktet $P(-2, 4)$ til kurven.

:::{plot}
width: 70%
curve: (t - 1)**2 - 2, t, (-10, 10), solid, blue
point: (-2, 4)
text: -2, 4, "$P(-2, 4)$", top-left
:::

:::::::::::::::
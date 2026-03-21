# Derivasjon av elementærfunksjoner


::::{admonition} Læringsmål
---
class: tip
---
* Kunne derivere polynomfunksjoner, potensfunksjoner, rotfunksjoner, eksponentialfunksjoner og logaritmefunksjoner
* Kunne bestemme likningen til tangenter, og forklare sammenhengen mellom den deriverte og stigningstallet til tangenter.
::::

## Derivasjonsregler for elementærfunksjoner

Vi må memorisere derivasjonsreglene til en del elementærfunksjoner for at vi skal være i stand til å derivere mer kompliserte funksjoner senere. Derivasjonsreglene for elementærfunksjonene vi skal jobbe med er: 

:::::::::::::::{summary} Derivasjonsreglene
:::{table}
labels:Funksjon, Derivert, Eksempel
$f(x) = x^n$, $f'(x) = n \cdot x^{n-1}$, $(x^3)' = 3x^2$
$f(x) = \sqrt{x}$, $f'(x) = \dfrac{1}{2\sqrt{x}}$, $(\sqrt{x})' = \dfrac{1}{2\sqrt{x}}$
$f(x) = e^x$, $f'(x) = e^x$, $(e^x)' = e^x$
$f(x) = e^{kx}$, $f'(x) = k \cdot e^{kx}$, $(e^{3x})' = 3 \cdot e^{3x}$
$f(x) = \ln(ax)$, $f'(x) = \dfrac{1}{x}$, $(\ln(3x))' = \dfrac{1}{x}$
$f(x) = a^x$, $f'(x) = a^x \cdot \ln(a)$, $(3^x)' = 3^x \cdot \ln(3)$
$f(x) = \log_a(x)$, $f'(x) = \dfrac{1}{x \cdot \ln(a)}$, $(\log_2(x))' = \dfrac{1}{x \cdot \ln(2)}$
:::

:::::::::::::::


Vi må også få til å derivere summer og differanser av elementærfunksjoner. Regnereglene for dette er:


:::::::::::::::{summary} Derivasjonsregler for sum og differanser
:::{table}
labels: Regel, Eksempel
$(f(x) + g(x))' = f'(x) + g'(x)$, $(x^3 + e^x)' = 3x^2 + e^x$
$(f(x) - g(x))' = f'(x) - g'(x)$, $(\sqrt{x} - \ln(3x))' = \dfrac{1}{2\sqrt{x}} - \dfrac{1}{x}$
$a \cdot f(x)' = a \cdot f'(x)$, $(3 \cdot e^x)' = 3 \cdot e^x$
:::

:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 1
Bestem den deriverte til funksjonene.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
f(x) = x^5
$$
:::::::::::::


:::::::::::::{tab-item} b
$$
g(x) = 4\sqrt{x}
$$
:::::::::::::


:::::::::::::{tab-item} c
$$
h(x) = \ln(8x)
$$
:::::::::::::


:::::::::::::{tab-item} d
$$
p(x) = e^{-3x}
$$
:::::::::::::


::::::::::::::

:::::::::::::::


---



:::::::::::::::{exercise} Underveisoppgave 2
Bestem den deriverte til funksjonene.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
f(x) = 3^x + 5x^2
$$

:::::::::::::


:::::::::::::{tab-item} b
$$
g(x) = \ln(4x) - 2\sqrt{x}
$$
:::::::::::::


:::::::::::::{tab-item} c
$$
h(x) = 4e^{2x} + 7\log_3(x)
$$

:::::::::::::


:::::::::::::{tab-item} d
$$
p(x) = 5x^3 - 2e^{-x} + \ln(6x)
$$
:::::::::::::


::::::::::::::
:::::::::::::::


## Likningen til tangenter

:::{plot}
align: right
fontsize: 32
width: 100%
function: exp(x), f
let: a = 1
point: (a, f(a))
tangent: a, f, solid
text: a, f(a), "$(a, f(a))$"
ticks: off
ymax: 10
hline: f(a), a, a + 1, dashed, gray
vline: a + 1, f(a), exp(a) * (a + 1 - a) + f(a), dashed, gray
ymin: -1
text: 0.5 * (a + a + 1), f(a), "$1$", bottom-center
text: a + 1, 0.5 * (f(a) + exp(a) * (a + 1 - a) + f(a)), "$f'(a)$", center-right
xmin: -0.2
xmax: 3.5
:::


Den deriverte $f'(a)$ til en funksjon $f$ gir oss stigningstallet til en tangent i punktet $(a, f(a))$ på grafen til $f$. 

Ettpunktsformelen for en linje med stigningstall $m$ som går gjennom punktet $(x_0, y_0)$ er gitt ved

$$
y - y_0 = m \cdot (x - x_0)
$$

Siden tangenten går gjennom punkt $(a, f(a))$, så er $(x_0, y_0) = (a, f(a))$. Siden stigningstallet til tangenten er $f'(a)$, så er $m = f'(a)$. Setter vi inn dette i ettpunktsformelen får vi

$$
y - f(a) = f'(a) \cdot (x - a)
$$

Dette kan vi skrive om til

$$
y = f'(a) \cdot (x - a) + f(a)
$$


:::::::::::::::{summary} Likningen til en tangent
En tangent til grafen til $f$ i punktet $(a, f(a))$ har likningen

$$
y = f'(a) \cdot (x - a) + f(a)
$$
:::::::::::::::



---




:::::::::::::::{exercise} Underveisoppgave 3
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Funksjonen $f$ er gitt ved 

$$
f(x) = x^3 - 3x + 1
$$

Bestem likningen til tangenten til grafen til $f$ i punktet $(1, f(1))$.
:::::::::::::


:::::::::::::{tab-item} b
Funksjonen $g$ er gitt ved 

$$
g(x) = e^{2x}
$$

Bestem likningen til tangenten til grafen til $g$ i punktet $(0, g(0))$.
:::::::::::::


:::::::::::::{tab-item} c
Funksjonen $h$ er gitt ved 

$$
h(x) = \ln(5x)
$$

Bestem likningen til tangenten til grafen til $h$ i punktet $(e, h(e))$.

:::::::::::::


::::::::::::::
:::::::::::::::








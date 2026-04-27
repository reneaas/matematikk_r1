# Numerisk derivasjon

:::::::::::::::{summary} Elementærfunksjoner i Python
Noen funksjoner vi jobber med i matematikk er ikke innebygd i Python fra før av og må **importeres**. I tabellen nedenfor vises en oversikt over ulike måter å skrive vanlige funksjoner i Python og hvordan de importeres så de kan brukes.

| Funksjon i matematikk | I Python            | Importer med                     |
|:-----------------------:|---------------------|----------------------------------|
| $e^x$                 | `exp(x)`{l=python}  | `from math import exp`{l=python}|
|                       | `e**x`{l=python}    | `from math import e`{l=python}  |
| $\ln x$               | `log(x)`{l=python}  | `from math import log`{l=python}|
| $\sqrt{x}$            | `sqrt(x)`{l=python} | `from math import sqrt`{l=python}|
|                       | `x**0.5`{l=python}  | (ingen import nødvendig)        | 
| $\log_a x$          | `log(x, a)`{l=python}| `from math import log`{l=python}|
|         | `log(x) / log(a)`{l=python}| `from math import log`{l=python}|


:::::::::::::::



:::::::::::::::{exercise} Oppgave 1
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Et program vises nedenfor. 

Bestem verdien programmet skriver ut når det kjøres. Sjekk svaret ditt ved å kjøre programmet.


:::{interactive-code}
---
predict:
---
def f(x):
    return x**3 + 2*x + 1


x = 2
h = 1e-7

dfdx = (f(x + h) - f(x)) / h
print(dfdx)
:::
:::::::::::::


:::::::::::::{tab-item} b
Et program vises nedenfor. 

Bestem verdien programmet skriver ut når det kjøres. Sjekk svaret ditt ved å kjøre programmet.

:::{interactive-code}
---
predict:
---
def g(x):
    from math import sqrt
    return x * sqrt(x)


x = 4
h = 1e-7

dgdx = (g(x + h) - g(x)) / h
print(dgdx)
:::

:::::::::::::


::::::::::::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 2
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Nedenfor vises et uferdig program som skal bestemme den deriverte til funksjonen

$$
f(x) = \sqrt{x + 1}
$$

i punktet $x = 3$. 

Fullfør programmet slik at det fungerer som beskrevet. 

:::{interactive-code}
def f(x):
    return ????

x = 3
h = 1e-7

f_derivert = ????

print(f_derivert)
:::

:::::::::::::


:::::::::::::{tab-item} b
Nedenfor vises et uferdig program som skal bestemme den deriverte til funksjonen 

$$
g(x) = x\ln x
$$

i punktet $x = 5$.

Fullfør programmet og bestem $g'(5)$. 


:::{interactive-code}
from math import log # log(x) er den naturlige logaritmen til x
def g(x):
    return ????


x = ????
h = 1e-7

g_derivert = ????

print(g_derivert)
:::

:::::::::::::


:::::::::::::{tab-item} c
Nedenfor vises et uferdig program som skal bestemme den deriverte til funksjonen 

$$
p(x) = x e^{-x^2}
$$

i punktet $x = 1$. 

Fullfør programmet og bestem $p'(1)$.


:::{interactive-code}
def p(x):
    from math import e # e er Eulers tall
    return ????

x = ????
h = 1e-7

p_derivert = ????

print(p_derivert)
:::

:::::::::::::


::::::::::::::
:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 3


:::{plot}
align: right
width: 100%
function: exp(-x**2 + x)
xmin: -3
xmax: 3
yticks: off
ymin: -1
ymax: 3
fontsize: 30
lw: 4
grid: off
:::



I figuren til høyre vises grafen til en funksjon $f$ gitt ved

$$
f(x) = e^{-x^2 + x}
$$



Nedenfor vises et program.

1. Hva er det programmet finner når det kjøres? 
2. Bestem en eksakt verdi for det programmet skriver ut. Sjekk svaret ved å kjøre programmet!


:::{clear}
:::

:::{interactive-code}
---
predict:
---
def f(x):
    from math import e
    return e**(-x**2 + x)


x = -2
h = 1e-7
while f(x) < f(x + h):
    x += 0.01

print(x)
:::



:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 4

:::{plot}
align: right
width: 100%
function: x * log(x**2)
xmin: -2
xmax: 2
yticks: off
grid: off
ymin: -3
ymax: 3
fontsize: 30
lw: 4
:::


I figuren til høyre vises grafen til en funksjon $f$ gitt ved

$$
f(x) = x \ln x^2
$$


Nedenfor vises et program.

:::{clear}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
1. Hva er det programmet finner når det kjøres?
2. Bestem en eksakt verdi for det programmet skriver ut. Sjekk svaret ved å kjøre programmet!



:::::::::::::


:::::::::::::{tab-item} b
Gjør nødvendige endringer og bruk det til å bestemme koordinatene til toppunktet til $f$.


:::::::::::::



::::::::::::::




:::{interactive-code}
---
predict:
---
def f(x):
    from math import log
    return x * log(x**2)


x = 0.0001
h = 1e-7
while (f(x + h) - f(x)) / h < 0:
    x += 0.0001

print(x)
:::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 5
En funksjon $f$ er gitt ved

$$
f(x) =
\begin{cases}
    \dfrac{1 - \sqrt{x}}{1 - x} & \qhvis x \neq 1 \qog x \geq 0 \\
    \\
    \dfrac{1}{2} & \qhvis x = 1
\end{cases}
$$


Bruk programmet nedenfor til å bestemme $f'(1)$.


:::{interactive-code}
def f(x):
    if x != 1 and x >= 0:
        return ????
    else:
        return ????


x = 1
h = 1e-6

f_derivert = ????

print(f_derivert)
:::

:::::::::::::::






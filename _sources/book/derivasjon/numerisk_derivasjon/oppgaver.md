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





:::::::::::::::{exercise} Oppgave X
> I denne oppgaven skal vi se på hvordan valget av $h$ påvirker hvor nøyaktig svaret vårt blir når vi deriverer numerisk.

En funksjon $f$ er gitt ved

$$
f(x) = x^2 e^{-x}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $f'(x)$


:::::::::::::


:::::::::::::{tab-item} b
I programmet nedenfor er det noen kodelinjer som ikke er fullstendig. Skriv ferdig programmet og kjør det.


:::::::::::::


::::::::::::::


:::{interactive-code}
def f(x):
    from math import e
    return ????

def f_derivert(x, h):
    return ????


x = 2
f_derivert_eksakt = ????
f_derivert_numerisk = f_derivert(x)


steglengder = []
relativ_feilverdier = []
h = 1
while h > 1e-6:
    relativ_feil = abs(f_derivert_eksakt - f_derivert_numerisk) / abs(f_derivert_eksakt)

    # Lagrer verdiene for h og relativ feil så vi plotte dem
    steglengder.append(h)
    relativ_feilverdier.append(relativ_feil)


import plotmath
fig, ax = plotmath.plot(steglengder, relativ_feilverdier)
ax.xscale("log")
ax.yscale("log")
plotmath.show()
:::

:::::::::::::::
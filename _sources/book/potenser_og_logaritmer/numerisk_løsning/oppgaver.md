# Numerisk løsning av likninger

## Halveringsmetoden

Halveringsmetoden er en strategi for å systematisk løse likninger. Ideen er som følger:


:::::::::::::::{summary} Halveringsmetoden
For en funksjon $f$, kan vi finne et nullpunkt $x$ slik at $f(x) = 0$ ved å bruke følgende strategi:

> 1. Velg et intervall $[a, b]$ slik at $f(a)$ og $f(b)$ har motsatte fortegn.
> 2. Beregn midtpunktet $c = \dfrac{a + b}{2}$ på intervallet.
> 3. Sjekk fortegnet til $f(c)$:
>    - Hvis $f(c) = 0$, har vi funnet nullpunktet.
>    - Hvis $f(c)$ har samme fortegn som $f(a)$, sett det nye intervallet til $[c, b]$.
>    - Hvis $f(c)$ har samme fortegn som $f(b)$, sett det nye intervallet til $[a, c]$.

> Gjenta dette frem til $f(c) \approx 0$ (det vil si at $f(c)$ er tilstrekkelig nærme null). Da er $x = c$ nullpunktet til $f$. 

Se animasjonen nedenfor.


:::{figure} https://upload.wikimedia.org/wikipedia/commons/d/d9/Bisection_anime.gif
---
class: no-click, adaptive-figure
width: 80%
---
Animasjonen starter med intervallet $[a_1, b_1]$ og regner ut et midtpunkt $c$. Deretter velges det intervallet hvor funksjonen skifter fortegn, og prosessen gjentas. Etter hvert nærmer $c$ seg verdien til nullpunktet.

Halveringsmetoden (Bisection method) laget av [Picknick](https://commons.wikimedia.org/wiki/User:Picknick), 
lisensiert under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) via Wikimedia Commons.
:::



:::::::::::::::


---



:::{margin}
`np.log(x)`{l=python} er det samme som $\ln(x)$.
:::

:::::::::::::::{exercise} Oppgave 1 
Programmet nedenfor bruker halveringsmetoden, men er plassert i tilfeldig rekkefølge.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Sett programmet i riktig rekkefølge.


:::::::::::::


:::::::::::::{tab-item} b
Kjør programmet nedenfor og gi en tolkning av det programmet skriver ut.


:::::::::::::


:::::::::::::{tab-item} c
I programmet nedenfor ser du noen kommentarer merket `# ????`{l=python}. 

Bytt ut `????`{l=python} og forklar hva programmet gjør med korte kommentarer.
:::::::::::::


:::::::::::::{tab-item} d
Hvilken betydning har `a`{l=python} og `b`{l=python} i programmet?

Hva skjer hvis `f(a)`{l=python} og `f(b)`{l=python} har samme fortegn? Prøv med i programmet.
:::::::::::::



:::::::::::::{tab-item} e
Hvilken betydning har `nøyaktighet`{l=python} i programmet? 

Prøv forskjellige verdier og trekk en konklusjon.
:::::::::::::


:::::::::::::{tab-item} f
Modifiser programmet og prøv følgende
* Velg en annen funksjon $f(x)$.
* La brukeren skriv inn verdiene til `a`{l=python} og `b`{l=python} med `input()`{l=python}-funksjonen. 
* Skriv en mer informativ melding som skrives ut når programmet har løst likningen.
* Skriv en informativ melding som forteller når intervallet $[a, b]$ ikke inneholder et nullpunkt.
:::::::::::::


::::::::::::::

:::{parsons-puzzle}

def f(x): # ????;    import numpy as np;    return 5 * np.log(x**3 + 2) - x - 6;;a = 0 # ????;b = 1 # ????;nøyaktighet = 0.01 # ????


c = (a + b) / 2


while abs(f(c)) >= nøyaktighet: # ????
    if f(c) * f(a) < 0: # ????
        b = c # ????
    else:
        a = c # ????

    c = (a + b) / 2


print(c)


:::

:::::::::::::::


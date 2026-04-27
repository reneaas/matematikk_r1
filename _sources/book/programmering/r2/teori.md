# Programmering av tallfølger

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne lage programmer som lager tallene i en tallfølge.
* Kunne lage programmer som finner summen av tall i en tallfølge.
:::::

Tallfølger er nært knyttet til de naturlige tallene og egenskaper ved tall. Du har kanskje møtt på figurtall før som trekanttall eller kvadrattall. Dette er eksempler på tallfølger som er representert med figurer. Her skal vi se på hvordan vi kan bruke programmering til å svare på spørsmål knyttet til tallfølger og figurtall. 


## `for`{l=python}-løkker

:::{margin}
Senere skal vi lære om en annen type løkke som kalles for en `while`{l=python}-løkke.
:::

En løkke er et verktøy i programmering som lar oss gjenta én eller flere linjer med kode flere ganger – vi kaller dette for en **kodeblokk**. Dette er nyttig når vi ønsker å lage tallfølger. Vi skal her fokusere på en type løkke som kalles `for`{l=python}-løkke. En `for`{l=python}-løkke lar oss gjenta en kodeblokk for hvert element i en liste eller en tallmengde.  

### `for`{l=python}-løkker med avstand $1$

:::::::::::::::{summary} `for`{l=python}-løkker
En `for`{l=python}-løkke som skal skrive ut tall fra og med `start`{l=python} og til `slutt`{l=python} kan skrives slik:

:::{code-block} python
---
linenos:
---
for n in range(start, slutt):
    # Kode som skal gjentas står her
:::

Det siste tallet som skrives ut er `slutt - 1`{l=python}.
:::::::::::::::

Nedenfor i Utforsk 1 kan du utforske nærmere hvordan en slik `for`{l=python}-løkke fungerer.

:::{margin} `print`{l=python}-funksjonen
I Utforsk 1 vil du se at koden som gjentas i `for`{l=python}-løkka er `print(n)`{l=python}. Denne kodelinjen skriver ut verdien av `n`{l=python} for hver runde i løkka.
:::

:::::::::::::::{explore} Utforsk 1
Nedenfor vises noen programmer som bruker `for`-løkker til å skrive ut noen tall. 

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Les programmet nedenfor og prøv å forutsi hvilke tall programmet skriver ut.

Skriv inn gjetningen din nedenfor og sjekk svaret ditt!


:::{interactive-code}
---
predict:
---
for n in range(1, 6):
    print(n)        # skriver ut verdien av n
:::
:::::::::::::


:::::::::::::{tab-item} b
Les programmet nedenfor og prøv å forutsi hvilke tall programmet skriver ut.

Skriv inn gjetningen din nedenfor og sjekk svaret ditt!


:::{interactive-code}
---
predict:
---
for n in range(2, 11):
    print(n)
:::
:::::::::::::


:::::::::::::{tab-item} c
Les programmet nedenfor og prøv å forutsi hvilke tall programmet skriver ut.

Skriv inn gjetningen din nedenfor og sjekk svaret ditt!


:::{interactive-code}
---
predict:
---
for n in range(-5, 6):
    print(n)
:::
:::::::::::::

::::::::::::::



:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 1
Ta quizen! 

:::{quiz}
Q: Hvilke tall skrives ut av programmet nedenfor?  <pre><code class="python">for n in range(1, 4):\n    print(n)</code></pre>
+ 1, 2, 3
- 1, 2, 3, 4
- 1, 4
- 1, 2, 3, 4, 5


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(0, 6):\n    print(n)</code></pre>
+ 0, 1, 2, 3, 4, 5
- 0, 1, 2, 3, 4, 5, 6
- 0, 6
- 1, 2, 3, 4, 5


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(-2, 2):\n    print(n)</code></pre>
+ -2, -1, 0, 1
- -2, -1, 0, 1, 2
- -2, 2
- -1, 0, 1, 2


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(-3, 4):\n    print(n)</code></pre>
+ -3, -2, -1, 0, 1, 2, 3
- -3, -2, -1, 0, 1, 2
- -3, 4
- -2, -1, 0, 1, 2, 3

:::
:::::::::::::::

---

### `for`{l=python}-løkker med en fast `avstand`{l=python}

Vi kan også bruke `for`{l=python}-løkker til å lage tallfølger der ikke alle tall bare er det forrige tallet pluss $1$. For eksempel kan vi lage `for`{l=python}-løkker som skriver ut partall, eller oddetall, eller tallfølger der det er fast avstand mellom hvert tall. 

:::::::::::::::{summary} `for`{l=python}-løkker 2
En `for`{l=python}-løkke som skriver ut tall fra og med `start`{l=python} og til `slutt`{l=python} med en fast `avstand`{l=python} mellom hvert tall kan skrives slik:

:::{code-block} python
---
linenos:
---
for n in range(start, stopp, avstand):
    print(n)
:::

Det siste tallet som skrives ut må være mindre enn `stopp`{l=python}. 

:::::::::::::::


Nedenfor i Utforsk 2 kan du utforske nærmere hvordan en slik `for`{l=python}-løkke fungerer.

:::::::::::::::{explore} Utforsk 2
Nedenfor vises noen programmer som bruker `for`{l=python}-løkker til å skrive ut noen tall.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Les programmet nedenfor og prøv å forutsi hvilke tall programmet skriver ut.

Skriv inn gjetningen din nedenfor og sjekk svaret ditt!


:::{interactive-code}
---
predict:
---
for n in range(2, 6, 2):
    print(n)
:::
:::::::::::::

:::::::::::::{tab-item} b
Les programmet nedenfor og prøv å forutsi hvilke tall programmet skriver ut.

Skriv inn gjetningen din nedenfor og sjekk svaret ditt!


:::{interactive-code}
---
predict:
---
for n in range(-5, 7, 3):
    print(n)
:::
:::::::::::::

:::::::::::::{tab-item} c
Les programmet nedenfor og prøv å forutsi hvilke tall programmet skriver ut.

Skriv inn gjetningen din nedenfor og sjekk svaret ditt!


:::{interactive-code}
---
predict:
---
for n in range(0, 100, 20):
    print(n)
:::
:::::::::::::
::::::::::::::

:::::::::::::::

---

:::::::::::::::{exercise} Underveisoppgave 2
:::{quiz}
Q: Hvilken tallfølge skrives ut av programmet? <pre><code class="python">for x in range(1, 5, 1):\n    print(x)</code></pre>
+ $1, 2, 3, 4$
- $1, 2, 3, 4, 5$
- $1, 2, 3$
- $1, 2, 3, 4, 5, 6$

Q: Hvilken tallfølge skrives ut av programmet? <pre><code class="python">for x in range(1, 5, 2): \n    print(x)</code></pre>
+ $1, 3$
- $1, 3, 5$
- $1, 3, 4$
- $0, 2, 4$

Q: Hvilket program gir utskriften <pre><code class="console">-4 \n-2 \n0 \n2 \n4</code></pre>
+ <pre><code class="python">for x in range(-4, 5, 2): \n    print(x)</code></pre>
- <pre><code class="python">for x in range(-4, 4, 2): \n    print(x)</code></pre>
- <pre><code class="python">for x in range(-4, 2, 4): \n    print(x)</code></pre>
- <pre><code class="python">for x in range(-4, 2, 5): \n    print(x)</code></pre>

Q: Hvilken tallfølge skrives ut av programmet? <pre><code class="python">for x in range(1, 10, 3): \n    print(x)</code></pre>
+ $1, 4, 7$
- $1, 4, 7, 10$
- $1, 3, 6, 10$
- $1, 3, 6, 9$

Q: Hvilken tallfølge skrives ut av programmet? <pre><code class="python">for x in range(12, 2, -4): \n    print(x)</code></pre> 
+ $12, 8, 4$
- $12, 8, 4, 0$
- $12, 8, 4, 2$
- $12, 2, -4$
:::
:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 3
Nedenfor finner du interaktive kodevinduer du kan skrive kode i og kjøre direkte.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som skriver ut partallene fra og med $2$ til og med $20$.

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? med riktig tall
    print(n)
:::

:::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(2, 22, 2):
    print(n)
:::
:::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som skriver ut oddetallene fra og med $1$ til og med $19$.

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? med riktig tall
    print(n)
:::


:::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 20, 2):
    print(n)
:::
:::::

:::::::::::::


:::::::::::::{tab-item} c
Lag et program som skriver ut tallfølgen $10, 20, 30, 40, 50$.

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? med riktig tall
    print(n)
:::


:::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(10, 60, 10):
    print(n)
:::
:::::

:::::::::::::

::::::::::::::
:::::::::::::::


## Formler

Når vi skriver et program, så ønsker vi ofte å regne med formler. 


:::::::::::::::{explore} Utforsk 3 
Nedenfor vises et program som bruker en formel for å regne ut og skrive ut noen tall i en tallfølge.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Les programmet og forutsi hvilke tall programmet skriver ut.

Skriv inn svaret ditt nedenfor sjekk. 


:::::::::::::


:::::::::::::{tab-item} b
Endre på programmet slik at det skriver ut verdiene til tallfølgen 

$$
a_n = n^2 \qfor n \in \set{1, 2, \ldots, 10}
$$

> For å opphøye et tall i Python, bruker vi `**`{l=python}. For eksempel er $2^3$ skrevet som `2 ** 3`{l=python} i Python.


:::::::::::::
::::::::::::::


:::{interactive-code}
---
predict:
---
for n in range(1, 5):
    a = 3 * n + 1
    
    print(a)
:::




:::::::::::::::


---

:::::::::::::::{exercise} Underveisoppgave 4

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor slik at det skriver ut verdiene til tallfølgen gitt ved 

$$
a_n = 2n + 3 \qfor n \in \set{1, 2, 3, 4, 5}
$$

:::{interactive-code}
for n in range(????): # FYLL INN
    a = # FYLL INN
    
    print(a)

:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 6):
    a = 2 * n + 3
    
    print(a)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det skriver ut verdiene til tallfølgen gitt ved 

$$
b_n = n^2 + 2n + 1 \qfor n \in \set{1, 3, 5, 7, 9}
$$

:::{interactive-code}
for n in range(????): # FYLL INN
    b = # FYLL INN
    
    print(b)

:::

::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 10, 2):
    b = n**2 + 2 * n + 1
    
    print(b)
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
Fyll ut programmet nedenfor slik at det skriver ut verdiene til tallfølgen gitt ved 

$$
c_n = 2^n \qfor n \in \set{-2, -1, 0, 1, 2}
$$

:::{interactive-code}
for n in range(????): # FYLL INN
    c = # FYLL INN
    
    print(c)

:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(-2, 3):
    c = 2 ** n
    
    print(c)
:::
::::
:::::::::::::
::::::::::::::



:::::::::::::::


## Summere tall i en tallfølge

I mange tilfeller er vi interessert i å summere tallene i en tallfølge. 


:::{margin} `s = s + n`{l=python}
Når vi skriver `s = s + n`{l=python}, så betyr det at vi legger til verdien til `n`{l=python} til verdien til `s`{l=python} og lagrer resultatet i `s`{l=python}. 
:::

:::::::::::::::{explore} Utforsk 4
Nedenfor vises et program som summerer noen tall. 


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Les programmet nedenfor og forutsi hva som skrives ut. 

Skriv inn svaret ditt nedenfor og sjekk.
:::::::::::::


:::::::::::::{tab-item} b
Endre på programmet slik at det summerer alle naturlig tall fra $1$ til og med $100$. 

Hva blir summen? 
:::::::::::::


:::::::::::::{tab-item} 
Endre på programmet slik at det finner summen av de $10$ første kvadrattallene

$$
S = 1^2 + 2^2 + 3^2 + \ldots + 10^2
$$
:::::::::::::

::::::::::::::

:::{interactive-code}
---
predict:
---
s = 0
for n in range(1, 6):
    s = s + n

print(s)
:::

:::::::::::::::



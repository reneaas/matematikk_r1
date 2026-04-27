# Oppgaver: Programmering av tallfølger


:::::::::::::::{exercise} Oppgave 1
---
level: 1
---
Ta quizen! 

:::{quiz}
Q: Hvilke tall skrives ut av programmet nedenfor?  <pre><code class="python">for n in range(-2, 3):\n    print(n)</code></pre>
+ $-2, -1, 0, 1, 2$
- $-2, 3$
- $-2, -1, 0, 1, 2, 3$
- $-2, 1, 3$


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(4):\n    print(n)</code></pre>
+ $0, 1, 2, 3$
- $0, 1, 2, 3, 4$
- $4$
- $1, 2, 3, 4$


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(-2, 2, 1):\n    print(n)</code></pre>
+ $-2, -1, 0, 1$
- $-2, 2, 1$
- $-2, -1, 0, 1, 2$
- $-1, 0, 1, 2$


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(1, 6, 2):\n    print(n)</code></pre>
+ $1, 3, 5$
- $1, 6, 2$
- $1, 2, 6$
- $1, 3, 5, 6$


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(1, 10, 3):\n    print(n)</code></pre>
+ $1, 4, 7$
- $1, 4, 7, 10$
- $1, 3, 10$
- $1, 10, 3$


Q: Hvilke tall skrives ut av programmet nedenfor? <pre><code class="python">for n in range(0, 101, 10):\n    print(n)</code></pre>
+ $0, 10, 20, \ldots, 90, 100$
- $0, 10, 20, \ldots, 90$
- $0, 101, 10$
- $0, 10, 100$
:::
:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 2
---
level: 1
---
Nedenfor vises noen programkoder som skriver ut noen tall. Les programmene og prøv å forutsi hvilke tall de skriver ut. 

Skriv inn gjetningen din og sjekk svaret ditt for hvert av programmene.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

:::{interactive-code}
---
predict:
---
for n in range(3):
    print(n)

:::

:::::::::::::


:::::::::::::{tab-item} b

:::{interactive-code}
---
predict:
---
for n in range(-4, 1):
    print(n)
    
:::

:::::::::::::


:::::::::::::{tab-item} c

:::{interactive-code}
---
predict:
---
for n in range(-10, 11, 4):
    print(n)

:::

:::::::::::::


:::::::::::::{tab-item} d

:::{interactive-code}
---
predict:
---
for n in range(10, 1, -2):
    print(n)
    
:::

:::::::::::::

::::::::::::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
---
level: 1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor slik at det skriver ut alle tallfølgen

$$
1, 2, 3, 4, 5, 6, 7, 8.
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? 
    print(n)


:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 9):
    print(n)
:::
::::

:::::::::::::



:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen 

$$
2, 4, 6, 8.
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? 
    print(n)


:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(2, 10, 2):
    print(n)
:::
::::

:::::::::::::



:::::::::::::{tab-item} c
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen 

$$
1, 5, 9, 13. 
$$


:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? 
    print(n)


:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 14, 4):
    print(n)
:::
::::

:::::::::::::



:::::::::::::{tab-item} d
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
-5, -3, -1, 1, 3, 5. 
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? 
    print(n)


:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(-5, 6, 2):
    print(n)
:::
::::

:::::::::::::

::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 4
---
level: 1
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
10, 6, 2
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ????
    print(n)


:::


:::::{answer}
:::{code-block} python
for n in range(10, 1, -4):
    print(n)
:::
:::::

:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ????
    print(n)


:::


:::::{answer}
:::{code-block} python
for n in range(100, -1, -10):
    print(n)
:::
:::::

:::::::::::::


:::::::::::::{tab-item} c
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
5, 3, 1, -1, -3, -5
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ????
    print(n)


:::


:::::{answer}
:::{code-block} python
for n in range(5, -6, -2):
    print(n)
:::
:::::

:::::::::::::


:::::::::::::{tab-item} d
Fyll ut programmet nedenfor slik at det skriver ut tallfølgen

$$
-2, -5, -8, -11, -14
$$

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ????
    print(n)


:::


:::::{answer}
:::{code-block} python
for n in range(-2, -15, -3):
    print(n)
:::
:::::

:::::::::::::

::::::::::::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 5
---
level: 2
---
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor slik at det skriver ut alle partallene til og med $20$. 


:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? med riktige tall
    print(n)


:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(2, 21, 2):
    print(n)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Fyll ut programmet nedenfor slik at det skriver ut alle oddetallene til og med $21$. 


:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? med riktige tall
    print(n)


:::


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 22, 2):
    print(n)
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
Lag et program som skriver ut de $20$ **første** partallene.


:::{interactive-code}
# Skriv ditt program her




:::



:::::{answer}
:::{code-block} python
for n in range(1, 21):
    partall = 2 * n
    print(partall)
:::
:::::

:::::::::::::


:::::::::::::{tab-item} d
Lag et program som skriver ut de $20$ **første** oddetallene.


:::{interactive-code}
# Skriv ditt program her




:::


:::::{answer}
:::{code-block} python
for n in range(1, 21):
    oddetall = 2 * n - 1
    print(oddetall)
:::
:::::

:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 6
---
level: 2
---
Anna og Bjørn snakker om en annen strategi for å skrive ut partall og oddetall. 

:::{dialogue}
---
name1: Anna
name2: Bjørn
speaker1: left
speaker2: right
---
Anna: Jeg har en annen idé for å skrive ut partallene på. Vi kan lage en løkke som går gjennom alle naturlige tall og sjekker om det er et partall.
Bjørn: Det er en god idé! Da kan vi bruke en `if`{l=python}-setning for å sjekke om tallet er partall.
Anna: Men hvordan sjekker vi at et tall er et partall igjen?
Bjørn: Det er vel bare å sjekke om det er delelig med $2$? Jeg har lest at det kan man gjøre ved å skrive <br> `if n % 2 == 0:`{l=python}
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Fyll ut programmet nedenfor slik at det skriver ut alle partallene til og med $20$ ved hjelp av en `if`{l=python}-setning.

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? med riktige tall
    if ????: # Sjekk om n er et partall
        print(n)

:::

:::::::::::::


:::::::::::::{tab-item} b
Anna og Bjørn fortsetter samtalen.

:::{dialogue}
---
name1: Anna
name2: Bjørn
speaker1: left
speaker2: right
---
Anna: Ok, så nå klarer vi å skrive ut partall ved å sjekke om et tall er delelig med $2$. Men hva med oddetallene?
Bjørn: Da har jeg lest at vi kan bruke en `if`{l=python}-`else`{l=python}-setning. Hvis tallet er delelig med $2$, så gjør vi ingenting. Da kan vi bruke `pass`{l=python}. Og så skriver vi ut tallet hvis det ikke er delelig med $2$.
:::


<br>

Bruk strategien til Anna og Bjørn i programmet nedenfor.

:::{interactive-code}
for n in range(????): # FYLL INN: bytt ut ???? med riktige tall
    if ????: # Sjekk om n er et partall
        # FYLL INN: gjør ingenting her!
    else:
        # FYLL INN: skriv ut tallet hvis det er et oddetall

:::

:::::::::::::

::::::::::::::


:::::::::::::::


---

:::::::::::::::{exercise} Oppgave 7
---
level: 2
---
Anna og Bjørn snakker om hvordan man kan avgjøre om et tall $p \in \mathbb{N}$ er et primtall med et program.


:::{dialogue}
---
name1: Anna
name2: Bjørn
speaker1: left
speaker2: right
---
Anna: Jeg har lest at et primtall er et tall som bare er delelig med $1$ og seg selv. 
Bjørn: Ja, det stemmer! Så hvis vi skal sjekke om et tall $n$ er et primtall, så må vi sjekke om det er delelig med alle tallene fra $2$ til $p - 1$.
Anna: Ja, men hvordan gjør vi det i et program?
Bjørn: Vi kan bruke en løkke som går gjennom alle tallene $n \in \{2, 3, \ldots, p - 1\}$ og sjekker om $p$ er delelig med hvert av dem. Da kan vi vel bruke en `if`{l=python}-setning litt som når vi sjekket om et tall var delelig med $2$?
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk strategien til Anna og Bjørn i programmet nedenfor. Sjekk at tallene $11$, $51$ og $729$ er primtall.



:::::::::::::


:::::::::::::{tab-item} b
Anna og Bjørn er ikke helt fornøyde.

:::{dialogue}
---
name1: Anna
name2: Bjørn
speaker1: left
speaker2: right
---
Anna: Men nå sjekker vi jo fryktelig mange tall. Trenger vi å sjekke alle tallene fra $2$ til $p - 1$?
Bjørn: Nei! Vi trenger bare å sjekke tallene opp til $\sqrt{p}$. Hvis $p$ er delelig med et tall større enn $\sqrt{p}$, så må det også være delelig med et tall mindre enn $\sqrt{p}$. 
Anna: Hvorfor er det slik? 
Bjørn: Det er jeg ikke sikker på. Var bare noe jeg så på Insta. Men hvordan regner vi ut $\sqrt{p}$ i et program?
Anna: Det er enkelt! Vi kan bruke `int(n ** 0.5)`{l=python}
:::


<br>

Endre på programmet ditt og prøv ut strategien de snakker om.


:::::::::::::


:::::::::::::{tab-item} c
Argumenter for at det største tallet man trenger å sjekke for å avgjøre om et tall $p$ er et primtall, er $\sqrt{p}$.

:::::::::::::


::::::::::::::

:::{interactive-code}
# Din kode her



:::


:::::::::::::::



---


:::{margin} Startverdien til `s`{l=python}
Vi setter startverdien til `s`{l=python} til `0`{l=python} fordi å plusse på `0`{l=python} ikke endrer verdien til en sum. 
:::

:::::::::::::::{exercise} Oppgave 8
---
level: 2
---
> I denne oppgaven skal du lære hvordan man summerer tall med et program.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I programmet nedenfor summeres noen tall med en variabel `s`{l=python} i en løkke. Linja `s = s + n`{l=python} legger til verdien av `n`{l=python} til summen `s`{l=python}.

Les programmet og forutsi hvilken verdi som skrives ut av programmet.

:::::::::::::


:::::::::::::{tab-item} b
Endre på programmet slik at det regner ut summen

$$
S = 1 + 2 + 3 + \ldots + 99 + 100
$$


::::{answer}
:::{code-block} python
---
linenos:
emphasize-lines: 2
---
s = 0   # variabel som skal lagre summen
for n in range(1, 101):
    s = s + n

print(s)
:::
::::

:::::::::::::


:::::::::::::{tab-item} c
Endre på programmet slik at det regner ut summen

$$
S = 1 + 3 + 5 + \ldots + 97 + 99
$$

::::{answer}
:::{code-block} python
---
linenos:
emphasize-lines: 2
---
s = 0   # variabel som skal lagre summen
for n in range(1, 101, 2):
    s = s + n

print(s)
:::
::::

:::::::::::::


:::::::::::::{tab-item} d
Endre på programmet slik at det regner ut summen

$$
S = 2 + 4 + 6 + \ldots + 98 + 100
$$


::::{answer}
:::{code-block} python
---
linenos:
emphasize-lines: 2
---
s = 0   # variabel som skal lagre summen
for n in range(2, 101, 2):
    s = s + n

print(s)
:::
::::

:::::::::::::

::::::::::::::

:::{interactive-code}
---
predict:
---
s = 0   # variabel som skal lagre summen
for n in range(1, 6):
    s = s + n

print(s)


:::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 9
---
level: 2
---

En sum er gitt ved 

$$
S = 1 + \dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{8} + \dfrac{1}{16} + \ldots
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som skriver ut de første 5 leddene i summen.




::::{answer}
:::{code-block} python
---
linenos:
---
for i in range(1, 6, 1):
    a = 1 / 2**(n + 1)
    print(a)

:::
::::


:::::::::::::


:::::::::::::{tab-item} b
Lag et program som regner ut summen av de 5 første leddene i summen



::::{answer}
:::{code-block} python
---
linenos:
---
s = 0
for i in range(1, 6, 1):
    a = 1 / 2**(n + 1)
    s = s + a

print(s)
    
:::
::::


:::::::::::::


:::::::::::::{tab-item} c
Bruk programmet ditt til å bestemme hvilken verdi summen nærmer seg når vi bruker veldig mange ledd.



::::{answer}
:::{code-block} python
---
linenos:
---
s = 0
for i in range(1, 10001, 1):
    a = 1 / 2**(n + 1)
    s = s + a

print(s)
    
:::
::::


:::::::::::::


::::::::::::::


:::{interactive-code}
# Din kode her




:::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 10
---
level: 3
---

Anna og Bjørn jobber med summen 

$$
S = 1 - \dfrac{1}{2} + \dfrac{1}{4} - \dfrac{1}{8} + \dfrac{1}{16} - \ldots
$$

:::{dialogue}
---
name1: Anna
name2: Bjørn
speaker1: left
speaker2: right
---
Anna: Jeg vet hvordan vi kan regne ut summen når alle leddene er positive, men nå er jo leddene positive og negative annen hver gang.
Bjørn: Kan vi ikke bare bruke en `if`{l=python}-`else`{l=python}-setning sånn at programmet bytter på fortegnet annen hver gang da?
Anna: Jo! Er ikke det litt som å bare sjekke om et tall er delelig med $2$ da?
Bjørn: Det tror jeg vil funke!
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Ta utgangspunkt i ideen til Anna og Bjørn, og lag et program som skriver ut de 5 første leddene i summen.



:::::::::::::


:::::::::::::{tab-item} b
Lag et program som regner ut summen av de 5 første leddene.


:::::::::::::


:::::::::::::{tab-item} c
Bruk programmet ditt til å bestemme hvilken verdi programmet nærmer seg når vi bruker veldig mange ledd. 


:::::::::::::


::::::::::::::


:::{interactive-code}
# Din kode her




:::



:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 11
---
level: 3
---

Nedenfor ser du tre figurer. Figurene er satt sammen av små kvadrater.

Tenk deg at du skal fortsette å lage figurer etter samme mønster. Vi lar $K_n$ være antall små kvadrater i figur $n$.

:::{figure} ./figurer/oppgaver/oppgave_11/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en formel for $K_n$.


::::{answer}
$$
K_n = 9 + 8(n - 1) = 8n + 1 \qder n \in \mathbb{N}
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som regner ut og skriver ut hvor mange små kvadrater det er i hver av de $10$ første figurene.

:::::::::::::


:::::::::::::{tab-item} c
Du starter med å lage figur $1$, så figur $2$, deretter figur $3$, og så videre.

Lag et program som finner ut hvor mange kvadrater du må bruke for å lage de 10 000 første figurene.

:::::::::::::

::::::::::::::

:::{interactive-code}
# Din kode her 




:::



:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 12
---
level: 3
---

Nedenfor ser du tre figurer. Figurene er satt sammen av små kvadrater.

Tenk deg at du skal fortsette å lage figurer etter samme mønster. Vi lar $K_n$ være antall små kvadrater i figur $n$. 


:::{figure} ./figurer/oppgaver/oppgave_12/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en formel for $K_n$. 


::::{answer}
$$
K(n) = (n + 1)^2 = n^2 + 2n + 1
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som beregner og skriver ut hvor mange små kvadrater det er i hver av de $20$ første figurene.

:::::::::::::



:::::::::::::{tab-item} c
Tenk deg at du har 1 000 000 små kvadrater. Du starter med å lage figur $1$, så figur $2$, deretter figur $3$, og så videre. 

Lag et program som finner ut
1. Hvor mange figurer du kan lage
2. Hvor mange små kvadrater du har igjen

:::::::::::::

::::::::::::::


:::{interactive-code}
# Din kode her




:::


:::::::::::::::


---




:::::::::::::::{exercise} Oppgave 13
---
level: 3
---
> I denne oppgaven skal du jobbe med summer av oddetall og partall. 

Vi lar $S_n$ være summen av de $n$ første oddetallene slik at 

\begin{align*}
    S_1 &= 1 \\
    S_2 &= 1 + 3 \\
    S_3 &= 1 + 3 + 5 \\
    S_4 &= 1 + 3 + 5 + 7 \\
    S_5 &= 1 + 3 + 5 + 7 + 9 \\
    S_6 &= 1 + 3 + 5 + 7 + 9 + 11 \\
    \vdots & \quad \quad \quad \vdots \quad \quad \quad \vdots \quad \quad \quad \vdots \\
\end{align*}


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som skriver ut de $20$ første oddetallene. Bruk formelen for oddetallene gitt ved 

$$
O_n = 2n - 1 \qder n \in \mathbb{N}
$$


::::{answer}
:::{code-block} python
---
linenos:
---
for n in range(1, 21):
    oddetall = 2 * n - 1

    print(oddetall)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som skriver ut $S_1, S_2, S_3, \ldots, S_{20}$.

::::{answer}
:::{code-block} python
---
linenos:
---
s = 0
for n in range(1, 21):
    oddetall = 2 * n - 1
    s = s + oddetall

    print(s)
:::
::::
:::::::::::::


:::::::::::::{tab-item} c
La $P_n$ være summen av de $n$ første partallene. 

Lag et program som skriver ut $P_1, P_2, P_3, \ldots, P_{20}$. 


::::{answer}
:::{code-block} python
---
linenos:
---
p = 0
for n in range(1, 21):
    partall = 2 * n
    p = p + partall
    
    print(p)
:::
::::


:::::::::::::

::::::::::::::


:::{interactive-code}
# TODO: skriv din kode her



:::


:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 14
---
level: 3
---
Anna og Nicolai jobber med å lage et program som regner ut $n$-fakultet definert med formelen:

$$
n! = 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (n - 1) \cdot n
$$

For eksempel er 

$$
5! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 = 120
$$

:::{dialogue}
---
name1: Anna
name2: Nicolai
speaker1: left
speaker2: right
---
Anna: Når vi regner ut summer, så setter vi en variabel `s = 0`{l=python} på starten av programmet, og så legger vi til leddene ved å skrive `s = s + ledd`{l=python}.
Nicolai: Ja, kanskje vi bare kan bytte ut plusstegnet med et gangetegn da?
Anna: Men hvis `s`{l=python} er `0`{l=python} i starten, så blir jo svaret alltid `0`{l=python}?
Nicolai: Ja, men vi startet med `0`{l=python} fordi å plusse på `0`{l=python} endrer ikke summen. Hvilket tall er det som ikke endrer verdien til et produkt?
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Ta utgangspunkt i dialogen mellom Anna og Nicolai og lag et program som regner ut $5!$. 


::::{answer}
:::{code-block} python
---
linenos:
---
s = 1
for n in range(1, 6):
    s = s * n
    
print(s)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Antall måter å stokke en kortstokk på er $52!$

Bruk programmet ditt til å regne ut $52!$. 

Kan du forklare hvorfor det sannsynligvis stemmer at når man stokker en kortstokk, så er det nesten umulig å få samme rekkefølge som en annen gang?

::::{answer}
:::{code-block} python
---
linenos:
---
s = 1
for n in range(1, 53):
    s = s * n
    
print(s)
:::

som gir utskriften

:::{code-block} console
80658175170943878571660636856403766975289505440883277824000000000000
:::
::::

:::::::::::::

::::::::::::::

:::{interactive-code}
# Din kode her



:::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 15
---
level: 3
---
Nedenfor vises et kvadrat med sidelengder $3$. 

Kvadratet er fylt med mindre fargelagte kvadrater som blir mindre og mindre. 


:::{figure} ./figurer/oppgaver/oppgave_15/figur.svg
---
width: 80%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som skriver ut arealet til de $10$ største fargelagte kvadratene i figuren. 


::::{answer}
:::{code-block} python
---
linenos:
---
s = 3
for n in range(1, 11):
    s = s / 2

    print(s**2)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som skriver regner ut summen av arealene til de $100$ største fargelagte kvadratene i figuren.


::::{answer}
:::{code-block} python
---
linenos:
---
areal = 0
s = 3
for n in range(1, 101):
    s = s / 2
    areal = areal + s**2


print(areal)
:::
::::

:::::::::::::

::::::::::::::


:::{interactive-code}
# Din kode her




:::

:::::::::::::::





---




:::::::::::::::{exercise} Oppgave 16
---
level: 3
---
Nedenfor vises en figur som er satt sammen av uendelige mange linjestykker.


Lengden til et linjestykke er alltid $90 \%$ av lengden til det forrige linjestykket. Det første linjestykket er $100$ cm langt. 


:::{figure} ./figurer/oppgaver/oppgave_16/figur.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som skriver ut lengden til de $10$ første linjestykkene i figuren.


::::{answer}
:::{code-block} python
---
linenos:
---
l = 100
for n in range(1, 11):
    print(l)
    
    l = 0.9 * l
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som regner ut summen av lengdene til de $100$ første linjestykkene i figuren. 


::::{answer}
:::{code-block} python
---
linenos:
---
s = 0
l = 100
for n in range(1, 101):
    s = s + l 
    l = 0.9 * l
    
print(s)
:::
::::

:::::::::::::

:::::::::::::{tab-item} c
Lag et program som finner hvor mange linjestykker du må sette sammen for at figuren skal være minst $9$ meter.

:::::::::::::
::::::::::::::


:::{interactive-code}
# Din kode her




:::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 17
---
level: 3
---
Nedenfor vises tre figurer som følger et bestemt mønster. 

La $K_n$ være antall små kvadrater i figur $n$. 


:::{figure} ./figurer/oppgaver/oppgave_17/figur.svg
---
class: no-click, adaptive-figure
width: 100%
---
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en formel for $K_n$.


:::::::::::::


:::::::::::::{tab-item} b
Lag et program som skriver ut $K_1$, $K_2$, $K_3$, $\ldots$, $K_{20}$.


:::::::::::::


:::::::::::::{tab-item} c
Lag et program som regner ut hvor mange små kvadrater du må bruke for å lage de 20 første figurene.


:::::::::::::



::::::::::::::


:::{interactive-code}
# Din kode her



:::


:::::::::::::::


---




:::::::::::::::{exercise} Oppgave 18
---
level: 3
---
Å regne ut $\pi$ med så mange desimaler som mulig har vært et mål for matematikere i over tusen år. En måte å komme fram til verdien til $\pi$ på er med summen

$$
\pi = \dfrac{4}{1} - \dfrac{4}{3} + \dfrac{4}{5} - \dfrac{4}{7} + \dfrac{4}{9} - \ldots
$$


Jo flere ledd man bruker, jo nærmere kommer man verdien til $\pi$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som skriver ut de $5$ første leddene i summen.

Du bør få disse verdiene i utskriften:

:::{code-block} console
4.0
-1.3333333333333333
0.8
-0.5714285714285714
0.4444444444444444
:::

::::{answer}
:::{code-block} python
---
linenos:
---
pi = 0

for n in range(1, 6):
    if n % 2 == 0: # Hvis n er delelig med 2. Ledd 2, 4, 6, osv.
        ledd = -4 / (2 * n - 1)
    else: # n er ikke delelig med 2. Ledd 1, 3, 5, osv.
        ledd = 4 / (2 * n - 1) 
    print(ledd)
:::
::::



:::::::::::::


:::::::::::::{tab-item} b
Lag et program som summerer de $5$ første leddene i tallfølgen.


::::{answer}
:::{code-block} python
---
linenos:
---
pi = 0

for n in range(1, 6):
    if n % 2 == 0: # Hvis n er delelig med 2. Ledd 2, 4, 6, osv.
        ledd = -4 / (2 * n - 1)
    else: # n er ikke delelig med 2. Ledd 1, 3, 5, osv.
        ledd = 4 / (2 * n - 1) 

    pi = pi + ledd # Legger til leddet i summen

print(pi)
:::
::::

:::::::::::::


:::::::::::::{tab-item} c

Bestem en god tilnærming til $\pi$ med programmet ditt fra **b**.

:::{sidebar}
$\pi = 3.141592653589793 \ldots$
:::

Hvor mange ledd trenger du for å få $\pi$ med $5$ riktige desimaler? 


:::::::::::::

::::::::::::::

::::{interactive-code}
# Din kode her



::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 19
---
level: 4
---
Summen av en annen tallfølge nærmer seg også $\pi$, men mye raskere enn den forrige. Summen er

$$
\pi = 3 + \dfrac{4}{2 \cdot 3 \cdot 4} - \dfrac{4}{4 \cdot 5 \cdot 6} + \dfrac{4}{6 \cdot 7 \cdot 8} - \dfrac{4}{8 \cdot 9 \cdot 10} + \ldots
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som skriver ut de $5$ første leddene i summen.

Du bør få utskriften:

:::{code-block} console
3
0.16666666666666666
-0.03333333333333333
0.011904761904761904
-0.005555555555555556
:::


::::{answer}
:::{code-block} python
---
linenos:
---
pi = 3
print(pi)

for i in range(1, 5):
    nevner = (2 * i) * (2 * i + 1) * (2 * i + 2)
    if i % 2 == 0:
        ledd = -4 / nevner        
    else:
        ledd = 4 / nevner
        
    print(ledd)
:::
::::

:::::::::::::


:::::::::::::{tab-item} b
Lag et program som regner ut en tilnærming til $\pi$ ved å bruke de 10 000 først leddene i summen.


::::{answer}
:::{code-block} python
---
linenos:
---
pi = 3
for i in range(1, 10_000):
    nevner = (2 * i) * (2 * i + 1) * (2 * i + 2)
    if i % 2 == 0:
        ledd = -4 / nevner        
    else:
        ledd = 4 / nevner


    pi = pi + ledd


print(pi)
:::

som gir utskriften

:::{code-block} console
3.1415926535900383
:::
::::

:::::::::::::

::::::::::::::


:::{interactive-code}
# Din kode her 




:::

:::::::::::::::


---




:::::::::::::::{exercise} Oppgave 20
---
level: 4
---
En rask måte å komme fram til sifrene til $\pi$ er ved ta utgangspunkt i **kjedebrøken** nedenfor:

$$
\pi = \dfrac{4}{1 + \dfrac{1^2}{3 + \dfrac{2^2}{5 + \dfrac{3^2}{7 + \dfrac{4^2}{9 + \ddots}}}}}
$$



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Regn ut en tilnærming til $\pi$ ved å bruke $3$ ledd i kjedebrøken:

$$
\pi \approx \dfrac{4}{1 + \dfrac{1^2}{3 + \dfrac{2^2}{5}}}
$$

:::::::::::::


:::::::::::::{tab-item} b
Lag en algoritme du kan bruke til å skrive et program som regner ut verdien til $\pi$ ved å bruke $n$ ledd i kjedebrøken.

:::::::::::::


:::::::::::::{tab-item} c
Lag et program med utgangspunkt i algoritmen din fra **b** og regn ut en tilnærming til $\pi$. 


:::{interactive-code}
# Din kode her



:::


::::{answer}
:::{code-block} python
---
linenos:
---
N = 100 # Antall ledd i kjedebrøken
nevner = 2 * N - 1 # først nevner

for n in range(N - 1, 0, -1): # Starter med det siste leddet
    nevner = 2 * n - 1 + n**2 / nevner # neste nevner
    
pi = 4 / nevner

print(pi)
:::

::::

:::::::::::::

::::::::::::::


:::::::::::::::



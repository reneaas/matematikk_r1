# Oppgaver: Logaritmer


:::{margin} Tips: Oppgave 1
Husk at $x$-koordinaten til et punkt $(x, y)$ gir logaritmen $x = \log_a(y)$.
:::

:::::::::::::::{exercise} Oppgave 1
I figuren nedenfor vises grafen til eksponentialfunksjonen

$$
f(x) = 10^x
$$

:::{plot}
width: 80%
function: 10**x
xmin: -0.1
xmax: 1.2
xstep: 0.1
ymax: 11
:::


> Bruk grafen til å lese av omtrentlige verdier for oppgavene nedenfor.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\log_{10}(5)$


::::{answer}
$$
\log_{10}(5) \approx 0.7
$$
::::


::::{solution}
Vi ser fra grafen at når $y = 5$, så er $x \approx 0.7$. Siden det er $x$-koordinaten til $10^x$ som gir oss $\log_{10}(y)$, så har vi at

$$
\log_{10}(5) \approx 0.7.
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem $\log_{10}(2)$


::::{answer}
$$
\log_{10}(2) \approx 0.3
$$
::::


::::{solution}
Vi ser fra grafen at når $y = 2$, så er $x \approx 0.3$. Siden det er $x$-koordinaten til $10^x$ som gir oss $\log_{10}(y)$, så har vi at

$$
\log_{10}(2) \approx 0.3.
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $\log_{10}(8)$


::::{answer}
$$
\log_{10}(8) \approx 0.9
$$
::::


::::{solution}
Vi ser fra grafen at når $y = 8$, så er $x \approx 0.9$. Siden det er $x$-koordinaten til $10^x$ som gir oss $\log_{10}(y)$, så har vi at

$$
\log_{10}(8) \approx 0.9.
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Bestem $\log_{10}(10)$


::::{answer}
$$
\log_{10}(10) = 1
$$
::::


::::{solution}
Vi ser fra grafen at når $y = 10$, så er $x = 1$. Siden det er $x$-koordinaten til $10^x$ som gir oss $\log_{10}(y)$, så har vi at

$$
\log_{10}(10) = 1.
$$

Dette stemmer også bra med at vi må opphøye $10$ med $1$ for å få $10$.
::::


:::::::::::::

::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2
I figuren nedenfor vises grafen til eksponentialfunksjonen

$$
f(x) = 4^x
$$

:::{plot}
width: 80%
function: 4**x
xmin: -0.5
xmax: 4
xstep: 0.5
ymax: 20
ystep: 2
:::


> Bruk grafen til å lese av omtrentlige verdier for oppgavene nedenfor.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\log_4(4)$.


::::{answer}
$$
\log_4(4) = 1
$$
::::


::::{solution}
Vi ser at grafen til $f$ skjærer linja $y = 4$ i $(1, 4)$ som betyr at $x \approx 1$ når $y = 4$. Siden det er $x$-koordinaten til $4^x$ som gir oss $\log_4(y)$, så har vi at

$$
\log_4(4) = 1.
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $\log_4(16)$.


::::{answer}
$$
\log_4(16) = 2
$$
::::

::::{solution}
Vi ser at grafen til $f$ skjærer linja $y = 16$ i $(2, 16)$ som betyr at $x \approx 2$ når $y = 16$. Siden det er $x$-koordinaten til $4^x$ som gir oss $\log_4(y)$, så har vi at

$$
\log_4(16) = 2.
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Bestem $\log_4(2)$.


::::{answer}
$$
\log_4(2) = \frac{1}{2} = 0.5
$$
::::


::::{solution}
Vi ser at grafen til $f$ skjærer linja $y = 2$ i $(0.5, 2)$ som betyr at $x \approx 0.5$ når $y = 2$. Siden det er $x$-koordinaten til $4^x$ som gir oss $\log_4(y)$, så har vi at

$$
\log_4(2) = \frac{1}{2} = 0.5.
$$
::::


:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
I grafen nedenfor vises grafen til en logaritmefunksjon $f(x) = \log_a(x)$.

Bestem verdien til grunntallet $a$.


:::{plot}
width: 80%
function: log(x) / log(4)
xmin: -1
xmax: 8
:::


::::{hints}
Uansett grunntall, så vil grafen til en logaritmefunksjon gå gjennom $(a, 1)$. Det betyr at $\log_a(a) = 1$.
::::


::::{answer}
$$
a = 4
$$
::::

::::{solution}
Vi vet at $\log_a(a) = 1$ siden grafen til en logaritmefunksjon alltid går gjennom $(a, 1)$. For grafen ovenfor er dette punktet $(4, 1)$ som betyr at grunntallet til logaritmen er

$$
a = 4
$$
::::



:::::::::::::


:::::::::::::{tab-item} b
I figuren nedenfor vises grafen til en logaritmefunksjon $g(x) = \log_b(x)$.

Bestem verdien til grunntallet $b$.


:::{plot}
width: 80%
function: log(x) / log(6)
xmin: -1
xmax: 8
:::

::::{answer}
$$
b = 6
$$
::::


::::{solution}
Vi vet at $\log_b(b) = 1$ siden grafen til en logaritmefunksjon alltid går gjennom $(b, 1)$. For grafen ovenfor er dette punktet $(6, 1)$ som betyr at grunntallet til logaritmen er

$$
b = 6
$$
::::



:::::::::::::


:::::::::::::{tab-item} c
I figuren nedenfor vises grafen til en logaritmefunksjon $g(x) = \log_c(x)$.

Bestem verdien til grunntallet $c$.


:::{plot}
width: 80%
function: log(x) / log(3)
xmin: -1
xmax: 8
:::


::::{answer}
$$
c = 3
$$
::::


::::{solution}
Vi vet at $\log_c(c) = 1$ siden grafen til en logaritmefunksjon alltid går gjennom $(c, 1)$. For grafen ovenfor er dette punktet $(3, 1)$ som betyr at grunntallet til logaritmen er

$$
c = 3
$$
::::



:::::::::::::
::::::::::::::
:::::::::::::::



---


:::{margin} Tips: Oppgave 4
Her kan det være lurt å faktorisere tallene slik at du får dem som en potens med samme grunntall som logaritmen du skal bestemme.

Husk at logaritmen er eksponenten vi må opphøye grunntallet med!

:::

:::::::::::::::{exercise} Oppgave 4
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\log_4(64)$


::::{answer}
$$
\log_4(64) = 3
$$
::::


::::{solution}

:::{factor-tree}
n: 64
width: 80%
align: right
figsize: (3, 7)
nocache:
:::

Vi skriver $64$ som en potens av $4$. Vi kan primtallsfaktorisere med faktortreet til høyre.
Da får vi at 

$$
64 = 2^6 = 2^{2 \cdot 3} = (2^2)^3 = 4^3
$$

Dermed er

$$
\log_4(64) = \log_4(4^3) = 3
$$

::::



:::::::::::::


:::::::::::::{tab-item} b
Bestem $\log_2(256)$.


::::{answer}
$$
\log_2(256) = 8
$$
::::

::::{solution}
:::{factor-tree}
n: 256
width: 100%
align: right
figsize: (5, 10)
nocache:
:::

Vi ønsker å skrive $256$ som en potens av $2$. Vi kan primtallsfaktorisere med faktortreet til høyre.
Da får vi at

$$
256 = 2^8
$$

Dermed er

$$
\log_2(256) = \log_2(2^8) = 8
$$

::::


:::::::::::::


:::::::::::::{tab-item} c
Bestem $\log_{10}(10000)$.


::::{answer}
$$
\log_{10}(10000) = 4
$$
::::

::::{solution}
Vi ønsker å skrive om $10000$ som en potens av $10$ som vi kan gjøre ved:

$$
10000 = 10^4
$$

siden $10000$ har $4$ nuller. Da får vi at

$$
\log_{10}(10000) = \log_{10}(10^4) = 4
$$

::::



:::::::::::::


:::::::::::::{tab-item} d
Bestem $\log_3(81)$.


::::{answer}
$$
\log_3(81) = 4
$$
::::

::::{solution}
:::{factor-tree}
n: 81
width: 60%
align: right
figsize: (3, 6)
nocache:
:::

Vi ønsker å skrive om $81$ som en potens av $3$. Vi kan oppnå dette ved å primtallsfaktorisere med faktortreet til høyre.
Da får vi at

$$
81 = 3^4
$$

Da følger det at

$$
\log_3(81) = \log_3(3^4) = 4
$$
::::


:::::::::::::


::::::::::::::
:::::::::::::::



---


:::{margin} Tips: Oppgave 5
Husk på sammenhengen mellom eksponentialfunksjoner og logaritmer!
:::

:::::::::::::::{exercise} Oppgave 5
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Programmet nedenfor regner med en eksponentialfunksjon og skriver ut en verdi. 

Les programmet og forutsi hva programmet skriver ut.

Hvilken logaritme kan du bestemme med utskriften til programmet?

:::{interactive-code}
---
predict:
---
x = 0
while 10**x < 1000:
    x = x + 0.125

print(x)
:::


::::{answer}
$$
\log_{10}(1000) = 3
$$
::::

::::{solution}
Utskriften fra programmet er $3$. Siden grunntallet til eksponentialfunksjonen er $10$, betyr det at

$$
\log_{10}(1000) = 3
$$
::::



:::::::::::::



:::::::::::::{tab-item} b
Programmet nedenfor regner med en eksponentialfunksjon og skriver ut en verdi. 

Les programmet og forutsi hva programmet skriver ut.

Hvilken logaritme kan du bestemme med utskriften til programmet?

:::{interactive-code}
---
predict:
---
x = 0
while 7**x < 49:
    x = x + 0.125

print(x)
:::


::::{answer}
$$
\log_{7}(49) = 2
$$
::::

::::{solution}
Utskriften fra programmet er $2$. Siden grunntallet til eksponentialfunksjonen er $7$, betyr det at

$$
\log_{7}(49) = 2
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Programmet nedenfor regner med en eksponentialfunksjon og skriver ut en verdi. 

Les programmet og forutsi hva programmet skriver ut.

Hvilken logaritme kan du bestemme med utskriften til programmet?

:::{interactive-code}
---
predict:
---
x = 0
while 2**x < 64:
    x = x + 0.125

print(x)
:::


::::{answer}
$$
\log_{2}(64) = 6
$$
::::

::::{solution}
Utskriften fra programmet er $6$. Siden grunntallet til eksponentialfunksjonen er $2$, betyr det at

$$
\log_{2}(64) = 6
$$

::::



:::::::::::::



::::::::::::::

:::::::::::::::


---


:::{margin} Tips: Oppgave 6
Husk at når vi ser på grafen til en eksponentialfunksjon med grunntall $a$ så vil et punkt $(x, y)$ tilsvare et punkt $(y, x)$ på grafen til logaritmen med samme grunntall. Altså, $x$- og $y$-koordinatene bytter rolle!
:::

:::::::::::::::{exercise} Oppgave 6
I figuren nedenfor vises logaritmefunksjonen 

$$
f(x) = \log_3(x).
$$


:::{plot}
width: 80%
function: log(x) / log(3)
xmin: -2
xmax: 30
ymin: -0.2
xstep: 2
ymax: 3
ystep: 0.2
:::

> Bruk grafen ovenfor til å finne omtrentlige svar i oppgavene nedenfor.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Løs likningen

$$
3^x = 22
$$


::::{answer}
$$
x \approx 2.8
$$
::::


::::{solution}
$\log_3(x)$ gir oss hvilken verdi vi må opphøye $3$ med for å få $x$. Vi ser fra grafen at $\log_3(22) \approx 2.8$ som betyr at løsningen av likningen er

$$
3^x = 22 \liff x \approx 2.8
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Løs likningen

$$
3^x = 6
$$


::::{answer}
$$
x \approx 1.6
$$
::::


::::{solution}
$\log_3(x)$ gir oss hvilken verdi vi må opphøye $3$ med for å få $x$. Vi ser fra grafen at $\log_3(6) \approx 1.6$ som betyr at løsningen av likningen er

$$
3^x = 6 \liff x \approx 1.6
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Løs likningen

$$
3^x = 2
$$


::::{answer}
$$
x \approx 0.6
$$
::::

::::{solution}
$\log_3(x)$ gir oss hvilken verdi vi må opphøye $3$ med for å få $x$. Vi ser fra grafen at $\log_3(2) \approx 0.6$ som betyr at løsningen av likningen er

$$
3^x = 2 \liff x \approx 0.6
$$
::::

:::::::::::::


::::::::::::::




:::::::::::::::


---


:::{margin} Tips: Oppgave 7
Her får du bruk for produktregelen til logaritmer: 

$$
\log_a(x\cdot y) = \log_a(x) + \log_a(y)
$$
:::

:::::::::::::::{exercise} Oppgave 7
I figuren nedenfor vises grafen til 

$$
f(x) = 5^x
$$

:::{plot}
width: 80%
function: 5**x
xmin: -0.2
xmax: 2
xstep: 0.2
ymin: -5
ymax: 10
ystep: 1
:::

> Du må her også lese av omtrentlige verdier. Men lurt å tenke på hvordan du kan faktorisere tallet ditt så du kan bruke produktregelen for logaritmer.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\log_5(10)$.


::::{hints}
Faktoriser først $10$ til to tall du kan lese av logaritmen for. Deretter bruk produktregelen for logaritmer til å bestemme $\log_5(10)$.
::::


::::{answer}
$$
\log_5(10) \approx 1.4
$$
::::


::::{solution}
Vi kan ikke lese av $\log_5(10)$ direkte fra grafen ovenfor, men vi kan skrive 

$$
10 = 2\cdot 5 \liff \log_5(10) = \log_5(2\cdot 5) = \log_5(2) + \log_5(5)
$$

Fra grafen kan vi lese av at

$$
\log_5(2) \approx 0.4 \and \log_5(5) = 1
$$

Dermed er 

$$
\log_5(10) = \log_5(2) + \log_5(5) \approx 0.4 + 1 = 1.4
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $\log_5(14)$.


::::{answer}
$$
\log_5(14) \approx 1.6
$$
::::


::::{solution}
Vi kan ikke lese av $\log_5(14)$ direkte, men vi kan skrive

$$
14 = 2 \cdot 7 \liff \log_5(14) = \log_5(2) + \log_5(7)
$$

Vi kan lese av fra grafen at

$$
\log_5(2) \approx 0.4 \and \log_5(7) \approx 1.2
$$

Dermed er

$$
\log_5(14) = \log_5(2) + \log_5(7) \approx 0.4 + 1.2 = 1.6
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
Bestem $\log_5(20)$.


::::{answer}
$$
\log_5(20) \approx 1.8
$$
::::

::::{solution}
Vi kan ikke lese av $\log_5(20)$ direkte fra grafen, men vi kan skrive

$$
20 = 2 \cdot 2 \cdot 5
$$

Da kan vi bruke produktregelen for logaritmer to ganger:

\begin{align*}
    \log_5(2\cdot 2 \cdot 5) &= \log_5(2 \cdot 2) + \log_5(5) \\
    \\
    &= \log_5(2) + \log_5(2) + \log_5(5) \\
    \\
    &= 2\log_5(2) + \log_5(5)
\end{align*}

Vi kan lese av fra grafen at

$$
\log_5(2) \approx 0.4 \and \log_5(5) = 1
$$

Dermed har vi at

$$
\log_5(20) = 2\log_5(2) + \log_5(5) \approx 2\cdot 0.4 + 1 = 0.8 + 1 = 1.8
$$
::::


:::::::::::::


::::::::::::::


:::::::::::::::


---


:::{margin} Oppgave 8
Her får du bruk for kvotientregelen for logaritmer:

$$
\log_a\left(\frac{x}{y}\right) = \log_a(x) - \log_a(y)
$$

:::

:::::::::::::::{exercise} Oppgave 8
I figuren nedenfor vises grafen til eksponentialfunksjonen 


$$
f(x) = 10^x
$$


:::{plot}
width: 80%
function: 10**x
xmin: -0.1
xmax: 1
ymin: -1
ymax: 11
xstep: 0.1
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\log_{10}\left(\dfrac{1}{2}\right)$.


::::{hints}
Les av $\log_{10}(1)$ og $\log_{10}(2)$. Bruk deretter kvotientregelen for å bestemme $\log_{10}\left(\dfrac{1}{2}\right)$
::::


::::{answer}
$$
\log_{10}\left(\dfrac{1}{2}\right) \approx -0.3
$$
::::


::::{solution}
Vi skriver først om uttrykket med kvotientregelen:

$$
\log_{10}\left(\dfrac{1}{2}\right) = \log_{10}(1) - \log_{10}(2)
$$

Vi husker på at $\log_{10}(1) = 0$ uansett hvilket grunntall det er. Men vi må bestemme $\log_{10}(2)$. Vi ser at grafen omtrent går gjennom $(0.3, 2)$. Det betyr at 

$$
\log_{10}(2) \approx 0.3
$$

Dermed har vi at

$$
\log_{10}\left(\dfrac{1}{2}\right) = 0 - 0.3 = -0.3
$$

::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $\log_{10}\left(\dfrac{5}{2}\right)$.


::::{answer}
$$
\log_{10}\left(\dfrac{5}{2}\right) \approx 0.4
$$
::::


::::{solution}
Vi kan ikke lese av $\log_{10}\left(\dfrac{5}{2}\right)$ direkte, men vi kan bruke kvotientregelen til å skrive om uttrykket til

$$
\log_{10}\left(\dfrac{5}{2}\right) = \log_{10}(5) - \log_{10}(2)
$$

Deretter leser vi at $\log_{10}(5)$ og $\log_{10}(2)$ fra grafen. Vi ser at grafen omtrent går gjennom $(0.7, 5)$ og $(0.3, 2)$. Det betyr at

$$
\log_{10}(5) \approx 0.7 \and \log_{10}(2) \approx 0.3
$$

Dermed har vi at

$$
\log_{10}\left(\dfrac{5}{2}\right) \approx 0.7 - 0.3 = 0.4
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $\log_{10}\left(\dfrac{5}{8}\right)$.


::::{answer}
$$
\log_{10}\left(\dfrac{5}{8}\right) \approx -0.2
$$
::::

::::{solution}
Vi kan ikke lese av $\log_{10}\left(\dfrac{5}{8}\right)$ direkte, men vi kan bruke kvotientregelen til å skrive om uttrykket til

$$
\log_{10}\left(\dfrac{5}{8}\right) = \log_{10}(5) - \log_{10}(8)
$$

Deretter leser vi at $\log_{10}(5)$ og $\log_{10}(8)$ fra grafen. Vi ser at grafen omtrent går gjennom $(0.7, 5)$ og $(0.9, 8)$. Det betyr at

$$
\log_{10}(5) \approx 0.7 \and \log_{10}(8) \approx 0.9
$$

Dermed har vi at

$$
\log_{10}\left(\dfrac{5}{8}\right) \approx 0.7 - 0.9 = -0.2
$$
::::


:::::::::::::


::::::::::::::



:::::::::::::::


---


:::{margin} Tips: Oppgave 9
Husk potensregelen for logaritmen:

$$
\log_a(x^y) = y \cdot \log_a(x)
$$
:::


:::::::::::::::{exercise} Oppgave 9
I grafen nedenfor vises grafen til logaritmefunksjonen

$$
f(x) = \log_3(x)
$$


:::{plot}
width: 80%
function: log(x) / log(3)
xmin: -1
xmax: 14
ymin: -0.2
ymax: 3
xstep: 1
ystep: 0.2
:::

> Bruk grafen ovenfor til å lese av omtrentlige verdier for logaritmene i oppgavene nedenfor.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\log_3(6^4)$.

::::{hints}
Kan du lese av en omtrentlig verdi for $\log_3(6)$ og så bruke potensregelen for logaritmer til å bestemme $\log_3(6^4)$?
::::


::::{answer}
$$
\log_3(6^4) \approx 6.4
$$
::::


::::{solution}
Vi skriver om uttrykket med potensregelen for logaritmer:

$$
\log_3(6^4) = 4 \cdot \log_3(6)
$$

Deretter ser vi om vi kan lese av en omtrentlig verdi for $\log_3(6)$ fra grafen. Vi ser at grafen går gjennom punktet $(6, 1.6)$ som betyr at

$$
\log_3(6) \approx 1.6
$$

Dermed har vi at

$$
\log_3(6^4) = 4 \cdot 1.6 = 6.4
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $\log_3(6^{7})$.


::::{answer}
$$
\log_3(6^{7}) \approx 11.2
$$
::::

::::{solution}
Vi skriver om uttrykket med potensregelen for logaritmer:

$$
\log_3(6^{7}) = 7 \cdot \log_3(6)
$$

Deretter ser vi om vi kan lese av en omtrentlig verdi for $\log_3(6)$ fra grafen. Vi ser at grafen går gjennom punktet $(6, 1.6)$ som betyr at

$$
\log_3(6) \approx 1.6
$$

Dermed har vi at

$$
\log_3(6^{7}) = 7 \cdot 1.6 = 11.2
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bestem $\log_3(7^{10})$.


::::{answer}
$$
\log_3(7^{10}) \approx 18
$$
::::

::::{solution}
Vi skriver om uttrykket med potensregelen for logaritmer:

$$
\log_3(7^{10}) = 10 \cdot \log_3(7)
$$

Deretter ser vi om vi kan lese av en omtrentlig verdi for $\log_3(7)$ fra grafen. Vi ser at grafen går gjennom punktet $(7, 1.8)$ som betyr at

$$
\log_3(7) \approx 1.8
$$

Dermed har vi at

$$
\log_3(7^{10}) \approx 10 \cdot 1.8 = 18
$$
::::


:::::::::::::


::::::::::::::


:::::::::::::::


---


:::{margin} Tips: Oppgave 10
Hvis du ikke vil *spoile* løsningen, kan du ta en ny titt på programmene i oppgave 5 for å få inspirasjon til hvor du kan begynne.
:::

:::::::::::::::{exercise} Oppgave 10 
Nedenfor vises en samtale mellom Anna og Bjørn.


:::{dialogue}
---
name1: Anna
name2: Bjørn
speaker1: left
speaker2: right
---
Anna: Jeg vil lage et program som regner ut logaritmen $\log_3(y)$ for en tilfeldig verdi av $y$ så lenge $y > 0$.
Bjørn: Men trenger du ikke bare å øke $x$ frem til $3^x < y$ ikke lenger er sant? Da blir $x \approx \log_3(y)$. 
Anna: Sant! Kan jeg ikke gjøre det med en `while`{l=python}-løkke som starter med `x = 0`{l=python}?
Bjørn: Jeg tror kanskje ikke det funker når $y \in \langle 0, 1\rangle$? 
:::



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Lag et program som bruker strategien Anna og Bjørn foreslår, og bruk det til å bestemme $\log_3(70)$.

> Sjekk først at programmet ditt gir riktig svar for $\log_3(1)$ og $\log_3(2)$ så du vet at programmet ditt funker som det skal.


::::{answer}
$$
\log_3(70) \approx 3.867
$$
::::

::::{solution}
:::{code-block} python
---
linenos:
---
x = 0
while 3**x < 70:
    x = x + 0.0001
    
print(x)
:::

som gir utskriften

:::{code-block} console
3.8672000000037365
:::

Dermed er 

$$
\log_3(70) \approx 3.867
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
Tenk over den siste innvendingen til Bjørn, og juster programmet ditt slik at du kan bestemme $\log_3(0.1)$. 

Hva blir verdien til $\log_3(0.1)$?


::::{answer}
$$
\log_3(0.1) \approx -2.1
$$
::::

::::{solution}
Vi må senke verdien til $x$ fremfor å øke den, siden $3^x$ blir bare mindre enn $1$ dersom $x < 0$. Da kan vi skrive et program som dette:

:::{code-block} python
---
linenos:
---
x = 0
while 3**x > 0.1:
    x = x - 0.001
    
print(x)
:::

Utskriften blir


:::{code-block} console
-2.09599999999988
:::

som betyr at 

$$
\log_3(0.1) \approx -2.1
$$


::::


:::::::::::::



::::::::::::::


:::{interactive-code}
# Din kode her




:::






:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 11
Regn ut.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\log_{10}(10^{-2})
$$


::::{answer}
$$
\log_{10}(10^{-2}) = -2
$$
::::


::::{solution}
Vi bruker potensregelen for logaritmer: 

$$
\log_{10}(10^{-2}) = -2 \cdot \log_{10}(10) = -2 \cdot 1 = -2.
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
$$
\log_2(4^{-2})
$$


::::{answer}
$$
\log_2(4^{-2}) = -4
$$
::::


::::{solution}
Vi bruker potensregelen for logaritmer:

$$
\log_2(4^{-2}) = -2 \cdot \log_2(4).
$$

Deretter kan vi merke oss at $4 = 2^2$, som betyr at $\log_2(2^2) = 2$. Da følger det at

$$
\log_2(4^{-2}) = -2 \cdot \log_2(4) = -2 \cdot 2 = -4.
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
$$
\log_3(9^{-4})
$$


::::{answer}
$$
\log_3(9^{-4}) = -8
$$
::::


::::{solution}
Vi bruker potensregelen for logaritmer:

$$
\log_3(9^{-4}) = -4 \cdot \log_3(9) = -4 \cdot 2 = -8.
$$

Her har vi brukt at $9 = 3^2$ som betyr at $\log_3(9) = 2$.

::::

:::::::::::::


:::::::::::::{tab-item} d
$$
\log_5(25^{-8})
$$


::::{answer}
$$
\log_5(25^{-8}) = -16
$$
::::


::::{solution}
Vi bruker potensregelen for logaritmer:

$$
\log_5(25^{-8}) = -8 \cdot \log_5(25) = -8 \cdot 2 = -16.
$$

Her har vi brukt at $25 = 5^2$ som betyr at $\log_5(25) = 2$.

::::

:::::::::::::




::::::::::::::





:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 12
Skriv så enkelt som mulig.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\log_a(x y^3) + \log_{a}\left(\dfrac{x}{y}\right)
$$

::::{answer}
$$
2 \log_a(xy)
$$
::::

::::{solution}
\begin{align*}
\log_a(x y^3) + \log_{a}\left(\dfrac{x}{y}\right) &= \log_a(x) + \log_a(y^3) + \log_{a}(x) - \log_{a}(y) \\
\\
&= 2\log_a(x) + 3\log_a(y) - \log_a(y) \\
\\
&= 2\log_a(xy).
\end{align*}
::::

:::::::::::::

:::::::::::::{tab-item} b
$$
\log_a(x^3 y^2) - 2\log_a(x y)
$$


::::{answer}
$$
\log_a(x)
$$
::::

::::{solution}
\begin{align*}
    \log_a(x^3 y^2) - 2\log_a(x y) &= \log_a(x^3) + \log_a(y^2) - 2\left(\log_a(x) + \log_a(y)\right) \\
    \\
    &= 3\log_a(x) + 2\log_a(y) - 2\log_a(x) - 2\log_a(y) \\
    \\
    &= \log_a(x).
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\log_a\left(\dfrac{x^5}{y^2}\right) - \log_a(x^2 y)
$$


::::{answer}
$$
3\log_a\left(\dfrac{x}{y}\right)
$$
::::


::::{solution}
\begin{align*}
    \log_a\left(\dfrac{x^5}{y^2}\right) - \log_a(x^2 y) &= \log_a(x^5) - \log_a(y^2) - \log_a(x^2) - \log_a(y) \\
    \\
    &= 5\log_a(x) - 2\log_a(y) - 2\log_a(x) - \log_a(y) \\
    \\
    &= 3\log_a(x) - 3\log_a(y) \\
    \\
    &= 3\left(\log_a(x) - \log_a(y)\right) \\
    \\
    &= 3\log_a\left(\dfrac{x}{y}\right)
\end{align*}
::::

:::::::::::::

:::::::::::::{tab-item} d
$$
\dfrac{1}{2}\log_a(x) - \log_a\left(\sqrt[4]{x}\right)
$$


::::{answer}
$$
\dfrac{1}{4}\log_a(x)
$$
::::

::::{solution}
\begin{align*}
    \dfrac{1}{2}\log_a(x) - \log_a\left(\sqrt[4]{x}\right) &= \dfrac{1}{2}\log_a(x) - \log_a\left(x^{1/4}\right) \\
    \\
    &= \dfrac{1}{2}\log_a(x) - \dfrac{1}{4}\log_a(x) \\
    \\
    &= \left(\dfrac{1}{2} - \dfrac{1}{4}\right)\log_a(x) \\
    \\
    &= \dfrac{1}{4}\log_a(x).
\end{align*}
::::


:::::::::::::



::::::::::::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 13
Utvid uttrykkene nedenfor til en sum av logaritmer.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\log_a(6x^3 y)
$$


::::{answer}
$$
\log_a(6) + 3\log_a(x) + \log_a(y)
$$
::::

::::{solution}
\begin{align*}
\log_a(6x^3 y) &= \log_a(6) + \log_a(x^3) + \log_a(y) \\
\\
&= \log_a(6) + 3\log_a(x) + \log_a(y)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} b
$$
\log_a\left(\dfrac{\sqrt[3]{x^2}}{5y}\right)
$$


::::{answer}
$$
\dfrac{2}{3}\log_a(x) - \log_a(y) - \log_a(5)
$$
::::

::::{solution}
\begin{align*}
\log_a\left(\dfrac{\sqrt[3]{x^2}}{5y}\right) &= \log_a(\sqrt[3]{x^2}) - \log_a(5y) \\
\\
&= \log_a(x^{2/3}) - \left(\log_a(5) + \log_a(y)\right) \\
\\
&= \dfrac{2}{3}\log_a(x) - \log_a(y) - \log_a(5)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\log_a\left(\dfrac{25x^4}{\sqrt{y}}\right)
$$


::::{answer}
$$
2\log_a(5) + 4\log_a(x) - \dfrac{1}{2}\log_a(y)
$$
::::

::::{solution}
\begin{align*}
\log_a\left(\dfrac{25x^4}{\sqrt{y}}\right) &= \log_a(25x^4) - \log_a(\sqrt{y}) \\
\\
&= \log_a(25) + \log_a(x^4) - \log_a(y^{1/2}) \\
\\
&= \log_a(5^2) + 4\log_a(x) - \dfrac{1}{2}\log_a(y)
\\
&= 2\log_a(5) + 4\log_a(x) - \dfrac{1}{2}\log_a(y)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
\log_a\left(\dfrac{(3x^2y^5)^4}{2x}\right)
$$


::::{answer}
$$
4\log_a(3) - \log_a(2) + 7\log_a(x) + 20\log_a(y)
$$
::::

::::{solution}
\begin{align*}
\log_a\left(\dfrac{(3x^2y^5)^4}{2x}\right) &= \log_a\left((3x^2y^5)^4\right) - \log_a(2x) \\
\\
&= \log_a(3^4 x^8 y^{20}) - \left(\log_a(2) + \log_a(x)\right) \\
\\
&= \log_a(3^4) + \log_a(x^8) + \log_a(y^{20}) - \log_a(2) - \log_a(x) \\
\\
&= 4\log_a(3) + 8\log_a(x) + 20\log_a(y) - \log_a(2) - \log_a(x) \\
\\
&= 4\log_a(3) - \log_a(2) + 7\log_a(x) + 20\log_a(y)
\end{align*}
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---



:::{margin} Så "enkelt" som mulig 
Det er ikke alltid like lett å vite nøyaktig hva vi mener med at du skal skrive en logaritme så "enkel" som mulig, siden det vil være avhengig av hva vi skal bruke det til. Når vi jobber med likninger er det typisk å skrive den så kompakt og enkel som mulig. Når vi skal regne ut verdien til logaritmer, er det i stedet nyttig å skrive den som en sum av så enkle som mulig logaritmer.
:::

:::::::::::::::{exercise} Oppgave 14
Skriv uttrykkene så enkelt som mulig.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\log_a(x^2 y^3) - \log_a(xy)
$$


::::{answer}
$$
\log_a(x y^2)
$$

eller

$$
\log_a(x) + 2\log_a(y)
$$
::::

::::{solution}
$$
\log_a(x^2 y^3) - \log_a(xy) = \log_a\left(\dfrac{x^2 y^3}{xy}\right) = \log_a(x y^2)
$$

Eventuelt som en sum:

$$
\log_a(x y^2) = \log_a(x) + \log_a(y^2) = \log_a(x) + 2\log_a(y)
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
$$
\log_a\left(\dfrac{x^4}{y^2}\right) + \log_a(y)
$$


::::{answer}
$$
4\log_a(x) - \log_a(y)
$$
::::

::::{solution}
\begin{align*}
\log_a\left(\dfrac{x^4}{y^2}\right) + \log_a(y) &= \log_a(x^4) - \log_a(y^2) + \log_a(y) \\
\\
&= 4\log_a(x) - 2\log_a(y) + \log_a(y) \\
\\
&= 4\log_a(x) - \log_a(y)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\log_a\left(\dfrac{x^3}{y}\right) - 2\log_a(x)
$$


::::{answer}
$$
\log_a(x) - \log_a(y)
$$

eller 

$$
\log_a\left(\dfrac{x}{y}\right)
$$
::::

::::{solution}
\begin{align*}
\log_a\left(\dfrac{x^3}{y}\right) - 2\log_a(x) &= \log_a(x^3) - \log_a(y) - 2\log_a(x) \\
\\
&= 3\log_a(x) - \log_a(y) - 2\log_a(x) \\
\\
&= \log_a(x) - \log_a(y)
\end{align*}

Som vi også kan skrive som

$$
\log_a(x) - \log_a(y) = \log_a\left(\dfrac{x}{y}\right)
$$
::::

:::::::::::::

:::::::::::::{tab-item} d
$$
\log_a\left((x^2 - 9)(x + 3)\right) - \log_a(x - 3)
$$


::::{answer}
$$
2 \log_a(x + 3)
$$
::::


::::{solution}
Vi husker først på at konjugatsetningen gir oss 

$$
x^2 - 9 = (x - 3)(x + 3)
$$

Da får vi

\begin{align*}
\log_a\left((x^2 - 9)(x + 3)\right) - \log_a(x - 3) &= \log_a\left( (x - 3)(x+3)(x+3) \right) - \log_a(x - 3) \\
\\
&= \log_a\left((x - 3)(x + 3)^2\right) - \log_a(x - 3) \\
\\
&= \log_a\left(\dfrac{\cancel{(x - 3)}(x + 3)^2}{\cancel{x - 3}}\right) \\
\\
&= \log_a((x + 3)^2) \\
\\
&= 2 \log_a(x + 3)
\end{align*}
::::


:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 15
> Det er såpass vanlig å jobbe med logaritmen med grunntall $10$, at man har innført en kortere notasjon for den. Vi definerer $\lg(x) = \log_{10}(x)$. Denne logaritmen er viktig fordi den bruker 10-tallssystemet.

Skriv så enkelt som mulig.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\lg\left(\dfrac{100x}{0.1y}\right)
$$


::::{answer}
$$
\lg(x) - \lg(y) + 3
$$
::::


::::{solution}
\begin{align*}
\lg\left(\dfrac{100x}{0.1y}\right) &= \lg(100x) - \lg(0.1y) \\
\\
&= \lg(100) + \lg(x) - \left(\lg(0.1) + \lg(y)\right) \\
\\
&= \lg(10^2) + \lg(x) - \lg(0.1) - \lg(y) \\
\\
&= 2\lg(10) + \lg(x) - \lg(10^{-1}) - \lg(y) \\
\\
&= 2 + \lg(x) - (-1) \cdot \lg(10) - \lg(y) \\
\\
&= 2 + \lg(x) + 1 - \lg(y) \\
\\
&= \lg(x) - \lg(y) + 3
\end{align*}
::::


:::::::::::::


:::::::::::::{tab-item} b
$$
\lg\left(\sqrt{x}{y^3}\right)
$$


::::{answer}
$$
\dfrac{1}{2}\lg(x) + 3 \lg(y)
$$
::::

::::{solution}
\begin{align*}
\lg\left(\sqrt{x}{y^3}\right) &= \lg(\sqrt{x}) + \lg(y^3) \\
\\
&= \lg(x^{1/2}) + 3 \lg(y) \\
\\
&= \dfrac{1}{2}\lg(x) + 3 \lg(y)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\lg(25x^4) - \lg(5x)
$$


::::{answer}
$$
\lg(5) + 3\lg(x)
$$
::::


::::{solution}
\begin{align*}
\lg(25x^4) - \lg(5x) &= \lg(25) + \lg(x^4) - \lg(5) - \lg(x) \\
\\
&= \lg(5^2) + 4\lg(x) - \lg(5) - \lg(x) \\
\\
&= 2\lg(5) + 3\lg(x) - \lg(5) \\
\\
&= \lg(5) + 3\lg(x)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
\lg\left(\sqrt{\dfrac{x}{y^3}}\right)
$$


::::{answer}
$$
\dfrac{1}{2}\lg(x) - \dfrac{3}{2}\lg(y)
$$
::::

::::{solution}
\begin{align*}
\lg\left(\sqrt{\dfrac{x}{y^3}}\right) &= \lg\left(\left(\dfrac{x}{y^3}\right)^{1/2}\right) \\
\\
&= \dfrac{1}{2}\lg\left(\dfrac{x}{y^3}\right) \\
\\
&= \dfrac{1}{2}\lg(x) - \dfrac{1}{2}\lg(y^3) \\
\\
&= \dfrac{1}{2}\lg(x) - \dfrac{3}{2}\lg(y)
\end{align*}
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 16
> Så langt har vi jobbet med grunntall som er hele tall. Nå skal vi se på et grunntall som har en veldig spesiell egenskap: Eksponentialfunksjonen med dette grunntallet er den eneste funksjonen som er lik sin egen deriverte overalt! Grunntallet kalles Eulers tall (leses: "Oilers tall") og vi skriver det som $e$. 


<!-- :::{dialogue}
---
name1: Euler
name2: Bernoulli
speaker1: left
speaker2: right
---
Euler: Jeg ser for meg at jeg vil sette inn $1 \, \mathrm{kr}$ på en bankkonto. Deretter vil jeg la det vokse med $100 \,%$. 
Bernoulli: Okei, det er lett. Det blir bare $2 \, \mathrm{kr}$ etter et år.
Euler: Ja sant. Men hva om jeg lar det vokse med $50 \%$ to ganger på ett år. Da får jeg vel $\left(1 + \dfrac{1}{2}\right)^2 \, \mathrm{kr}$ på bankkontoen.
Bernoulli: Ja. Det blir $2.25 \, \mathrm{kr}$. Men hvor vil du med dette?
Euler: Vel se for deg at vi øker $1 \, \mathrm{kr}$ med $100 \%$ fire ganger i løpet av et år – altså $25 \%$ av gangen. Da får jeg vel $\left(1 + \dfrac{1}{4}\right)^4 \, \mathrm{kr}$ på bankkontoen.
Bernoulli: Hmm. Jeg lurer på hva som skjer med verdien hvis du gjør det veldig mange ganger, og ikke bare fire ganger.
::: -->

:::{dialogue}
---
name1: Bernoulli
name2: Euler
speaker1: left
speaker2: right
---
Bernoulli: Jeg har tenkt på dette med renter. Hvis jeg setter inn $1 \, \mathrm{kr}$ i banken og får $100 \%$ rente en gang i året, så dobles pengene til $2 \, \mathrm{kr}$.
Euler: Det gir mening. Men hva om banken betaler ut renten oftere, for eksempel halvårlig?
Bernoulli: Da vokser pengene med $50 \%$ to ganger. Det blir $\left(1 + \dfrac{1}{2}\right)^2 = 2.25 \, \mathrm{kr}$.  
Euler: Aha, så vi får mer enn $2 \, \mathrm{kr}$! Hva om vi får rente fire ganger i året, altså $25 \%$ av gangen?
Bernoulli: Da får vi $\left(1 + \dfrac{1}{4}\right)^4 = 2.4414 \, \mathrm{kr}$. Enda litt mer!  
Euler: Interessant … jeg lurer på hva som skjer hvis vi øker antallet renteutbetalinger mot uendelig mange ganger i året.
:::

<br>

Det Euler og Bernoulli snakker om ovenfor vil lede fram til en god tilnærming til verdien til tallet $e$. 

Bruk programmet nedenfor til å bestemme tallet $e$ med $5$ desimaler. Hvor mye vil $1 \, \mathrm{kr}$ vokse til etter ett år hvis vi får $100 \%$ rente til sammen, når banken betaler ut renten veldig ofte?

:::{interactive-code}
n = 1
while n < 100_000_000:

    e = (1 + 1/n)**n
    n = n * 10

    print(f"{e = :0.5f}") # skriver ut verdien med 5 desimaler
:::


::::{answer}
$$
e \approx 2.71828
$$
::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 17
> Når vi bruker $e$ som grunntall for en logaritme, så skriver vi $\ln(x)$. Det vil si at $\ln(x) = \log_e(x)$. 

Skriv så enkelt som mulig.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\ln(xy^2) + 4 \ln(x^3 y) - 2\ln(xy^6)
$$



::::{answer}
$$
10\ln(x) - 8\ln(y)
$$
::::

::::{solution}
\begin{align*}
&\ln(xy^2) + 4 \ln(x^3 y) - 2\ln(xy^6)\\ 
\\
&= \ln(x) + 2\ln(y) + 4(3\ln(x) + \ln(y)) - 2(\ln(x) + 6\ln(y)) \\
\\
&= 10\ln(x) - 8\ln(y)
\end{align*}
::::
:::::::::::::



:::::::::::::{tab-item} b
$$
\ln\left(\dfrac{5x^3}{\sqrt[4]{y^2}}\right)
$$


::::{answer}
$$
\ln(5) + 3\ln(x) - \dfrac{1}{2}\ln(y)
$$
::::

::::{solution}
\begin{align*}\ln\left(\dfrac{5x^3}{\sqrt[4]{y^2}}\right) &= \ln(5x^3) - \ln\left(\sqrt[4]{y^2}\right) \\
\\
&= \ln(5x^3) - \dfrac{1}{4}\ln(y^2) \\
\\
&= \ln(5) + 3\ln(x) - \dfrac{1}{2}\ln(y)
\end{align*}
::::


:::::::::::::

:::::::::::::{tab-item} c
$$
\ln \left(\sqrt[3]{a^2 b^5}\right)
$$


::::{answer}
$$
\dfrac{2}{3} \ln(a) + \dfrac{5}{3} \ln(b)
$$
::::

::::{solution}
\begin{align*}
\ln \left(\sqrt[3]{a^2 b^5}\right) &= \ln \left((a^2 b^5)^{1/3}\right) \\
\\
&= \dfrac{1}{3} \ln(a^2 b^5) \\
\\
&= \dfrac{1}{3} \left(2\ln(a) + 5\ln(b)\right) \\
\\
&= \dfrac{2}{3} \ln(a) + \dfrac{5}{3} \ln(b)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
\ln (e^3 x \sqrt{y})
$$


::::{answer}
$$
3 + \ln (x) + \dfrac{1}{2} \ln (y)
$$
::::

::::{solution}
\begin{align*}
\ln (e^3 x \sqrt{y}) &= \ln (e^3) + \ln (x) + \ln (\sqrt{y}) \\
\\
&= 3 + \ln (x) + \dfrac{1}{2} \ln (y)
\end{align*}
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 18
Trekk sammen og skriv som én logaritme.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
2 \ln(x) - \ln(5) + \dfrac{1}{2}\ln(y)
$$

::::{answer}
$$
\ln\left(\dfrac{x^2\sqrt{y}}{5}\right)
$$
::::

::::{solution}
\begin{align*}
2\ln(x) - \ln(5) + \dfrac{1}{2}\ln(y)
&= \ln(x^2) - \ln(5) + \ln\!\left(y^{1/2}\right) \\
&= \ln\left(\dfrac{x^2\,y^{1/2}}{5}\right)
\end{align*}
::::

:::::::::::::



:::::::::::::{tab-item} b
$$
3 \ln(a) - 2\ln(b) + \ln(4)
$$

::::{answer}
$$
\ln\left(\dfrac{4a^3}{b^2}\right)
$$
::::

::::{solution}
\begin{align*}
3\ln(a) - 2\ln(b) + \ln(4)
&= \ln(a^3) - \ln(b^2) + \ln(4) \\
&= \ln\left(\dfrac{4a^3}{b^2}\right)
\end{align*}
::::

:::::::::::::



:::::::::::::{tab-item} c
$$
\dfrac{1}{3}\ln(x) + \dfrac{2}{5}\ln(y) - \ln(z)
$$

::::{answer}
$$
\ln\left(\dfrac{x^{1/3} y^{2/5}}{z}\right)
$$
::::

::::{solution}
\begin{align*}
	\dfrac{1}{3}\ln(x) + \dfrac{2}{5}\ln(y) - \ln(z)
&= \ln\!\left(x^{1/3}\right) + \ln\!\left(y^{2/5}\right) - \ln(z) \\
&= \ln\left(\dfrac{x^{1/3} y^{2/5}}{z}\right)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
\ln(x) + \ln(x + 1) - \dfrac{1}{2}\ln(3)
$$

::::{answer}
$$
\ln\left(\dfrac{x(x+1)}{\sqrt{3}}\right)
$$
::::

::::{solution}
\begin{align*}
\ln(x) + \ln(x+1) - \dfrac{1}{2}\ln(3)
&= \ln\bigl(x(x+1)\bigr) - \ln\!\left(3^{1/2}\right) \\
&= \ln\left(\dfrac{x(x+1)}{\sqrt{3}}\right)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} e
$$
4 \ln(2x) - \ln(8) - 2\ln(x)
$$
 
::::{answer}
$$
\ln\bigl(2x^2\bigr)
$$
::::

::::{solution}
\begin{align*}
4\ln(2x) - \ln(8) - 2\ln(x)
&= \ln\bigl((2x)^4\bigr) - \ln(8) - \ln(x^2) \\
&= \ln\left(\dfrac{(2x)^4}{8x^2}\right) \\
&= \ln\left(\dfrac{16x^4}{8x^2}\right) \\
&= \ln\left(2x^2\right)
\end{align*}
::::
:::::::::::::

::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 19
Skriv så enkelt som mulig.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\ln(3) + 2\ln(x) - \dfrac{1}{2}\ln(y)
$$

::::{answer}
$$
\ln\left(\dfrac{3x^2}{\sqrt{y}}\right)
$$
::::

::::{solution}
\begin{align*}
\ln(3) + 2\ln(x) - \dfrac{1}{2}\ln(y)
&= \ln(3) + \ln(x^2) - \ln\!\left(y^{1/2}\right) \\
&= \ln\left(\dfrac{3x^2}{\sqrt{y}}\right)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} b
$$
3\ln(x+1) - \ln(x) - \ln(2)
$$

::::{answer}
$$
\ln\left(\dfrac{(x+1)^3}{2x}\right)
$$
::::

::::{solution}
\begin{align*}
3\ln(x+1) - \ln(x) - \ln(2)
&= \ln\bigl((x+1)^3\bigr) - \ln(2x) \\
&= \ln\left(\dfrac{(x+1)^3}{2x}\right)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\dfrac{1}{3}\ln(x^2 y) + \ln(5) - \ln(x)
$$

::::{answer}
$$
\ln\left(5\,\Bigl(\dfrac{y}{x}\Bigr)^{\!1/3}\right)
$$
::::

::::{solution}
\begin{align*}
	frac{1}{3}\ln(x^2 y) + \ln(5) - \ln(x)
&= \ln\!\left((x^2 y)^{1/3}\right) + \ln(5) - \ln(x) \\
&= \ln\!\left(5\,x^{2/3} y^{1/3}\right) - \ln(x) \\
&= \ln\!\left(\dfrac{5\,x^{2/3} y^{1/3}}{x}\right)
= \ln\!\left(5\,x^{-1/3} y^{1/3}\right) \\
&= \ln\left(5\,\Bigl(\dfrac{y}{x}\Bigr)^{1/3}\right)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
\ln\left(\dfrac{e^{4} x^2}{\sqrt{y}}\right) - \ln(e)
$$

::::{answer}
$$
\ln\left(\dfrac{e^{3} x^2}{\sqrt{y}}\right)
$$
::::

::::{solution}
\begin{align*}
\ln\left(\dfrac{e^{4} x^2}{\sqrt{y}}\right) - \ln(e)
&= \ln\left(\dfrac{e^{4} x^2}{\sqrt{y}}\cdot \dfrac{1}{e}\right) \\
&= \ln\left(\dfrac{e^{3} x^2}{\sqrt{y}}\right)
\end{align*}
::::

:::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 20
Trekk sammen og skriv som én logaritme.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\lg(5) + 2\lg(x) - \dfrac{1}{2}\lg(y)
$$

::::{answer}
$$
\lg\left(\dfrac{5x^2}{\sqrt{y}}\right)
$$
::::

::::{solution}
\begin{align*}
\lg(5) + 2\lg(x) - \dfrac{1}{2}\lg(y)
&= \lg(5) + \lg(x^2) - \lg\!\left(y^{1/2}\right) \\
\\
&= \lg\left(\dfrac{5x^2}{\sqrt{y}}\right)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} b
$$
3\lg(x+1) - \lg(2) - \lg(x)
$$

::::{answer}
$$
\lg\left(\dfrac{(x+1)^3}{2x}\right)
$$
::::

::::{solution}
\begin{align*}
3\lg(x+1) - \lg(2) - \lg(x)
&= \lg\bigl((x+1)^3\bigr) - \lg(2x) \\
\\
&= \lg\left(\dfrac{(x+1)^3}{2x}\right)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\dfrac{1}{3}\lg(25x^2) + \lg(y) - 2\lg(5)
$$

::::{answer}
$$
\lg\left(\dfrac{x^{2/3} y}{5^{4/3}}\right)
$$
::::

::::{solution}
\begin{align*}
	\dfrac{1}{3}\lg(25x^2) + \lg(y) - 2\lg(5)
&= \dfrac{1}{3}\bigl(\lg(25) + 2\lg(x)\bigr) + \lg(y) - 2\lg(5) \\
\\
&= \dfrac{2}{3}\lg(5) + \dfrac{2}{3}\lg(x) + \lg(y) - 2\lg(5) \\
\\
&= \dfrac{2}{3}\lg(x) + \lg(y) - \dfrac{4}{3}\lg(5) \\
\\
&= \lg\left(\dfrac{x^{2/3} y}{5^{4/3}}\right)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
4\lg(3x) - \lg(9) - \lg(x)
$$

::::{answer}
$$
\lg\bigl(9x^3\bigr)
$$
::::

::::{solution}
\begin{align*}
4\lg(3x) - \lg(9) - \lg(x)
&= \lg\bigl((3x)^4\bigr) - \lg(9) - \lg(x) \\
\\
&= \lg\left(\dfrac{(3x)^4}{9x}\right) \\
\\
&= \lg\left(\dfrac{81x^4}{9x}\right) = \lg(9x^3)
\end{align*}
::::

:::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 21
Skriv så enkelt som mulig.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\ln\left(\dfrac{e^5}{x^3}\right)
$$


::::{answer}
$$
5 - 3\ln(x)
$$
::::

::::{solution}
\begin{align*}
\ln\left(\dfrac{e^5}{x^3}\right)
&= \ln(e^5) - \ln(x^3) \\
&= 5 - 3\ln(x)
\end{align*}
::::


:::::::::::::



:::::::::::::{tab-item} b
$$
\ln\left(\sqrt{\dfrac{e^2 x}{y^3}}\right)
$$


::::{answer}
$$
1 + \dfrac{1}{2}\ln(x) - \dfrac{3}{2}\ln(y)
$$
::::

::::{solution}
\begin{align*}
\ln\left(\sqrt{\dfrac{e^2 x}{y^3}}\right)
&= \dfrac{1}{2}\,\ln\left(\dfrac{e^2 x}{y^3}\right) \\
&= \dfrac{1}{2}\big(\ln(e^2) + \ln(x) - 3\ln(y)\big) \\
&= \dfrac{1}{2}\big(2 + \ln(x) - 3\ln(y)\big) \\
&= 1 + \dfrac{1}{2}\ln(x) - \dfrac{3}{2}\ln(y)
\end{align*}
::::


:::::::::::::


:::::::::::::{tab-item} c
$$
\ln \left((e^3 x^2)^3\right) - \ln (e^6 x)
$$


::::{answer}
$$
3 + 5\ln(x)
$$
::::

::::{solution}
\begin{align*}
\ln \left((e^3 x^2)^3\right) - \ln (e^6 x)
&= \ln\big(e^9 x^6\big) - \ln\big(e^6 x\big) \\
&= \ln\left(\dfrac{e^9 x^6}{e^6 x}\right) \\
&= \ln\big(e^3 x^5\big) \\
&= 3 + 5\ln(x)
\end{align*}
::::


:::::::::::::


:::::::::::::{tab-item} d
$$
\ln\left(\dfrac{1}{\sqrt[3]{e x^3}}\right) + \ln (5e^2 x)
$$



::::{answer}
$$
\ln(5) + \dfrac{5}{3}
$$
::::

::::{solution}
\begin{align*}
\ln\left(\dfrac{1}{\sqrt[3]{e x^3}}\right) + \ln (5e^2 x)
&= -\,\ln\big(\sqrt[3]{e x^3}\big) + \ln(5) + \ln(e^2) + \ln(x) \\
&= -\,\dfrac{1}{3}\,\ln(e x^3) + \ln(5) + 2 + \ln(x) \\
&= -\,\dfrac{1}{3}\big(\ln(e) + 3\ln(x)\big) + \ln(5) + 2 + \ln(x) \\
&= -\,\dfrac{1}{3} - \ln(x) + \ln(5) + 2 + \ln(x) \\
&= \ln(5) + \dfrac{5}{3}
\end{align*}
::::


:::::::::::::


::::::::::::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 22
Skriv så enkelt som mulig.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
5 \lg(x^3) + \lg\left(\dfrac{1}{x^2}\right) + \lg(1000x^5)
$$


::::{answer}
$$
\lg\bigl(1000\,x^{18}\bigr)
$$
::::

::::{solution}
\begin{align*}
5\,\lg(x^3) + \lg\left(\dfrac{1}{x^2}\right) + \lg(1000x^5)
&= \lg\bigl((x^3)^5\bigr) + \lg\left(\dfrac{1}{x^2}\right) + \lg(1000x^5) \\
&= \lg\left(\dfrac{x^{15}\cdot 1000x^5}{x^2}\right) \\
&= \lg\bigl(1000\,x^{18}\bigr)
\end{align*}
::::

:::::::::::::



:::::::::::::{tab-item} b
$$
lg(\sqrt[3]{x^6}) + 10 \lg(\sqrt[5]{x}) - \lg(x^3)
$$


::::{answer}
$$
\lg(x)
$$
::::

::::{solution}
\begin{align*}
\lg\big(\sqrt[3]{x^6}\big) + 10\,\lg\big(\sqrt[5]{x}\big) - \lg(x^3)
&= \lg(x^2) + 10\,\lg\big(x^{1/5}\big) - 3\lg(x) \\
&= 2\lg(x) + 2\lg(x) - 3\lg(x) \\
&= \lg(x)
\end{align*}
::::

:::::::::::::



:::::::::::::{tab-item} c
$$
\ln(x^3) + \ln \left(\dfrac{e^2}{x^5}\right) - \ln \left(\dfrac{e^{-2}}{x}\right)
$$


::::{answer}
$$
\ln\left(\dfrac{e^{4}}{x}\right)
$$
::::

::::{solution}
\begin{align*}
\ln(x^3) + \ln\left(\dfrac{e^2}{x^5}\right) - \ln\left(\dfrac{e^{-2}}{x}\right)
&= \ln\left(\dfrac{x^3\,e^2}{x^5}\right) - \big(\ln(e^{-2}) - \ln x\big) \\
&= \ln\big(e^2 x^{-2}\big) - (-2 - \ln x) \\
&= 2 - 2\ln x + 2 + \ln x \\
&= 4 - \ln x \\
&= \ln\left(\dfrac{e^{4}}{x}\right)
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
\ln(x^2 - e^2) + \ln(x + 3) - 2\ln(x - e)
$$


::::{answer}
$$
\ln\left(\dfrac{(x+e)(x+3)}{x-e}\right)
$$
::::

::::{solution}
\begin{align*}
\ln(x^2 - e^2) + \ln(x + 3) - 2\ln(x - e)
&= \ln\left(\dfrac{(x^2 - e^2)(x+3)}{(x-e)^2}\right) \\
&= \ln\left(\dfrac{(x-e)(x+e)(x+3)}{(x-e)^2}\right) \\
&= \ln\left(\dfrac{(x+e)(x+3)}{x-e}\right)
\end{align*}
::::

:::::::::::::



::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 23
> Det er mulig å bytte fra en logaritme med grunntall $a$, $\log_a(x)$, til en logaritme med grunntall $b$, $\log_b(x)$. Noen ganger vil det gjøre det enklere å regne ut logaritmen avhengig av hvilket tall $x$ vi jobber med.



::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Forklar at hvis $x = a^p$ så er

$$
p = \log_a(x)
$$
::::{answer}
$$
p = \log_a(x)
$$
::::

::::{solution}
Med definisjonen av logaritmen er $\log_a(x)$ tallet $p$ slik at $a^p = x$.
::::

:::::::::::::

:::::::::::::{tab-item} b
Hvis $x = a^q$, hva er da $q$ lik?


::::{answer}
$$
q = \log_a(x)
$$
::::

::::{solution}
Samme definisjon: $a^q = x$ gir $q = \log_a(x)$.
::::

:::::::::::::


:::::::::::::{tab-item} c
Forklar at det må finnes et tall $r$ slik at man kan skrive 

$$
b = a^r
$$

Hva blir da $r$ lik?


::::{answer}
$$
r = \log_a(b)
$$
::::

::::{solution}
Per definisjon: $a^r = b$ betyr $r = \log_a(b)$.
::::

:::::::::::::


:::::::::::::{tab-item} d
Vis at med resultatene fra **a**, **b** og **c**, så vil følgende formel være sann: 

$$
\log_b(x) = \dfrac{\log_a(x)}{\log_a(b)}
$$
::::{answer}
$$
\log_b(x) = \dfrac{\log_a(x)}{\log_a(b)}
$$
::::

::::{solution}
La $t = \log_b(x)$. Da er $x = b^t$. Fra c) har vi $b = a^r$ med $r = \log_a(b)$, så
\begin{align*}
x = b^t = (a^r)^t = a^{rt}\;\Rightarrow\; \log_a(x) = rt = \log_a(b)\,\log_b(x).
\end{align*}
Dermed $\displaystyle \log_b(x) = \dfrac{\log_a(x)}{\log_a(b)}$.
::::

:::::::::::::

::::::::::::::


:::::::::::::::


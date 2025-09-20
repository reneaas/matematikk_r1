# Oppgavesamling


:::::::::::::::{exercise} Oppgave 1
Skriv så enkelt som mulig.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\dfrac{a^2 \cdot (2a^{-1} b^2)^2}{2^{-1} a^{-1} b^2}
$$


::::{answer}
$$
8ab^2
$$
::::

::::{solution}
\begin{align*}
    \dfrac{a^2 \cdot (2a^{-1} b^2)^2}{2^{-1} a^{-1} b^2} &= \dfrac{a^2 \cdot 2^2 \cdot a^{-2} \cdot b^4}{2^{-1} \cdot a^{-1} \cdot b^2} \\
    \\
    &= 2^{2 - (-1)} \cdot a^{2 - 2 - (-1)} \cdot b^{4 - 2} \\
    \\
    &= 2^3 \cdot a^1 \cdot b^2 \\
    \\
    &= 8ab^2
\end{align*}
::::


:::::::::::::



:::::::::::::{tab-item} b
$$
\sqrt{2} \cdot \sqrt{8} \cdot \sqrt[3]{4} \cdot \sqrt[3]{2}
$$


::::{answer}
$$
8
$$
::::

::::{solution}
\begin{align*}
    \sqrt{2} \cdot \sqrt{8} \cdot \sqrt[3]{4} \cdot \sqrt[3]{2} &= 2^{1/2} \cdot 2^{3/2} \cdot 2^{2/3} \cdot 2^{1/3} \\
    \\
    &= 2^{1/2 + 3/2 + 2/3 + 1/3} \\
    \\
    &= 2^{4/2 + 3/3} \\
    \\
    &= 2^{2 + 1} \\
    \\
    &= 2^3 \\
    \\
    &= 8
\end{align*}
::::


:::::::::::::


:::::::::::::{tab-item} c
$$
\dfrac{a^2 \cdot (a^2)^3}{(a^{-2} \cdot a^{-1})^3}
$$


::::{answer}
$$
a^{17}
$$
::::


::::{solution}
\begin{align*}
    \dfrac{a^2 \cdot (a^2)^3}{(a^{-2} \cdot a^{-1})^3} &= \dfrac{a^2 \cdot a^6}{a^{-6} \cdot a^{-3}} \\
    \\
    &= a^{2 + 6 - (-6) - (-3)} \\
    \\
    &= a^{2 + 6 + 6 + 3} \\
    \\
    &= a^{17}
\end{align*}
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
\dfrac{3b^2 \cdot 36a^3 \cdot 9(ab)^3}{12 (a^2b)^2}
$$



::::{answer}
$$
81a^2b^3
$$
::::

::::{solution}
\begin{align*}
    \dfrac{3b^2 \cdot 36a^3 \cdot 9(ab)^3}{12 (a^2b)^2} &= \dfrac{3 \cdot 36 \cdot 9}{12} \cdot \dfrac{b^2 \cdot a^3 \cdot (ab)^3}{(a^2b)^2} \\
    \\
    &= \dfrac{3 \cdot 3 \cdot 12 \cdot 9}{12} \cdot \dfrac{b^2 \cdot a^3 \cdot a^3 \cdot b^3}{a^4 \cdot b^2} \\
    \\
    &= 3 \cdot 3 \cdot 9 \cdot a^{3 + 3 - 4} \cdot b^{2 + 3 - 2} \\
    \\
    &= 81a^2b^3
\end{align*}
::::



:::::::::::::


:::::::::::::{tab-item} e
$$
\dfrac{\sqrt[3]{a^2 b} \cdot \sqrt{ab^3} \cdot \sqrt[6]{b}}{\sqrt[6]{a}}
$$



::::{answer}
$$
ab^2
$$
::::


::::{solution}
\begin{align*}
    \dfrac{\sqrt[3]{a^2 b} \cdot \sqrt{ab^3} \cdot \sqrt[6]{b}}{\sqrt[6]{a}} &= \dfrac{a^{2/3} \cdot b^{1/3} \cdot a^{1/2} \cdot b^{3/2} \cdot b^{1/6}}{a^{1/6}} \\
    \\
    &= a^{2/3 + 1/2 - 1/6} \cdot b^{1/3 + 3/2 + 1/6} \\
    \\
    &= a^{4/6 + 3/6 - 1/6} \cdot b^{2/6 + 9/6 + 1/6} \\
    \\
    &= a^{6/6} \cdot b^{12/6} \\
    \\
    &= ab^2
\end{align*}
::::


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
Sorter i stigende rekkefølge.

$$
\lg 100 \qquad \lg 10 \qquad \lg \dfrac{1}{100} \qquad \lg 0.1 \qquad \lg \sqrt{10} \qquad \lg \sqrt[3]{\dfrac{1}{10}}
$$


::::{answer}
1. $\lg \dfrac{1}{100}$
2. $\lg 0.1$
3. $\lg \sqrt[3]{\dfrac{1}{10}}$
4. $\lg \sqrt{10}$
5. $\lg 10$
6. $\lg 100$
::::


::::{solution}
Vi regner ut verdien til alle logaritmene:

\begin{align*}
    \lg 100 &= \lg 10^2 = 2 \\
    \\
    \lg 10 &= 1 \\
    \\
    \lg \dfrac{1}{100} &= \lg \dfrac{1}{10^2} = \lg 10^{-2} = -2 \\
    \\
    \lg 0.1 &= \lg 10^{-1} = -1 \\
    \\
    \lg \sqrt{10} &= \lg 10^{1/2} = \dfrac{1}{2} \\
    \\
    \lg \sqrt[3]{\dfrac{1}{10}} &= \lg \left( 10^{-1} \right)^{1/3} = \lg 10^{-1/3} = -\dfrac{1}{3}
\end{align*}

Dermed vil de stå i stigende rekkefølge som følger:

1. $\lg \dfrac{1}{100}$
2. $\lg 0.1$
3. $\lg \sqrt[3]{\dfrac{1}{10}}$
4. $\lg \sqrt{10}$
5. $\lg 10$
6. $\lg 100$

::::

:::::::::::::


:::::::::::::{tab-item} b
Sorter i stigende rekkefølge.

$$
\ln e^2 \qquad \ln \sqrt{e} \qquad \ln \dfrac{1}{e} \qquad \ln \dfrac{1}{e^2} \qquad \ln \sqrt[4]{e^3} \qquad e^{\ln 5}
$$


::::{answer}
1. $\ln \dfrac{1}{e^2}$
2. $\ln \dfrac{1}{e}$
3. $\ln \sqrt{e}$
4. $\ln \sqrt[4]{e^3}$
5. $\ln e^2$
6. $e^{\ln 5}$
::::

::::{solution}
Vi regner ut verdien til alle logaritmene:

\begin{align*}
    \ln e^2 &= 2 \\
    \\
    \ln \sqrt{e} &= \ln e^{1/2} = \dfrac{1}{2} \\
    \\
    \ln \dfrac{1}{e} &= \ln e^{-1} = -1 \\
    \\
    \ln \dfrac{1}{e^2} &= \ln e^{-2} = -2 \\
    \\
    \ln \sqrt[4]{e^3} &= \ln (e^3)^{1/4} = \ln e^{3/4} = \dfrac{3}{4} \\
    \\
    e^{\ln 5} &= 5
\end{align*}

Dermed vil de stå i stigende rekkefølge som følger:
1. $\ln \dfrac{1}{e^2}$
2. $\ln \dfrac{1}{e}$
3. $\ln \sqrt{e}$
4. $\ln \sqrt[4]{e^3}$
5. $\ln e^2$
6. $e^{\ln 5}$

::::
:::::::::::::



:::::::::::::{tab-item} c
Hvilke av tallene nedenfor er mindre enn $10$?

$$
3 \sqrt{11} \qquad 10 \lg 9 \qquad 5 \ln 9
$$


::::{answer}
$3 \sqrt{11}$ og $10 \lg 9$ er mindre enn $10$. 

$5 \ln 9$ er ikke mindre enn $10$.
::::


::::{solution}
Vi sjekker hver av tallene: 

$$
3 \sqrt{11} = \sqrt{9} \cdot \sqrt{11} = \sqrt{99} < \sqrt{100} = 10
$$

$$
10 \lg 9 < 10 \lg 10 = 10 \cdot 1 = 10
$$

$$
5 \ln 9 > 5 \ln e^2 = 5 \cdot 2 = 10
$$

Dermed er $3 \sqrt{11}$ og $10 \lg 9$ mindre enn $10$, mens $5 \ln 9$ ikke er det.
::::

:::::::::::::


::::::::::::::
:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
Løs likningene.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
2 \cdot 6^x = 8 \cdot 3^x
$$


::::{answer}
$$
x = 2
$$
::::

::::{solution}
$$
2 \cdot 6^x = 8 \cdot 3^x
$$

$$
\ln (2 \cdot 6^x) = \ln (8 \cdot 3^x)
$$

$$
\ln 2 + \ln 6^x = \ln 8 + \ln 3^x
$$

$$
\ln 2 + x \ln 6 = \ln 8 + x \ln 3
$$

$$
x \ln 6 - x \ln 3 = \ln 8 - \ln 2
$$

$$
x (\ln 6 - \ln 3) = \ln \dfrac{8}{2}
$$

$$
x \ln \dfrac{6}{3} = \ln 4
$$

$$
x \ln 2 = \ln 4
$$

$$
x = \dfrac{\ln 4}{\ln 2} = \dfrac{\ln 2^2}{\ln 2} = \dfrac{2 \ln 2}{\ln 2} = 2
$$

::::


:::::::::::::



:::::::::::::{tab-item} b
$$
2^{4x - 1} = 1
$$


::::{answer}
$$
x = \dfrac{1}{4}
$$
::::


::::{solution}
$$
2^{4x - 1} = 1
$$

$$
\log_2 (2^{4x - 1}) = \log_2 (1)
$$

$$
(4x - 1) \log_2 (2) = \log_2 (1)
$$

$$
(4x - 1) \cdot 1 = 0
$$

$$
4x - 1 = 0
$$

$$
4x = 1
$$

$$
x = \dfrac{1}{4}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
3\cdot 5^x = 4 \cdot 3^x
$$


::::{answer}
$$
x = \dfrac{\ln \frac{3}{4}}{\ln \frac{3}{5}} = \dfrac{\ln 3 - \ln 4}{\ln 3 - \ln 5}
$$
::::

::::{solution}
$$
3\cdot 5^x = 4 \cdot 3^x
$$

$$
\ln (3 \cdot 5^x) = \ln (4 \cdot 3^x)
$$

$$
\ln 3 + \ln 5^x = \ln 4 + \ln 3^x
$$

$$
\ln 3 + x \ln 5 = \ln 4 + x \ln 3
$$

$$
\ln 3 - \ln 4 = x \ln 3 - x \ln 5
$$

$$
\ln 3 - \ln 4 = x (\ln 3 - \ln 5)
$$

$$
\ln \dfrac{3}{4} = x \ln \dfrac{3}{5}
$$

$$
x = \dfrac{\ln \frac{3}{4}}{\ln \frac{3}{5}} = \dfrac{\ln 3 - \ln 4}{\ln 3 - \ln 5}
$$

::::
:::::::::::::


:::::::::::::{tab-item} d
$$
e^{2x} - 4e^x + 3 = 0
$$


::::{answer}
$$
x = 0 \or x = \ln 3
$$
::::


::::{solution}
Vi gjør variabelskifte $u = e^x$. Da kan likningen skrives om til andregradslikningen

$$
u^2 - 4u + 3 = 0
$$

Vi bruker $abc$-formelen:

$$
u = \dfrac{4 \pm \sqrt{(-4)^2 - 4 \cdot 1 \cdot 3}}{2 \cdot 1} = \dfrac{4 \pm \sqrt{16 - 12}}{2} = \dfrac{4 \pm 2}{2}
$$

Altså er 

$$
u = 2 \pm 1 = \begin{cases}
    3 \\
    1
\end{cases}
$$

Det betyr at 

$$
u = 1 \or u = 3
$$

$$
e^x = 1 \or e^x = 3
$$

$$
x = \ln 1 \or x = \ln 3
$$

$$
x = 0 \or x = \ln 3
$$
::::


:::::::::::::



::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 4 
Løs likningene.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
10 \cdot 3^x = 5 \cdot 2^x
$$


::::{answer}
$$
x = -\dfrac{\lg 2}{\lg 3 - \lg 2}
$$
::::

::::{solution}
$$
10 \cdot 3^x = 5 \cdot 2^x
$$

$$
\lg (10 \cdot 3^x) = \lg (5 \cdot 2^x)
$$

$$
\lg 10 + \lg 3^x = \lg 5 + \lg 2^x
$$

$$
x \lg 3 - x \lg 2 = \lg 5 - \lg 10
$$

$$
x (\lg 3 - \lg 2) = \lg \dfrac{5}{10}
$$

$$
x \lg \dfrac{3}{2} = \lg \dfrac{1}{2}
$$

$$
x = \dfrac{\lg \frac{1}{2}}{\lg \frac{3}{2}} = \dfrac{\lg 1 - \lg 2}{\lg 3 - \lg 2} = -\dfrac{\lg 2}{\lg 3 - \lg 2}
$$

::::

:::::::::::::


:::::::::::::{tab-item} b
$$
\lg x^2 = 3 \lg x + 4
$$


::::{answer}
$$
x = 10^{-4}
$$
::::

::::{solution}
$$
\lg x^2 = 3 \lg x + 4
$$

$$
2 \lg x = 3 \lg x + 4
$$

$$
- \lg x = 4
$$

$$
\lg x = -4
$$

$$
x = 10^{-4}
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
$$
(\lg x)^2 = 3 \lg x + 4
$$


::::{answer}
$$
x = 10^4 \or x = 10^{-1}
$$
::::


::::{solution}
Vi gjør variabelskifte $u = \lg x$. Da kan likningen skrives om til andregradslikningen

$$
u^2 = 3u + 4
$$

$$
u^2 - 3u - 4 = 0
$$

Så bruker vi $abc$-formelen:

$$
u = \dfrac{3 \pm \sqrt{(-3)^2 - 4 \cdot 1 \cdot (-4)}}{2 \cdot 1} = \dfrac{3 \pm \sqrt{9 + 16}}{2} = \dfrac{3 \pm 5}{2}
$$

Det gir 

$$
u = 4 \or u = -1
$$

som betyr at

$$
\lg x = 4 \or \lg x = -1
$$

som betyr at

$$
x = 10^4 \or x = 10^{-1}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
2 \cdot 6^x = 18 \cdot 2^x
$$


::::{answer}
$$
x = 2
$$
::::


::::{solution}
$$
2 \cdot 6^x = 18 \cdot 2^x
$$

$$
\ln (2 \cdot 6^x) = \ln (18 \cdot 2^x)
$$

$$
\ln 2 + \ln 6^x = \ln 18 + \ln 2^x
$$

$$
\ln 2 + x \ln 6 = \ln 18 + x \ln 2
$$

$$
x \ln 6 - x \ln 2 = \ln 18 - \ln 2
$$

$$
x (\ln 6 - \ln 2) = \ln \dfrac{18}{2}
$$

$$
x \ln \dfrac{6}{2} = \ln 9
$$

$$
x \ln 3 = \ln 9
$$

$$
x = \dfrac{\ln 9}{\ln 3} = \dfrac{\ln 3^2}{\ln 3} = \dfrac{2 \ln 3}{\ln 3} = 2
$$

::::


:::::::::::::


::::::::::::::
:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 5
Løs likningene.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\lg (x^2 - 3) = \lg (2x)
$$


::::{answer}
$$
x = 3
$$
::::

::::{solution}
$$
\lg (x^2 - 3) = \lg (2x)
$$

$$
x^2 - 3 = 2x
$$

$$
x^2 - 2x - 3 = 0
$$

$$
(x - 3)(x + 1) = 0
$$

$$
x = 3 \or x = -1
$$

Vi må sjekke om begge løsningene er gyldige. For $x = -1$, så vil vi prøve å ta logaritmen av et negativt tall på høyre side av likningen som betyr at denne løsningen ikke er gyldig. Vi får ikke samme problem med $x = 3$ siden $x^2 - 3 > 0$ og $2x > 0$ når $x = 3$. Dermed er den eneste gyldige løsningen

$$
x = 3
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
$$
(\lg x)^2 = 4 - 3 \lg x
$$


::::{answer}
$$
x = 10 \or x = 10^{-4}
$$
::::

::::{solution}
Vi gjør variabelskifte $u = \lg x$. Da kan likningen skrives om til andregradslikningen

$$
u^2 = 4 - 3u
$$

$$
u^2 + 3u - 4 = 0
$$

Så bruker vi $abc$-formelen:

$$
u = \dfrac{-3 \pm \sqrt{3^2 - 4 \cdot 1 \cdot (-4)}}{2 \cdot 1} = \dfrac{-3 \pm \sqrt{9 + 16}}{2} = \dfrac{-3 \pm 5}{2}
$$

Det gir

$$
u = 1 \or u = -4
$$

som betyr at

$$
\lg x = 1 \or \lg x = -4
$$

som betyr at

$$
x = 10 \or x = 10^{-4}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\lg (2x - 3) - \lg x = 0
$$


::::{answer}
$$
x = 3
$$
::::


::::{solution}
$$
\lg (2x - 3) - \lg x = 0
$$

$$
\lg (2x - 3) = \lg x
$$

$$
2x - 3 = x
$$

$$
x = 3
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
$$
10^{\lg 6 + 3x} - 4 = 56
$$


::::{answer}
$$
x = \dfrac{1}{3}
$$
::::


::::{solution}
$$
10^{\lg 6 + 3x} - 4 = 56
$$

$$
10^{\lg 6 + 3x} = 60
$$

$$
\lg 6 + 3x = \lg 60
$$

$$
3x = \lg 60 - \lg 6
$$

$$
3x = \lg \dfrac{60}{6}
$$

$$
3x = \lg 10
$$

$$
3x = 1
$$

$$
x = \dfrac{1}{3}
$$
::::

:::::::::::::



::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 6
Løs likningene.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
\ln (x^2 + 2) - \ln x = \ln 3
$$


::::{answer}
$$
x = 2 \or x = 1
$$
::::


::::{solution}
$$
\ln (x^2 + 2) - \ln x = \ln 3
$$

$$
\ln (x^2 + 2) = \ln 3 + \ln x
$$

$$
\ln (x^2 + 2) = \ln (3x)
$$

$$
x^2 + 2 = 3x
$$

$$
x^2 - 3x + 2 = 0
$$

$$
x = \dfrac{3 \pm \sqrt{(-3)^2 - 4 \cdot 1 \cdot 2}}{2 \cdot 1} = \dfrac{3 \pm \sqrt{9 - 8}}{2} = \dfrac{3 \pm 1}{2}
$$

$$
x = 2 \or x = 1
$$

Begge løsningene oppfyller den opprinnelige likningen siden $x^2 + 2 > 0$ og $x > 0$ når $x = 1$ eller $x = 2$. Dermed er begge løsningene gyldige

::::

:::::::::::::


:::::::::::::{tab-item} b
$$
\ln (x + 1) + \ln (x - 2) = \ln (x - 3)
$$


::::{answer}
$$
x \in \emptyset
$$
::::

::::{solution}
$$
\ln (x + 1) + \ln (x - 2) = \ln (x - 3)
$$

$$
\ln ((x + 1)(x - 2)) = \ln (x - 3)
$$

$$
(x + 1)(x - 2) = x - 3
$$

$$
x^2 - x - 2 = x - 3
$$

$$
x^2 - 2x + 1 = 0
$$

$$
(x - 1)^2 = 0
$$

$$
x = 1
$$

Vi må sjekke om løsningen er gyldig. For $x = 1$, vil vi prøve å ta logaritmen av et negativt tall i to av leddene som opptrer i den opprinnelige likningen. Dermed har ikke likningen noen løsning. Altså er 

$$
x \in \emptyset
$$
::::

:::::::::::::

:::::::::::::{tab-item} c
$$
100^x + 4 \cdot 10^x = 5
$$


::::{answer}
$$
x = 0
$$
::::

::::{solution}
$$
100^x + 4 \cdot 10^x = 5
$$

$$
(10^x)^2 + 4 \cdot 10^x - 5 = 0
$$

Vi gjør variabelskifte $u = 10^x$. Da kan likningen skrives om til andregradslikningen

$$
u^2 + 4u - 5 = 0
$$

Så bruker vi $abc$-formelen:

$$
u = \dfrac{-4 \pm \sqrt{4^2 - 4 \cdot 1 \cdot (-5)}}{2 \cdot 1} = \dfrac{-4 \pm \sqrt{16 + 20}}{2} = \dfrac{-4 \pm \sqrt{36}}{2}
$$

$$
u = \dfrac{-4 \pm 6}{2}
$$

$$
u = 1 \or u = -5
$$

$$
10^x = 1 \or 10^x = -5
$$

Det vil ikke være mulig å tilfredsstille $10^x = -5$ siden $10^x > 0$ for alle $x$. Dermed er den eneste gyldige løsningen

$$
10^x = 1 \liff x = 0
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
$$
4^x + 4\cdot 2^x = 12
$$


::::{answer}
$$
x = 1
$$
::::

::::{solution}
$$
4^x + 4\cdot 2^x = 12
$$

$$
(2^x)^2 + 4 \cdot 2^x - 12 = 0
$$

Vi gjør variabelskifte $u = 2^x$. Da kan likningen skrives om til andregradslikningen

$$
u^2 + 4u - 12 = 0
$$

Så bruker vi $abc$-formelen:

$$
u = \dfrac{-4 \pm \sqrt{4^2 - 4 \cdot 1 \cdot (-12)}}{2 \cdot 1} = \dfrac{-4 \pm \sqrt{16 + 48}}{2} = \dfrac{-4 \pm \sqrt{64}}{2}
$$

$$
u = \dfrac{-4 \pm 8}{2}
$$

$$
u = 2 \or u = -6
$$

$$
2^x = 2 \or 2^x = -6
$$

Det vil ikke være mulig å tilfredsstille $2^x = -6$ siden $2^x > 0$ for alle $x$. Dermed er den eneste gyldige løsningen

$$
2^x = 2 \liff x = 1
$$
::::
:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 7
Grafen til funksjonen $f(x) = 10^x$ er vist i figuren nedenfor.

:::{plot}
width: 80%
function: 10^x
xmin: -0.1
xmax: 1.1
xstep: 0.1
ymin: -1
ymax: 11
ystep: 1
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk figuren til å bestemme en tilnærmet verdi for $\lg 3$.

::::{answer}
$$
\lg 3 \approx 0.5
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bruk figuren til å bestemme en tilnærmet verdi for $\lg 8$.


::::{answer}
$$
\lg 8 \approx 0.9
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
Bruk figuren til å bestemme en tilnærmet verdi for $\lg 5$.


::::{answer}
$$
\lg 5 \approx 0.7
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
Bruk figuren til å bestemme en tilnærmet verdi for $\lg 40$.

::::{answer}
$$
\lg 40 \approx 1.6
$$
::::

:::::::::::::


::::::::::::::




:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8
I figuren nedenfor vises grafen til $f(x) = e^x$. 


:::{plot}
width: 80%
function: exp(x)
xmin: -0.1
xmax: 1.3
xstep: 0.1
ymin: -0.5
ymax: 4
ystep: 0.5
:::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk figuren til å bestemme en tilnærmet verdi for $\ln 2$.


::::{answer}
$$
\ln 2 \approx 0.7
$$
::::

:::::::::::::



:::::::::::::{tab-item} b
Bruk figuren til å bestemme en tilnærmet verdi for $\ln 3$


::::{answer}
$$
\ln 3 \approx 1.1
$$
::::
:::::::::::::


:::::::::::::{tab-item} c
Bruk figuren til å bestemme en tilnærmet løsning til likningen $e^x = 6$. 


::::{answer}
$$
x \approx 1.8
$$
::::
:::::::::::::


:::::::::::::{tab-item} d
Bruk figuren til å bestemme en tilnærmet løsning til likningen $e^x = 24$. 


::::{answer}
$$
x \approx 3.2
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 9
::::::::::::::{tab-set}
---
class: tabs-parts
---


:::::::::::::{tab-item} a
I figuren nedenfor vises grafen til en funksjon $f$ gitt ved

$$
f(x) = \log_a(x)
$$

Bestem $a$.

:::{plot}
width: 80%
function: log(x)/log(5)
xmin: -1
xmax: 16
xstep: 1
ymin: -2
ymax: 6
ystep: 1
:::


::::{answer}
$$
a = 5
$$
::::




:::::::::::::


:::::::::::::{tab-item} b
I figuren nedenfor vises grafen til en funksjon

$$
f(x) = \log_a(x) \cdot (\log_a(x) - 1)
$$

Bestem $a$.

:::{plot}
width: 80%
function: log(x)/log(3) * (log(x) / log(3) - 1)
xmin: -1
xmax: 9
xstep: 1
ymin: -2
ymax: 4
ystep: 1
:::


::::{answer}
$$
a = 3
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
I figuren nedenfor vises grafen til 

$$
f(x) = -(\log_a(x) - 2) \cdot (\log_a(x) - 4)
$$

Bestem $a$.


:::{plot}
width: 80%
function: -(log(x)/log(2) - 2)*(log(x)/log(2) - 4)
xmin: -2
xmax: 20
xstep: 2
ymin: -4
ymax: 4
ystep: 1
:::


::::{answer}
$$
a = 2
$$
::::



:::::::::::::
::::::::::::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 10
Løs likningene.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
$$
e^{2x} - e^x = 2
$$



::::{answer}
$$
x = \ln 2
$$
::::

::::{solution}
Vi skriver om likningen til

$$
e^{2x} - e^x - 2 = 0
$$

Vi gjør variabelskifte $u = e^x$. Da kan likningen skrives om til andregradslikningen

$$
u^2 - u - 2 = 0
$$

Så bruker vi $abc$-formelen:

$$
u = \dfrac{1 \pm \sqrt{(-1)^2 - 4 \cdot 1 \cdot (-2)}}{2 \cdot 1} = \dfrac{1 \pm \sqrt{1 + 8}}{2} = \dfrac{1 \pm \sqrt{9}}{2}
$$

$$
u = \dfrac{1 \pm 3}{2}
$$

$$
u = 2 \or u = -1
$$

Så setter vi tilbake definisjonen av $u$:

$$
e^x = 2 \or e^x = -1
$$

Det vil ikke være mulig å tilfredsstille $e^x = -1$ siden $e^x > 0$ for alle $x$. Dermed er den eneste gyldige løsningen

$$
e^x = 2 \liff x = \ln 2
$$

::::


:::::::::::::


:::::::::::::{tab-item} b
$$
(\ln x)^2 - \ln x = 6
$$


::::{answer}
$$
x = e^3 \or x = e^{-2}
$$
::::

::::{solution}
Vi skriver om likningen til

$$
(\ln x)^2 - \ln x - 6 = 0
$$

Vi gjør variabelskifte $u = \ln x$. Da kan likningen skrives om til andregradslikningen

$$
u^2 - u - 6 = 0
$$

Så bruker vi $abc$-formelen:

$$
u = \dfrac{1 \pm \sqrt{(-1)^2 - 4 \cdot 1 \cdot (-6)}}{2 \cdot 1} = \dfrac{1 \pm \sqrt{1 + 24}}{2} = \dfrac{1 \pm \sqrt{25}}{2}
$$

$$
u = \dfrac{1 \pm 5}{2}
$$

$$
u = 3 \or u = -2
$$

Så setter vi tilbake definisjonen av $u$:

$$
\ln x = 3 \or \ln x = -2
$$

$$
x = e^3 \or x = e^{-2}
$$


::::

:::::::::::::


:::::::::::::{tab-item} c
$$
3^{3x + 2} - 5 = 76
$$


::::{answer}
$$
x = \dfrac{2}{3}
$$
::::

::::{solution}
Vi forenkler likningen litt først:

$$
3^{3x + 2} = 81
$$

Så bruker vi logaritme på begge sider:

$$
\ln (3^{3x + 2}) = \ln 81
$$

$$
(3x + 2) \ln 3 = \ln 81
$$

$$
3x + 2 = \dfrac{\ln 81}{\ln 3}
$$

Vi kan skrive $81 = 3^4$, så

$$
3x + 2 = \dfrac{\ln 3^4}{\ln 3} = \dfrac{4 \ln 3}{\ln 3} = 4
$$

Dermed får vi

$$
3x + 2 = 4
$$

$$
3x = 2
$$

$$
x = \dfrac{2}{3}
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
$$
3 \lg x + 2 \lg x^2 + \lg \dfrac{1}{x^9} = 2
$$


::::{answer}
$$
x = 10^{-1} = \dfrac{1}{10}
$$
::::

::::{solution}
Vi bruker logaritmesetningene til å skrive om venstresiden til én logaritme:

$$
3 \lg x + 2 \lg x^2 + \lg \dfrac{1}{x^9} = 2
$$

$$
3 \lg x + 2 \cdot 2 \lg x + \lg x^{-9} = 2
$$

$$
3 \lg x + 4 \lg x - 9 \lg x = 2
$$

$$
-2 \lg x = 2
$$


$$
\lg x = -1
$$

$$
x = 10^{-1}
$$
::::


:::::::::::::


:::::::::::::{tab-item} e
Løs likningen 

$$
100^x - 3\cdot 10^x = 4
$$


::::{solution}
Siden $100 = 10^2$, kan vi skrive om likningen til

$$
10^{2x} - 3\cdot 10^x = 4
$$

Vi gjør variabelskifte $u = 10^x$ som gir oss likningen

$$
u^2 - 3u = 4 \liff u^2 - 3u - 4 = 0
$$

Så bruker vi $abc$-formelen til å bestemme $u$

$$
u = \dfrac{3 \pm \sqrt{3^2 - 4 \cdot 1 \cdot (-4)}}{2 \cdot 1} = \dfrac{3 \pm 5}{2}
$$

$$
u = 4 \or u = -2
$$

Så setter vi definisjonen av $u$ tilbake i likningene:

$$
10^x = 4 \or 10^x = -2
$$

Vi kan ikke opphøye $10$ i noe for å få et negativt tall, så $10^x = -2$ har ingen løsning. Det betyr at løsningen av likningen bare kan være

$$
10^x = 4 \liff x = lg(4)
$$
::::

:::::::::::::




::::::::::::::

:::::::::::::::





:::::::::::::::{exercise} Oppgave 11 
Newtons avkjølingslov sier at for temperaturen $T \, \degree \mathrm{C}$ til en gjenstand som avkjøles i et rom med temperatur $T_0 \, \degree \mathrm{C}$, så vil temperaturen til gjenstanden etter $t$ minutter oppfylle likningen

$$
\ln(T - T_0) = -k\cdot t + r
$$

der $k$ og $r$ er konstanter som avhenger av gjenstanden og rommet.

En kaffekopp fylles opp med kaffe som har en temperatur på $100 \degree \mathrm{C}$, og settes i et rom med temperatur $20 \degree \mathrm{C}$. Etter $10$ minutter er temperaturen til kaffen $60 \degree \mathrm{C}$.

Bestem en tilnærmet verdi hvor lang tid det tar før temperaturen til kaffen er $40 \, \degree \mathrm{C}$.


::::{answer}
20 minutter.
::::



::::{solution}
Siden romtemperaturen er $20 \degree \mathrm{C}$, så er $T_0 = 20$. Vi starter med å bestemme konstanten $r$ ved å bruke at når $t = 0$, så er $T = 100$: 

$$
\ln(100 - 20) = -k \cdot 0 + r = r
$$

som gir

$$
r = \ln 80
$$

Etter $t = 10$ minutter, så er temperaturen $T = 60$. Vi bruker dette til å bestemme konstanten $k$:

$$
\ln(60 - 20) = -k \cdot 10 + \ln 80
$$

$$
\ln 40 = -10k + \ln 80
$$

$$
10k = \ln 80 - \ln 40 = \ln \dfrac{80}{40} = \ln 2
$$

$$
k = \dfrac{\ln 2}{10}
$$

Deretter bruker vi dette til å bestemme hvor lang tid det tar før temperaturen er $T = 40$:

$$
\ln(40 - 20) = -\dfrac{\ln 2}{10} \cdot t + \ln 80
$$

$$
\ln 20 = -\dfrac{\ln 2}{10} \cdot t + \ln 80
$$

$$
\dfrac{\ln 2}{10} \cdot t = \ln 80 - \ln 20 = \ln \dfrac{80}{20} = \ln 4
$$

$$
t = \dfrac{10 \ln 4}{\ln 2} = 10 \cdot \dfrac{\ln 2^2}{\ln 2} = 10 \cdot \dfrac{2 \ln 2}{\ln 2} = 20
$$

Altså tar det $20$ minutter før temperaturen til kaffen er $40 \degree \mathrm{C}$.

::::



:::::::::::::::


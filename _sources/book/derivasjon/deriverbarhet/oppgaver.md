# Deriverbarhet


:::::::::::::::{summary} Deriverbarhet
En funksjon $f$ er deriverbar i $x = a$ hvis 
1. $f$ er kontinuerlig i $x = a$.
2. Grenseverdien nedenfor eksisterer

$$
\lim_{x \to a} \frac{f(x) - f(a)}{x - a}
$$

Grenseverdien eksisterer bare hvis

$$
\lim_{x \to a^-} \frac{f(x) - f(a)}{x - a} = \lim_{x \to a^+} \frac{f(x) - f(a)}{x - a}
$$
:::::::::::::::


---


:::::::::::::::{summary} Deriverbarhet: Hjelpesetning
La en funksjon $f$ være kontinuerlig i $x = a$ og la

$$
f(x) = 
\begin{cases}
    g(x) \qfor x < a \\
    \\
    h(x) \qfor x \geq a
\end{cases}
$$

Hvis $g(x)$ er kontinuerlig og deriverbar i $x = a$ og $h(x)$ er kontinuerlig og deriverbar i $x = a$, så er $f$ deriverbar i $x = a$ hvis og bare hvis

$$
g'(a) = h'(a)
$$

:::::::::::::::

:::::::::::::::{exercise} Oppgave 1
En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    x^2 \qfor x < 1 \\
    \\
    2x - 1 \qfor x \geq 1
\end{cases}
$$


Bestem $f'(1)$ hvis den eksisterer.

::::{answer}
$$
f'(1) = 2
$$
::::
:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 2
En funksjon $f$ er gitt ved


$$
\begin{cases}
    x^2 + 2 \qfor x < 1 \\
    \\
    -x^2 + 2x \qfor x \geq 1
\end{cases}
$$

Bestem $f'(1)$ hvis den eksisterer.


::::{answer}
$f$ er ikke kontinuerlig i $x = 1$, så $f'(1)$ eksisterer ikke.
::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3
En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    \dfrac{x^3 + 8}{x + 2} \qhvis x \neq -2 \\
    \\
    a \qhvis x = -2
\end{cases}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$ slik at $f$ er kontinuerlig i $x = -2$.

::::{answer}
$$
a = 12
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $f'(-2)$ hvis den eksisterer.


::::{answer}
$$
f'(-2) = -6
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 4
En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    \dfrac{x^3 - 27}{x - 3} \qfor x \neq 3 \\
    \\
    a \qfor x = 3
\end{cases}
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$ slik at $f$ er kontinuerlig i $x = 3$.


::::{answer}
$$
a = 27
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $f'(3)$ hvis den eksisterer.


::::{answer}
$$
f'(3) = 9
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 5
En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    \dfrac{e^x - 1 - x}{x} \qfor x < 0 \\
    \\
    a \qfor x = 0 \\
    \\
    \dfrac{1}{2} \ln (x + 1) \qfor x > 0
\end{cases}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$ slik at $f$ er kontinuerlig i $x = 0$.


::::{answer}
$$
a = 0
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $f'(0)$ hvis den eksisterer.


::::{answer}
$$
f'(0) = \dfrac{1}{2}
$$
::::

:::::::::::::


::::::::::::::

:::::::::::::::






---



:::::::::::::::{exercise} Oppgave 6
En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    e^x - 1 \qfor x < 0 \\
    \\
    x \ln (x + 1) \qfor x \geq 0
\end{cases}
$$

Bestem $f'(0)$ hvis den eksisterer.


::::{answer}
$f'(0)$ eksisterer ikke.
::::


:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 7
En funksjon $f$ er gitt ved

$$
f(x) =
\begin{cases}
    \dfrac{x - 4}{\sqrt{x} - 2} \qfor x \neq 4 \qog x \geq 0 \\
    \\
    a \qfor x = 4
\end{cases}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$ slik at $f$ er kontinuerlig i $x = 4$.


::::{answer}
$$
a = 4
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $f'(4)$ hvis den eksisterer.


::::{answer}
$$
f'(4) = \dfrac{1}{4}
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 8
En funksjon $f$ er gitt ved

$$
f(x) =
\begin{cases}
    \dfrac{\sqrt{x} - 1}{x - 1} \qfor x \neq 1 \qog x \geq 0 \\
    \\
    a \qfor x = 1
\end{cases}
$$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $a$ slik at $f$ er kontinuerlig i $x = 1$.


::::{answer}
$$
a = \dfrac{1}{2}
$$
::::

:::::::::::::


:::::::::::::{tab-item} b
Bestem $f'(1)$ hvis den eksisterer.


::::{answer}
$$
f'(1) = - \dfrac{1}{8}
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---




:::::::::::::::{exercise} Oppgave 9

:::{cas-popup}
---
layout: sidebar
---
:::

En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    -9x - 15, \quad x \leq -2 \\
    \\
    g(x), \quad -2 < x < 1 \\
    \\
    \dfrac{x^2}{2} - x - \dfrac{7}{2}\, , \quad x \geq 1
\end{cases}
$$

Funksjonen $f$ er kontinuerlig og deriverbar for alle $x \in \mathbb{R}$. Funksjonen $g$ er en tredjegradsfunksjon.

Bestem $g(x)$.


::::{answer}
$$
a = -\dfrac{13}{27} \and b = \dfrac{7}{9} \and c = -\dfrac{1}{9} \and d = -\dfrac{113}{27}
$$
::::

:::::::::::::::



---




:::::::::::::::{exercise} Oppgave 10


:::{cas-popup}
---
layout: sidebar
---
:::



En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    ax + b \qfor x < 2 \\
    \\
    2x^3 + 2x^2 - 2x \qfor -2 < x < k \\
    \\
    c \qfor x \geq k
\end{cases}
$$

der $a, b, c \in \mathbb{R}$ og $k > -2$. 


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør om $f$ er kontinuerlig i $x = -2$ dersom $a = 2$ og $b = -2$.


::::{answer}
Nei 
::::


:::::::::::::


:::::::::::::{tab-item} b
Bestem $a$, $b$, $c$, og $k$ slik at $f$ er kontinuerlig og deriverbar i $x = -2$ og $x = k$. 


::::{answer}
Det er to muligheter.

Mulighet 1:

$$
a = 14 \and b = 24 \and c = 2 \and k = -1
$$

Mulighet 2:

$$
a = 14 \and b = 24 \and c = -\dfrac{10}{27} \and k = \dfrac{1}{3}
$$
::::
:::::::::::::


::::::::::::::

:::::::::::::::

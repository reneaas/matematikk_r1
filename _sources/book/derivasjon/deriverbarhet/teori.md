# Deriverbarhet 


:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke grenseverdier til å avgjøre om en funksjon er deriverbar i et punkt.
* Kunne avgjøre om funksjoner med delt forskrift er deriverbare i bruddpunkter.
:::


:::::::::::::::{summary} Deriverbarhet
En funksjon $f$ er deriverbar i $x = a$ hvis 
1. $f$ er kontinuerlig i $x = a$.
2. Grenseverdien nedenfor eksisterer

$$
\lim_{x \to a} \frac{f(x) - f(a)}{x - a}
$$

Dersom grenseverdien eksisterer, må $f$ være kontinuerlig i $x = a$.

Grenseverdien eksisterer bare hvis

$$
\lim_{x \to a^-} \frac{f(x) - f(a)}{x - a} = \lim_{x \to a^+} \frac{f(x) - f(a)}{x - a}
$$
:::::::::::::::



---



:::::::::::::::{example} Eksempel 1
Funksjonen $f$ er gitt ved

$$
f(x) = \begin{cases}
    \dfrac{e^x - 1}{x}, & x \neq 0 \\
    \\
    1, & x = 0
\end{cases}
$$

Bestem $f'(0)$.


::::{solution}
---
dropdown: 0
---
$$
\begin{align*}
    f'(0) &= \lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} \\
    \\
    &= \lim_{x \to 0} \frac{\frac{e^x - 1}{x} - 1}{x} \\
    \\
    &= \lim_{x \to 0} \frac{e^x - 1 - x}{x^2} \\
    \\
    &\overset{[\frac{0}{0}]}{=} \lim_{x \to 0} \frac{e^x - 1}{2x} \\
    \\
    &= \lim_{x \to 0} \frac{e^x}{2} \\
    \\
    &= \frac{1}{2}
\end{align*}
$$
::::


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
g(a) = h(a) \and g'(a) = h'(a)
$$

:::::::::::::::



---




:::::::::::::::{example} Eksempel 2
Funksjonen $f$ er gitt ved

$$
f(x) = \begin{cases}
    ax + b \qfor x < 0 \\
    \\
    x^2 + 2x + 1 \qfor x \geq 0
\end{cases}
$$

Bestem $a$ og $b$ slik at $f$ er kontinuerlig og deriverbar i $x = 0$.


::::{solution}
---
dropdown: 0
---
Vi lar 

$$
g(x) = ax + b \qog h(x) = x^2 + 2x + 1.
$$

Siden $g$ og $h$ er kontinuerlige og deriverbare i $x = 0$, så vil $f$ være kontinuerlig og deriverbar i $x = 0$ dersom

$$
g(0) = h(0) \and g'(0) = h'(0)
$$

Det første kriteriet gir at

$$
g(0) = b \and h(0) = 1 \liff b = 1
$$

Det andre kriteriet gir at

$$
g'(0) = a \and h'(0) = 2 \liff a = 2
$$

Altså er $f$ kontinuerlig og deriverbar i $x = 0$ hvis

$$
a = 2 \and b = 1
$$


::::


:::::::::::::::
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
g(a) = h(a) \qog g'(a) = h'(a)
$$

:::::::::::::::
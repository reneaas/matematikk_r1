# Formler

::::::::{grid}
---
gutter: 2
---
::::::{grid-item-card}
**Potensregler**
^^^
$$
\begin{align*}
    x^{p} \cdot x^q &= x^{p+q} \\
    \\
    \dfrac{x^{p}}{x^q} &= x^{p-q} \\
    \\
    (x^p)^q &= x^{p \cdot q} \\
    \\
    x^0 &= 1 \\
    \\
    x^{-p} &= \dfrac{1}{x^p} \\
\end{align*}
$$

::::::

::::::{grid-item-card}
**Logaritmeregler**
^^^
$$
\begin{align*}
    x &= \log_a y \liff y = a^x \\
    \\
    \log_a(xy) &= \log_a x + \log_a y \\
    \\
    \log_a\left(\dfrac{x}{y}\right) &= \log_a x - \log_a y \\
    \\
    \log_a(x^p) &= p \cdot \log_a x \\
    \\
    \log_a 1 &= 0 \\
\end{align*}
$$


::::::

::::::{grid-item-card}
**Derivasjonsregler**
^^^
$$
\begin{align*}
    (x^p)' &= p x^{p-1} \\
    \\
    (e^x)' &= e^x \\
    \\
    (\ln ax)' &= \dfrac{1}{x} \\
    \\
    (a^x)' &= a^x \ln a \\
    \\
    (\log_a x)' &= \dfrac{1}{x \ln a} \\
    \\
\end{align*}
$$
::::::

::::::{grid-item-card} 
**Derivasjonssetninger**
^^^
$$
\begin{align*}
    (fg)' &= f' g + f g' \\
    \\
    \left(\dfrac{f}{g}\right)' &= \dfrac{f' g - f g'}{g^2} \\
    \\
    \left(f(g(x))\right)' &= f'(g(x)) \cdot g'(x) \\
\end{align*}
$$

::::::

::::::{grid-item-card}
**Den deriverte og numerisk derivasjon**
^^^

$$
\begin{align*}
    f'(a) &= \lim_{x \to a} \dfrac{f(x) - f(a)}{x - a} \\
    \\
    f'(x) &= \lim_{h \to 0} \dfrac{f(x+h) - f(x)}{h} \\
    \\
    f'(x) &\approx \dfrac{f(x+h) - f(x)}{h} \\
\end{align*}
$$
::::::

::::::{grid-item-card}
**Funksjonsdrøfting**
^^^
Toppunkt $(m, f(m))$ 
: $f'(m) = 0$ og $f''(m) < 0$ 

Bunnpunkt $(m, f(m))$
: $f'(m) = 0$ og $f''(m) > 0$

Vendepunkt $(m, f(m))$
: $f''(m) = 0$ og $f''(x)$ skifter fortegn når $x$ går gjennom $m$
::::::


::::::{grid-item-card}
**Tangenter**
^^^

$$
y = f(a) + f'(a) \cdot (x - a)
$$


:::{plot}
width: 100%
function: x * exp(-x**2), f
tangent: 1, f
ticks: off
xmin: -1
xmax: 3
ymin: -0.2
ymax: 1
point: (1, f(1))
text: 1, f(1), "$(a, f(a))$", top-right
:::




::::::


::::::{grid-item-card}
**Grenseverdier**
^^^


Grunnleggende grenser
: $$
\begin{align*}
    \lim_{x\to \infty} e^x &= \infty && \lim_{x\to \infty} e^{-x} = 0 \\
    \\
    \lim_{x \to 0^+} \ln x &= -\infty && \lim_{x \to \infty} \ln x = \infty \\
\end{align*}
$$

L'Hopitals regel
: $$
\begin{align*}
    \lim_{x \to a} \dfrac{f(x)}{g(x)} &\overset{[\frac{0}{0}]}{=} \lim_{x \to a} \dfrac{f'(x)}{g'(x)} \\
    \\
    \lim_{x \to a} \dfrac{f(x)}{g(x)} &\overset{[\frac{\infty}{\infty}]}{=} \lim_{x \to a} \dfrac{f'(x)}{g'(x)} 
\end{align*}
$$

::::::



::::::{grid-item-card}
**Asymptoter**
^^^

:::{plot}
width: 100%
function: x + 1 - 1/(x + 1) + 1 / (x - 2)**2, (-1, 20)
function: (x - 1) / (x + 1), (-20, -1), blue
vline: -1
vline: 2
hline: 1
line: 1, 1
ticks: off
ymax: 10
xmin: -6
xmax: 6
:::

Skrå asymptote $y = ax + b$
: $\lim\limits_{x \to \pm \infty} \left(f(x) - (ax + b)\right) = 0$

Vertikal asymptote $x = a$
: $\lim\limits_{x \to a^{\pm}} f(x) = \pm \infty$

Horisontal asymptote $y = a$
: $\lim\limits_{x \to \pm \infty} f(x) = a$

::::::


::::::{grid-item-card}
**Kontinuitet og deriverbarhet**
^^^

Eksistens av grenseverdi
: $\lim\limits_{x \to a} f(x)$ finnes hvis $\lim\limits_{x \to a^-} f(x) = \lim\limits_{x \to a^+} f(x)$

Kontinuitet i $x = a$
: $\lim\limits_{x \to a} f(x) = f(a)$

Deriverbarhet i $x = a$
: $f'(a) = \lim\limits_{x \to a} \dfrac{f(x) - f(a)}{x - a}$ må eksistere

Funksjon med delt forskrift
: $
f(x) =
\begin{cases}
    g(x) & \qhvis x < a \\
    \\
    h(x) & \qhvis x \geq a
\end{cases}
$

: Kontinuerlig i $a$ hvis $g(a) = h(a)$
: Deriverbar i $a$ hvis kontinuerlig i $a$ og $g'(a) = h'(a)$

::::::



::::::::




# Brøkregelen

:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke brøkregelen til å derivere brøker av funksjoner.
:::




:::::::::::::::{summary} Brøkregelen
La en funksjon $f$ være på formen

$$
f(x) = \frac{u(x)}{v(x)}
$$

Da er den deriverte av funksjonen

$$
f'(x) = \frac{u'(x) \cdot v(x) - u(x) \cdot v'(x)}{(v(x))^2}
$$

Vi skriver denne regelen mer kompakt som

$$
\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}
$$
:::::::::::::::



---




:::::::::::::::{example} Eksempel 1
Funksjonen $f$ er gitt ved

$$
f(x) = \dfrac{e^x}{x}
$$

Bestem $f'(x)$.


::::{solution}
---
dropdown: 0
---
Brøkregelen gir at

$$
\begin{align*}
f'(x) &= \frac{(e^x)' \cdot x - e^x \cdot (x)'}{x^2} \\
\\
&= \dfrac{e^x \cdot x - e^x \cdot 1}{x^2} \\
\\
&= \dfrac{e^x(x - 1)}{x^2}
\end{align*}
$$
::::
:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 1
Funksjonen $f$ er gitt ved

$$
f(x) = \dfrac{e^{-2x}}{x^2}
$$

Bestem $f'(x)$.

::::{answer}
$$
f'(x) = \frac{-2e^{-2x}(x + 1)}{x^3}
$$
::::

::::{solution}
$$
\begin{align*}
f'(x) &= \frac{(e^{-2x})' \cdot x^2 - e^{-2x} \cdot (x^2)'}{(x^2)^2} \\
\\
&= \frac{-2e^{-2x} \cdot x^2 - e^{-2x} \cdot 2x}{x^4} \\
\\
&= \frac{-2e^{-2x}(x^2 + x)}{x^4} \\
\\
&= \frac{-2e^{-2x}(x + 1)}{x^3}
\end{align*}
$$
::::

:::::::::::::::
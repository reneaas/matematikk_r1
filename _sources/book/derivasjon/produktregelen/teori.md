# Produktregelen



:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke produktregelen til å derivere produkter av funksjoner.
:::




:::::::::::::::{summary} Produktregelen
La en funksjon $f(x) = u(x) \cdot v(x)$. Da er 

$$
f'(x) = u'(x) \cdot v(x) + u(x) \cdot v'(x)
$$

Vi skriver dette mer kompakt som

$$
(uv)' = u'v + uv'
$$
:::::::::::::::


---




:::::::::::::::{example} Eksempel 1
Funksjonen $f$ er gitt ved 

$$
f(x) = x \cdot e^x
$$

Bestem $f'(x)$.


::::{solution}
---
dropdown: 0
---
Funksjonen $f(x) = x \cdot e^x$ der

$$
u(x) = x \qog v(x) = e^x.
$$

Produktregelen for derivasjon gir da at

$$
f'(x) = u'(x) \cdot v(x) + u(x) \cdot v'(x) = 1 \cdot e^x + x \cdot e^x = (1 + x)e^x.
$$

::::

:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 1
Funksjonen $f$ er gitt ved

$$
f(x) = x \cdot \ln x.
$$

Bestem $f'(x)$.


::::{answer}
$$
f'(x) = \ln x + 1
$$
::::


::::{solution}
$$
f'(x) = x' \cdot \ln x + x \cdot (\ln x)' = 1 \cdot \ln x + x \cdot \frac{1}{x} = \ln x + 1
$$
::::


:::::::::::::::



---


I blant må vi kombinere produktregelen med kjerneregelen.


:::::::::::::::{example} Eksempel 2
Funksjonen $f$ er gitt ved

$$
f(x) = x \sqrt{x - 1}.
$$

Bestem $f'(x)$.


::::{solution}
---
dropdown: 0
---
$$
\begin{align*}
f'(x) &= x' \cdot \sqrt{x - 1} + x \cdot (\sqrt{x - 1})' \\
\\
&= 1 \cdot \sqrt{x - 1} + x \cdot \frac{1}{2\sqrt{x - 1}} \\
\\
&= \sqrt{x - 1} + \frac{x}{2\sqrt{x - 1}} \\
\\
&= \frac{2(x - 1) + x}{2\sqrt{x - 1}} \\
\\
&= \frac{3x - 2}{2\sqrt{x - 1}}
\end{align*}
$$
::::

:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 2
Funksjonen $f$ er gitt ved

$$
f(x) = \sqrt{x} \cdot \ln x.
$$

Bestem $f'(x)$.


::::{answer}
$$
f'(x) = \frac{\ln x + 2}{2\sqrt{x}}
$$
::::

::::{solution}
$$
\begin{align*}
f'(x) &= (\sqrt{x})' \cdot \ln x + \sqrt{x} \cdot (\ln x)' \\
\\
&= \frac{1}{2\sqrt{x}} \cdot \ln x + \sqrt{x} \cdot \frac{1}{x} \\
\\
&= \frac{\ln x}{2\sqrt{x}} + \frac{1}{\sqrt{x}} \\
\\
&= \frac{\ln x + 2}{2\sqrt{x}}
\end{align*}
$$
::::
:::::::::::::::


# Produktregelen og brøkregelen


::::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke produktregelen til å derivere produkter av funksjoner.
* Kunne bruke brøkregelen til å derivere brøker av funksjoner.
* Kunne kombinere kjerneregelen med produktregelen og brøkregelen for å deriverere funksjoner.
::::





## Produktregelen

Når en funksjon $f$ er et produkt av to andre funksjoner $u$ og $v$, altså $f(x) = u(x) \cdot v(x)$, kan vi bruke produktregelen for å derivere $f$. Produktregelen sier at:


:::::::::::::::{summary} Produktregelen for derivasjon
La $f(x) = u(x) \cdot v(x)$. Da er den deriverte av $f$ gitt ved:

$$
f'(x) = u'(x) \cdot v(x) + u(x) \cdot v'(x)
$$


Vi skriver denne regelen ofte på en mer kompakt måte som:

$$
(uv)' = u'v + uv'
$$
:::::::::::::::


---


Vi tar et eksempel:


:::::::::::::::{example} Eksempel 1
En funksjon $f$ er gitt ved 

$$
f(x) = x e^{2x}
$$


Bestem $f'(x)$.


::::{solution}
---
dropdown: 0
---
Her har vi at $f(x) = u(x) \cdot v(x)$ med 

$$
u(x) = x \qog v(x) = e^{2x}
$$

Vi har at 

$$
u'(x) = 1 \qog v'(x) = 2e^{2x}
$$

Etter produktregelen får vi da

$$
\begin{align*}
f'(x) &= u'(x) v(x) + u(x) v'(x)  \\
\\
&= 1 \cdot e^{2x} + x \cdot 2e^{2x} \\
\\
&= e^{2x} + 2xe^{2x} \\
\\
&= (1 + 2x)e^{2x}
\end{align*}
$$

::::

:::::::::::::::



---




:::::::::::::::{exercise} Underveisoppgave 1
En funksjon $f$ er gitt ved 

$$
f(x) = x^2 e^{3x}
$$

Bestem $f'(x)$.


::::{answer}
$$
f'(x) = (2x + 3x^2)e^{3x}
$$
::::

::::{solution}
Vi har at $f(x) = u(x) \cdot v(x)$ med

$$
u(x) = x^2 \qog v(x) = e^{3x}
$$

Vi har at

$$
u'(x) = 2x \qog v'(x) = 3e^{3x}
$$

Etter produktregelen får vi da

$$
\begin{align*}
f'(x) &= u'(x) v(x) + u(x) v'(x)  \\
\\
&= 2x \cdot e^{3x} + x^2 \cdot 3e^{3x} \\
\\
&= 2xe^{3x} + 3x^2e^{3x} \\
\\
&= (2x + 3x^2)e^{3x}
\end{align*}
$$
::::

:::::::::::::::





## Brøkregelen
Brøkregelen bruker vi når en funksjon $f$ kan skrives på formen $f(x) = \dfrac{u(x)}{v(x)}$. Brøkregelen sier at:

:::::::::::::::{summary} Brøkregelen for derivasjon
La $f(x) = \dfrac{u(x)}{v(x)}$. Da er den deriverte av $f$ gitt ved:

$$
f'(x) = \dfrac{u'(x) \cdot v(x) - u(x) \cdot v'(x)}{(v(x))^2}
$$

Vi skriver denne regelen ofte på en mer kompakt måte som:

$$
\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}
$$
:::::::::::::::



---



:::::::::::::::{example} Eksempel 2
En funksjon $f$ er gitt ved 

$$
f(x) = \dfrac{x^2 + 1}{x - 1}
$$

Bestem $f'(x)$.

::::{solution}
---
dropdown: 0
---
Her har vi at $f(x) = \dfrac{u(x)}{v(x)}$ med

$$
u(x) = x^2 + 1 \qog v(x) = x - 1
$$

Vi har at

$$
u'(x) = 2x \qog v'(x) = 1
$$

Etter brøkregelen får vi da

$$
\begin{align*}
f'(x) &= \dfrac{u'(x) v(x) - u(x) v'(x)}{(v(x))^2} \\
\\
&= \dfrac{2x (x - 1) - (x^2 + 1) \cdot 1}{(x - 1)^2} \\
\\
&= \dfrac{2x^2 - 2x - x^2 - 1}{(x - 1)^2} \\
\\
&= \dfrac{x^2 - 2x - 1}{(x - 1)^2}
\end{align*}
$$
::::
:::::::::::::::


---


Så var det din tur!


:::::::::::::::{exercise} Underveisoppgave 2
En funksjon $f$ er gitt ved

$$
f(x) = \dfrac{3x + 2}{x^2 - 1}
$$

Bestem $f'(x)$.


::::{answer}
$$
f'(x) = \dfrac{-3x^2 - 4x - 3}{(x^2 - 1)^2}
$$
::::


::::{solution}
Vi har at $f(x) = \dfrac{u(x)}{v(x)}$ med

$$
u(x) = 3x + 2 \qog v(x) = x^2 - 1
$$

Vi har at

$$
u'(x) = 3 \qog v'(x) = 2x
$$

Etter brøkregelen får vi da

$$
\begin{align*}
f'(x) &= \dfrac{u'(x) v(x) - u(x) v'(x)}{(v(x))^2} \\
\\
&= \dfrac{3 (x^2 - 1) - (3x + 2) \cdot 2x}{(x^2 - 1)^2} \\
\\
&= \dfrac{3x^2 - 3 - 6x^2 - 4x}{(x^2 - 1)^2} \\
\\
&= \dfrac{-3x^2 - 4x - 3}{(x^2 - 1)^2}
\end{align*}
$$
::::

:::::::::::::::
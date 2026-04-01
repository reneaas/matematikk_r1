# Kjerneregelen

:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke kjerneregelen til å derivere sammensatte funksjoner.
:::

:::::::::::::::{summary} Kjerneregelen
La $f$ være en funksjon på formen 

$$
f(x) = g(u(x))
$$

Da er

$$
f'(x) = g'(u(x)) \cdot u'(x)
$$
:::::::::::::::


---



:::::::::::::::{example} Eksempel 1
Funksjonen $f$ er gitt ved

$$
f(x) = (3x^2 + 2)^5
$$


Bestem $f'(x)$.


::::{solution}
---
dropdown: 0
---
Vi kan skrive $f(x)$ som 

$$
f(x) = u^5
$$

der $u(x) = 3x^2 + 2$. Da sier kjerneregelen at 

$$
f'(x) = (u^5)' \cdot u'(x) = 5u^4 \cdot (6x) = 30xu^4
$$

så setter vi tilbake definisjonen av $u$ i uttrykket til slutt:

$$
f'(x) = 30 x(3x^2 + 2)^4
$$
::::

:::::::::::::::



---



:::::::::::::::{exercise} Underveisoppgave 1
Funksjonen $f$ er gitt ved

$$
f(x) = \sqrt{x^2 - 1}
$$

Bestem $f'(x)$.


::::{answer}
$$
f'(x) = \frac{x}{\sqrt{x^2 - 1}}
$$
::::

::::{solution}
Vi kan skrive $f(x)$ som

$$
f(x) = \sqrt{u}
$$

der $u = x^2 - 1$. Fra kjerneregelen får vi da at

$$
f'(x) = (\sqrt{u})' \cdot u'(x) = \frac{1}{2\sqrt{u}} \cdot 2x = \dfrac{x}{\sqrt{u}} = \frac{x}{\sqrt{x^2 - 1}}
$$
::::

:::::::::::::::

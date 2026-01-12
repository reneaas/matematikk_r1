# Kjerneregelen


::::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke kjerneregelen til å derivere sammensatte funksjoner.
::::



Kjerneregelen er en derivasjonsregel som lar oss derivere sammensatte funksjoner.


:::::::::::::::{summary} Kjerneregelen for derivasjon
La en funksjon $f$ være gitt ved 

$$
f(x) = g(u(x))
$$

Da er den deriverte av $f$ gitt ved 

$$
f'(x) = g'(u) \cdot u'(x)
$$
:::::::::::::::


---


Vi tar et eksempel: 


:::::::::::::::{example} Eksempel 1
En funksjon $f$ er gitt ved 

$$
f(x) = \sqrt{x^2 + 1}
$$

Bestem $f'(x)$.

::::{solution}
---
dropdown: 0
---
Her har vi at $f(x) = g(u(x))$ med

$$
g(u) = \sqrt{u} \quad \text{og} \quad u(x) = x^2 + 1
$$

Vi deriverer først $g(u)$ med hensyn på $u$:

$$
g'(u) = \dfrac{1}{2\sqrt{u}}
$$

Deretter deriverer vi $u(x)$ med hensyn på $x$:

$$
u'(x) = 2x
$$

Etter kjerneregelen får vi da

$$
\begin{align*}
f'(x) &= g'(u) \cdot u'(x) \\
\\
&= \dfrac{1}{2\sqrt{u}} \cdot 2x \\
\\
&= \dfrac{2x}{2\sqrt{u}} \\
\\
&= \dfrac{x}{\sqrt{u}}
\end{align*}
$$

Til slutt setter vi tilbake definisjonen av $u$ som gir oss 

$$
f'(x) = \dfrac{x}{\sqrt{x^2 + 1}}
$$


::::
:::::::::::::::


---


Så var det din tur. 


:::::::::::::::{exercise} Underveisoppgave 1
En funksjon $f$ er gitt ved 

$$
f(x) = e^{x^2 - 1}
$$


::::{answer}
$$
f'(x) = 2xe^{x^2 - 1}
$$
::::

::::{solution}
Vi har at 

$$
f(x) = g(u(x))
$$


der 

$$
g(u) = e^u \qog u(x) = x^2 - 1
$$

Vi har at 

$$
g'(u) = e^u 
$$

Videre har vi at 

$$
u'(x) = 2x
$$

Etter kjerneregelen har vi da 

$$
f'(x) = g'(u) \cdot u'(x) = e^{u} \cdot 2x
$$

Så setter vi tilbake definisjonen av $u$. Da får vi:

$$
f'(x) = 2xe^{x^2 - 1}
$$
::::

:::::::::::::::


---


Vi kan også bruke kjerneregelen flere ganger dersom vi har en sammensatt funksjon med flere sammensetninger.


:::::::::::::::{summary} Kjerneregelen med flere sammensetninger
La $f$ være en funksjon 

$$
f(x) = g(u(v(x)))
$$

Da er 

$$
f'(x) = g'(u) \cdot u'(v) \cdot v'(x)
$$
:::::::::::::::


Regelen forteller oss at vi bare deriverer oss "innover" i sammensetningen fra den ytterste funksjonen inn til "kjernen" av sammensetningen. Dette kan vi gjøre i en kjede så langt vi må for å komme helt inn til kjernen av funksjonen. 


:::::::::::::::{example} Eksempel 2
En funksjon $f$ er gitt ved 

$$
f(x) = e^{\sqrt{x^2 + 1}}
$$

Bestem $f'(x)$.

::::{solution}
---
dropdown: 0
---
Her har vi at

$$
f(x) = g(u(v(x)))
$$

der

$$
g(u) = e^u, \quad u(v) = \sqrt{v}, \quad \text{og} \quad v(x) = x^2 + 1
$$

Da er 

$$
f'(x) = g'(u) \cdot u'(v) \cdot v'(x)
$$

Vi deriverer hver funksjon for seg:

$$
g'(u) = e^u \qog u'(v) = \dfrac{1}{2\sqrt{v}} \qog v'(x) = 2x
$$

Setter vi dette sammen får vi:

$$
\begin{align*}
f'(x) &= g'(u) \cdot u'(v) \cdot v'(x) \\
\\
&= e^u \cdot \dfrac{1}{2\sqrt{v}} \cdot 2x \\
\\
&= \dfrac{2x e^u}{2\sqrt{v}} \\
\\
&= \dfrac{x e^u}{\sqrt{v}}
\end{align*}
$$

Til slutt setter vi tilbake definisjonene av $u$ og $v$ som gir oss

$$
f'(x) = \dfrac{x e^{\sqrt{x^2 + 1}}}{\sqrt{x^2 + 1}}
$$
::::

:::::::::::::::


---


:::::::::::::::{exercise} Underveisoppgave 2
En funksjon $f$ er gitt ved

$$
f(x) = \left(\ln(x^3 + 1)\right)^2
$$


::::{answer}
$$
f'(x) = \dfrac{6x^2 \ln(x^3 + 1)}{x^3 + 1}
$$
::::


::::{solution}
Vi har at 

$$
f(x) = g(u(v(x)))
$$

der 

$$
g(u) = u^2 \qog u(v) = \ln(v) \qog v(x) = x^3 + 1
$$

Etter kjerneregelen er da 

$$
f'(x) = g'(u) \cdot u'(v) \cdot v'(x)
$$

Vi deriverer hver funksjon for seg: 

$$
g'(u) = 2u \qog u'(v) = \dfrac{1}{v} \qog v'(x) = 3x^2
$$

Deretter kombinerer vi resultatene: 

$$
\begin{align*}
f'(x) &= g'(u) \cdot u'(v) \cdot v'(x) \\
\\
&= 2u \cdot \dfrac{1}{v} \cdot 3x^2 \\
\\
&= \dfrac{6x^2 u}{v}
\end{align*}
$$

Så setter vi tilbake definisjonen av $u$ og $v$: 

$$
f'(x) = \dfrac{6x^2 \ln(x^3 + 1)}{x^3 + 1}
$$

::::

:::::::::::::::
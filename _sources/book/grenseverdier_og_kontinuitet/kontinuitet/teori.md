# Kontinuitet

:::{admonition} Læringsmål
---
class: tip
---
* Kunne avgjøre om delte funksjoner er kontinuerlig i et punkt.
* Kunne avgjøre om en funksjon er kontinuerlig i et punkt ved å bruke grenseverdier.
:::


Intuitivt er en funksjon kontinuerlig i et punkt dersom grafen til funksjonen ikke har noen "hull" eller "hopp" i punktet.


## Kontinuitet for delte funksjoner

:::::::::::::::{summary} Kontinuitet: Delte funksjoner
En funksjon $f$ på formen

$$
f(x) = \begin{cases}
    g(x) & \qhvis x \lt a \\
    \\
    h(x) & \qhvis x \geq a
\end{cases}
$$

er kontinuerlig i punktet $x = a$ dersom $g(a) = h(a)$. 

:::::::::::::::



---



:::::::::::::::{example} Eksempel 1
Funksjonen $f$ er gitt ved

$$
f(x) = \begin{cases}
    2x + 1 & \qhvis x \lt 1 \\
    \\
    x^2 + 2 & \qhvis x \geq 1
\end{cases}
$$


Avgjør om $f$ er i kontinuerlig i punktet $x = 1$.


::::{solution}
---
dropdown: 0
---
Vi lar

$$
g(x) = 2x + 1 \qog h(x) = x^2 + 2
$$

Da er $f$ kontinuerlig i $x = 1$ dersom $g(1) = h(1)$. Vi sjekker:

$$
g(1) = 2 \cdot 1 + 1 = 3
$$

$$
h(1) = 1^2 + 2 = 3
$$

Altså er $g(1) = h(1)$, og $f$ er kontinuerlig i punktet $x = 1$.
::::


:::::::::::::::



---




:::::::::::::::{example} Eksempel 2
Funksjonen $f$ er gitt ved

$$
f(x) = \begin{cases}
    ax - 3 & \qhvis x \lt 2 \\
    \\
    x^2 + 3 & \qhvis x \geq 2
\end{cases}
$$

Bestem $a$ slik at $f$ er kontinuerlig i punktet $x = 2$.

::::{solution}
---
dropdown: 0
---
Vi lar

$$
g(x) = ax - 3 \qog h(x) = x^2 + 3
$$

Da er $f$ kontinuerlig i $x = 2$ dersom $g(2) = h(2)$. Vi setter opp likningen:

$$
g(2) = h(2) \liff a \cdot 2 - 3 = 2^2 + 3
$$

$$
2a - 3 = 4 + 3 \liff 2a = 10 \liff a = 5
$$

Altså er $f$ kontinuerlig i punktet $x = 2$ dersom $a = 5$.
::::
:::::::::::::::



---



## Kontinuitet ved hjelp av grenseverdier

Noen ganger vil vi jobbe med delte funksjoner som er bygget av funksjoner som ikke er definert i bruddpunktene til funksjonen. Da trenger vi en mer generell måte å tenke på kontinuitet. Her kommer grenseverdier til unnsetning.


:::::::::::::::{summary} Kontinuitet med grenseverdier
En funksjon $f$ er kontinuerlig i et punkt $x = a$ dersom:
1. Grenseverdien $\lim\limits_{x \to a} f(x)$ eksisterer.
2. $f(a)$ er definert.
3. $\lim_{x \to a} f(x) = f(a)$
:::::::::::::::


---


:::::::::::::::{example} Eksempel 3
Funksjonen $f$ er gitt ved

$$
f(x) = \begin{cases}
    \dfrac{x^2 - 8}{x - 2} & \qhvis x \neq 2 \\
    \\
    a & \qhvis x = 2
\end{cases}
$$

Bestem $a$ slik at $f$ er kontinuerlig i punktet $x = 2$.


::::{solution}
---
dropdown: 0
---
Vi prøver først å finne grenseverdien $\lim\limits_{x \to 2} f(x)$. For $x \neq 2$ så er $f(x) = \dfrac{x^3 - 8}{x - 2}$, så da får vi

$$
\lim_{x \to 2} f(x) = \lim_{x \to 2} \frac{x^3 - 8}{x - 2} = \dfrac{2^3 - 8}{2 - 2} = \dfrac{0}{0}
$$

Vi får et ubestemt uttrykk på formen $0/0$, så vi kan bruke L'Hôpitals regel for å regne ut grenseverdien. Vi deriverer teller og nevner hver for seg:

$$
\lim_{x \to 2} f(x) = \lim_{x \to 2} \frac{x^3 - 8}{x - 2} \overset{[\frac{0}{0}]}{=} \lim_{x \to 2} \frac{3x^2}{1} = 3 \cdot 2^2 = 12
$$

Siden $f(2) = a$, må vi derfor kreve at $a = 12$ for at $f$ skal være kontinuerlig i punktet $x = 2$. Bare da er

$$
\lim_{x \to 2} f(x) = f(2) = 12
$$
::::
:::::::::::::::
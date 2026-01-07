# Den deriverte av den omvendte funksjonen

::::{goals}
* Kunne bestemme den deriverte av en omvendt funksjon.
::::

Selv om en funksjon $f$ har en omvendt funksjon $f^{-1}$ er det ikke alltid vi kan bestemme $f^{-1}(x)$ som en formel. I en del sammenhenger ønsker vi likevel å kunne bestemme den deriverte av den omvendte funksjonen, $\left(f^{-1}\right)'(x)$, og her skal vi se at dette er mulig å gjøre uten å kjenne formelen til den omvendte funksjonen. 


La $g = f^{-1}$ være den omvendte funksjonen til $f$. Fra definisjonen av omvendte funksjoner vet vi at

$$
g(f(x)) = x
$$

Vi deriverer likningen på hver side. Fra kjerneregelen for derivasjon får vi da

$$
(g(f(x)))' = x' \limplies g'(f(x)) \cdot f'(x) = 1
$$

som betyr at

$$
g'(f(x)) = \frac{1}{f'(x)}
$$

Altså kan vi bestemme den deriverte til en omvendt funksjon dersom vi kjenner til $f(x)$ og $f'(x)$. Formelen forutsetter at $f'(x) \neq 0$ slik at vi ikke deler på null.



:::::::::::::::{summary} Den deriverte av en omvendt funksjon
La $f$ være en funksjon og $g = f^{-1}$ være den omvendte funksjonen til $f$. Da er den deriverte til den omvendte funksjonen i $y = f(x)$ gitt ved

$$
g'(y) = \frac{1}{f'(x)}
$$


der $y = f(x)$ og $f'(x) \neq 0$.

:::::::::::::::


Formelen ovenfor er en konsekvens av 1) definisjonen av en omvendt funksjon. 2) kjerneregelen for derivasjon. Men vi kan også gi den en geometrisk tolkning som hjelper litt med å forstå hva formelen egentlig sier.

I et punkt $x$, så vil $f'(x)$ være gitt ved

$$
f'(x) = \lim_{\Delta x \to 0} \dfrac{\Delta y}{\Delta x}
$$

Men siden $g$ er den omvendte funksjonen til $f$, så vil $x$-koordinatene til punkter $(x, y)$ på grafen til $f$ tilsvare $y$-koordinatene til punkter $(y, x)$ på grafen til $g$. Det betyr at vi kan skrive

$$
g'(y) = \lim_{\Delta y \to 0} \dfrac{\Delta x}{\Delta y} = \lim_{\Delta y \to 0} \dfrac{1}{\dfrac{\Delta y}{\Delta x}} = \frac{1}{f'(x)}
$$

Se figuren nedenfor.


:::{plot}
width: 70%
function: (x - 1)**2 + 2, f, 
:::








---


:::::::::::::::{example} Eksempel 1
En funksjon $f$ er gitt ved

$$
f(x) = x^2 - 4x + 3 \qder D_f = [2, \to\rangle.
$$

La $g$ være den omvendte funksjonen til $f$.

Bestem $g'(3)$.


::::{solution}
---
dropdown: 0
---
Først må vi løse likningen $f(x) = 3$ for å finne $x$-verdien som tilsvarer $y = 3$.

$$
f(x) = 3 \liff x^2 - 4x + 3 = 3
$$

$$
x^2 - 4x = 0 \liff x(x - 4) = 0
$$

som gir

$$
x = 0 \or x = 4
$$

Det er bare $x = 4 \in D_f$, så vi har at $f(4) = 3$. Da har vi at

$$
g'(y) = \dfrac{1}{f'(x)} \limplies g'(3) = \frac{1}{f'(4)}
$$

Vi bestemmer $f'(4)$:

$$
f'(x) = 2x - 4 \limplies f'(4) = 4
$$

Altså er

$$
g'(3) = \frac{1}{4}
$$


::::

:::::::::::::::


---



:::::::::::::::{exercise} Underveisoppgave 1
En funksjon $f$ er gitt ved

$$
f(x) = -x^2 + 2x + 8 \qder D_f = [2, \to\rangle.
$$


La $g = f^{-1}$ være den omvendte funksjonen til $f$.

Bestem $g'(0)$.


::::{answer}
$$
g'(0) = -\frac{1}{6}
$$
::::

::::{solution}
Siden vi skal regne ut $g'(0)$, så må vi vite $x$-verdien som tilsvarer $y = 0$. Vi løser derfor likningen

$$
f(x) = 0 \liff -x^2 + 2x + 8 = 0
$$

$$
x = -\dfrac{2 \pm \sqrt{2^2 - 4 \cdot (-1) \cdot 8}}{2 \cdot (-1)} = -\frac{2 \pm 6}{-2}
$$

$$
x = 4 \or x = -2
$$

Det er bare $x = 4 \in D_f$, så vi har at $f(4) = 0$. Da har vi at

$$
g'(y) = \dfrac{1}{f'(x)} \limplies g'(0) = \frac{1}{f'(4)}
$$

Vi bestemmer $f'(4)$:

$$
f'(x) = -2x + 2 \limplies f'(4) = -6
$$

Altså er

$$
g'(0) = -\frac{1}{6}
$$
::::

:::::::::::::::


Vi tar et eksempel til.


---


:::::::::::::::{example} Eksempel 2
En funksjon $f$ er gitt ved

$$
f(x) = x\ln x \qder D_f = \langle 1, \to\rangle.
$$


La $g = f^{-1}$. 


Bestem stigningstallet til tangenten til grafen til $g$ i punktet $(1, e)$.


::::{solution}
---
dropdown: 0
---
Punkter $(b, a)$ på grafen til $g$ vil tilsvare punkter $(a, b)$ på grafen til $f$. Det betyr at punktet $(1, e)$ på grafen til $g$ tilsvarer punktet $(e, 1)$ på grafen til $f$. Vi skal altså bestemme $g'(1)$, og det kan vi gjøre ved å finne $f'(e)$ først og så bruke

$$
g'(y) = \frac{1}{f'(x)} \limplies g'(1) = \frac{1}{f'(e)}
$$

Vi bestemmer $f'(e)$:

$$
f'(x) = \ln x + 1 \limplies f'(e) = 2
$$

Altså er

$$
g'(1) = \frac{1}{2}
$$

Dermed er stigningstallet til tangenten til grafen til $g$ i punktet $(1, e)$ lik $\frac{1}{2}$.
::::


:::::::::::::::


## Motsatt vei



---



## Løsning med digitale verktøy 

For en del funksjoner er det vanskelig å løse likningen $f(x) = y$ for hånd. I slike tilfeller kan vi bruke digitale hjelpemidler for å finne den tilhørende $x$-verdien slik at vi kan bestemme $g'(y)$. 

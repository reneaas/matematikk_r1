# Den deriverte av den omvendte funksjonen

::::{goals}
* Kunne bestemme den deriverte av en omvendt funksjon.
::::

Vi har sett at selv om en funksjon $f$ har en omvendt funksjon $g$, så er det slettes ikke sikkert at vi klarer å bestemme funksjonsuttrykket til den omvendte funksjonen. I noen tilfeller kan vi klare å finne en funksjon $f(x)$ der vi egentlig er mer interessert i hvordan $x$ oppfører seg, fremfor $f(x)$. Men siden vi ikke nødvendigvis klarer å finne et funksjonsuttrykk som beskriver $x$ (ved hjelp av den omvendte funksjonen), så står vi ovenfor et problem dersom vi ønsker å forstå hvordan $x$ endrer seg når $f(x)$ endrer seg.

Heldigvis skal vi se at det er en ganske enkel sammenheng som lar oss finne den deriverte av en omvendt funksjon så lenge vi vet hvordan den opprinnelige funksjonen oppfører seg.


Kjerneregelen gir oss heldigvis hovedresultatet vi trenger. Hvis $f$ og $g$ er omvendte funksjoner, så vet vi at

$$
g(f(x)) = x
$$

Hvis vi deriverer begge sider med hensyn på $x$, så får vi

$$
\left(g(f(x))\right)' = (x)' \\
\\
g'(f(x)) \cdot f'(x) = 1\\
\\
g'(f(x)) = \dfrac{1}{f'(x)}
$$

Men vi har at $y = f(x)$, så dermed får vi at

$$
g'(y) = \dfrac{1}{f'(x)}
$$


:::::::::::::::{summary} Den deriverte av en omvendte funksjon
La $f$ være en funksjon og $g$ være den omvendte funksjonen til $f$. Da er

$$
g'(y) = \dfrac{1}{f'(x)}
$$

der $y = f(x)$ og $x = g(y)$.
:::::::::::::::


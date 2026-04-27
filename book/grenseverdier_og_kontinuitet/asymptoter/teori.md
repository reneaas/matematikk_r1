# Asymptoter


:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke grenseverdier til å avgjøre om en funksjon har asymptoter, og bestemme likningene til asymptoter.
:::



## Horisontale asymptoter
Dersom grafen til en funksjon $f$ "flater ut" og nærmer seg en horisontal linje når vi lar $x \to \infty$ eller $x \to -\infty$, så sier vi at den horisontale linja er en horisontal asymptote for $f$.

:::::::::::::::{summary} Horisontale asymptoter



:::{plot}
width: 100%
align: right
let: L = 1
function: L + 2 / (1 + exp(-0.5 * x)), f
hline: L + 2, 0, 20, red, dashed
ticks: off
fontsize: 28
ymin: -1
ymax: 4
xmax: 10
xmin: -10
text: 0, L + 2, "$L_1$", center-left
hline: L, -20, 0, red, dashed
text: 0, L, "$L_2$", center-right
:::

Linja $y = L_1$ er en horisontal asymptote for $f$ hvis

$$
\lim_{x \to \infty} f(x) = L_1
$$

Linja $y = L_2$ er en horisontal asymptote for $f$ hvis

$$
\lim_{x \to -\infty} f(x) = L_2
$$


> De horisontale asymptotene kan også gjelde begge veier slik at $f(x) \to L$ både når $x \to \infty$ og når $x \to -\infty$.

:::::::::::::::



---



:::::::::::::::{example} Eksempel 1
Funksjonen $f$ er gitt ved

$$
f(x) = \dfrac{3 + 2e^{-x}}{1 + e^{-x}}
$$

Bestem eventuelle horisontale asymptoter til grafen til $f$.


::::{solution}
---
dropdown: 0
---
Vi sjekker først om det finnes en horisontal asymptote når $x \to \infty$. Vi regner ut grenseverdien

$$
\lim_{x \to \infty} f(x) = \lim_{x \to \infty} \dfrac{3 + 2e^{-x}}{1 + e^{-x}} = \dfrac{3 + 2 \cdot 0}{1 + 0} = 3
$$

Altså er $y = 3$ en horisontal asymptote for $f$ når $x \to \infty$.


Vi sjekker så om det finnes en horisontal asymptote når $x \to -\infty$. Vi regner ut grenseverdien

$$
\lim_{x \to -\infty} f(x) = \lim_{x \to -\infty} \dfrac{3 + 2e^{-x}}{1 + e^{-x}} = \dfrac{3 + 2 \cdot \infty}{1 + \infty} = \dfrac{\infty}{\infty}
$$

Vi får et ubestemt uttrykk $\infty/\infty$, så vi kan bruke L'Hôpitals regel:

$$
\lim_{x \to -\infty} f(x) \overset{[\frac{\infty}{\infty}]}{=} \lim_{x \to -\infty} \dfrac{-2e^{-x}}{-e^{-x}} = \lim_{x \to -\infty} 2 = 2
$$

Altså er $y = 2$ en horisontal asymptote for $f$ når $x \to -\infty$.
::::


:::::::::::::::

## Vertikale asymptoter
Dersom det finnes punkter $x = a$ hvor grafen til $f$ "skyter i været" og vokser eller synker mot uendelig slik at funksjonen nærmer seg en vertikal linje $x = a$, så sier vi at linja $x = a$ er en vertikal asymptote for $f$. 


:::::::::::::::{summary} Vertikale asymptoter

:::{plot}
width: 100%
align: right
function: 1 / (exp(x - 2) - 1), f
vline: 2, dashed, red
ticks: off
text: 2, 0, "$x = a$", bottom-right
fontsize: 25
:::



Linja $x = a$ er en vertikal asymptote for $f$ dersom

$$
\lim_{x \to a^+} f(x) = \pm\infty
$$

eller 

$$
\lim_{x \to a^-} f(x) = \pm\infty
$$

> Det holder av én av de to grenseverdiene går mot uendelig for at $x = a$ skal være en vertikal asymptote for $f$.
:::::::::::::::


I praksis så leter vi etter vertikale asymptoter ved å finne punkter der vi deler på $0$ i funksjonsuttrykket. Deretter sjekker vi om grenseverdiene fra høyre og venstre går mot uendelig for å avgjøre om det faktisk er en vertikal asymptote i det punktet.



---


:::::::::::::::{example} Eksempel 2
Funksjonen $f$ er gitt ved

$$
f(x) = \dfrac{1}{e^{x - 2} - 1}
$$

Bestem eventuelle vertikale asymptoter til grafen til $f$.

::::{solution}
---
dropdown: 0
---
Vi må først lete etter punkter hvor vi ender opp med å dele på null i $f(x)$. Da løser vi nevneren lik null:

$$
e^{x - 2} - 1 = 0 \liff e^{x - 2} = 1
$$

$$
\ln e^{x - 2} = \ln 1 \liff x - 2 = 0 \liff x = 2
$$


Altså kan $x = 2$ være en vertikal asymptote for $f$. Vi må sjekke ved å regne ut de ensidige grensene:

$$
\lim_{x \to 2^+} f(x) = \lim_{x \to 2^+} \dfrac{1}{e^{x - 2} - 1} = \dfrac{1}{e^{2^+ - 2} - 1} = \dfrac{1}{e^{0^+} - 1} = \dfrac{1}{0^+} = \infty
$$

Siden grenseverdien fra høyre er $\infty$, så vet vi at $x = 2$ er en vertikal asymptote for $f$. Vi trenger ikke å sjekke den andre grenseverdien, men vi bare viser hvordan det gjøres for å være grundige:

$$
\lim_{x \to 2^-} f(x) = \lim_{x \to 2^-} \dfrac{1}{e^{x - 2} - 1} = \dfrac{1}{e^{2^- - 2} - 1} = \dfrac{1}{e^{0^-} - 1} = \dfrac{1}{0^-} = -\infty
$$


> Legg merke til at vi bruker notasjonen $0^+$ for å vise at vi nærmer oss $0$, men at verdien alltid er positiv. På samme måte så bruker vi $0^-$ for å vise at vi nærmer oss $0$, men at verdien alltid er negativ.

::::
:::::::::::::::



## Skrå asymptoter
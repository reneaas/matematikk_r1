# Grenseverdier



:::{admonition} Læringsmål
---
class: tip
---
* Kunne bruke ulike strategier for å regne ut grenseverdier.
* Kunne avgjøre om en grenseverdi eksisterer eller ikke.
:::


## Definisjon av grenseverdier
Å regne ut grenseverdier handler om å undersøke om en funksjon $f(x)$ nærmer seg et bestemt tall $L$ når vi lar $x$ nærme seg et bestem tall $a$ på tallinja. Hvis dette er tilfellet, så skriver vi at

$$
\lim_{x \to a} f(x) = L
$$

og leser det som at "$f(x)$ nærmer seg $L$ når $x$ nærmer seg $a$".

Før vi ser på noen detaljer, så tar vi den første strategien vi skal bruke når vi regner ut grenseverdier:


:::::::::::::::{summary} Strategi 1 for grenseverdier
For å regne ut grenseverdien

$$
\lim_{x \to a} f(x)
$$

så prøver vi å sette inn $x = a$ direkte i uttrykket for $f(x)$. Hvis vi får et tallsvar, så er grenseverdien lik det tallet. Det vil si

$$
\lim_{x \to a} f(x) = f(a)
$$
:::::::::::::::


---


:::::::::::::::{example} Eksempel 1
Bestem grenseverdien

$$
\lim_{x \to 4} \dfrac{x^2 + 8}{2x}
$$

::::{solution}
---
dropdown: 0
---
Vi prøver å sette inn $x = 4$ direkte i uttrykket og sjekker om vi får et tallsvar:


$$
\lim_{x \to 4} \dfrac{x^2 + 8}{2x} = \dfrac{4^2 + 8}{2 \cdot 4} = \dfrac{24}{8} = 3
$$

Vi fikk et tallsvar, så da er grenseverdien lik $3$. 

::::
:::::::::::::::


## Eksistens av grenseverdier

I figuren nedenfor til venstre, så vil vi nærme oss samme verdi $L$ om vi bruker forskriften til $f(x)$ på venstre side av $x = a$ eller på høyre side av $x = a$. Da sier vi at grenseverdien eksisterer.


I figuren nedenfor til høyre så vil derimot $g(x)$ nærme seg to forskjellige verdier $L_1$ og $L_2$ avhengig av om vi bruker forskriften til venstre for $x = a$ eller forskriften til høyre for $x = a$. Da sier vi at grenseverdien ikke eksisterer fordi den ikke nærmer seg ett bestemt tall fra begge sider av $x = a$.


::::{multi-plot2}
---
rows: 1
cols: 2
fontsize: 25
---

:::{plot}
width: 100%
function: (x - 1)**2 - 2, (-6, 3), f, blue
function: (x - 3) + 2, [3, 8), blue
function-endpoints: true
ticks: off
let: a = 3
vline: a, 0, f(a), dashed, gray
hline: f(a), 0, a, dashed, gray
text: a, 0, "$a$", bottom-center
text: 0, f(a), "$L$", center-left
xmin: -2
xmax: 7
ymin: -3
nocache:
:::


:::{plot}
width: 100%
function: (x - 1)**2 - 2, (-6, 3), g, red
function: (x - 3) + 4, [3, 8), red
def: g1(x) = (x - 1)**2 - 2
def: g2(x) = (x - 3) + 4
function-endpoints: true
ticks: off
let: a = 3
vline: a, 0, g2(a), dashed, gray
text: a, 0, "$a$", bottom-center
hline: g1(a), 0, a, dashed, gray
text: 0, g1(a), "$L_1$", center-left
hline: g2(a), 0, a, dashed, gray
text: 0, g2(a), "$L_2$", center-left
xmin: -2
xmax: 7
ymin: -3
nocache:
:::
::::




## Ensidige grenseverdier
For at en grenseverdi skal eksistere, så må $f(x)$ nærme seg samme tall $L$ både når vi nærmer oss $x = a$ fra venstre og når vi nærmer oss $x = a$ fra høyre.

:::::::::::::::{summary} Ensidige grenseverdier og eksistens av en grenseverdi
Når vi vil undersøke hva $f(x)$ nærmer seg når vi lar $x$ nærme seg $x = a$ fra venstre side (nedenfra), så skriver vi

$$
\lim_{x \to a^-} f(x)
$$

Når vi vil undersøke hva $f(x)$ nærmer seg når vi lar $x$ nærme seg $x = a$ fra høyre side (ovenfra), så skriver vi

$$
\lim_{x \to a^+} f(x)
$$

Hvis vi får samme tall $L$ for begge de ensidige grenseverdiene, så eksisterer grenseverdien og vi skriver at

$$
\lim_{x \to a} f(x) = L
$$


Grenseverdien eksisterer altså hvis og bare hvis

$$
\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L
$$
:::::::::::::::



---



:::::::::::::::{example} Eksempel 2
Funksjonen $f$ er gitt ved

$$
f(x) = \begin{cases}
x^2 - 1 & \qhvis x < 2 \\
\\
x + 1 & \qhvis x \geq 2
\end{cases}
$$

Bestem $\lim\limits_{x \to 2} f(x)$ dersom den eksisterer.

::::{solution}
---
dropdown: 0
---
Vi lar $g(x) = x^2 - 1$ og $h(x) = x + 1$. Vi starter med å regne ut de ensidige grenseverdiene. For $x < 2$ så er $f(x) = g(x)$, så da får vi

$$
\lim_{x \to 2^-} f(x) = \lim_{x \to 2^-} g(x) = \lim_{x \to 2^-} (x^2 - 1) = 2^2 - 1 = 3
$$

For $x \geq 2$ så er $f(x) = h(x)$, så da får vi

$$
\lim_{x \to 2^+} f(x) = \lim_{x \to 2^+} h(x) = \lim_{x \to 2^+} (x + 1) = 2 + 1 = 3
$$

Siden vi fikk samme verdi for de ensidige grenseverdiene, så eksisterer grenseverdien og vi har at

$$
\lim_{x \to 2} f(x) = 3
$$
::::


:::::::::::::::




## L'Hôpitals regel
L'Hôpitals regel lar oss regne ut grenseverdier av uttrykk på formen $\frac{f(x)}{g(x)}$ når både $f(x)$ og $g(x)$ nærmer seg 0 når $x$ nærmer seg en bestemt verdi $a$. 



:::::::::::::::{summary} L'Hôpitals regel: Versjon 1
Hvis $\lim\limits_{x \to a} \dfrac{f(x)}{g(x)} = \dfrac{0}{0}$ så gjelder

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}
$$


> Merk at vi også kan ha at $a = \infty$ eller $a = -\infty$.
:::::::::::::::



---


:::::::::::::::{example} Eksempel 3
Regn ut grenseverdien

$$
\lim_{x \to 2} \frac{x^3 - 8}{x - 2}
$$

::::{solution}
---
dropdown: 0
---
Vi prøver først å sette inn $x = 2$ direkte:

$$
\lim_{x \to 2} \frac{x^3 - 8}{x - 2} = \dfrac{2^3 - 8}{2 - 2} = \frac{0}{0}
$$

Vi får et ubestemt uttrykk som er $0/0$. Da kan vi bruke L'Hôpitals regel. Vi deriverer teller og nevner hver for seg og prøver å sette inn $x = 2$ igjen:

$$
\lim_{x \to 2}\frac{x^3 - 8}{x - 2} \overset{[\frac{0}{0}]}{=} \lim_{x \to 2} \frac{(x^3 - 8)'}{(x - 2)'} = \lim_{x\to 2} \dfrac{3x^2}{1} = \dfrac{3 \cdot 2^2}{1} = 12
$$

Nå fikk vi et tallsvar som betyr at

$$
\lim_{x \to 2} \frac{x^3 - 8}{x - 2} = 12
$$


> Legg merke til at vi markerer at vi bruker L'Hôpitals regel ved å skrive $[\frac{0}{0}]$ over likhetstegnet. Dette er for å vise at vi har brukt regelen *på grunn av* at vi fikk et ubestemt uttrykk som er $0/0$.
::::
:::::::::::::::


---


L'Hôpitals regel fungerer også i tilfeller der $\lim\limits_{x \to a} \dfrac{f(x)}{g(x)} = \dfrac{\infty}{\infty}$, altså når både $f(x)$ og $g(x)$ nærmer seg uendelig når $x$ nærmer seg en bestemt verdi $a$. 


:::::::::::::::{summary} L'Hôpitals regel: Versjon 2
Hvis $\lim\limits_{x \to a} \dfrac{f(x)}{g(x)} = \dfrac{\infty}{\infty}$ så gjelder

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}
$$


> Merk at vi også kan ha at $a = \infty$ eller $a = -\infty$.
:::::::::::::::



---



:::::::::::::::{example} Eksempel 4
Bestem grenseverdien

$$
\lim_{x \to \infty} \frac{8x^2 - 5x + 1}{2x^2 + 3}
$$


::::{solution}
---
dropdown: 0
---
Vi prøver først å sette inn $x = \infty$ direkte:

$$
\lim_{x \to \infty} \frac{8x^2 - 5x + 1}{2x^2 + 3} = \dfrac{\infty}{\infty}
$$

Vi får et ubestemt uttrykk som er $\infty/\infty$. Da kan vi bruke L'Hôpitals regel. Vi deriverer teller og nevner hver for seg og prøver å sette inn $x = \infty$ igjen:

$$
\begin{align*}
\lim_{x \to \infty} \frac{8x^2 - 5x + 1}{2x^2 + 3} &\overset{[\frac{\infty}{\infty}]}{=} \lim_{x \to \infty} \dfrac{16x - 5}{4x} \\
\\
&\overset{[\frac{\infty}{\infty}]}{=} \dfrac{16}{4} \\
\\
&= 4
\end{align*}
$$

Altså er grenseverdien lik $4$.
::::
:::::::::::::::



## Spesielle grenseverdier
Det er noen grenseverdier som er verdt å lære seg utenat fordi de dukker opp såpass ofte.



:::::::::::::::{summary} Grenseverdier for eksponentialfunksjoner
:::{plot}
width: 100%
align: right
function: exp(x), blue
ymin: -1
ticks: off
fontsize: 28
text: -4, 5, "$f(x) = e^x$", center-center, bbox
:::

$$
\begin{align*}
\lim_{x\to \infty} e^x = \infty && \lim_{x\to -\infty} e^x = 0 \\
\\
\lim_{x\to \infty} e^{-x} = 0 && \lim_{x\to -\infty} e^{-x} = \infty \\
\end{align*}
$$


:::::::::::::::



:::::::::::::::{summary} Grenseverdier for logaritmefunksjoner
:::{plot}
width: 100%
align: right
function: log(x), blue
ymin: -6
xmin: -1
ticks: off
fontsize: 28
text: 3, 5, "$f(x) = \ln(x)$", center-center, bbox
:::


$$
\begin{align*}
\lim_{x\to \infty} \ln(x) = \infty \\
\\
\lim_{x\to 0^+} \ln(x) = -\infty
\end{align*}
$$

:::::::::::::::



---



:::::::::::::::{example} Eksempel 5
Regn ut grenseverdien

$$
\lim_{x \to \infty} \frac{e^{3x} - 1}{e^x + 5}
$$


::::{solution}
---
dropdown: 0
---
Vi prøver først å sette inn $x = \infty$ direkte:

$$
\lim_{x \to \infty} \frac{e^{3x} - 1}{e^x + 5} = \dfrac{\infty - 1}{\infty + 5} = \dfrac{\infty}{\infty}
$$

Vi får et ubestemt uttrykk som er $\infty/\infty$. Da kan vi bruke L'Hôpitals regel. Vi deriverer teller og nevner hver for seg og prøver å sette inn $x = \infty$ igjen:

$$
\lim_{x \to \infty} \frac{e^{3x} - 1}{e^x + 5} \overset{[\frac{\infty}{\infty}]}{=} \lim_{x \to \infty} \frac{(e^{3x} - 1)'}{(e^x + 5)'} = \lim_{x \to \infty} \dfrac{3e^{3x}}{e^x} = \lim_{x \to \infty} 3e^{2x} = \infty
$$

> Når en grenseverdi er lik $\infty$ eller $-\infty$ så sier vi også at grenseverdien ikke eksisterer siden den ikke nærmer seg et bestemt tall. Men her er det vanlig å skrive at grenseverdien er lik $\infty$ eller lik $-\infty$ for å vise at den ikke eksisterer på grunn av at funksjonen vokser eller synker uten begrensning.
::::
:::::::::::::::




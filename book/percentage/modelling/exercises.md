# Modellering med eksponentiell vekst

:::::::{admonition} Oppsummering
---
class: summary, dropdown
---

::::::{tab-set}
---
class: tabs-parts
---
:::::{tab-item} Vekstfaktor
Vekstfaktoren er et tall vi ganger med for å gå fra en "gammel" verdi til en "ny" verdi.

Formel for vekstfaktor (økning):
: $V = 100 \% + \mathrm{prosent}$

Formel for vekstfaktor (nedgang): 
: $V = 100 \% - \mathrm{prosent}$
:::::


:::::{tab-item} Eksponentiell vekst
Gitt en prosentvis endring som er den *samme* ved hver periode kan vi modellere veksten med en eksponentialfunksjonen:

$$
f(x) = G \cdot V^x
$$

der 

* $f(x)$ er verdien etter $x$ perioder
* $G$ er verdien ved $x = 0$ (startverdi)
* $V$ er vekstfaktoren til den prosentvise endringen

:::{figure} ./figures/summary/exponential_functions.svg
---
width: 80%
---
:::

:::::
::::::

:::::::

---

::::::{admonition} Oppgave 1
---
class: problem-level-1
---
Ta quizen! 

:::{raw} html
---
file: ./quiz/quiz_1/quiz_1.html
---
:::

::::::


---

::::::::::::{admonition} Oppgave 2
---
class: problem-level-1
---
Espen har investert i en bruktbil. Han antar at verdien av bilen etter $x$ år vil være $f(x)$ kr, beskrevet av modellen

$$
f(x) = 45 \, 000 \cdot 0.85^x
$$


:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Hvor mye kostet bilen til Espen, ifølge modellen?


:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(0) = 45 \, 000 \mathrm{kr}
$$
:::

::::::::::

::::::::::{tab-item} b
Hvor mange prosent synker verdien til bilen med hvert år?


:::{admonition} Fasit
---
class: answer, dropdown
---
$15 \%$ nedgang per år
:::

::::::::::


::::::::::{tab-item} c
Hva er verdien av bilen om $3$ år?

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
f(3) = 45 \, 000 \cdot 0.85^3 = 38250 \, \mathrm{kr}
$$
:::
::::::::::


::::::::::{tab-item} d
Når vil verdien til bilen være under $10 \, 000$ kr?

:::{admonition} Fasit
---
class: dropdown, answer
---
Etter ca. $9$ år ($x \approx 9.25$)
:::

::::::::::

:::::::::::


::::::::::::


---

::::::::::::{admonition} Oppgave 3
---
class: problem-level-1
---
Ida har kjøpt en ny laptop. Hun antar at verdien av laptopen etter $x$ år vil være $g(x)$ kr, beskrevet av modellen

$$
g(x) = 15 \, 000 \cdot 0.8^x
$$

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Hva var prisen på laptopen til Ida da hun kjøpte den?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
g(0) = 15 \, 000 \, \mathrm{kr}
$$
:::

::::::::::

::::::::::{tab-item} b
Hvor mange prosent synker verdien av laptopen hvert år?


:::{admonition} Fasit
---
class: answer, dropdown
---
$20 \%$ nedgang per år
:::


::::::::::

::::::::::{tab-item} c
Hva er verdien av laptopen om $4$ år?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
g(4) = 15 \, 000 \cdot 0.8^4 = 6144 \, \mathrm{kr}
$$
:::

::::::::::

::::::::::{tab-item} d
Ida vil gjerne selge laptopen før verdien er under $10 000 \, \mathrm{kr}$. 

Når må hun selge laptopen? 

:::{admonition} Fasit
---
class: dropdown, answer
---
Etter ca. $2$ år ($x \approx 1.82$)
:::


::::::::::
:::::::::::
::::::::::::


---

::::::::::::{admonition} Oppgave 4
---
class: problem-level-1
---
Petter har kjøpt en sykkel for konkurransebruk. Han antar at verdien av sykkelen etter $x$ år vil være $f(x)$ kr, beskrevet av modellen

$$
f(x) = 30 \, 000 \cdot 0.88^x
$$

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Hva var den opprinnelige prisen på sykkelen?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(0) = 30 \, 000 \mathrm{kr}
$$
:::

::::::::::

::::::::::{tab-item} b
Hvor mange prosent synker verdien av sykkelen hvert år?

:::{admonition} Fasit
---
class: answer, dropdown
---
$13 \%$ nedgang per år.
:::

::::::::::

::::::::::{tab-item} c
Hva vil verdien av sykkelen være etter $5$ år?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(5) = 30 \, 000 \cdot 0.88^5 \approx 15 \, 832 \, \mathrm{kr}
$$
:::

::::::::::

::::::::::{tab-item} d
Når vil sykkelen ha $75 \%$ av sin opprinnelige verdi?


:::{admonition} Fasit
---
class: dropdown, answer
---
Etter ca. $2$ år ($x \approx 2.25$)
:::



::::::::::
:::::::::::
::::::::::::



---


::::::::::::{admonition} Oppgave 5
---
class: problem-level-2
---
Gunnar skal kjøpe en bil som koster $300 \, 000 \, \mathrm{kr}$. <br> Hvert år synker verdien på bilen med $10 \%$.

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a

Sett opp en modell som gir bilens verdi i $f(x) \, \mathrm{kr}$ – $x$ år etter kjøpet.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 300 \, 000 \cdot 0.9^x
$$
:::

::::::::::

::::::::::{tab-item} b

Bestem verdien av bilen etter $5$ år.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(5) = 300 \, 000 \cdot 0.9^5 \approx 170 \, 354 \, \mathrm{kr}
$$
:::

::::::::::

::::::::::{tab-item} c
Hvor mange år tar det før verdien til bilen er halvert?

:::{admonition} Fasit
---
class: answer, dropdown
---
Vi må må bestemme løsningen av likningen:

$$
300 \, 000 \cdot 0.9^x = 150 \, 000 \quad \to \quad x \approx 6.57 \, \mathrm{år}
$$

eller da i løpet av det syvende året. 
::: 
::::::::::
:::::::::::

::::::::::::

---

::::::::::::{admonition} Oppgave 6
---
class: problem-level-2
---
En by har i dag en befolkning på $50 \, 000$ mennesker. Det antas at befolkningen vokser med $3 \%$ hvert år.

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a

Sett opp en modell som gir byens befolkning som gir antall innbyggere $B(x)$ i byen $x$ år etter i dag.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
B(x) = 50 \, 000 \cdot 1.03^x
$$
:::

::::::::::

::::::::::{tab-item} b

Hva vil byens befolkning være etter $10$ år?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
B(10) = 50 \, 000 \cdot 1.03^{10} \approx 67 \, 196 \, \mathrm{personer}
$$
:::

::::::::::

::::::::::{tab-item} c

Hvor lang tid tar det før byens befolkning har økt til $100 \, 000$ mennesker?

:::{admonition} Fasit
---
class: answer, dropdown
---
Løs likningen:

$$
50 \, 000 \cdot 1.03^x = 100 \, 000 \quad \to \quad x \approx 23.45 \, \mathrm{år}
$$

Altså tar det ca. $24$ år før byens befolkning har økt til $100 \, 000$ mennesker.
::: 
::::::::::
:::::::::::
::::::::::::

---

::::::::::::{admonition} Oppgave 7
---
class: problem-level-2
---
Martin investerte $10 \, 000 \, \mathrm{kr}$ i et fond. Fondet har en årlig avkastning på $5 \%$.

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a

Lag en modell som gir sparebeløpet $f(x)$ i kr etter $x$ år.

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 10 \, 000 \cdot 1.05^x
$$
:::

::::::::::

::::::::::{tab-item} b

Hva vil verdien av investeringen være etter $5$ år?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(5) = 10 \, 000 \cdot 1.05^5 \approx 12 \, 763 \, \mathrm{kr}
$$
:::

::::::::::

::::::::::{tab-item} c

Hvor lang tid tar det før investeringen har doblet seg i verdi?

:::{admonition} Fasit
---
class: answer, dropdown
---
Løs likningen:

$$
10 \, 000 \cdot 1.05^x = 20 \, 000 \quad \to \quad x \approx 14.21 \, \mathrm{år}
$$

Altså ca. 14 år.
:::
::::::::::
:::::::::::
::::::::::::

---


::::::{admonition} Oppgave 8
---
class: problem-level-2
---
Norge myndigheter har satt som mål at klimagassutslippet skal reduseres til $55 \%$ av hva det var i $1990$ innen $2030$. 

* I 1990 var klimagassutslippet tilsvarende $51.3$ millioner tonn $\mathrm{CO_2}$. 
* I 2022 var klimmautslippet tilsvarende $48.9$ millioner tonn $\mathrm{CO_2}$.

Vi ser for oss at klimagassutslippet reduseres med en fast prosent hvert år. 

`````{tab-set}
---
class: tabs-parts
---
````{tab-item} a

La $x$ være antall år etter 2022. 

Lag en modell der $f(x)$ er antall millioner tonn $\mathrm{CO_2}$ som slippes ut $x$ år etter 2022.


::::{admonition} Fasit
---
class: answer, dropdown
---
$$
f(x) = 48.9 \cdot 0.93^x
$$
::::

````

````{tab-item} b

Norge har som mål at klimagassutslippet reduseres med $90 \%$ sammenliknet med utslippet i 1990 innen 2050. 

Bruk modellen din til å bestemme når Norge vil nå dette målet.  


::::{admonition} Fasit
---
class: answer, dropdown
---
Norge når målet etter omtrent $31$ år ($x \approx 31.07$) som betyr at Norge vil nå målet i 2051, ifølge modellen.
::::

````



::::::

---

::::::::::::{admonition} Oppgave 9
---
class: problem-level-3
---
Gunnar og Greve jobber med en oppgave. De har fått opplysningene:
* I mai kostet to varer, A og B, like mye.
* Prisen for vare A har økt med $10 \%$ hver måned siden januar.
* Prisen for vare B har sunket md $10 \%$ hver måned siden januar.

Vi antar at trenden til de to varene fortsetter som før. 

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Gjør beregninger og undersøk om vare A vil koste det samme om tre måneder, som vare B kostet for tre måneder siden.
::::::::::

::::::::::{tab-item} b
Hvis utregninger i oppgave a ikke underbygget hypotesen, gjør beregninger og undersøk på hvilket tidspunkt de to varene kostet det samme.
::::::::::

::::::::::::

---

::::::::::::{admonition} Oppgave 10
---
class: problem-level-3
---
En elev skal spare penger til russetiden i mai 2025. Eleven har bestemt seg for å sette inn 5000 kr nå. Beløpet øker med en rente på $0.4 \%$ hver måned.


:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a
Fyll ut programmet under slik at det regner ut sparebeløpet til eleven i mai 2025.

::::::::::

::::::::::{tab-item} b
Eleven tenker at det er lurt å sette inn en innskudd på $500$ kr hver måned etter første innskudd.

Endre på programmet slik at det regner ut sparebeløpet til eleven i mai 2025.
::::::::::

::::::::::{tab-item} c
Eleven har som mål å spare opp 25 000 kr. 

Bruk programmet ditt til å undersøke hvor mye eleven må sette inn som innskudd per måned for å nå sparemålet sitt.
::::::::::


:::::::::::

:::{raw} html
---
file: ./interactive_code/exercises/exercise_10.html
---
:::

::::::::::::

---

::::::::::::{admonition} Oppgave 11
---
class: problem-level-3
---
En pasient tar en dose med 1000 mg Paracetamol. Halveringstiden til Paracetamol er på 3 timer.

:::::::::::{tab-set}
---
class: tabs-parts
---
::::::::::{tab-item} a

Fyll ut programmet slik at det regner ut mengden Paracetamol i pasientens kropp etter $6$ timer.

Hva forventer du svaret skal bli? 

::::::::::

::::::::::{tab-item} b
Pasienten her sykt mye tannverk og tar en dose med 1000 mg Paracetamol hver 6 time.

Endre på programmet slik at det regner ut hvor mye Paracetamol pasienten har i kroppen etter $24$ timer.

::::::::::


::::::::::{tab-item} c
Pasienten tar en dose med 1000 mg Paracetamol hver 6 time over veldig lang tid.

Hvor mye Paracetamol vil pasienten ha i kroppen etter gjentatt inntak av dosen over lang tid?

::::::::::

:::::::::::

---

:::{raw} html
---
file: ./interactive_code/exercises/exercise_11.html
---
:::




::::::::::::

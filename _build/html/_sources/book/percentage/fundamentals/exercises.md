# Prosent, prosentpoeng og vekstfaktor

::::::::{admonition} Oppsummering: Prosent, prosentpoeng og vekstfaktor
---
class: summary
---
:::::{tab-set}
---
class: tabs-parts
---
::::{tab-item} Prosent
Prosent er et forholdstall som vi kan uttrykke på tre forskjellige måter:

$$
\underbrace{30 \%}_{\displaystyle \mathrm{Prosentandel}} = \underbrace{0.3}_{\displaystyle \mathrm{Prosentfaktor/desimaltall}} = \underbrace{\frac{30}{100}}_{\displaystyle \mathrm{Brøk}}
$$

For å regne ut prosentandelen, kan vi bruke sammenhengen:

$$
\mathrm{Prosentandel} = \frac{\mathrm{Del}}{\mathrm{Helheten}} \cdot 100 \%
$$
::::

::::{tab-item} Prosentpoeng
Prosentpoeng handler om **differanser** mellom prosentandeler. Endringen i prosentpoeng er gitt ved 

$$
\mathrm{Prosentpoeng} = (\mathrm{Ny \ prosentandel}) - (\mathrm{Gammel \ prosentandel})
$$
::::

::::{tab-item} Vekstfaktor
Vekstfaktoren er et tall vi ganger med for å gå fra en "gammel" verdi til en "ny" verdi.

Formel for vekstfaktor (økning):
: $V = 100 \% + \mathrm{prosent}$

Formel for vekstfaktor (nedgang): 
: $V = 100 \% - \mathrm{prosent}$
::::

::::{tab-item} Prosentvise endringer

`````{tab} Fremover i "tid"
Når vi går fremover i "tid" (ser på verdien *etter* en endring), så **ganger** vi alltid med vekstfaktorer.
````{tab-set}
```{tab-item} Én endring
Formel:
: $$
N = G \cdot V
$$

der 

* $N$ er verdien **etter** endringen
* $G$ er verdien **før** endringen
* $V$ er vekstfaktoren

```

```{tab-item} To endringer
Formel:
: $$
N = G\cdot V_1 \cdot V_2
$$

der 

* $N$ er verdien **etter** begge endringer. 
* $G$ er verdien **før** begge endringer.
* $V_1$ er vekstfaktor for prosentvis endring 1.
* $V_2$ er vekstfaktor for prosentvis endring 2.

```

```{tab-item} Mange endringer - samme økning/nedgang
Formel:
: $$
N = G \cdot V^T
$$

der

* $N$ er verdien **etter** endringene
* $G$ er verdien **før** endringene
* $V$ er vekstfaktoren
* $T$ er antall perioder eller antall ganger endringene skjer.
```
````
`````
`````{tab} Bakover i "tid"
Når vi går bakover i "tid" (ser på verdien *før* en endring skjedde), **deler** vi alltid med vekstfaktorer.
````{tab-set}
```{tab-item} Én endring
Formel
: $$
G = \dfrac{N}{V}
$$

der

* $G$ er verdien **før** endringen
* $N$ er verdien **etter** endringen
* $V$ er vekstfaktoren
```

```{tab-item} To endringer
Formel
: $$
G = \dfrac{N}{V_1 \cdot V_2}
$$

der

* $G$ er verdien **før** begge endringer
* $N$ er verdien **etter** begge endringer
* $V_1$ er vekstfaktor for prosentvis endring 1
* $V_2$ er vekstfaktor for prosentvis endring 2
```

```{tab-item} Mange endringer - samme økning/nedgang
Formel
: $$
G = \dfrac{N}{V^T}
$$

der

* $G$ er verdien **før** endringene
* $N$ er verdien **etter** endringene
* $V$ er vekstfaktoren
* $T$ er antall perioder eller antall ganger endringene skjer. 
```
````
`````
::::

::::::::


::::{admonition} Oppgave 1
---
class: problem-level-1
---
Ta quizen! (Mer enn ett svar kan være riktig!)

:::{raw} html
---
file: quiz/quiz_1/quiz_1.html
---
:::

::::

---

::::{admonition} Oppgave 2
---
class: problem-level-1
---
På en videregående skole valgte $30 \%$ av elevene fransk som fremmedspråk. Skolen har 600 elever.

````{tab-set}
---
class: tabs-parts
---
```{tab-item} a
Hvor mange elever valgte fransk som fremmedspråk? 


:::{admonition} Fasit
---
class: dropdown, answer
---
$180$ elever.
:::
```

```{tab-item} b
Av elevene som valgte fransk som fremmedspråk, valgte $70 \%$ av dem fransk II. 

Hvor mange elever valgte fransk II?

:::{admonition} Fasit
---
class: dropdown, answer
---
$126$ elever.
:::
```
````

::::

---


:::::{admonition} Oppgave 2
---
class: problem-level-1
---

`````{tab-set}
---
class: tabs-parts
---
````{tab-item} a
Prisen på en vare øker med en prosentvis endring på $40 \%$.

Bestem vekstfaktoren. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
V = 100 \% + 40 \% = 140 \% = 1.4
$$
:::
````

````{tab-item} b
Prisen på en vare synker med prosentvis endring på $8 \%$. 

Bestem vekstfaktoren. 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
V = 100 \% - 8 \% = 92 \% = 0.92
$$
:::
````

````{tab-item} c
Prisen på en vare øker med en prosentvis endring på $20 \%$ og deretter synker med en prosentvis endring på $10 \%$.

Bestem vekstfaktoren. 

:::{admonition} Fasit
---
class: dropdown, answer
---
Endring 1
: $$
V_1 = 100 \% + 20 \% = 120 \% = 1.2
$$

Endring 2
: $$
V_2 = 100 \% - 10 \% = 90 \% = 0.9
$$

Samlet vekstfaktor
: $$
V = V_1 \cdot V_2 = 1.2 \cdot 0.9 = 1.08
$$
:::
````

````{tab-item} d
Prisen på en vare øker med en prosentvis endring på $20 \%$ og deretter øker med en prosentvis endring på $10 \%$.

Bestem vekstfaktoren. 

:::{admonition} Fasit
---
class: dropdown, answer
---
Endring 1
: $$
V_1 = 100 \% + 20 \% = 120 \% = 1.2
$$

Endring 2
: $$
V_2 = 100 \% + 10 \% = 110 \% = 1.1
$$

Samlet vekstfaktor
: $$
V = V_1 \cdot V_2 = 1.2 \cdot 1.1 = 1.32
$$
:::
````

`````

:::::

---

:::::{admonition} Oppgave 3
---
class: problem-level-1
---
I en butikk kostet en vare $600 \, \mathrm{kr}$ før en prisøkning på $20 \%$. 

````{tab-set}
---
class: tabs-parts
---
```{tab-item} a
Hvor mye kostet var etter prisøkningen? 

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
720 \, \mathrm{kr}
$$
:::
```

```{tab-item} b
Varen ble deretter satt ned med $10 \%$. 

Hvor mye kostet varen etter prisnedsettelsen? 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
648 \, \mathrm{kr}
$$
:::
```

```{tab-item} c
Til slutt satt butikken opp varen med $10 \%$ igjen. 

Hvor mye kostet varen til slutt? 

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
712.8 \ \mathrm{kr}
$$
:::
```
````

:::::

---

:::::{admonition} Oppgave 4
---
class: problem-level-2
---
Et år ble antall brukere av en mobilapp redusert med $50 \%$. På dette tidspunktet var det $100 \, 000$ brukere igjen.

Utviklerne av appen bestemte seg for å utføre en reklamekampanse for å øke antall brukere igjen, som ledet til en $50 \%$ økning. 

`````{tab-set}
---
class: tabs-parts
---
````{tab-item} a
Hvor mange brukere var det *etter* økningen?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
150 \, 000
$$
:::
````

````{tab-item} b
Hvor mange brukere var det *før* reduksjonen?

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
200 \, 000
$$
:::
````
`````
:::::

---


:::::{admonition} Oppgave 5
---
class: problem-level-2
---
Rabattmodellen som Ruter brukte for enkeltbilletter i Oslo opptil svært nylig er grafisk representert i {numref}`fig-percentage-fundamentals-exercise-5`.

Prisen på en enkeltbillett for voksen *uten* rabatt er $42 \, \mathrm{kr}$.

:::{figure} ./figures/exercises/exercise_5.svg
---
name: fig-percentage-fundamentals-exercise-5
width: 80%
---
viser en oversikt over rabattmodellen til Ruter hadde rett før en nylig endring som ble vedtatt for kjøp av enkeltbilletter. 
:::


````{tab-set}
---
class: tabs-parts
---

```{tab-item} a
Hvor mye må du betale for din femte enkeltbillett etter rabattmodellen?

:::{admonition} Fasit
---
class: dropdown, answer
---
$$
37.8 \, \mathrm{kr}
$$
:::
```

```{tab-item} b
Omtrent hvor mange billetter må du kjøpe før billettprisen blir mindre enn $30 \, \mathrm{kr}$?

:::{admonition} Fasit
---
class: dropdown, answer
---
Mellom 17 og 20 billetter.
:::
```


````

:::::

---

:::::{admonition} Oppgave 6
---
class: problem-level-3
---

En elev jobber med en oppgave. 

::::{admonition} Oppgaven
---
class: check
---
En bakteriepopulasjon starter med én bakterie. Hver time dobler populasjonen seg. 

Lag et program som modellerer veksten til bakteriepopulasjonen per time.
::::

Eleven har skrevet et program for å bestemme svaret.

````{tab-set}
---
class: tabs-parts
---
```{tab-item} a
Les programmet under og forutsi hva programmet skriver ut.

Skriv inn hypotesen din og sjekk svaret ditt! 
```

```{tab-item} b
Endre på programmet slik at det finner antall bakterier etter 10 timer.

Kjør programmet og sjekk hvor mange bakterier det blir.

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{code-block} python
---
linenos: true
---
antall_bakterier = 1
vekstfaktor = 2

antall_timer = 10
for i in range(antall_timer):
    antall_bakterier = antall_bakterier * vekstfaktor

print(antall_bakterier)
:::
som gir utskriften
:::{code-block} console
1024
:::

som betyr at det er 1024 bakterier etter 10 timer.
::::
:::
```

```{tab-item} c
Etter 10 timer har gått, senkes den prosentvise økningen av bakteriepopulasjonen til $20 \%$ per time. 

Juster programmet og bruk det til å beregne hvor mange bakterier det er etter 20 timer.

::::{admonition} Fasit
---
class: dropdown, answer
---
:::{code-block} python
---
linenos: true
---
# NOTE: 10 første timer
antall_bakterier = 1
vekstfaktor = 2
antall_timer = 10
for i in range(antall_timer):
    antall_bakterier = antall_bakterier * vekstfaktor
    
# NOTE: de 10 neste timene    
antall_timer = 10
vekstfaktor = 1.2
for i in range(antall_timer):
    antall_bakterier = antall_bakterier * vekstfaktor
    
print(antall_bakterier)
::: 
som gir utskriften
:::{code-block} console
6340.338096537599
:::
som betyr at det er ca. 6340 bakterier etter 20 timer.
::::
```
````

:::{raw} html
---
file: ./interactive_code/exercise_6.html
---
:::

:::::

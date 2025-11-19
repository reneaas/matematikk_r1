# Oppgaver: Størst og minst vekst



:::::::::::::::{exercise} Oppgave 1
Nedenfor vises en figurer der 
* Én graf viser grafen til $f$ 
* Én graf viser grafen til $f'$
* Én graf viser grafen til $f''$

Avgjør hvilken graf som viser $f$ og $f'$ og $f''$. 



:::{multi-plot}
width: 100%
functions: x*exp(-x), exp(-x) - x*exp(-x), -2*exp(-x) + x*exp(-x) 
function-names: A, B, C
rows: 1
cols: 3
xmin: -1
xmax: 5
ymin: -1
ymax: 1
ticks: off
:::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2
Nedenfor vises en figurer der 
* Én graf viser grafen til $f$ 
* Én graf viser grafen til $f'$
* Én graf viser grafen til $f''$

Avgjør hvilken graf som viser $f$ og $f'$ og $f''$. 


:::{multi-plot}
width: 100%
functions: (x**2 - 1) * exp(-x), 2*x*exp(-x) - (x**2 - 1) * exp(-x), (2 - 4*x) * exp(-x) - 2*x*exp(-x)
function-names: A, B, C
rows: 1
cols: 3
xmin: -2
xmax: 5
ymin: -2
ymax: 2
ticks: off
:::


:::::::::::::::

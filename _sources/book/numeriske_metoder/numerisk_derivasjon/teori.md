# Numerisk derivasjon

:::{admonition} Læringsmål
---
class: tip
---
* Kunne forklare Newtons fremover-kvotient, Newtons bakover-kvotient og Newtons symmetriske kvotient og bruke dem til å finne tilnærmede verdier for deriverte.
:::



::::{margin}
:::{figure} ./figurer/dumbledore.png
---
class: no-click
width: 100%
---
:::
::::

Selv om alle deriverbare funksjoner i prinsippet kan deriveres hvis vi følger derivasjonsreglene til *punkt og prikke*, så kan det bli fryktelig knotete å derivere noen funksjoner. For eksempel vil det være et mildt mareritt å derivere funksjonen

$$
f(x) = \dfrac{\sqrt{\log_5 x} \cdot e^{\sqrt{x}} \cdot \sqrt{\ln (x^2 + 1)} + (x^2 + 1) }{\sqrt{x^2 - 3x + 2} + \ln x}
$$

Vi er jo ikke nødvendigvis interessert i hva uttrykket til $f'(x)$ *er*. I stedet er vi kanskje interessert i hvor $f'(x) = 0$ eller hvor $f'(x)$ er positiv eller negativ. For å angripe funksjoner som dette, kan vi derivere dem **numerisk**. 


## Hva er numerisk derivasjon?

Numerisk derivasjon går ut på å finne **tilnærmede verdier** for den deriverte. Det at vi kaller det for **numerisk** derivasjon kommer fra at vi bruker tallverdier – **numeriske verdier** – for å finne en numerisk verdi til den deriverte i bestemt punkt $x$. For å lage oss meningsfulle fremgangsmåter for å gjøre dette, skal vi ta utgangspunkt i **definisjonen** av den deriverte:

$$
f'(x) = \lim_{h \to 0} \dfrac{f(x + h) - f(x)}{h}
$$

For at den deriverte skal eksistere, må grenseverdien **ovenfra** og **nedenfra** være like som gir oss utgangspunktet for de to første strategiene vi skal se på.



## Newtons fremover-kvotient
Definisjonen av den deriverte når vi tar grenseverdien **ovenfra** vil gi oss at

$$
f'(x) = \lim_{h \to 0^+} \dfrac{f(x + h) - f(x)}{h}
$$

Men på en datamaskin er det ikke mulig å la $h \to 0$ i en teoretisk forstand slik vi kan gjøre i matematikken ved å "tenke oss" at $h$ nærmer seg null, men likevel kommer aldri helt fram til null. I stedet velger vi oss et lite tall $h$ som er nesten lik null, og så anser vi det som er *grei nok* tilnærming til å la $h \to 0$. 

$$
f'(x) \approx \dfrac{f(x + h) - f(x)}{h}
$$

der $h$ er et *lite* positivt tall som angir avstanden mellom $x$ og $x + h$. Denne fremgangsmåten kalles for **Newtons fremover-kvotient**. 

Rent geometrisk kan vi tolke dette som at vi finner stigningstallet til en sekant som går gjennom punktene $(x, f(x))$ og $(x + h, f(x + h))$ på grafen til $f$. Se figuren nedenfor.


:::{plot}
width: 70%
function: (x**2 - 1) / exp(x), (-1, 4), f
ymax: 1
ymin: -1.5
xmin: -2
xmax: 5
ticks: off
tangent: (0.5, f(0.5)), dashed, red
point: (0.5, f(0.5))
nocache:
:::




## Newtons bakover-kvotient

## Newtons symmetriske kvotient

## Bestemme andrederiverte numeriske


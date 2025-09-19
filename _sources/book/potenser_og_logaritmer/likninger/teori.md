# Logaritmelikninger og eksponentiallikninger

> Merk at i alle typene likninger nedenfor, så vil hvilken som helst logaritme funke. Vi bruker ofte den naturlige logaritmen $\ln(x)$ eller den 10-logaritmen $\lg(x)$ i eksemplene, men de samme strategiene funker uansett hvilken logaritme vi bruker.

## Logaritmelikninger


### Type 1: $\ln a = \ln b$ eller $\ln a = b$.

:::::::::::::::{example} Eksempel 1
Løs likningen $\ln(2x) = \ln(3x - 5)$.

::::{solution}
---
dropdown: 0
---
$$
\ln (2x) = \ln (3x - 5)
$$

$$
2x = 3x - 5
$$

$$
-x = -5
$$


$$
x = 5.
$$
::::

:::::::::::::::


---


:::::::::::::::{example} Eksempel 2
Løs likningen

$$
\lg (4x + 36) = 2
$$

::::{solution}
---
dropdown: 0
---
$$
\lg (4x + 36) = 2
$$

$$
4x + 36 = 10^2
$$

$$
4x = 100 - 36
$$

$$
4x = 64
$$

$$
x = 16.
$$
::::

:::::::::::::::





### Type 2: $\lg f(x) \pm \lg g(x) = k$

:::::::::::::::{summary} Strategi for likninger på formen $\lg f(x) \pm \lg g(x) = k$
1. Bruk logaritmesetningene til å skrive om venstresiden til **én logaritme** $\lg p(x)$.
2. Bruk at $\lg p(x) = k \iff p(x) = 10^{k}$ til å skrive om likningen til en **eksponentiallikning**

:::::::::::::::


:::::::::::::::{example} Eksempel 3
Løs likningen

$$
\lg x^2 + 3 \lg x^2 + \lg \dfrac{1}{x^4} = 8
$$

::::{solution}
---
dropdown: 0
---
Vi bruker logaritmesetningene til å skrive om venstresiden til én logaritme:

$$
\lg x^2 + 2 \lg x^3 + \lg \dfrac{1}{x^4} = 8
$$

$$
2 \lg x + 2 \cdot 3 \lg x + \lg x^{-4} = 8
$$

$$
2 \lg x + 6 \lg x - 4\lg x = 8
$$

$$
4 \lg x = 8
$$

$$
\lg x = 2
$$

$$
x = 10^2 = 100
$$

Siden opprinnelige likningen inneholder en logaritme der vi bruker en potens av $x$ som er opphøyd i et oddetall, så vil ikke noen negative løsninger være gyldige. Dermed vil den eneste mulige løsningen være

$$
x = 100
$$

> Hvis derimot en likning bare inneholdt logaritmen til potenser av $x^2$, $x^4$, $x^6$, så en negativ løsning og være gyldig. Hvis løsningen da var $x = 100$, så ville $x = -100$ og $x = 100$ være gyldige løsninger siden både $(-100)^2$, $(-100)^4$, $(-100)^6$ og så videre er positive tall. 
::::
:::::::::::::::


---


:::::::::::::::{example} Eksempel 4 
Løs likningen 

$$
\lg x + \lg (x - 3) = 1
$$

::::{solution}
---
dropdown: 0
---
Vi samler venstresiden som én logaritme:

$$
\lg x + \lg (x - 3) = 1
$$

$$
\lg (x(x - 3)) = 1
$$

Så bruker vi at $\lg p(x) = k \iff p(x) = 10^{k}$:

$$
x(x - 3) = 10^1
$$

$$
x^2 - 3x - 10 = 0
$$

$$
x = \dfrac{3 \pm \sqrt{3^2 + 4 \cdot 10}}{2} = \dfrac{3 \pm \sqrt{49}}{2} = \dfrac{3 \pm 7}{2}
$$

$$
x = 5 \or x = -2
$$

Vi må sjekke at løsningene er gyldige. Vi ser at med $x = -2$, så vil den opprinnelige likningen inneholde $\lg(-2)$, som ikke er definert. Dermed er $x = -2$ ikke en gyldig løsning. Med $x = 5$ er begge logaritmene i den opprinnelige likningen definert, så dette er en gyldig løsning. Dermed er den eneste løsningen:

$$
x = 5.
$$

::::

:::::::::::::::


### Type 3: $a(\log_m x)^2 + b \log_m x + c = 0$


:::::::::::::::{summary} Strategi for likninger på formen $a(\log_m x)^2 + b \log_m x + c = 0$
1. Gjør et variabelskifte $u = \log_m x$.
2. Skriv om likningen til en andregradslikning på formen $au^2 + bu + c = 0$.
3. Løs andregradslikningen for $u$.
4. Bruk at $u = \log_m x \iff x = m^u$ til å finne $x$.
:::::::::::::::


:::::::::::::::{example} Eksempel 5
Løs likningen

$$
(\ln x)^2 - 5 \ln x + 6 = 0
$$


::::{solution}
---
dropdown: 0
---
Vi setter $u = \ln x$. Da kan vi skrive om likningen slik:

$$
(\ln x)^2 - 5 \ln x + 6 = 0
$$

$$
u^2 - 5u + 6 = 0
$$

Så bruker vi $abc$-formelen til å løse andregradslikningen for $u$:

$$
u = \dfrac{5 \pm \sqrt{(-5)^2 - 4 \cdot 1 \cdot 6}}{2 \cdot 1} = \dfrac{5 \pm \sqrt{25 - 24}}{2} = \dfrac{5 \pm 1}{2}
$$

$$
u = 3 \or u = 2
$$

Nå bruker vi at $u = \ln x \iff x = e^u$ til å finne $x$:

$$
\ln x = 3 \or \ln x = 2
$$

$$
x = e^3 \or x = e^2
$$
::::

:::::::::::::::




## Eksponentiallikninger


### Type 1: $a^{f(x)} = k$


:::::::::::::::{summary} Strategi for likninger på formen $a^{f(x)} = k$
1. Bruk en valgfri logaritme på hver side av likningen – velg gjerne den naturlige logaritmen $\ln (x)$
2. Løs likningen for $x$.
:::::::::::::::


:::::::::::::::{example} Eksempel 6
Løs likningen

$$
2^x = 7
$$

::::{solution}
---
dropdown: 0
---
Vi bruker den naturlige logaritmen på hver side av likningen:

$$
\ln(2^x) = \ln(7)
$$

$$
x \cdot \ln(2) = \ln(7)
$$

$$
x = \dfrac{\ln(7)}{\ln(2)}
$$

::::

:::::::::::::::



### Type 2: $a^{f(x)} = b^{g(x)}$

:::::::::::::::{summary} Strategi for likninger på formen $a^{f(x)} = b^{g(x)}$
1. Bruk en valgfri logaritme på hver side av likningen – velg gjerne den naturlige logaritmen $\ln (x)$
2. Løs likningen for $x$.
:::::::::::::::


---



:::::::::::::::{example} Eksempel 7
Løs likningen

$$
3 \cdot 5^x = 7 \cdot 2^x
$$

::::{solution}
---
dropdown: 0
---
Vi bruker den naturlige logaritmen på hver side av likningen:

$$
\ln (3 \cdot 5^x) = \ln (7 \cdot 2^x)
$$

$$
\ln 3 + \ln (5^x) = \ln 7 + \ln (2^x)
$$

$$
\ln 3 + x \ln 5 = \ln 7 + x \ln 2
$$

$$
x \ln 5 - x \ln 2 = \ln 7 - \ln 3
$$

$$
x (\ln 5 - \ln 2) = \ln 7 - \ln 3
$$

$$
x \cdot \ln \left(\dfrac{5}{2}\right) = \ln \left(\dfrac{7}{3}\right)
$$

$$
x = \dfrac{\ln \left(\dfrac{7}{3}\right)}{\ln \left(\dfrac{5}{2}\right)}
$$

Eventuelt kan vi skrive svaret som

$$
x = \dfrac{\ln 7 - \ln 3}{\ln 5 - \ln 2}
$$

Spiller ingen rolle hvilket av de to svarene vi velger.

::::

:::::::::::::::


### Type 3: $a \cdot (k^x)^2 + b \cdot k^x + c = 0$


:::::::::::::::{summary} Strategi for likninger på formen $a \cdot (k^x)^2 + b \cdot k^x + c = 0$

1. Sett $u = k^x$.
2. Skriv om likningen til en andregradslikning på formen $au^2 + bu + c = 0$.
3. Løs andregradslikningen for $u$.
4. Bruk at $u = k^x \iff x = \log_k u$ til å finne $x$. 

:::::::::::::::


---


:::::::::::::::{example} Eksempel 8
Løs likningen

$$
10^{2x} - 5 \cdot 10^x + 6 = 0
$$

::::{solution}
---
dropdown: 0
---
Vi setter $u = 10^x$. Da kan vi skrive om likningen slik:

$$
u^2 - 5u + 6 = 0
$$

Så bruker vi $abc$-formelen til å løse andregradslikningen for $u$:

$$
u = \dfrac{5 \pm \sqrt{(-5)^2 - 4 \cdot 1 \cdot 6}}{2 \cdot 1} = \dfrac{5 \pm \sqrt{25 - 24}}{2} = \dfrac{5 \pm 1}{2}
$$

$$
u = 3 \or u = 2
$$

Nå bruker vi at $u = 10^x \iff x = \lg u$ til å finne $x$:

$$
10^x = 3 \or 10^x = 2
$$

$$
x = \lg 3 \or x = \lg 2
$$
::::


:::::::::::::::


---


:::::::::::::::{example} Eksempel 9
Løs likningen

$$
e^x - 2 = 8e^{-x}
$$

::::{solution}
---
dropdown: 0
---
Vi må skrive om likningen slik at det blir en andregradslikning i $e^x$. Vi ganger begge sider av likningen med $e^x$:

$$
e^x \cdot e^x - 2 \cdot e^x = 8e^{-x} \cdot e^x
$$

$$
e^{2x} - 2e^x = 8
$$

$$
e^{2x} - 2e^x - 8 = 0
$$

Så gjør vi et variabelskifte $u = e^x$ som gir likningen

$$
u^2 - 2u - 8 = 0
$$

Nå bruker vi $abc$-formelen til å løse andregradslikningen for $u$:

$$
u = \dfrac{2 \pm \sqrt{(-2)^2 - 4 \cdot 1 \cdot (-8)}}{2 \cdot 1} = \dfrac{2 \pm \sqrt{4 + 32}}{2} = \dfrac{2 \pm \sqrt{36}}{2}
$$

$$
u = \dfrac{2 \pm 6}{2}
$$

$$
u = 4 \or u = -2
$$

Så setter vi tilbake definisjonen av $u$:

$$
e^x = 4 \or e^x = -2
$$

Likningen $e^x = -2$ har ingen løsningen siden vi ikke kan opphøye $e$ med noe som gir oss et negativt tall. Dermed er det bare $e^x = 4$ som gir en løsning:

$$
e^x = 4
$$

$$
\ln e^x = \ln 4
$$

$$
x \cdot \ln e = \ln 4
$$

$$
x = \ln 4
$$

der vi har brukt at $\ln e = 1$. 
::::

:::::::::::::::




## Generell strategi: Produktregelen


:::::::::::::::{summary} Strategi: $f(x) \cdot g(x) = 0$
Bruk produktregelen for likninger. Hvis $a \cdot b = 0$, så er enten $a = 0$ eller $b = 0$. Dermed er

$$
f(x) \cdot g(x) = 0 \liff f(x) = 0 \or g(x) = 0.
$$


Løs hver av de to likningene for seg.


:::::::::::::::


:::::::::::::::{example} Eksempel 10
Løs likningen

$$
\lg (x - 2) \cdot (\lg x - 2) = 0
$$

::::{solution}
---
dropdown: 0
---
Vi bruker produktregelen for likninger:

$$
\lg (x - 2) \cdot (\lg x - 2) = 0
$$

$$
\lg (x - 2) = 0 \or \lg (x) - 2 = 0
$$

$$
\lg (x - 2) = 0 \or \lg (x) = 2
$$

$$
x - 2 = 10^0 \or x = 10^2
$$

$$
x - 2 = 1 \or x = 100
$$

$$
x = 3 \or x = 100
$$
::::

:::::::::::::::


---


:::::::::::::::{example} Eksempel 11
Løs likningen

$$
(e^x - 3)(e^x + 4) = 0
$$

::::{solution}
---
dropdown: 0
---
Vi bruker produktregelen for likninger:


$$
(e^x - 3)(e^x + 4) = 0
$$

$$
e^x - 3 = 0 \or e^x + 4 = 0
$$

$$
e^x = 3 \or e^x = -4
$$

Likningen $e^x = -4$ har ingen løsning siden vi ikke kan opphøye $e$ med noe som gir oss et negativt tall. Dermed er det bare $e^x = 3$ som gir en løsning:

$$
e^x = 3
$$

$$
\ln e^x = \ln 3
$$

$$
x \cdot \ln e = \ln 3
$$

$$
x = \ln 3
$$

der vi har brukt at $\ln e = 1$.
::::

:::::::::::::::
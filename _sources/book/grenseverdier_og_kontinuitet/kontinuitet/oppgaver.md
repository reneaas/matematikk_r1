# Kontinuitet

:::::::::::::::{exercise} Oppgave 1
En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    x + 2 \qfor x < 1 \\
    \\
    2x + b \qfor 1 \leq x < 3 \\
\end{cases}
$$

Bestem $b$ slik at $f$ er kontinuerlig i $x = 1$. 


::::{answer}
$$
b = 1
$$
::::

::::{solution}
For at $f$ skal være kontinuerlig i $x = 1$, må

$$
\lim_{x\to 1^-} f(x) = \lim_{x\to 1^+} f(x) = f(1)
$$

Vi har at

$$
\lim_{x\to 1^-} f(x) =  \lim_{x\to 1^-} x + 2 = 1 + 2 = 3
$$

Videre er

$$
\lim_{x\to 1^+} f(x) = \lim_{x\to 1^+} 2x + b = 2\cdot 1 + b = 2 + b
$$

Hvis vi regner ut $f(1)$ ved å bruke forskriften som er gyldig når $x = 1$ får vi:

$$
f(1) = 2\cdot 1 + b = 2 + b
$$

Altså må 

$$
2 + b = 3 \liff b = 3 - 2 = 1
$$

Dermed er $f$ kontinuerlig i $x = 1$ hvis $b = 1$.

::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 2
En funksjon $f$ er gitt ved 

$$
f(x) = 
\begin{cases}
    x^2 - 4 \qfor x < 2 \\
    \\
    ax + 3 \qfor x \geq 2 \\
\end{cases}
$$

Bestem $a$ slik at $f$ er kontinuerlig i $x = 2$.

::::{answer}
$$
a = -\dfrac{3}{2}
$$
::::


::::{solution}
For at $f$ skal være kontinuerlig i $x = 2$, må

$$
\lim_{x\to 2^-} f(x) = \lim_{x\to 2^+} f(x) = f(2)
$$

Funksjonen er definert i $x = 2$, og vil da ha funksjonsverdien

$$
f(2) = a\cdot 2 + 3 = 2a + 3.
$$

Videre har vi at grenseverdiene er gitt ved

$$
\lim_{x\to 2^-} f(x) = \lim_{x\to 2^-} x^2 - 4 = 2^2 - 4 = 0
$$

og 

$$
\lim_{x\to 2^+} f(x) = \lim_{x\to 2^+} ax + 3 = 2a + 3
$$

Dermed må 

$$
2a + 3 = 0 \liff 2a = -3 \liff a = -\dfrac{3}{2}
$$

Altså er $f$ kontinuerlig i $x = 2$ hvis $a = -\dfrac{3}{2}$.
::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 3
En funksjon $f$ er gitt ved 

$$
f(x) = 
\begin{cases}
    x^2 + 1, \quad x < 2 \\
    \\
    x - t, \quad x \geq 2
\end{cases}
$$

Bestem $t$ slik at $f$ er kontinuerlig i $x = 2$.


::::{answer}
$$
t = -3
$$
::::


::::{solution}
For at $f$ skal være kontinuerlig i $x = 2$ må 

$$
\lim_{x\to 2^-} f(x) = \lim_{x\to 2^+} f(x) = f(2)
$$

Først sjekker vi om $f(2)$ eksisterer. Det gjør den siden $x = 2$ er med i definisjonsmengden til $f$: 

$$
f(2) = 2 - t
$$

Deretter regner vi ut grenseverdiene:

$$
\lim_{x\to 2^-} f(x) = \lim_{x\to 2^-} x^2 + 1 = 2^2 + 1 = 5
$$

og 

$$
\lim_{x\to 2^+} f(x) = \lim_{x\to 2^+} x - t = 2 - t
$$

Så setter vi de to grenseverdiene lik hverandre:

$$
5 = 2 - t \liff t = 2 - 5 = -3
$$

Dermed er $f$ kontinuerlig i $x = 2$ hvis $t = -3$.
::::


:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 4
En funksjon $f$ er gitt ved 

$$
f(x) = 
\begin{cases}
    x^2 + a \qfor x \leq a \\
    \\
    ax + 2 \qfor x > a \\
\end{cases}
$$

Bestem $a$ slik at $f$ er kontinuerlig (overalt!).


::::{answer}
$$
a = 2.
$$
::::


::::{solution}
Vi har at $f$ i utgangspunktet er kontinuerlig overalt bortsett fra muligens i $x = a$. For at $f$ skal være kontinuerlig i dette punktet, må 

$$
\lim_{x\to a^-} f(x) = \lim_{x\to a^+} f(x) = f(a)
$$

Først bestemmer vi $f(a)$ som gir

$$
f(a) = a^2 + a
$$

Deretter regner vi ut de to grenseverdiene:

$$
\lim_{x\to a^-} f(x) = \lim_{x\to a^-} x^2 + a = a^2 + a
$$

og 

$$
\lim_{x\to a^+} f(x) = \lim_{x\to a^+}  ax + 2 = a^2 + 2
$$

Setter vi de to grenseverdiene lik hverandre, får vi

$$
a^2 + a = a^2 + 2 \liff a = 2
$$

Dermed er $f$ kontinuerlig hvis $a = 2$.

::::

:::::::::::::::

---


:::::::::::::::{exercise} Oppgave 5
En funksjon $f$ er gitt ved

$$
f(x) = 
\begin{cases}
    x, \quad 0 \leq x \leq 2 \\
    \\
    5 - x, \quad 2 < x \leq 5 \\
\end{cases}
$$

Nedenfor vises noen påstander.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør om påstanden nedenfor stemmer.

> $f$ er kontinuerlig i $x = 2$.


::::{answer}
$f$ er ikke kontinuerlig i $x = 2$.
::::

::::{solution}
For at $f$ skal være kontinuerlig i $x = 2$ må $f(2)$ eksistere og 

$$
\lim_{x\to 2^-} f(x) = \lim_{x\to 2^+} f(x) = f(2)
$$

Vi regner først ut $f(2)$ siden $x = 2$ er i definisjonsmengden til $f$:

$$
f(2) = 2
$$

Deretter bestemmer vi de to grenseverdiene:

$$
\lim_{x\to 2^-} f(x) = \lim_{x\to 2^-} x = 2
$$

og

$$
\lim_{x\to 2^+} f(x) = \lim_{x\to 2^+} 5 - x = 5 - 2 = 3
$$

Siden de to grenseverdiene ikke er like, så er ikke $f$ kontinuerlig i $x = 2$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Avgjør om påstanden nedenfor stemmer.

> Hvis vi endrer definisjonsmengden til $D_f = [0, 5] \setminus \{2\}$, så er $f$ en kontinuerlig funksjon.

::::{answer}
Påstanden er sann.
::::

::::{solution}
Dersom vi fjerner $x = 2$ fra definisjonsmengden til $f$, så vil $f$ være kontinuerlig i alle punkter i definisjonsmengden sin siden hver forskrift er i seg selv kontinuerlige funksjoner og siden definisjonsmengden nå er åpne mengder (slik at det *alltid* er mulig å regne ut ensidige grenser fra hver side av alle punkter i definisjonsmengden som vil nærme seg samme verdi). Dermed er $f$ kontinuerlig hvis vi endrer definisjonsmengden til $D_f = [0, 5] \setminus \{2\}$.
::::

:::::::::::::


:::::::::::::{tab-item} c
Avgjør om påstanden nedenfor stemmer.

> Hvis vi endrer definisjonsmengden til $D_f = [0, 5] \setminus \{2\}$, så er verdimengden til $f$ uendret.


::::{answer}
Påstanden er sann.
::::

::::{solution}
Hvis vi endrer definsjonsmengden til den oppgitte mengden, så vil verdimengden fortsatt være den samme.
::::

:::::::::::::


::::::::::::::

:::::::::::::::



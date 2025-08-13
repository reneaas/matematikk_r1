# Forarbeid: Algebraisk løsning av likninger
 

## Lineære likninger

::::{admonition} Regneregler for lineære likninger
---
class: theory
---
Når vi jobber med en lineær likning, kan vi gjøre følgende på hver side av en likning:
1. Plusse på et tall.
2. Trekk fra et tall.
3. Gange med et tall.
4. Dele på et tall.
::::

---

::::{admonition} Eksempel 1
---
class: example
---
Løs likningen

$$
4x - 2 = 2x + 6. 
$$

:::{admonition} Løsning
---
class: solution
---
\begin{align*}
4x - 2 &= 2x + 6 \\
 \\
4x - 2 \textcolor{red}{-2x} &= 2x + 6 \textcolor{red}{-2x} && \text{Trekker fra $2x$ på begge sider}\\
\\
2x - 2 &= 6 \\
\\
2x - 2 \textcolor{red}{+2} &= 6 \textcolor{red}{+2} && \text{Legger til $2$ på begge sider}\\
\\
2x &= 8 \\
\\
\frac{\bcancel{2}x}{\bcancel{\textcolor{red}{2}}} &= \frac{\cancelto{\, \displaystyle 4}{8}}{\cancel{\textcolor{red}{2}}} && \text{Deler med 2 på begge sider}\\
\\
x &= 4
\end{align*}

:::
::::

**Din tur!**

::::{admonition} Underveisoppgave 1
---
class: check
---
Løs likningen

$$
x - 1 = -2x + 5.
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$x = 2$
:::

:::{admonition} Løsning
---
class: solution, dropdown
---
\begin{align*}
x - 1 &= -2x + 5 \\
\\
x - 1 \textcolor{red}{+2x} &= -2x + 5 \textcolor{red}{+2x} && \text{Legger til $2x$ på begge sider}\\
\\
3x - 1 &= 5 \\
\\
3x - 1 \textcolor{red}{+1} &= 5 \textcolor{red}{+1} && \text{Legger til $1$ på begge sider}\\
\\
3x &= 6 \\
\\
\frac{\bcancel{3}x}{\bcancel{\textcolor{red}{3}}} &= \frac{\cancelto{\, \displaystyle  2}{6}}{\cancel{\textcolor{red}{3}}} && \text{Deler med 3 på begge sider}\\
\\
x &= 2
\end{align*}
:::

::::


## Andregradslikninger

::::{admonition} Eksempel 2: likninger på formen $ax^2 + c = 0$
---
class: example
---
Løs likningen

$$
x^2 - 4 = 0
$$

:::{admonition} Løsning
---
class: solution
---
Vi skriver om likningen litt først:

\begin{align*}
x^2 - 4 &= 0 \\
\\
x^2 - 4 \textcolor{red}{+4} &= 0 \textcolor{red}{+4} && \text{Legger til 4 på begge sider}\\
\\
x^2 &= 4
\end{align*}

Dersom $x^2 = 4$, er det fristende å konkludere at 

$$
x = 2  \quad \text{siden} \quad 2^2 = 4 
$$

Men det samme ville vært sant når

$$
x = -2 \quad \text{siden} \quad (-2)^2 = 4.
$$

Altså betyr dette at løsningen av en slik likning har to verdier:

$$
x = \sqrt{4} = 2 \quad \text{eller} \quad x = -\sqrt{4} = -2.
$$

Vi skriver noen ganger dette som

$$
x = \pm 2
$$

der vi leser $\pm$ som "pluss eller minus". 
:::
::::

**Din tur!**

::::{admonition} Underveisoppgave 2
---
class: check
---
Løs likningen

$$
x^2 - 9 = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -3 \quad \text{eller} \quad x = 3
$$
:::

:::{admonition} Løsning
---
class: solution, dropdown
---
\begin{align*}
x^2 - 9 &= 0 \\
\\
x^2 - 9 \textcolor{red}{+9} &= 0 \textcolor{red}{+9} && \text{Legger til 9 på begge sider}\\
\\
x^2 &= 9
\end{align*}

Løsningen blir derfor 

$$
x = -\sqrt{9} = -3 \quad \text{eller} \quad x = \sqrt{9} = 3
$$

:::
::::

---


```{admonition} Produktregelen
---
class: theory
---
Hvis $A$ og $B$ er to tall og produktet $A\cdot B = 0$, så er enten $A = 0$ eller $B = 0$.

```


::::{admonition} Eksempel 3: likninger på formen $(x - a) (x - b) = 0$
---
class: example
---
Løs likningen

$$
(x - 1)(x + 3) = 0
$$

:::{admonition} Løsning
---
class: solution
---
Her kan vi bruke produktregelen ved å tenke på den ene faktoren som et tall $A$ og den andre faktoren som et tall $B$. Da forteller setningen oss at vi kan tolke likningen som

$$
\underbrace{(x - 1)}_{A}\cdot \underbrace{(x + 3)}_{B} = 0
$$

slik at 

$$
x - 1 = 0 \quad \text{eller} \quad x + 3 = 0
$$

Dette er bare to lineære likninger så vi kan løse hver for seg:

\begin{align*}
x - 1 &= 0 \\
\\
x - 1 \textcolor{red}{+1} &= 0 \textcolor{red}{+1} && \text{Legger til 1 på begge sider}\\
\\
x &= 1
\end{align*}

og 

\begin{align*}
x + 3 &= 0 \\
\\
x + 3 \textcolor{red}{-3} &= 0 \textcolor{red}{-3} && \text{Trekker fra 3 på begge sider}\\
\\
x &= -3
\end{align*}

Altså er løsningen

$$
x = -3 \quad \text{eller} \quad x = 1
$$
:::

::::

---

**Din tur!**

::::{admonition} Underveisoppgave 3
---
class: check
---
Løs likningen

$$
(x + 1)(x - 3) = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = -1 \quad \text{eller} \quad x = 3
$$
:::

:::{admonition} Løsning
---
class: solution, dropdown
---

Vi bruker produktregelen og får

$$
\underbrace{(x + 1)}_{A} \cdot \underbrace{(x - 3)}_{B} = 0
$$

som gir oss to lineære likninger:

$$
x + 1 = 0 \quad \text{eller} \quad x - 3 = 0
$$

som vi løser for $x$:

\begin{align*}
x + 1 &= 0 \\
\\
x + 1 \textcolor{red}{-1} &= 0 \textcolor{red}{-1} && \text{Trekker fra 1 på begge sider}\\
\\
x &= -1
\end{align*}

og

\begin{align*}
x - 3 &= 0 \\
\\
x - 3 \textcolor{red}{+3} &= 0 \textcolor{red}{+3} && \text{Legger til 3 på begge sider}\\
\\
x &= 3
\end{align*}

Altså er løsningen

$$
x = -1 \quad \text{eller} \quad x = 3
$$

:::
::::

---

::::{admonition} Eksempel 4: likninger på formen $ax^2 + bx = 0$
---
class: example
---
Løs likningen

$$
2x^2 - 4x = 0
$$

:::{admonition} Løsning
---
class: solution
---
Her kan vi merke oss at $2x$ er en felles faktor i begge leddene så vi kan trekke ut denne faktoren:

\begin{align*}
2x^2 - 4x &= 0 \\
\\
\textcolor{red}{2x} \cdot x - 2 \cdot \textcolor{red}{2x} &= 0 \\
\\
\textcolor{red}{2x}(x - 2) &= 0 && \text{Faktoriserte ut $2x$ fra begge ledd.}
\end{align*} 


Nå har vi produktet av to tall igjen, som vi kan se ved å tenke på venstre side av likningen som et tall $A$ og et tall $B$ ganget sammen:

$$
\underbrace{2x}_{A} \cdot \underbrace{(x - 2)}_{B} = 0
$$

Dette gir oss to lineære likninger:

$$
2x = 0 \quad \text{eller} \quad x - 2 = 0
$$

som vi kan løse for $x$:

\begin{align*}
2x &= 0 \\
\\
\frac{\bcancel{2}x}{\bcancel{2}} &= \frac{0}{2} && \text{Deler med 2 på begge sider}\\
\\
x &= 0
\end{align*}

og

\begin{align*}
x - 2 &= 0 \\
\\
x - 2 \textcolor{red}{+2} &= 0 \textcolor{red}{+2} && \text{Legger til 2 på begge sider}\\
\\
x &= 2
\end{align*}

Altså er løsningen

$$
x = 0 \quad \text{eller} \quad x = 2
$$


:::
::::

---

**Din tur!**

::::{admonition} Underveisoppgave 4
---
class: check
---

Løs likningen

$$
3x^2 + 6x = 0
$$

:::{admonition} Fasit
---
class: answer, dropdown
---
$$
x = 0 \quad \text{eller} \quad x = -2
$$
:::

:::{admonition} Løsning
---
class: solution, dropdown
---

Først starter med å faktorisere ut en felles faktor med $x$ i seg:

\begin{align*}
3x^2 + 6x &= 0 \\
\\
\textcolor{red}{3x} \cdot x + 2 \cdot \textcolor{red}{3x} &= 0 \\
\\
\textcolor{red}{3x}(x + 2) &= 0 && \text{Faktoriserte ut $3x$ fra begge ledd.}
\end{align*}

Nå har vi produktet av to tall igjen, som vi kan se ved å tenke på venstre side av likningen som et tall $A$ og et tall $B$ ganget sammen:

$$
\underbrace{3x}_{A} \cdot \underbrace{(x + 2)}_{B} = 0
$$

Dette gir oss to lineære likninger:

$$
3x = 0 \quad \text{eller} \quad x + 2 = 0
$$

som vi kan løse for $x$:

\begin{align*}
3x &= 0 \\
\\
\frac{\bcancel{3}x}{\bcancel{3}} &= \frac{0}{3} && \text{Deler med 3 på begge sider}\\
\\
x &= 0
\end{align*}

og

\begin{align*}
x + 2 &= 0 \\
\\
x + 2 \textcolor{red}{-2} &= 0 \textcolor{red}{-2} && \text{Legger til 2 på begge sider}\\
\\
x &= -2
\end{align*}

Altså er løsningen

$$
x = 0 \quad \text{eller} \quad x = -2
$$

:::
::::




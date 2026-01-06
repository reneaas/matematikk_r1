# Jeopardy: Vektorregning

> Oppgaver der hjelpemidler er ment til å brukes, så er det er CAS-vindu tilgjengelig.

::::::::{jeopardy-2}


:::::::{jeopardy-question}
---
category: Vektorer i geometri
points: 100
---
Hvor mange vektorer i koordinatsystemet nedenfor er like?


:::{plot}
width: 70%
vector: (0, 0), 2, 1, blue
vector: (-3, 2), 2, 1, blue
vector: (1, 1), -4, 2, blue
vector: (3, 1), 1, 2, blue 
vector: (2, 3), -4, 2, blue
vector: (0, -2), 3, 1, blue
:::




:::::::


:::::::{jeopardy-answer}
---
category: Vektorer i geometri
points: 100
---
Fire vektorer er like. 
:::::::



:::::::{jeopardy-question}
---
category: Vektorer i geometri
points: 200
---
En vektor $\vec{a}$ er gitt ved

$$
\vec{a} = [1, -2]
$$

Bestem $|\vec{a}|$.
:::::::

:::::::{jeopardy-answer}
---
category: Vektorer i geometri
points: 200
---
$$
|\vec{a}| = \sqrt{5}
$$
:::::::


:::::::{jeopardy-question}
---
category: Vektorer i geometri
points: 300
---
To vektorer $\vec{a}$ og $\vec{b}$ er gitt ved

$$
\vec{a} = [3, 4] \quad \mathrm{og} \quad \vec{b} = [k, 8]
$$

Bestem $k$ slik at $\vec{a} \parallel \vec{b}$.
:::::::


:::::::{jeopardy-answer}
---
category: Vektorer i geometri
points: 300
---
$$
k = 6
$$
:::::::


:::::::{jeopardy-question}
---
category: Vektorer i geometri
points: 400
---
For en vektor $\vec{a}$ er $|\vec{a}| = 4$.

En annen vektor $\vec{b}$ er gitt ved

$$
\vec{b} = -3\vec{a}
$$

Bestem $|\vec{b}|$.


:::::::


:::::::{jeopardy-answer}
---
category: Vektorer i geometri
points: 400
---
$$
|\vec{b}| = 12
$$
:::::::




:::::::{jeopardy-question}
---
category: Vektorer i koordinatsystemet
points: 100
---
Bestem $\overrightarrow{AB}$ mellom punktene vist i figuren nedenfor.

:::{plot}
width: 60%
point: (1, 2)
point: (2, 4)
vector: (1, 2), (2, 4), blue
text: 1, 2, "$A$", bottom-left
text: 2, 4, "$B$", top-right
text: 0.5 * (1 + 2), 0.5 * (2 + 4), "$\overrightarrow{AB}$", bottom-right
fontsize: 25
xmin: -2
ymin: -2
nocache:
:::




:::::::

:::::::{jeopardy-answer}
---
category: Vektorer i koordinatsystemet
points: 100
---
$$
\overrightarrow{AB} = [1, 2]
$$
:::::::




:::::::{jeopardy-question}
---
category: Skalarproduktet
points: 100
---
To vektorer er gitt ved 

$$
\vec{a} = [-2, 1] \quad \mathrm{og} \quad \vec{b} = [4, 3]
$$

Bestem $\vec{a} \cdot \vec{b}$.
:::::::


:::::::{jeopardy-answer}
---
category: Skalarproduktet
points: 100
---
$$
\vec{a} \cdot \vec{b} = -5
$$
:::::::



:::::::{jeopardy-question}
---
category: Skalarproduktet
points: 200
---

Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

- $|\vec{a}| = 5$
- $|\vec{b}| = 4$
- $\cos \varphi = \dfrac{1}{2}$ der $\varphi$ er vinkelen mellom vektorene.

Bestem $\vec{a} \cdot \vec{b}$.

:::::::


:::::::{jeopardy-answer}
---
category: Skalarproduktet
points: 200 
---
$$
\vec{a} \cdot \vec{b} = 10
$$
:::::::



:::::::{jeopardy-question}
---
category: Skalarproduktet
points: 300
---

:::{cas-popup}
:::




To vektorer er gitt ved 

$$
\vec{a} = [1, 2] \quad \mathrm{og} \quad \vec{b} = [-4, 3]
$$

Bestem vinkelen mellom vektorene $\vec{a}$ og $\vec{b}$.

:::::::


:::::::{jeopardy-answer}
---
category: Skalarproduktet
points: 300
---
$$
\varphi \approx 79.7^\circ
$$
:::::::



:::::::{jeopardy-question}
---
category: Skalarproduktet
points: 400
---
Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $|\vec{a}| = 3$
* $|\vec{b}| = 2$
* $\vec{a} \cdot \vec{b} = -2$

To andre vektorer er gitt ved 

$$
\vec{p} = 4\vec{a} - \vec{b} \quad \mathrm{og} \quad \vec{q} = \vec{a} + 3\vec{b}
$$

Bestem $\vec{p} \cdot \vec{q}$.

:::::::




:::::::{jeopardy-question}
---
category: Linjer
points: 100
---
Om en linje $\ell$ får du vite at

* Punktet $A(1, 0)$ ligger på linja.
* Linja har retningsvektor $\vec{v} = [2, 3]$.

Bestem en parameterframstilling for linja $\ell$.
:::::::


:::::::{jeopardy-answer}
---
category: Linjer
points: 100
---
$$
\vec{r}(t) = [1 + 2t, 3t] \quad \mathrm{eller} \quad \ell : \begin{cases} x = 1 + 2t \\ \\ y = 3t \end{cases}
$$
:::::::



:::::::{jeopardy-question}
---
category: Linjer
points: 200
---
En linje $\ell$ går gjennom punktene $A(2, 1)$ og $B(4, 5)$.

Bestem en retningsvektor til linja.
:::::::


:::::::{jeopardy-answer}
---
category: Linjer
points: 200
---
En retningsvektor for linja til være alle vektorer som er parallelle med:

$$
\vec{v} = [2, 4]
$$

:::::::


:::::::{jeopardy-question}
---
category: Linjer
points: 300
---
En linje $\ell$ er beskrevet av parameterframstillingen

$$
\vec{r}(t) = [3 + t, 2 - 2t]
$$

Bestem retningsvektoren til linja.
:::::::


:::::::{jeopardy-answer}
---
category: Linjer
points: 300
---
$$
\vec{v} = [1, -2]
$$
:::::::



::::::::
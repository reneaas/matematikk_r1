# Oppgaver: Skalarproduktet


:::::::::::::::{exercise} Oppgave 1
Regn ut skalarproduktet mellom vektorene.
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a

$$
\vec{a} = [2, 3] \qog \vec{b} = [4, -1]
$$


::::{answer}
$$
\vec{a} \cdot \vec{b} = 5
$$
::::


::::{solution}
$$
\vec{a} \cdot \vec{b} = 2 \cdot 4 + 3 \cdot (-1) = 8 - 3 = 5
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
$$
\vec{c} = [-2, 1] \qog \vec{d} = [5, 3]
$$


::::{answer}
$$
\vec{c} \cdot \vec{d} = -7
$$
::::

::::{solution}
$$
\vec{c} \cdot \vec{d} = -2 \cdot 5 + 1 \cdot 3 = -10 + 3 = -7
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
$$
\vec{p} = [-2, 0] \qog \vec{q} = [1, 4]
$$

::::{answer}
$$
\vec{p} \cdot \vec{q} = -2
$$
::::

::::{solution}
$$
\vec{p} \cdot \vec{q} = -2 \cdot 1 + 0 \cdot 4 = -2 + 0 = -2
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
$$
\vec{u} = [2, 3] \qog \vec{v} = [-3, 4]
$$



::::{answer}
$$
\vec{u} \cdot \vec{v} = 6
$$
::::

::::{solution}
$$
\vec{u} \cdot \vec{v} = 2 \cdot (-3) + 3 \cdot 4 = -6 + 12 = 6
$$
::::
:::::::::::::





::::::::::::::

:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 2


::::{hints} Den geometriske formelen for skalarproduktet

$$
\vec{a} \cdot \vec{b} = \len{a} \cdot \len{b} \cdot \cos \varphi
$$
::::


::::{hints} Kjente cosinusverdier

| $\varphi$ | $0\degree$ | $30\degree$ | $45\degree$ | $60\degree$ | $90\degree$ | $120\degree$ | $135\degree$ | $150\degree$ | $180\degree$ | 
|:-----------:|:------------:|:-------------:|:-------------:|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|:--------------:|
| $\cos \varphi$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-\dfrac{1}{2}$ | $-\dfrac{\sqrt{2}}{2}$ | $-\dfrac{\sqrt{3}}{2}$ | $-1$ |
::::


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $\len{a} = 5$ og $\len{b} = 4$
* vinkelen mellom dem er $60\degree$

Bestem $\dot{a}{b}$. 


::::{answer}
$$
\dot{a}{b} = 10
$$
::::

::::{solution}
Vi bruker den geometriske formelen for skalarproduktet:

$$
\begin{align*}
\dot{a}{b} &= \len{a} \cdot \len{b} \cdot \cos \varphi \\
\\
&= 5 \cdot 4 \cdot \cos 60\degree \\
\\
&= 20 \cdot \dfrac{1}{2} \\
\\
&= 10
\end{align*}
$$

der vi har brukt at $\cos 60\degree = \dfrac{1}{2}$.
::::

:::::::::::::


:::::::::::::{tab-item} b
Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $\len{a} = 2$
* $\dot{a}{b} = -4$
* vinkelen mellom dem er $150\degree$

Bestem $\len{b}$.


::::{answer}
$$
\len{b} = \dfrac{4}{\sqrt{3}} = \dfrac{4 \sqrt{3}}{3}
$$
::::


::::{solution}
Vi bruker den geometriske formelen for skalarproduktet:

$$
\vec{a} \cdot \vec{b} = \len{a} \cdot \len{b} \cdot \cos \varphi
$$

Så setter vi inn det vi vet:

$$
-4 = 2 \cdot \len{b} \cdot \cos 150\degree
$$

Vi har at $\cos 150\degree = -\dfrac{\sqrt{3}}{2}$, så vi får

$$
-4 = 2 \cdot \len{b} \cdot \left(-\dfrac{\sqrt{3}}{2}\right)
$$

$$
-4 = -\len{b} \cdot \sqrt{3}
$$

$$
\len{b} = \dfrac{4}{\sqrt{3}} = \dfrac{4 \sqrt{3}}{3}
$$
::::


:::::::::::::



:::::::::::::{tab-item} c
Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $\len{a} = 3$ og $\len{b} = 6$
* $\dot{a}{b} = 0$

Bestem vinkelen $\varphi$ mellom $\vec{a}$ og $\vec{b}$.


::::{answer}
$$
\varphi = 90\degree
$$
::::
:::::::::::::



:::::::::::::{tab-item} d
Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $\len{a} = 2$ og $\len{b} = 4$
* $\dot{a}{b} = -4$

Bestem vinkelen $\varphi$ mellom $\vec{a}$ og $\vec{b}$.


::::{answer}
$$
\varphi = 120\degree
$$
::::


::::{solution}
Vi bruker den geometriske formelen for skalarproduktet:

$$
\vec{a} \cdot \vec{b} = \len{a} \cdot \len{b} \cdot \cos \varphi
$$

Så setter vi inn det vi vet og løser for $\cos \varphi$:

$$
-4 = 2 \cdot 4 \cdot \cos \varphi
$$

$$
-4 = 8 \cdot \cos \varphi
$$

$$
\cos \varphi = -\dfrac{1}{2}
$$

Fra hinttabellen ser vi at $\cos 120\degree = -\dfrac{1}{2}$, altså er vinkelen mellom vektorene 

$$
\varphi = 120\degree.
$$

::::


:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 3

::::{hints} Kjente cosinusverdier

| $\varphi$ | $0\degree$ | $30\degree$ | $45\degree$ | $60\degree$ | $90\degree$ | $120\degree$ | $135\degree$ | $150\degree$ | $180\degree$ | 
|:-----------:|:------------:|:-------------:|:-------------:|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|:--------------:|
| $\cos \varphi$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-\dfrac{1}{2}$ | $-\dfrac{\sqrt{2}}{2}$ | $-\dfrac{\sqrt{3}}{2}$ | $-1$ |
::::

Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $\len{a} = 4$ og $\len{b} = 2$
* vinkelen mellom dem er $60\degree$


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $\dot{a}{b}$.


::::{answer}
$$
\dot{a}{b} = 4
$$
::::

::::{solution}
Vi bruker den geometriske formelen for skalarproduktet:

$$
\begin{align*}
\dot{a}{b} &= \len{a} \cdot \len{b} \cdot \cos \varphi \\
\\
&= 4 \cdot 2 \cdot \cos 60\degree \\
\\
&= 8 \cdot \dfrac{1}{2} \\
\\
&= 4
\end{align*}
$$
::::

:::::::::::::

:::::::::::::{tab-item} b
En annen vektor er gitt ved

$$
\vec{c} = \vec{a} + \vec{b}. 
$$

Bestem $\len{c}$.


::::{answer}
$$
\len{c} = 2\sqrt{7}
$$
::::

::::{solution}
Vi har at $\len{c}^2 = \vec{c} \cdot \vec{c}$. Da får vi


$$
\begin{align*}
\len{c}^2 &= (\vec{a} + \vec{b}) \cdot (\vec{a} + \vec{b}) \\
\\
&= \vec{a} \cdot \vec{a} + 2 \cdot \vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{b} \\
\\
&= \len{a}^2 + 2 \cdot \dot{a}{b} + \len{b}^2 \\
\\
&= 16 + 8 + 4 \\
\\
&= 28
\end{align*}
$$

Altså er lengden av $\vec{c}$ gitt ved

$$
\len{c} = \sqrt{28} = \sqrt{4 \cdot 7} = 2\sqrt{7}.
$$

::::

:::::::::::::

:::::::::::::{tab-item} c
En vektor $\vec{d} = \vec{a} - \vec{b}$.

Bestem $\dot{d}{a}$.


::::{answer}
$$
\dot{d}{a} = 12
$$
::::

::::{solution}
Vi har at

$$
\begin{align*}
\dot{d}{a} &= (\vec{a} - \vec{b}) \cdot \vec{a} \\
\\
&= \vec{a} \cdot \vec{a} - \vec{b} \cdot \vec{a} \\
\\
&= \len{a}^2 - \dot{a}{b} \\
\\
&= 16 - 4 \\
\\
&= 12
\end{align*}
$$
::::

:::::::::::::


:::::::::::::{tab-item} d
To vektorer $\vec{p}$ og $\vec{q}$ er gitt ved

$$
\vec{p} = 2\vec{a} - \vec{b} \qog \vec{q} = \vec{a} + 3\vec{b}
$$

Bestem $\dot{p}{q}$.


::::{answer}
$$
\dot{p}{q} = 40
$$
::::

::::{solution}
Vi har at

$$
\begin{align*}
\dot{p}{q} &= (2\vec{a} - \vec{b}) \cdot (\vec{a} + 3\vec{b}) \\
\\
&= 2\vec{a} \cdot \vec{a} + 6\vec{a} \cdot \vec{b} - \vec{b} \cdot \vec{a} - 3\vec{b} \cdot \vec{b} \\
\\
&= 2\len{a}^2 + 5\dot{a}{b} - 3\len{b}^2 \\
\\
&= 2 \cdot 16 + 5 \cdot 4 - 3 \cdot 4 \\
\\
&= 32 + 20 - 12 \\
\\
&= 40
\end{align*}
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 4
::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
To vektorer er gitt ved

$$
\vec{a} = [2, 3] \qog \vec{b} = [-4, t] \qfor t \in \real
$$


Bestem $t$ slik at $\vec{a}$ og $\vec{b}$ er ortogonale.


::::{answer}
$$
t = \dfrac{8}{3}
$$
::::

::::{solution}
Vektorene er ortogonale dersom skalarproduktet deres blir null:

$$
\vec{a} \cdot \vec{b} = 0
$$

som gir

$$
[2, 3] \cdot [-4, t] = 0
$$

$$
2 \cdot (-4) + 3 \cdot t = 0
$$

$$
-8 + 3t = 0 \liff t = \dfrac{8}{3}
$$

::::


:::::::::::::


:::::::::::::{tab-item} b
To vektorer er gitt ved 

$$
\vec{p} = [1, 2] \qog \vec{q} = [k, 4] \qfor k \in \real 
$$

Bestem $k$ slik at $\vec{p} \perp \vec{q}$.


::::{answer}
$$
k = -8
$$
::::

::::{solution}
Vi har at 

$$
\vec{p} \perp \vec{q} \liff \vec{p} \cdot \vec{q} = 0.
$$

Dette gir oss likningen

$$
[1, 2] \cdot [k, 4] = 0
$$

$$
1 \cdot k + 2 \cdot 4 = 0
$$

$$
k + 8 = 0 \liff k = -8.
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
En vektor $\vec{a} = [5, 2]$. 

Bestem en vektor $\vec{b}$ slik at $\vec{a} \perp \vec{b}$ og $\len{a} = \len{b}$.


::::{answer}
$$
\vec{b} = [-2, 5] \qeller \vec{b} = [2, -5]
$$
::::

::::{solution}
Vi kommer til å bruke dette stadig vekk senere, men hvis vi bytter om på rekkefølgen til koordinatene og endrer fortegnet på én av koordinatene, så får vi:

$$
\vec{b} = [-2, 5]
$$

Vi regner ut skalarproduktet:

$$
\vec{a} \cdot \vec{b} = [5, 2] \cdot [-2, 5] = 5 \cdot (-2) + 2 \cdot 5 = -10 + 10 = 0
$$

Så de er ortogonale! Lengden til $\vec{b}$ må også være lik som før siden vi bare byttet plass på koordinatene og endret fortegnet på én av dem. Dette svarer til å bare rotere den opprinnelige vektoren $90\degree$. 
::::


:::::::::::::


::::::::::::::
:::::::::::::::


---



:::::::::::::::{exercise} Oppgave 5

::::{hints} Kjente cosinusverdier

| $\varphi$ | $0\degree$ | $30\degree$ | $45\degree$ | $60\degree$ | $90\degree$ | $120\degree$ | $135\degree$ | $150\degree$ | $180\degree$ | 
|:-----------:|:------------:|:-------------:|:-------------:|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|:--------------:|
| $\cos \varphi$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$ | $0$ | $-\dfrac{1}{2}$ | $-\dfrac{\sqrt{2}}{2}$ | $-\dfrac{\sqrt{3}}{2}$ | $-1$ |
::::

Om to vektorer $\vec{a}$ og $\vec{b}$ får du vite at

* $\len{a} = 2$ og $\len{b} = 3$
* $\dot{a}{b} = -3 \sqrt{2}$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem vinkelen $\varphi$ mellom $\vec{a}$ og $\vec{b}$.

::::{answer}
$$
\varphi = 135\degree
$$
::::


::::{solution}
Vi bruker den geometriske formelen for skalarproduktet:

$$
\vec{a} \cdot \vec{b} = \len{a} \cdot \len{b} \cdot \cos \varphi
$$

Så setter vi inn det vi vet og løser for $\cos \varphi$:

$$
-3 \sqrt{2} = 2 \cdot 3 \cdot \cos \varphi
$$

$$
-3 \sqrt{2} = 6 \cdot \cos \varphi
$$

$$
\cos \varphi = -\dfrac{\sqrt{2}}{2}
$$

Fra hinttabellen ser vi at $\cos 135\degree = -\dfrac{\sqrt{2}}{2}$, altså er vinkelen mellom vektorene

$$
\varphi = 135\degree.
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
To vektorer $\vec{p}$ og $\vec{q}$ er gitt ved 

$$
\vec{p} = 2\vec{a} + \vec{b} \qog \vec{q} = \vec{a} - \vec{b}
$$

Bestem $\dot{p}{q}$.


::::{answer}
$$
\dot{p}{q} = -1 + 3\sqrt{2}
$$
::::

::::{solution}
Vi har at

$$
\begin{align*}
\dot{p}{q} &= (2\vec{a} + \vec{b}) \cdot (\vec{a} - \vec{b}) \\
\\
&= 2\vec{a} \cdot \vec{a} - 2\vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{a} - \vec{b} \cdot \vec{b} \\
\\
&= 2\len{a}^2 - \dot{a}{b} - \len{b}^2 \\
\\
&= 2 \cdot 4 - (-3 \sqrt{2}) - 9 \\
\\
&= 8 + 3\sqrt{2} - 9 \\
\\
&= -1 + 3\sqrt{2}
\end{align*}
$$
::::


:::::::::::::


:::::::::::::{tab-item} c
En vektor $\vec{r}$ er gitt ved

$$
\vec{r} = \vec{a} + t\cdot \vec{b} \qder t \in \real
$$

Bestem $t$ slik at vinkelen mellom $\vec{a}$ og $\vec{r}$ er $90\degree$.


::::{answer}
$$
t = \dfrac{4}{3 \sqrt{2}} = \dfrac{2 \sqrt{2}}{3}
$$
::::

::::{solution}
Vi har at vinkelen mellom $\vec{a}$ og $\vec{r}$ skal være $90\degree$. Det er den dersom skalarproduktet deres blir null:

$$
\vec{a} \cdot \vec{r} = 0
$$


$$
\vec{a} \cdot (\vec{a} + t \cdot \vec{b}) = 0
$$

$$
\vec{a} \cdot \vec{a} + t \cdot \vec{a} \cdot \vec{b} = 0
$$

$$
\len{a}^2 + t \cdot \dot{a}{b} = 0
$$

$$
4 + t \cdot (-3 \sqrt{2}) = 0
$$

$$
4 - 3\sqrt{2} \cdot t = 0 \liff t = \dfrac{4}{3 \sqrt{2}}
$$

Dette kan vi skrive om til 

$$
t = \dfrac{4 \sqrt{2}}{6} = \dfrac{2 \sqrt{2}}{3}
$$
::::


:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 6
Tre vektorer er gitt ved

$$
\vec{a} = [1, 2] \qog \vec{b} = [4, -1] \qog \vec{c} = [-2, 3]
$$

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør hvilken vektor som er lengst.


::::{answer}
Vektoren $\vec{b}$ er lengst.
::::

::::{solution}
Vi regner ut lengden til hver av vektorene:

$$
\len{a} = \sqrt{1^2 + 2^2} = \sqrt{5}
$$

$$
\len{b} = \sqrt{4^2 + (-1)^2} = \sqrt{17}
$$

$$
\len{c} = \sqrt{(-2)^2 + 3^2} = \sqrt{13}
$$

Altså er det vektoren $\vec{b}$ som er lengst.
::::

:::::::::::::


:::::::::::::{tab-item} b
Undersøk hvilke vektorpar som har en vinkel $\varphi$ mellom seg der: 

1. $\varphi \in [0, 90\degree\rangle$
2. $\varphi = 90\degree$
3. $\varphi \in \langle 90\degree, 180\degree]$

::::{answer}
* Vinkelen mellom $\vec{a}$ og $\vec{b}$ er i intervallet $\varphi \in [0, 90\degree\rangle$. 
* Vinkelen mellom $\vec{a}$ og $\vec{c}$ er i intervallet $\varphi \in [0, 90\degree\rangle$.
* Vinkelen mellom $\vec{b}$ og $\vec{c}$ er i intervallet $\varphi \in \langle 90\degree, 180\degree]$.
::::

::::{solution}
Vi regner ut skalarproduktene mellom vektorparene:

$$
\vec{a} \cdot \vec{b} = [1, 2] \cdot [4, -1] = 1 \cdot 4 + 2 \cdot (-1) = 4 - 2 = 2
$$

Altså er vinkelen mellom $\vec{a}$ og $\vec{b}$ i intervallet $\varphi \in [0, 90\degree\rangle$ siden skalarproduktet er positivt.

$$
\vec{a} \cdot \vec{c} = [1, 2] \cdot [-2, 3] = 1 \cdot (-2) + 2 \cdot 3 = -2 + 6 = 4
$$

Altså er vinkelen mellom $\vec{a}$ og $\vec{c}$ i intervallet $\varphi \in [0, 90\degree\rangle$ siden skalarproduktet er positivt.

$$
\vec{b} \cdot \vec{c} = [4, -1] \cdot [-2, 3] = 4 \cdot (-2) + (-1) \cdot 3 = -8 - 3 = -11
$$

Altså er vinkelen mellom $\vec{b}$ og $\vec{c}$ i intervallet $\varphi \in \langle 90\degree, 180\degree]$ siden skalarproduktet er negativt.
::::

:::::::::::::


::::::::::::::

:::::::::::::::



---



:::::::::::::::{exercise} Oppgave 7
For to vektorer $\vec{a}$ og $\vec{b}$ er $\len{a} = 4$, $\len{b} = 2\sqrt{3}$ og vinkelen mellom $\vec{a}$ og $\vec{b}$ er $30\degree$.

En vektor $\vec{p} = \vec{a} + \vec{b}$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem en eksakt verdi for $\len{p}$.

::::{answer}
$$
\len{p} = 2\sqrt{13}
$$
::::

::::{solution}
Vi har at $\len{p}^2 = \vec{p} \cdot \vec{p}$. Da får vi

$$
\begin{align*}
\len{p}^2 &= (\vec{a} + \vec{b}) \cdot (\vec{a} + \vec{b}) \\
\\
&= \vec{a} \cdot \vec{a} + 2 \cdot \vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{b} \\
\\
&= \len{a}^2 + 2 \cdot \dot{a}{b} + \len{b}^2 \\
\\
&= 16 + 2 \cdot (4 \cdot 2\sqrt{3} \cdot \cos 30\degree) + 12 \\
\\
&= 16 + 16\sqrt{3} \cdot \dfrac{\sqrt{3}}{2} + 12 \\
\\
&= 16 + 24 + 12 \\
\\
&= 52
\end{align*}
$$

der vi har brukt at $\cos 30\degree = \dfrac{\sqrt{3}}{2}$. Dermed er lengden av $\vec{p}$ gitt ved

$$
\len{p} = \sqrt{52} = \sqrt{4 \cdot 13} = 2\sqrt{13}.
$$
::::


:::::::::::::


:::::::::::::{tab-item} b
En annen vektor $\vec{q}$ er gitt ved 

$$
\vec{q} = t \cdot \vec{a} + \vec{b} \qder t \in \real
$$

Bestem $t$ slik at $\vec{p}$ og $\vec{q}$ er ortogonale.


::::{answer}
$$
t = -\dfrac{6}{7}
$$
::::

::::{solution}
Vi har at vektorene er ortogonale dersom skalarproduktet deres blir null:

$$
\vec{p} \cdot \vec{q} = 0
$$

$$
(\vec{a} + \vec{b}) \cdot (t \cdot \vec{a} + \vec{b}) = 0
$$

$$
t \cdot \vec{a} \cdot \vec{a} + \vec{a} \cdot \vec{b} + t \cdot \vec{b} \cdot \vec{a} + \vec{b} \cdot \vec{b} = 0
$$

$$
t \cdot \len{a}^2 + (1 + t) \cdot \dot{a}{b} + \len{b}^2 = 0
$$

$$
t \cdot 16 + (1 + t) \cdot (4 \cdot 2\sqrt{3} \cdot \cos 30\degree) + 12 = 0
$$

$$
16t + (1 + t) \cdot 4 \cdot 2\sqrt{3} \cdot \dfrac{\sqrt{3}}{2} + 12 = 0
$$

$$
16t + (1 + t) \cdot 12 + 12 = 0
$$

$$
16t + 12 + 12t + 12 = 0
$$

$$
28t + 24 = 0 \liff t = -\dfrac{24}{28} = -\dfrac{6}{7}
$$
::::

:::::::::::::


::::::::::::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 8
For vektorene $\vec{a}$ og $\vec{b}$ er $\len{a} = 2$, $\len{b} = 3$ og $\dot{a}{b} = -3$.


La $\vec{u} = \vec{a} + \vec{b}$ og $\vec{v} = \vec{a} - 6\vec{b}$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem lengden av $\vec{u}$ og $\vec{v}$.


::::{answer}
$$
\len{u} = \sqrt{7} \and \len{v} = 2\sqrt{91}
$$
::::


::::{solution}
Vi har at $\len{u}^2 = \vec{u} \cdot \vec{u}$. Da får vi

$$
\begin{align*}
\len{u}^2 &= (\vec{a} + \vec{b}) \cdot (\vec{a} + \vec{b}) \\
\\
&= \vec{a} \cdot \vec{a} + 2 \cdot \vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{b} \\
\\
&= \len{a}^2 + 2 \cdot \dot{a}{b} + \len{b}^2 \\
\\
&= 4 + 2 \cdot (-3) + 9 \\
\\
&= 4 - 6 + 9 \\
\\
&= 7
\end{align*}
$$

derfor er lengden av $\vec{u}$ gitt ved

$$
\len{u} = \sqrt{7}.
$$

Vi har at $\len{v}^2 = \vec{v} \cdot \vec{v}$. Da får vi

$$
\begin{align*}
\len{v}^2 &= (\vec{a} - 6\vec{b}) \cdot (\vec{a} - 6\vec{b}) \\
\\
&= \vec{a} \cdot \vec{a} - 12 \cdot \vec{a} \cdot \vec{b} + 36 \cdot \vec{b} \cdot \vec{b} \\
\\
&= \len{a}^2 - 12 \cdot \dot{a}{b} + 36 \cdot \len{b}^2 \\
\\
&= 4 - 12 \cdot (-3) + 36 \cdot 9 \\
\\
&= 4 + 36 + 324 \\
\\
&= 364
\end{align*}
$$


:::{factor-tree}
n: 364
align: right
width: 60%
figsize: 4, 4
nocache:
:::

Det kan være lurt å primtallsfaktorisere $364$ for å forenkle kvadratroten, som vi viser i faktortreet til høyre. Dermed får vi at 

$$
\len{v}^2 = 364 = 2^2 \cdot 7 \cdot 13.
$$

Altså blir lengden

$$
\len{v} = \sqrt{364} = \sqrt{2^2 \cdot 7 \cdot 13} = 2\sqrt{91}.
$$



::::

:::::::::::::



:::::::::::::{tab-item} b
Bestem $\dot{u}{v}$.


::::{answer}
$$
\dot{u}{v} = -35
$$
::::

::::{solution}
Vi har at

$$
\begin{align*}
\dot{u}{v} &= (\vec{a} + \vec{b}) \cdot (\vec{a} - 6\vec{b}) \\
\\
&= \vec{a} \cdot \vec{a} - 6\vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{a} - 6\vec{b} \cdot \vec{b} \\
\\
&= \len{a}^2 - 5\dot{a}{b} - 6\len{b}^2 \\
\\
&= 4 - 5 \cdot (-3) - 6 \cdot 9 \\
\\
&= 4 + 15 - 54 \\
\\
&= -35
\end{align*}
$$
::::

:::::::::::::


:::::::::::::{tab-item} c
En annen vektor $\vec{w}$ er gitt ved 

$$
\vec{w} = t \cdot \vec{a} + \vec{b} \qder t \in \real
$$

Bestem $t$ slik at $\vec{w} \perp \vec{u}$.

::::{answer}
$$
t = 6
$$
::::


:::::::::::::


:::::::::::::{tab-item} d
En vektor $\vec{p}$ er gitt ved 

$$
\vec{p} = \vec{a} + t\cdot \vec{b} \qder t \in \real
$$

Bestem $t$ slik at $\len{p}$ blir minst mulig. Hva er den minste lengden $\vec{p}$ kan ha?

::::{answer}
$$
t = \dfrac{1}{3} \qog \abs{\vec{p}}_\mathrm{minst} = \sqrt{3}
$$
::::
:::::::::::::



::::::::::::::


:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 9
Tre punkter er gitt ved $A(1, 1)$, $B(9, 7)$ og $P(5, 9)$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bruk vektorregning til å vise at $\angle APB = 90\degree$.


:::::::::::::


:::::::::::::{tab-item} b
En linje $\ell$ er parallell med $\lvec{AB}$ og går gjennom punktet $P$. 

Det er også et annet punkt $Q$ på $\ell$ slik at $\angle AQB = 90\degree$.

Bestem koordinatene til $Q$.

:::::::::::::
::::::::::::::

:::::::::::::::



---


:::::::::::::::{exercise} Oppgave 10
I en trekant $\triangle ABC$ er hjørnene $A(-3, -1)$, $B(2, -2)$ og $C(5, 2)$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Avgjør ved hjelp av vektorregning hvilken side i trekanten som er kortest.


:::::::::::::

:::::::::::::{tab-item} b
Avgjør ved hjelp av vektorregning om noen av vinklene i trekanten er $90\degree$.


:::::::::::::
::::::::::::::

:::::::::::::::


---


:::::::::::::::{exercise} Oppgave 11
Tre punkter er gitt ved $A(1, 2)$, $B(-1, 5)$ og $C(t, 4)$ der $t \in \real$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $t$ slik at $\angle BAC = 90\degree$


:::::::::::::



:::::::::::::{tab-item} b
Bestem $t$ slik at $A$, $B$ og $C$ ligger på en rett linje.
:::::::::::::


::::::::::::::

:::::::::::::::




---




:::::::::::::::{exercise} Oppgave 12
Vi har gitt tre punkter $A(3, 4)$, $B(-1, -2)$ og $C(3 + t, 2t)$ der $t \in \real$.

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $t$ slik at punktene $A$, $B$ og $C$ ligger på en rett linje.


:::::::::::::


:::::::::::::{tab-item} b
Bestem $t$ slik at punktene $A$, $B$ og $C$ danner en trekant $\triangle ABC$ der $\angle C = 90\degree$.
:::::::::::::


::::::::::::::
:::::::::::::::




---



:::::::::::::::{exercise} Oppgave 13
I et koordinatsystemet har vi gitt punktene $A(-2, 3)$ og $B(3, 2)$.


::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem lengden av linjestykket $AB$.


:::::::::::::


:::::::::::::{tab-item} b
Linja gjennom $A$ og $B$ skjærer $x$-aksen i punktet $C$.

Bestem koordinatene til $C$.
:::::::::::::


:::::::::::::{tab-item} c
Et punkt $D$ er gitt ved $D(2, t)$ der $t \in \real$.

Bestem $t$ slik at $\angle ABD = 90\degree$.
:::::::::::::


::::::::::::::
:::::::::::::::
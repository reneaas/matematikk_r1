# Dev



:::{plot}
width: 70%
function: -(x + 1)**2 + 4, [-1, 2), f, blue
function-endpoints: true
xmin: -2
xmax: 3
ymax: 6
ymin: -7
fontsize: 25
:::



::::{multi-plot2}
---
rows: 1
cols: 2
fontsize: 30
---
:::{plot}
function: sqrt(x + 2) + 1, [-2, 7), A, blue
function-endpoints: true
xmin: -3
xmax: 8
ymax: 5
ymin: -1  
yticks: off
grid: off
:::


:::{plot}
function: x * exp(-x), (0, 4), B, blue
function-endpoints: true
xmin: -1
xmax: 5
ymax: 1
ymin: -0.5 
yticks: off
grid: off
:::


::::



---


:::{plot}
width: 70%
function: sqrt(x + 2) + 1, [-2, 7), f, blue
function-endpoints: true
xmin: -3
xmax: 8
ymax: 6
ymin: 0 
fontsize: 25
:::
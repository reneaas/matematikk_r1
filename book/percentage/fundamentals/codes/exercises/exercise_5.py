import numpy as np
import matplotlib.pyplot as plt


rabatt = [
    0,
    3,
    6,
    8,
    10,
    13,
    16,
    18,
    19,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
]

antall_billetter = [i for i in range(1, 30)]


fig, ax = plt.subplots()
ax.plot(antall_billetter, rabatt, color="teal", lw=1.5, alpha=0.7)


ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
ax.set_xlabel(r"Antall billetter", fontsize=16, loc="right")
ax.set_ylabel(r"Rabatt (%)", fontsize=16, loc="top", rotation="horizontal")

plt.grid(True, linestyle="--", alpha=0.7, color="gray")


plt.xlim(0, 32)

xticks = [i for i in range(1, 30, 3)]
plt.xticks(xticks, fontsize=16)
plt.yticks(fontsize=16)

plt.tight_layout()
plt.savefig("../../figures/exercises/exercise_5.svg")

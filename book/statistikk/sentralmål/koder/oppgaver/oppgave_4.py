import plotmath
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define function

    # List of functions and their labels.
    functions = []

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-6,
        xmax=6,
        ymin=-2,
        ymax=6,
        ticks=True,
    )

    frekvenser = [5, 20, 50, 20, 5]
    bredder = [5, 10, 10, 10, 5]
    høyder = [f / b for f, b in zip(frekvenser, bredder)]
    xmin = 0
    x = [xmin]
    for i, bredde in enumerate(bredder):
        xmin = xmin + bredde
        x.append(xmin)

    plt.xlim(-10, x[-1] + 5)
    plt.ylim(-0.5, max(høyder) + 1.5)

    xticks = x[:]
    if 0 in xticks:
        xticks.remove(0)
    ax.set_xticks(xticks)
    ax.set_xticklabels([f"${i}$" for i in xticks], fontsize=20, rotation=0)

    yticks = [i for i in range(1, int(max(høyder)) + 1)]
    ax.set_yticks(yticks)
    ax.set_yticklabels([f"${i}$" for i in range(1, int(max(høyder)) + 1)], fontsize=20)

    ax.set_ylabel(
        r"$\displaystyle \frac{\mathrm{Frekvens}}{\mathrm{Klassebredde}}$",
        fontsize=16,
        rotation=0,
        loc="top",
    )

    ax.set_xlabel(
        r"$x$",
        fontsize=16,
        loc="right",
    )

    for i in range(len(x) - 1):
        ax.plot([x[i], x[i + 1]], [høyder[i], høyder[i]], color="teal", lw=2, alpha=0.7)
        ax.plot([x[i], x[i]], [0, høyder[i]], color="teal", lw=2, alpha=0.7)
        ax.plot([x[i + 1], x[i + 1]], [0, høyder[i]], color="teal", lw=2, alpha=0.7)

        ax.fill(
            [x[i], x[i + 1], x[i + 1], x[i]],
            [0, 0, høyder[i], høyder[i]],
            color="teal",
            alpha=0.3,
        )

    ax.grid(False)

    plt.subplots_adjust(
        left=0.2,
        bottom=0.068,
        top=0.885,
    )

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

    if not save:

        plotmath.show()


if __name__ == "__main__":

    import pathlib

    # Get the directory where the script is located
    current_dir = str(pathlib.Path(__file__).resolve().parent)

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=True)

import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return 0.5 * (x - 3) ** 3 - (x - 3) + 2

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=True,
        xmin=-2,
        xmax=6,
        ymin=-6,
        ymax=6,
        ticks=False,
        xstep=1,
        ystep=1,
        grid=False,
        lw=2.5,
        alpha=None,
        domain=False,
        fontsize=20,
        figsize=None,
    )

    a = 0.5
    b = 4
    m = 0.5 * (a + b)

    xticks = [a, b, m]
    xtick_labels = [r"$a$", r"$b$", r"$m$"]

    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels, fontsize=20)

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
    main(dirname=dirname, save=False)

import plotmath


def main(dirname, save):

    frekvenser = [20, 30, 40, 10]
    bredder = [10, 10, 20, 10]
    xmin = 0

    fig, ax = plotmath.histogram(
        xmin=xmin,
        frequencies=frekvenser,
        binsizes=bredder,
        xlabel="$\\mathrm{Reisetid} \\,\\,  (\\mathrm{minutter})$",
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

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from load_csv import load


def parse_population(s):
    suffixes = {"k": 1_000, "M": 1_000_000}
    if s[-1] in suffixes:
        return float(s[:-1]) * suffixes[s[-1]]
    return float(s)


def format_pop(x, _):
    if x >= 1_000_000:
        return f"{x/1_000_000:.0f}M"
    if x >= 1_000:
        return f"{x/1_000:.0f}K"
    return str(x)


def aff_pop():

    try:

        df = load("../population_total.csv", "country")

        cols = np.array(df.columns.values).astype(np.float32)

        france_data = df.loc["France"]
        morocco_data = df.loc["Morocco"]

        morocco_data_parsed = morocco_data.apply(parse_population)
        france_data_parsed = france_data.apply(parse_population)

        fig, ax = plt.subplots()
        ax.plot(cols, morocco_data_parsed.values, label="Morocco")
        ax.plot(cols, france_data_parsed.values, label="France")
        ax.legend()

        ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_pop))

        ax.set(
            ylabel="Population",
            xlabel="year",
            title="France life expectancy Predictions",
        )

        fig.savefig("population.jpg")
        plt.show()

    except Exception as e:
        print(e)
        print("error!")


aff_pop()

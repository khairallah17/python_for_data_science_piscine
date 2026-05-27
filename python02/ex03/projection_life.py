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


def life_projection():

    try:

        df_life = load("../life_expectancy_years.csv", "country")
        life_expectancy_years = np.array(df_life["1900"].fillna(0).values).astype(
            np.uint32
        )

        df_income = load(
            "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv", "country"
        )
        income = np.array(df_income["1900"].values).astype(np.uint32)

        fig, ax = plt.subplots()

        ax.set(xlabel="Gross domestic product", ylabel="Life Expectancy", title="1900")

        mask = life_expectancy_years > 0
        ax.scatter(income[mask], life_expectancy_years[mask])
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_pop))

        plt.show()
        """
        population_1900 = df_population["1900"]
        population_1900_parsed = np.array(
            population_1900.apply(parse_population)
        ).astype(np.float32)

        income_1900 = {}

        # print(population_1990)
        """
    except Exception as e:
        print(e)
        print("error!")


life_projection()

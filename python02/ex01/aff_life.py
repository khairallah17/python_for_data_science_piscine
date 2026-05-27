import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def plot_chart():

    try:

        df = load("../life_expectancy_years.csv", "country")

        # print(df[1:])
        france_data = df.loc[["France"]]
        cols = np.array(france_data.columns.values).astype(np.float32)
        rows = np.array(france_data.values[0]).astype(np.float32)

        fig, ax = plt.subplots()
        ax.plot(cols, rows)

        ax.set(
            ylabel="Life Expectancy",
            xlabel="year",
            title="France life expectancy Predictions",
        )

        fig.savefig("lif_expectancy_char.jpg")
        plt.show()

    except Exception as e:
        print(e)
        print("error!")


plot_chart()

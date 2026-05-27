import pandas as pd


def load(path: str, index: str = "") -> DataFrame:

    try:

        df = pd.read_csv(path, index_col=index)
        return df

    except Exception as e:
        print("error!")
        return None

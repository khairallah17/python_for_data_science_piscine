import pandas as pd


def load(path: str) -> DataFrame:

    try:

        df = pd.read_csv(path)

        print(f"loading dataset of dimensions {df.shape}")
        print(df.head())

        return df

    except Exception as e:
        print("error!")
        return None

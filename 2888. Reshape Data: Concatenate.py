import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    new = pd.concat([df1, df2], ignore_index=True)

    return new
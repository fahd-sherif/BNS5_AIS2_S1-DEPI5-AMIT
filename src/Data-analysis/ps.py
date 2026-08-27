import pandas as pd

def get_check_dtype(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "Dtypes": df.dtypes,
        "Num_Uniqu": df.nunique()
    }).T


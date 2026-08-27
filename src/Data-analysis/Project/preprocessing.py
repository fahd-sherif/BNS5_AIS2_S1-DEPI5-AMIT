import pandas as pd


def Read_data_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Error: File not found.")

def Drop_unnecessary_features(df, cols_to_drop):
    return df.drop(columns=cols_to_drop)

def Check_data_type(df):
    report = pd.DataFrame({
        "Data Type": df.dtypes,
        "Unique Values": df.nunique()
    })
    return report.T
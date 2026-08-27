from preprocessing import (
    Read_data_file,
    Drop_unnecessary_features,
    Check_data_type
)
from config.Config import COLS_TO_DROP

file_path = r"D:\DEPI\BNS5_AIS2_S1--DEPI5-AMIT\src\Data-analysis\Project\data\raw\Titanic.csv"
df = Read_data_file(file_path)
df = Drop_unnecessary_features(df, COLS_TO_DROP)
report = Check_data_type(df)
print(report)
import pandas as pd
import numpy as np

data ={
    "Column1": [22,33,44,55],
    "Column2": [1,2,3,4],
    "Column3": ["Abc","cde","fgr","hkf"]
}


df = pd.DataFrame(data)

def kareal(x):
    return x*x

kareal2 = lambda x: x*x



result =  df                    #KOLON İŞLEMLERİ
result = df["Column2"].unique()
result = df["Column2"].nunique()
result = df["Column2"].value_counts()
result = df["Column2"] *2

result = df["Column1"].apply(kareal)
result = df["Column1"].apply(kareal2)

result = df.columns
result = len(df.columns)
result = df.info

result = df.sort_values("Column2")
result = df.sort_values("Column3", ascending=False)


print(result)
from os import error
import pandas as pd
import numpy as np


df = pd.read_csv('IBMD-Analysis/NetflixOriginals.csv',encoding='ANSI',sep=";")


result = df 
result = df.columns
result = df.info

result = df.head(5)

result = df.head(10) # ilk 10 kayıt gelir

result = df.tail(5) # son 5 kayıt gelir

resut = df.tail(10)

result = df["Language"]

result = df["Language"].head(5)

result = df[["Title","Language"]].head(5) # baslik ve dil alanlarını 5'e kadar getirdik.

result = df[["Title","Language"]].tail(5)

result = df[5:][["Title","Language"]].head()

#result = df[df["Runtime]" >= 100.0][["Title","Language"]].head(50)

result = df[(df["Premiere"] >= 2016) & (df["Premiere"] <= 2017)]["Title"]















print(result)
print(df.columns)
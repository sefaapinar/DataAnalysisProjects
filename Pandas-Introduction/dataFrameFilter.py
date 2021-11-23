import pandas as pd

import numpy as np



data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns= ["Column1","Column2","Column3","Column4","Column5"])

result = df

result = df.columns
result = df.head(5) # ilk 5 tane kayıtı getirir.
result = df.tail(4) # tail kuyruk, yani sondan alınır bilgiler.
result = df["Column1"].head()
result = df.Column1.head()
result = df[["Column1","Column2"]].head(2)
result = df[["Column1","Column2"]].tail(2)

result = df[5:15][["Column1","Column2"]].head()
result = df[5:15][["Column1","Column2"]].tail()


# filtreleme islemleri

result = df > 50
result = df[df<50]  # kosul islemleri
result = df[df%2==0] #cift olanlara bakar.

result = df[df["Column1"] > 50][["Column1","Column2"]]
result = df[(df["Column2"] >50) & (df["Column1"] <=70)]

result = df[(df["Column2"] >50) | (df["Column1"] <=70)]

result = df.query("Column1 >=50 $ Column1 % 2==0")

print(result)
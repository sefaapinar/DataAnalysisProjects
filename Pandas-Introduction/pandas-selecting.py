from numpy.random.mtrand import rand
import pandas as pd
from numpy.random import randn 


df = pd.DataFrame(rand(3,3), index = ["A","B","C"], columns= ["Column1","Column2","Column3"])


result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]

# loc["row","column"] =>loc["row"] => loc[":","column"]
result = df.loc["A"]

result = df.iloc[2]

result = df.loc[:,"Column1"]

result = df.loc[:,"Column1"]

result = df.loc[:,["Column1","Column2"]]
result = df.loc[:,"Column1":"Column3"]

result = df.loc[:,"Column3"]

result = df.loc["A","Column2"]
result = df.loc["C","Column1"]



# kolon ekleme

df["Column4"] = pd.Series(randn(3),["A","B","C"])

df["Column5"] = df["Column1"] + df["Column3"]



# kolon silme

print(df.drop("Column5", axis=1))


print(df)









print(result)
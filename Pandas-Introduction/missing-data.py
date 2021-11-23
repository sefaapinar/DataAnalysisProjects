import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index= ['a','c','e','f','h'], columns= ['column1','column2','column3'])
df = df.reindex(['a','b','c','d','e','f','g','h'])

result = df
result = df.drop(["column1","column2"], axis = 1) #kolon silme.
result = df.drop('a', axis =0)


result = df.isnull()  # kontrol etmek için yani 'nan' alanlarını belirler
result = df.notnull()
result = df.isnull().sum()
result = df["column1"].isnull().sum()

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn


# result = df.dropna() # axis = 0 => satıra göre silme işlemi yapar.
# result = df.dropna(axis =1)
# result = df.dropna(how = "any")
# result = df.dropna(how = "all")
# result = df.dropna(supset = ["column1","column2"], how = "all")

# result = df.dropna(thresh = 2)
# result = df.dropna(thresh = 4) # en az sayıda normal veri

# result = df.fillna(value = 'no input')


result = df.sum().sum()
result = df.size
result = df.isnull().sum()
result = df.isnull().sum().sum()


def means(df):
    top = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return top / adet

result = df.fillna(value = means(df))




print(df)
print(result)
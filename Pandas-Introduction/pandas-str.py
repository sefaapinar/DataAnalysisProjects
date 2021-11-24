from os import sep
import pandas as pd
import numpy as np


data = pd.read_csv("Pandas-Introduction/NetflixOriginals.csv",encoding="ANSI", sep=";")

data.dropna(inplace= True)


print(data.columns)

# data["Title"] = data["Title"].str.upper()

# data["Title"] = data["Title"].str.lower()

# data["index"] = data["Title"].str.find("a")  # a harfini veride aratma

# data = data[data.Title.str.contains('Enter the anime')]

# data = data.Title.str.replace(' ', '-') # bosluk alanlarına - işareti koy.

data[['Title','Genre']] = data['Title'].loc[data['Title'].str.split().str.len()==2].str.split(expend = True)

print(data.head(5))
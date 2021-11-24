import pandas as pd
import numpy as np


df = pd.read_csv("Turkey Super League Championship in History/tcl.csv",sep=";")

result = df.head(10) # İlk 10 kaydı getirme

result = len(df.index) # Kaç tane kayıt oldugunu gösterir.

result = df["won"].mean()  # Won = Kazanma oranlarının ortalaması karşımıza gelir.

result = df["won"].max() # maximum ve minimum kazanma oranları.
result = df["won"].min() 

result = df[df["won"]==df["won"].max()]["team"].iloc[0] # Kazanma oranı en yüksek takım 

result = df[(df["goals_for"]>=20) & (df["goals_for"] <=25 )][["team","year","points"]].sort_values("year", ascending=False)

result = df.groupby("team").mean()["goals_for"] # takım gol ortalamarını bulma

result = len(df.groupby("team"))  #takım sayısını bulma
result = df["team"].nunique()    #takım sayınısı teke bulma


result = df["team"].value_counts()  # hangi takımdan kaç tane vardır


result = df[df["team"].str.contains("y")]  # takım isminde "y" harfi geçenleri getirdik.


def str_find(teams):
    if "y" in teams.lower():
        return True
    return False

result = df[df["team"].apply(str_find)]  # Kosul olusturduk ve kosula göre Takım içerisinde "Y" harfi olanları getirdik.



print(result) 
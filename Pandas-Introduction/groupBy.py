import pandas as pd
import numpy as np

personeller = {
    'Çalışan':['Mehmet','Fatih','Sefa','Erkan'],
    'Departman':['Bilgi İşlem','Muhasebe ve Finans','İnsan Kaynakları','Bilgi İşlem'],
    'Yaş':[23,43,32,32],
    'Semt':['Kadıköy','Darıca','Gebze','Darıca'],
    'Maaş':[3333,4444,5555,5555]

}

df = pd.DataFrame(personeller)  #gruplama işlemleri

result = df
result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

for name, group in df.groupby("Semt"):
    print(name)
    print(group)

for name, group in df.groupby("Departman"):
    print(name)
    print(group)

result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").get_group("Bilgi İşlem")
result = df.groupby("Departman").sum()
result = df.groupby("Departman")["Maaş"].mean()
result = df.groupby("Semt")["Yaş"].mean()
result = df.groupby("Semt")["Çalışan"].count()
result = df.groupby("Departman")["Yaş"].min()
result = df.groupby("Departman").agg(np.mean)
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]) # 4 farklı hesaplama işlemleri yapılmıştır.







print(result)
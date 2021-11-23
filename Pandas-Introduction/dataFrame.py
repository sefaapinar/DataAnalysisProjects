import pandas as pd

list = ([["Ahmet",50],["Mehmet",41],["Sefa",100]])
dict = {"Name":["Sefa","Mehmet","Ali","Çınar","Yağmur"],"Grade":[50,12,89,100]}
dict_list = [{"Name":"Ahmet","Grade":59},
    {"Name":"Mehmet","Grade":59},
    {"Name":"Fatih","Grade":59},
    {"Name":"Yavuz","Grade":59},
    {"Name":"Samet","Grade":59},


]





df = pd.DataFrame([1,2,3,4,5,6])
df = pd.DataFrame(list, columns= ['Name','Grade'], index=[1,2,3], dtype=float)

# df = pd.DataFrame(dict, index=["213","2344","102"])


df = pd.DataFrame(dict_list)


print(df)

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)

# print(df)
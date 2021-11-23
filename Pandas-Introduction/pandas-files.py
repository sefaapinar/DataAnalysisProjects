import sqlite3
import pandas as pd




connection = sqlite3.connect("sample.db")  # data bağlantısı.

df = pd.read_sql_query("SELECT * FROM students",connection) # veri tabanından students tablosunu getir.

# df = pd.read_csv('tr_food.csv')

# df = pd.read_json('sample.json') # json uzantılı dosyayı okur.



# df = pd.read_excel('tr_food.db')  # Database uzantılı veriler için kullanilir.

df = pd.read_excel('values.xlsx')  # excel dosyaları okumak için kullanilir.


















print(df)
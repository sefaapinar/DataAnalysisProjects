import pandas as pd

import numpy as np

df = pd.read_csv("YoutubeTrendAnalysis/youtube-ing.csv")

result = df.head(10) # İlk 10 kaydı getirme

result = df[5:10].head(5) # İkinci 5 Kaydı getirme

result = df.columns # listede var olan kolonları getirir.

result = len(df.columns) # kolonların sayısını bize getirir.

df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True) # Tablomuzdan bazı kayıtları silmek.
result = df
 
 #Like ve Dislike alanlarının sayısını bulalım ortalamalarını bulalım.

result = df["likes"].mean()  # beğeni sayılarının ortalaması gelir.
result = df["dislikes"].mean() 

result = df.head(50)[["title","likes","dislikes"]] # ilk 50 videonun like ve dislikes alanları bizlere gelmiş olur.

result = df[df["views"].max() == df["views"]][["title","views"]] # Görüntüleme sayısı en fazla olan video ve içeriği

result = df[df["views"].min() == df["views"]][["title","views"]] # Görüntülenme sayısı en az olan video ve içeriği

result = df.sort_values("views", ascending=False).head(10)        # en fazla görüntülenen ilk 10 video.

result = df.groupby("category_id").mean().sort_values("likes")["likes"]  # Kategoriye göre beğeni ortalamarını sıralı şekilde getiririniz.

result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"] # kategoriye göre yorum sayılarını sıralı bir şekilde getirir.

result = df["category_id"].value_counts()   # her kategoride kaç video vardır 

df["title_len"] = df["title"].apply(len)          # her videonun title(başlık) uzunluğunun bilgisini yeni bir kolonda gösterelim.
df= result


# def tagCount(tag):
#     return len(tag.split('|'))

# df["tag_count"] = df["tags"].apply(tagCount)     # her video için kullanılan tag sayınını yeni kolonda gösteriniz.


likesList = list(df["likes"])  # En popüler videoları listeyelim.
dislikeList = list(df["dislikes"]) # en kötü olan videoları getirir.


print(likesList)
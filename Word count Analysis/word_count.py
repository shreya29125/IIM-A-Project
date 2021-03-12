import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import ast
data=pd.read_excel('twitter_data (3)_modified.xlsx','twitter_data (3)')
print(data.head())
str=''
print(type(data['hashtags'][0]))
for hashtags in data['hashtags']:
    hashtags=ast.literal_eval(hashtags)
    for hashtag in hashtags:
        str+=hashtag+" "
word_cloud = WordCloud(width = 600,height = 600,max_font_size = 200).generate(str)
plt.figure(figsize=(12,10))# create a new figure
plt.imshow(word_cloud,interpolation="bilinear")
plt.axis("off")
plt.show()

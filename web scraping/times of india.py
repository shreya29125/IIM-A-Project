import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url="https://timesofindia.indiatimes.com/city/indore/hindu-outfit-forces-3-tanishq-stores-to-put-up-apology-in-gujarat-mp/articleshow/78693579.cms"
news_contents=[]
list_links=[]
list_titles=[]
list_dates=[]
for i in range(1,2):
    r1=requests.get(url)
    coverpage=r1.content
    soup1=BeautifulSoup(coverpage,"html.parser")
    coverpage_news=soup1.find_all('div',class_='ga-headlines')[0].get_text()
    title=soup1.find_all('h1',class_='_23498')[0].get_text()
    news_contents.append(coverpage_news)
    list_links.append(url)
    list_titles.append(title)
df = pd.DataFrame(
    {'Title': list_titles,
     'Link': list_links,
     'Content':news_contents})
with pd.ExcelWriter('articles_tanishq.xlsx',
                    mode='a') as writer:  
    df.to_excel(writer)

    
    

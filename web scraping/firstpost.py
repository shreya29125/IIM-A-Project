import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url="https://www.firstpost.com/tag/tanishq"
news_contents=[]
list_links=[]
list_titles=[]
list_dates=[]
for i in range(1,2):
    r1=requests.get(url)
    coverpage=r1.content
    soup1=BeautifulSoup(coverpage,"html.parser")
    coverpage_news=soup1.find_all('div',class_='main-content')[0].find_all('div',class_='big-thumb')
    for n in np.arange(0,len(coverpage_news)):
        link=coverpage_news[n].find_all('a')[0]['href']
        title=coverpage_news[n].find_all('div',class_='title-wrap')[0].find('h3').get_text()
        article=requests.get(link)
        article_content=article.content
        soup_article=BeautifulSoup(article_content,'html.parser')
        #x=soup_article.find_all('div')
        #for p in range(0,len(x)):
         #   try:
          #      print(x[p]['class'])
           # except:
            #    print("No")
        try:
            x=soup_article.find('div',class_='article-sect').find('div',class_='inner-copy').find_all('p')
            time=soup_article.find('div',class_='article-sect').find('div',class_='author-info').find_all('span')[1].get_text()
            list_paras=[]
            for p in range(0,len(x)):
                para=x[p].get_text()
                list_paras.append(para)
            full_article=" ".join(list_paras)
            news_contents.append(full_article)
            list_dates.append(time)
            list_links.append(link)
            list_titles.append(title)
        except:
            print(n)
df = pd.DataFrame(
    {'Title': list_titles,
     'Link': list_links,
     'Timestamp':list_dates,
     'Content':news_contents})
with pd.ExcelWriter('articles_tanishq.xlsx',
                    mode='a') as writer:  
    df.to_excel(writer)

    
    

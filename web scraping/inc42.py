import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url="https://inc42.com/tag/byju's/page/"
news_contents=[]
list_links=[]
list_titles=[]
list_dates=[]
for i in range(8,9):
    _url=url+str(i)+"/"
    r1=requests.get(_url)
    coverpage=r1.content
    soup1=BeautifulSoup(coverpage,"html.parser")
    coverpage_news=soup1.find_all('div',class_='row')[3].find('main').find_all('div',class_='card-wrapper horizontal-card')
    for n in np.arange(0,len(coverpage_news)):
        link=coverpage_news[n].find('a')['href']
        title=coverpage_news[n].find('a')['title']
        time=coverpage_news[n].find('div',class_='meta-wrapper').find('div',class_='meta').find('span',class_='date').get_text()
        article=requests.get(link)
        article_content=article.content
        soup_article=BeautifulSoup(article_content,'html.parser')
        try:
            #x=soup_article.find_all('div',class_='row')[3].find('main').find('div',class_='single-post-summary').get_text()
            y=soup_article.find_all('div',class_='row')[3].find('main').find('div',class_='entry-content clearfix').get_text()
            list_para=[]
            #list_para.append(x)
            list_para.append(y)
            full_article=" ".join(list_para)
            news_contents.append(full_article)
            list_links.append(link)
            list_titles.append(title)
            list_dates.append(time)
        except:
            print(i,n)
df = pd.DataFrame(
    {'Title': list_titles,
     'Link': list_links,
     'Timestamp':list_dates,
     'Content':news_contents})
with pd.ExcelWriter('articles.xlsx',
                    mode='a') as writer:  
    df.to_excel(writer)

    
    

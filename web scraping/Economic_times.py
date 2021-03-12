import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url="https://economictimes.indiatimes.com/topics_all.cms?type=article,image,video&query=tanishq&curpg="
news_contents=[]
list_links=[]
list_titles=[]
list_dates=[]
for i in range(1,2):
    _url=url+str(i)
    r1=requests.get(_url)
    coverpage=r1.content
    soup1=BeautifulSoup(coverpage,"html.parser")
    coverpage_news=soup1.find_all('div',class_='topicstry')
    for n in np.arange(0,15):
        link=coverpage_news[n].find('a')['href']
        link='https://economictimes.indiatimes.com'+link
        title=coverpage_news[n].find('h3').get_text()
        time=coverpage_news[n].find('time').get_text()
        article=requests.get(link)
        article_content=article.content
        soup_article=BeautifulSoup(article_content,'html.parser')
        x=soup_article.find_all('div',class_='artText')
        try:
            news_contents.append(x[0].get_text())
            list_links.append(link)
            list_titles.append(title)
            list_dates.append(time)
        except:
            print(i,n)
df = pd.DataFrame(
    {'Title': list_titles,
     'Link': list_links,
     'Tiemstamp':list_dates,
     'Content':news_contents})
with pd.ExcelWriter('articles.xlsx',
                    mode='a') as writer:  
    df.to_excel(writer)

    
    

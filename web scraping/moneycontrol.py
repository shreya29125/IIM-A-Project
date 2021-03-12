import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url="https://www.moneycontrol.com/news/tags/tanishq.html/"
news_contents=[]
list_links=[]
list_titles=[]
list_dates=[]
r1=requests.get(url)
coverpage=r1.content
soup1=BeautifulSoup(coverpage,"html.parser")
coverpage_news=soup1.find('div',class_='topictabpane').find('ul',id='cagetory').find_all('li',class_='clearfix')
for n in np.arange(0,len(coverpage_news)):
    link=coverpage_news[n].find('a')['href']
    title=coverpage_news[n].find('a')['title']
    time=coverpage_news[n].find('span').get_text()
    article=requests.get(link)
    article_content=article.content
    soup_article=BeautifulSoup(article_content,'html.parser')
    x=soup_article.find_all('div',class_='content_wrapper')
    try:
        paras=x[0].find_all('p')
    except:
        continue
    list_paras=[]
    for j in range(0,len(paras)):
        para=paras[j].get_text()
        list_paras.append(para)
    para=x[0].contents[-1]
    list_paras.append(para)
    try:
        full_article=" ".join(list_paras)
        news_contents.append(full_article)
        list_links.append(link)
        list_titles.append(title)
        list_dates.append(time)
    except:
        print(n)
df = pd.DataFrame(
    {'Title': list_titles,
     'Link': list_links,
     'Tiemstamp':list_dates,
     'Content':news_contents})
with pd.ExcelWriter('articles_tanishq.xlsx',
                    mode='a') as writer:  
    df.to_excel(writer)

    
    

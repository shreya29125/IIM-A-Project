import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url="https://www.thehindubusinessline.com/search/?order=DESC&page="
news_contents=[]
list_links=[]
list_titles=[]
list_dates=[]
for i in range(1,3):
    _url=url+str(i)+"&q=tanishq&sort=publishdate"
    r1=requests.get(_url)
    coverpage=r1.content
    soup1=BeautifulSoup(coverpage,"html.parser")
    coverpage_news=soup1.find_all('div',class_='row')[5].find_all('article')
    for n in np.arange(0,len(coverpage_news)):
        link=coverpage_news[n].find('a')['href']
        title=coverpage_news[n].find_all('a')[1].get_text()
        time=coverpage_news[n].find('span').get_text()
        article=requests.get(link)
        article_content=article.content
        soup_article=BeautifulSoup(article_content,'html.parser')
        x=soup_article.find('div',class_='contentbody inf-body')
        try:
            para=x.find('h2').get_text()
        except:
            print(i,n)
        list_para=[]
        list_para.append(para)
        paras=x.find_all('p')
        try:
            for j in range(0,len(paras)):
                para=paras[j].get_text()
                list_para.append(para)
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
with pd.ExcelWriter('articles_tanishq.xlsx',
                    mode='a') as writer:  
    df.to_excel(writer)

    
    

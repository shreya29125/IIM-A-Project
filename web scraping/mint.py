import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url="https://www.livemint.com/searchlisting/"
news_contents=[]
list_links=[]
list_titles=[]
list_dates=[]
for i in range(0,3):
    _url=url+str(i)+"/tanishq"
    r1=requests.get(_url)
    coverpage=r1.content
    soup1=BeautifulSoup(coverpage,"html.parser")
    coverpage_news=soup1.find_all('div',class_='headlineSec')
    for n in np.arange(0,len(coverpage_news)):
        link=coverpage_news[n].find('h2').find('a')['href']
        link='https://www.livemint.com'+link
        title=coverpage_news[n].find('h2').get_text()
        try:
            time=coverpage_news[n].find('span',class_='fl date').find_all('span')[1].get_text()
        except:
            print(i,n)
        article=requests.get(link)
        article_content=article.content
        soup_article=BeautifulSoup(article_content,'html.parser')
        try:
            para=soup_article.find('div',class_='FirstEle').find('p').get_text()
        except:
            print(i,n)
        try:
            x=soup_article.find('div',class_='paywall').find_all('p')
        except:
            print(i,n)
        list_para=[]
        list_para.append(para)
        try:
            for j in range(0,len(x)):
                para=x[j].get_text()
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

    
    

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url="https://www.business-standard.com/topic/tanishq"
news_contents=[]
list_links=[]
list_titles=[]
list_dates=[]
for i in range(1,2):
    r1=requests.get(url)
    coverpage=r1.content
    soup1=BeautifulSoup(coverpage,"html.parser")
    coverpage_news=soup1.find('div',class_='warp-inner').find_all('div',class_='content-main')[1].find('div',class_='row-panel').find('div',class_='row-inner').find('div',class_='row-panel').find('ul',class_='listing').find_all('li')
    for n in np.arange(0,len(coverpage_news)):
        link=coverpage_news[n].find('a')['href']
        link='https://www.business-standard.com/'+link
        title=coverpage_news[n].find('h2').find('a').get_text()
        try:
            time=coverpage_news[n].find_all('p')[0].get_text()
        except:
            print(i,n)
        article=requests.get(link)
        article_content=article.content
        soup_article=BeautifulSoup(article_content,'html.parser')
        x=soup_article.find('div',class_='warp-inner').find('div',class_='row-panel').find('div',class_='row-inner').find('span',class_='p-content').find_all('p')
        print(len(x))
        #x=soup_article.find('div',class_='warp-inner').find('div',class_='row-panel').find('div',class_='row-inner').find('span',class_='p-content').find_all('p')
        list_para=[]
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
with pd.ExcelWriter('articles.xlsx',
                    mode='a') as writer:  
    df.to_excel(writer)

    
    

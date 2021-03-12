import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
url="https://yourstory.com/search?page=1&tag=Byju&tag=Byju%27s&tag=byjus"
news_contents=[]
list_links=[]
list_titles=[]
list_dates=[]
for i in range(1,2):
    print(url)
    r1=requests.get(url)
    coverpage=r1.content
    soup1=BeautifulSoup(coverpage,"html.parser")
    coverpage_news=soup1.find_all('main')
    print(coverpage_news)
    for div in coverpage_news:
        print(div['class'])
    for n in np.arange(1,len(coverpage_news)):
        link="https://yourstory.com"+coverpage_news[n].find('a')['href']
        title=coverpage_news[n].find_all('div')[2].find_all('span')[1].get_text()
        time=coverpage_news[n].find_all('div')[2].find('span').get_text()
        article=requests.get(link)
        article_content=article.content
        soup_article=BeautifulSoup(article_content,'html.parser')
        x=soup_article.find('div',class_='quill-content')
        for div in x.find_all('div'):
            div.decompose()
        for fig in x.find_all('figure'):
            fig.decompose()
        print(len(x.find_all('div')))
        full_article=x.get_text()
        news_contents.append(full_article)
df = pd.DataFrame(
    {'Title': list_titles,
     'Link': list_links,
     'Timestamp':list_dates,
     'Content':news_contents})
with pd.ExcelWriter('articles.xlsx',
                    mode='a') as writer:  
    df.to_excel(writer)

    
    

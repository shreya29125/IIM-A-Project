import praw
import pandas as pd
import datetime as dt
import sys
from prawcore.exceptions import Forbidden,Redirect,NotFound
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
reddit = praw.Reddit(client_id='LsSu52yydRBE6w', \
                     client_secret='pFsEdM_9tacBA6ULeSVmH8oSePJ8uA', \
                     user_agent='whitehatjr', \
                     username='Ok-Stretch2806', \
                     password='shreya29.')
my_keywords = ['whitehatjunior','whitehatjr','whitehat'] #to search for all posts containing any of these words
#there is a community of whitehat jr on reddit but it is not very active so I searched for all commuitites on reddit which posted about whitehat jr and below is a list of all of them
my_subreddits=['india','indianpeoplequora','developersIndia','IndiaSpeaks','librandu','Indian_Academia','whitehatjr','whiteHatSr','Chodi','unitedstatesofindia','Kerala','SaimanSays',\
               'indiasocial','IndianDankMemes','indianmeme','dankmemes','CricketShitpost','theunkillnetwork','FuckBYJUS','JEENEETards','removalbot','hackernews','IndianLeft','sunraybee',\
               'patient_hackernews','FAQsutra','TamilNadu','PooniaVsWhiteHatJr','rdtcopypasta','TanmayBhatKeDost','peterjblogger','DaniDev','KartheekGopu','IndianTeenagers','ProgrammerHumor',\
               'technology','Coding_for_Teens','dankrishu','SchumyVannaKaviyangal','OutOfTheLoop','mumbai','BITSPilani','programmingforkids','IndiaInvestments','programming','learnprogramming',\
               'Lal_Salaam','SomeOrdinaryGmrs','YouTube_startups','theworldnews','thugeshh','indianstartups','realtech','r4rindia']
comments_dict={'id':[],'body':[],'created':[],'author':[],'is_submitter':[],'link_id':[],'parent_id':[],'score':[],'subreddit_id':[]}
for subreddit in my_subreddits:
    my_subreddit=reddit.subreddit(subreddit)
    posts=my_subreddit.search(my_keywords)
    try:
        for post in posts:
            submission=reddit.submission(id=post.id)
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                comments_dict["id"].append(comment.id)
                comments_dict["body"].append(comment.body.translate(non_bmp_map))
                comments_dict["created"].append(comment.created)
                comments_dict['author'].append(comment.author)
                comments_dict['is_submitter'].append(comment.is_submitter)
                comments_dict['link_id'].append(comment.link_id)
                comments_dict['parent_id'].append(comment.parent_id)
                comments_dict['score'].append(comment.score)
                comments_dict['subreddit_id'].append(comment.subreddit_id)
    except Forbidden:
        print(subreddit)
    except Redirect:
        print(subreddit)
    except NotFound:
        print(subreddit)
comments_data = pd.DataFrame(comments_dict)
def get_date(created):
    return dt.datetime.fromtimestamp(created)
_timestamp = comments_data["created"].apply(get_date)
comments_data = comments_data.assign(timestamp = _timestamp)
comments_data.to_csv('reddit_data.csv', index=False) 
# for post in reddit.subreddit('india').stream.comments():
#  cbody = comment.body
#if any(keyword in cbody for keyword in my_keywords):
#  print(cbody)

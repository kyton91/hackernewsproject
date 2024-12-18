import requests
from bs4 import BeautifulSoup
import pprint
import time

mega_links=[]
mega_votes=[]
for page in range(1,5):
    res=requests.get(f"https://news.ycombinator.com/?p={page}")
    if res.status_code != 200:
        raise RuntimeError(f"Error: {res.status_code} Check Entered Page Number And Try Again")
    scrape=BeautifulSoup(res.text,'html.parser')
    links=scrape.select('.titleline > a')
    votes=scrape.select('.subtext')
    mega_links+=links
    mega_votes+=votes
    time.sleep(1)


def create_custom_news(links,votes):
    news=[]
    for idx,item in enumerate(links):
        try:
            text=item.getText()
            link=item.get("href",None)
            vote=int(votes[idx].getText().split(" ")[0])
            if vote>99:
                news.append({'title':text,'link':link,'votes':vote})
        except IndexError:
            break
    return sort_according_to_votes(news)


def sort_according_to_votes(news_list):
    return sorted(news_list,key=lambda k:k['votes'],reverse=True)


print("Stories having more than or equal to 100 votes:")
pprint.pprint(create_custom_news(mega_links,mega_votes))
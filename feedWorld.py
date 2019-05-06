import feedparser
from time import sleep

url = "http://www.scmp.com/rss/91/feed"  #all
#url = "http://www.scmp.com/rss/2/feed"   #hk

lastpublished = None

while True:
    NewsFeed = feedparser.parse(url)

    NewFeed = sorted(NewsFeed['entries'], key=lambda k: k['published_parsed'])
    for entry in NewFeed:
        if lastpublished and not lastpublished<entry.published_parsed:
            pass
        else:
            lastpublished = entry.published_parsed
            print('-------------------'+entry.published+'----------------')
            print(entry.title)
            print('------------------------------------------------------')
            print(entry.summary)
            print('------------------------------------------------------')
    sleep(60)

#title
#summary
#published

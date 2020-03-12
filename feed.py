import feedparser
from time import sleep

urls = []
urls.append("http://www.scmp.com/rss/91/feed")          #all
#urls.append("http://www.scmp.com/rss/2/feed")          #hk
urls.append("http://rss.cnn.com/rss/edition.rss")       #cnn top stories
urls.append("http://rss.cnn.com/rss/edition_world.rss") #cnn world

lastpublished = None

ids = []

while True:

    new_ids = []

    for url in urls:
        NewsFeed = feedparser.parse(url)

        try:
            NewFeed = sorted(NewsFeed['entries'], key=lambda k: k['published_parsed'])
        except KeyError:
            NewFeed = []
            for entry in NewsFeed['entries']: NewFeed.insert(0, entry)

        for entry in NewFeed:
            new_ids.append(entry['id'])
            if entry['id'] in ids: pass
            else:
                if 'published' in entry.keys():
                    print('-------------------'+entry.published+'----------------')
                print(entry.get('title', 'NO TITLE'))
                print('------------------------------------------------------')
                if 'summary' in entry.keys():
                    print(entry.get('summary', '******************'))
                if 'link' in entry.keys():
                    print('=> '+entry.get('link', '******************'))
                if 'summary' in entry.keys() and 'link' in entry.keys():
                    print('------------------------------------------------------')

    ids = new_ids
    sleep(60)

#title
#summary
#published

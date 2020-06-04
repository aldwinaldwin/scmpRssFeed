import feedparser
from time import sleep

urls = []
urls.append("https://rthk.hk/rthk/news/rss/e_expressnews_elocal.xml")
urls.append("https://rthk.hk/rthk/news/rss/e_expressnews_einternational.xml")
urls.append("https://rthk.hk/rthk/news/rss/e_expressnews_egreaterchina.xml")
urls.append("https://rthk.hk/rthk/news/rss/e_expressnews_efinance.xml")
urls.append("https://rthk.hk/rthk/news/rss/e_expressnews_esport.xml")

lastdt = {}

while True:
    NewFeed = []                                                                #collect feeds/entries
    for url in urls:                                                            #from each url in list
        new_lastdt = None
        for entry in feedparser.parse(url)['entries']:                          #check each entry
            if not lastdt.get(url, None) or lastdt[url]<entry.published_parsed: #if newly published since last check
                if not new_lastdt or new_lastdt<entry.published_parsed:         #if it's a newer new publish date
                    new_lastdt = entry.published_parsed                         #collect new date
                NewFeed.append(entry)
        if new_lastdt: lastdt[url] = new_lastdt                                 #keep new publish date for next run
    NewFeed = sorted(NewFeed, key=lambda k: k['published_parsed'])              #sort all entries from all urls
    for entry in NewFeed:                                                       #and print them
        print('-------------------'+entry.published+'----------------')
        print(entry.title)
        print('------------------------------------------------------')
        print(entry.summary)
        print(entry.link)
        print('------------------------------------------------------')
        pass
    sleep(60)

#title
#summary
#published

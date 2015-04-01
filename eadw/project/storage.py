import feedparser


f = open("feeds.txt","r")
feeds = f.read().splitlines()
f.close()
    
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['eadw_proj']
if db['news'] is None:
    db['news'] = db.CreateCollection("news")
news = db['news']

    

for url in feeds:
    print "###### ", url, " #####"

    feed = feedparser.parse( url )
    for entry in feed.entries:
        date = entry.published
   
        title = entry.title
        description = entry.summary
        link =entry.link

        obj = news.find_one({"t":title,"p":date})
        if not obj:
            news.insert({"t":title,"d":description,"l":link,"p":date})
            print title

    

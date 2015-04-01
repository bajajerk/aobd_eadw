import feedparser
import socket
from pymongo import MongoClient

print "#########################################################"
print "################### STORE PROCESS #######################"
print "#########################################################"

socket.setdefaulttimeout(10)
f = open("feeds.txt","r")
feeds = f.read().splitlines()
f.close()
    

client = MongoClient('localhost', 27017)
db = client['eadw_proj']
if db['news'] is None:
    db['news'] = db.CreateCollection("news")
news = db['news']



for url in feeds:
    print url

    feed = feedparser.parse( url )
    for entry in feed.entries:
        try:
            date = entry.published
       
            title = entry.title
            description = entry.summary
            link =entry.link
    
            obj = news.find_one({"t":title,"p":date})
            if not obj:
                news.insert({"t":title,"d":description,"l":link,"p":date})
                print "\t",title
        except AttributeError, e:
            print "[ERROR]"
    

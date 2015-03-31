import urllib2
from bs4 import BeautifulSoup


file = open("feeds.txt","r")
feeds = file.read().splitlines()
file.close()
print feeds
    
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['eadw_proj']
if db['news'] is None:
    db['news'] = db.CreateCollection("news")
news = db['news']

    

for feed in feeds:
    try:
        response = urllib2.urlopen(feed)
        print "##### ",feed, " #####"
        rss = response.read()
        soup = BeautifulSoup(rss, "xml")
        soup.prettify()
        for item in soup.findAll('item'):
            date = item.findAll('pubDate')[0].string.strip();
       
            title = item.findAll('title')[0].string.strip();
            description = item.findAll('description')[0].string.strip();
            link = item.findAll('link')[0].string.strip();
            

            obj = news.find_one({"l":link})
            if not obj:
                news.insert({"t":title,"d":description,"l":link,"p":date})
                print "###########################\n",description


    except urllib2.URLError, e:
        print feed, " | ", e


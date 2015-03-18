import urllib2
from bs4 import BeautifulSoup


file = open("feeds.txt","r")
feeds = file.read().splitlines()
   
print feeds
    

for feed in feeds:
    try:
        response = urllib2.urlopen(feed)
        print "##### ",feed, " #####"
        rss = response.read()
        soup = BeautifulSoup(rss, "xml")
        soup.prettify()
        for tag in soup.findAll('title'):
            print tag.string.strip()
    except urllib2.URLError, e:
        print feed, " | ", e


import re
import robotparser
from sets import Set
import time
from urllib2 import urlopen
import urlparse


rp = robotparser.RobotFileParser("http://www.ist.utl.pt/robots.txt")
rp.read()


def extractUrls(url,html):
    unique_set = Set()
    linksre = '<a\s.*?href=[\'"](.*?)[\'"].*?</a>'
    links = re.findall(linksre, html, re.I)
    for link in links:
        new_link = urlparse.urljoin(url, link)
        if new_link not in unique_set and new_link.startswith("http://") and rp.can_fetch("*", new_link):
            unique_set.add(new_link)    
    return list(unique_set)
    

print rp.can_fetch("*", "http://www.ist.utl.pt/newscache/")

already_crawled = Set()

def horizontalCrawler(links,depth):
    if depth < 3:

        new_links = Set()
        
        for link in links:
            if link not in already_crawled:
                time.sleep(1)
                
                try:
                    site = urlopen(link)
                    content = site.read()
                    site.close()
                    already_crawled.add(link)
                    
                    file_ = open(link[7:].replace("/","_").replace(".","_")+".html", 'w')
                    file_.write(content)
                    file_.close()
                    print "SAVED",depth,"/",str(len(links)), link
                    
                    temp_links =extractUrls(link,content)
                    for temp_link in temp_links:
                        if temp_link not in already_crawled and temp_link not in new_links:
                            new_links.add(temp_link)
                    
                
                except:
                    print "ERROR"
        horizontalCrawler(list(new_links),depth+1)         
                

horizontalCrawler(["http://www.ist.utl.pt"],0)
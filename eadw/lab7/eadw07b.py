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
    



site = urlopen("http://www.ist.utl.pt")
content = site.read()
links =  extractUrls("http://www.ist.utl.pt/",content)
site.close()




print rp.can_fetch("*", "http://www.ist.utl.pt/newscache/")

already_crawled = Set()

def verticalCrawler(links, words):
    for link in links:
        if link not in already_crawled:
            time.sleep(1)
            
            try:
                site = urlopen(link)
                content = site.read()
                links = extractUrls(link,content)
                site.close()
                
                count = 0
                for word in words:
                    if word in content:
                        count += 1
                
                if float(count)/len(words) > 2.0/3.0:
                    print "MATCH ", link
                else:
                    print "NO ", link
                
                    
                new_links =extractUrls(link,content)
                already_crawled.add(link)
                verticalCrawler(new_links,words)

            except:
                print "ERROR"
verticalCrawler(links,"Candidatos Alunos Docentes Pessoal".split())
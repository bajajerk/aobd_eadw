from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['eadw_proj']
if db['news'] is None:
    db['news'] = db.CreateCollection("news")
news = db['news']

    


for post in news.find():
    date = post["p"]   
    title = post["t"]
      
    
    more = news.find({"t":title,"p":date})
    if more.count() > 1:
        i =0
        for excess in more:
            if i> 0:
                news.remove(excess)
            i+=1
    
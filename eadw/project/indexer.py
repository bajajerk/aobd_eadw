import json
import os

from bson.objectid import ObjectId
from pymongo import MongoClient
from whoosh.fields import ID, TEXT, Schema
from whoosh.index import open_dir, create_in, exists_in
from whoosh.qparser.default import QueryParser
from whoosh.qparser.syntax import OrGroup


print "#########################################################"
print "################### INDEX PROCESS #######################"
print "#########################################################"

client = MongoClient('localhost', 27017)
db = client['eadw_proj']
if db['index'] is None:
    db['index'] = db.CreateCollection("index")
collection = db['index']
last_id = collection.find_one()
if last_id is None:
    collection.insert({"last_id":ObjectId()})
    last_id = collection.find_one()



# collection index only has one element
news = db['news']

# create directory for index if not exists
if not os.path.exists("news"):
    os.makedirs("news")


# do query for new news
news_index = None
if not exists_in("news"):
    schema = Schema(id=ID(unique=True,stored=True), d=TEXT(spelling=True),t=TEXT(spelling=True),tags=TEXT(stored=True))
    news_index = create_in("news", schema)
    result = news.find()
else:
    news_index = open_dir("news")
    result = news.find({"_id": {"$gt": ObjectId(last_id["last_id"])}})

news_writer = news_index.writer()

# do query for new entities
entities_index = None
entities_index = open_dir("entities")


# index each entry here
last_post = None
i = 0

for post in result:
    description = post["d"]
    title = post["t"]
    dpt = title + " "+description 
 
    print title

    
    tags = {}
    already={}
    
    
    for word in dpt.split():
        if word not in already.keys():
            already[word]=1
            with entities_index.searcher() as searcher:
                parser = QueryParser("name", entities_index.schema, group=OrGroup).parse(word)
                results = searcher.search(parser, limit=100)
                # Paris VS Paris Hilton - f#ck th3m 4ll
                for e in results:
                    name = e["name"]
                    url = e["url"]
                    opt = e["opt"]
                    if name not in tags.keys() and name in dpt and (len(opt)==0 or opt in dpt):
                        tags[name]=url
                            
    
    
    
    print tags
    news_writer.add_document(id=unicode(str(post['_id'])),d=description,t=title,tags=unicode(json.dumps(tags)))

    last_post = post
    i+=1
    if i>=1000:
        break


if last_post is not None:
    last_id["last_id"]=last_post['_id']
    collection.save(last_id)


news_writer.commit()    
print "END"



import os

from bson.objectid import ObjectId
from pymongo import MongoClient
from whoosh.fields import ID, TEXT, Schema
from whoosh.index import open_dir, create_in




client = MongoClient('localhost', 27017)
db = client['eadw_proj']
if db['index'] is None:
    db['index'] = db.CreateCollection("index")
collection = db['index']

# collection index only has one element
last_id = collection.find_one()
news = db['news']

# create directory for index if not exists
directory ="index"
if not os.path.exists(directory):
    os.makedirs(directory)

# do query for new news
ix = None
if not last_id:
    schema = Schema(id=ID(stored=True), d=TEXT,t=TEXT)
    ix = create_in(directory, schema)
    result = news.find()
else:
    ix = open_dir(directory)
    result = news.find({"_id": {"$gt": ObjectId(last_id["last_id"])}})

writer = ix.writer()


# index each entry here
last_post = None
for post in result:
    description = post["d"]
    title = post["t"]
    writer.add_document(id=unicode(str(post['_id'])),d=description,t=title)
    print post
    last_post = post
writer.commit()    

# update last_id on database
if last_post is not None:
    if not last_id:
        collection.insert({"last_id":last_post['_id']})
    else :
        last_id["last_id"]=last_post['_id']
        collection.save(last_id)




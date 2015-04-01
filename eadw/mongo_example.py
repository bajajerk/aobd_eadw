import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test-database']
if db['test-collection'] is None:
    db['test-collection'] = db.CreateCollection("test-collection")
collection = db['test-collection']

email = "hdlopesrocha91@gmail.com"
obj = collection.find_one({"email":email})
if not obj:
    collection.insert({"name":"Henrique Rocha","email":email,"counter":0})
else :
    obj["counter"]+=1
    collection.save(obj)

for result in collection.find():
    print result
    
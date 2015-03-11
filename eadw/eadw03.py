from whoosh.fields import *
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.qparser import *


file1 = open("aula03_cfc.txt","r")
lines = file1.readlines()

print "Exercise 1"
schema = Schema(id = NUMERIC(stored=True), content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()
for line in lines:
    
    partition = line.split(' ',1)
    i = partition[0]
    c = partition[1]
    writer.add_document(id=i,content=unicode(c,"UTF-8"))
writer.commit()



print "Exercise 2"

def search(query):
    ix = open_dir("indexdir")
    
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema, group=OrGroup).parse(unicode(query,"UTF-8"))
        results = searcher.search(query, limit=100)
        for r in results:
            print r
        print "Number of results:", results.scored_length()
        
search("first document")
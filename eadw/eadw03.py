from whoosh.fields import *
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.qparser import *

from utils_whoosh import search, precision, recall


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
result = search(ix,"first document")
print result

print "Exercise 3"
print "Pr = ", precision(result,['00664','00276'])
print "Re = ", recall(result,['00664','00276'])
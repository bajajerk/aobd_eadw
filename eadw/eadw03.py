from whoosh.fields import *
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.qparser import *

from utils_whoosh import search, precision, recall, f1, score


file1 = open("aula03_cfc.txt","r")
lines1 = file1.readlines()

file2 = open("aula03_queries.txt","r")
lines2 = file2.readlines()


print "Exercise 1"
schema = Schema(id = NUMERIC(stored=True), content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()
for line in lines1:
    
    partition = line.split(' ',1)
    i = int(partition[0])
    c = partition[1]
    writer.add_document(id=i,content=unicode(c,"UTF-8"))
writer.commit()



print "Exercise 2"
result = search(ix,"first document",100)
print result

print "Exercise 3"
print "Pr = ", precision(result,[664,276,1])
print "Re = ", recall(result,[664,276,1])
print "F1 = ", f1(result,[664,276,1])

print "Exercise 4"
for i in range(0,len(lines2)/2):
    text = lines2[i*2+0];
    number_strings = lines2[i*2+1].split();
    expected = [int(el) for el in number_strings]
    search2 = search(ix,text,100)
    print score(search2,expected)



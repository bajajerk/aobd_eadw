from utils import PageRank, PageRankAuto
from utils_whoosh import index, searchPageRank


file1 = open("aula04_links.txt","r")
lines1 = file1.readlines()


print "Exercise 1"
dictionary1 = {1: [3], 2: [1, 3], 3: [1, 2]}
print PageRank(dictionary1,5000,0.2)

print "Exercise 2"
dictionary2 = {}
for line in lines1:
    splits = line.split()
    doc = splits[0]
    dictionary2[doc] = []
    for i in xrange(1,len(splits)):
        dictionary2[doc].append(splits[i])
    
rank = PageRankAuto(dictionary2,0.15)
print rank

print "Exercise 3"
file2 = open("../lab3/aula03_cfc.txt","r")
lines2 = file2.readlines()
ix = index("indexl4",lines2)

result = searchPageRank("indexl4",ix,"first document",100,rank)

print result
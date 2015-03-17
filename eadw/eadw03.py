

from utils_whoosh import precision, recall, f1, score, searchBM25, searchCOS, \
    index, stop, indexNoStopWords


file1 = open("aula03_cfc.txt","r")
lines1 = file1.readlines()

file2 = open("aula03_queries.txt","r")
lines2 = file2.readlines()


print "Exercise 1"
ix = index("indexdir",lines1)


print "Exercise 2"
result = searchBM25("indexdir",ix,"first document",100)
print result

print "Exercise 3"
print "Pr = ", precision(result,[664,276,1])
print "Re = ", recall(result,[664,276,1])
print "F1 = ", f1(result,[664,276,1])

print "Exercise 4"
average = {"Pr":0,"Re":0,"F1":0}
for i in range(0,len(lines2)/2):
    text = lines2[i*2+0];
    number_strings = lines2[i*2+1].split();
    expected = [int(el) for el in number_strings]
    result2 = searchBM25("indexdir",ix,text,100)
    score2 = score(result2,expected)
    score2["query"]=text
    average["Pr"]+=score2["Pr"]
    average["Re"]+=score2["Re"]
    average["F1"]+=score2["F1"]
    print score2

average["Pr"]/=len(lines2)/2
average["Re"]/=len(lines2)/2
average["F1"]/=len(lines2)/2
print "Avg = ",average


print "Exercise 5A"
average = {"Pr":0,"Re":0,"F1":0}
for i in range(0,len(lines2)/2):
    text = lines2[i*2+0];
    number_strings = lines2[i*2+1].split();
    expected = [int(el) for el in number_strings]
    result2 = searchCOS("indexdir",ix,text,100)
    score2 = score(result2,expected)
    score2["query"]=text
    average["Pr"]+=score2["Pr"]
    average["Re"]+=score2["Re"]
    average["F1"]+=score2["F1"]
    print score2

average["Pr"]/=len(lines2)/2
average["Re"]/=len(lines2)/2
average["F1"]/=len(lines2)/2
print "Avg = ",average



print "Exercise 5B"
ix2 = indexNoStopWords("indexdir2",lines1)
average = {"Pr":0,"Re":0,"F1":0}
for i in range(0,len(lines2)/2):
    text = stop(unicode(lines2[i*2+0]));
    number_strings = lines2[i*2+1].split();
    expected = [int(el) for el in number_strings]
    result2 = searchBM25("indexdir2",ix2,text,100)
    score2 = score(result2,expected)
    score2["query"]=text
    average["Pr"]+=score2["Pr"]
    average["Re"]+=score2["Re"]
    average["F1"]+=score2["F1"]
    print score2

average["Pr"]/=len(lines2)/2
average["Re"]/=len(lines2)/2
average["F1"]/=len(lines2)/2
print "Avg = ",average

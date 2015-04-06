from numpy import linalg

import numpy as np
from utils import PageRank, PageRankAuto
from utils_whoosh import searchL2R, score


def lregression(X,y):
    l = len(y)
    A = np.vstack([np.array(X).T, np.ones(l)])
    return linalg.lstsq(A.T,y)[0]

X = [(0,3), (2,3), (2.5,3.6), (4,4.8)]
y = [7.3, 8.6, 8.5, 9.0]
w = lregression(X,y)


print w

print "Exercise 1"
file1 = open("aula05_features.txt","r")
lines1 = file1.readlines()

BM25 = 0
COSS = 1
RANK = 2
XPCT = 3

X = []
y = []

for line in lines1:
    splits = line.split()
    bm25 = float(splits[BM25])
    coss = float(splits[COSS])
    rank = float(splits[RANK])
    expt = int(splits[XPCT])
    X.append((bm25,coss,rank))
    y.append(expt)

w = lregression(X,y)
print w

print "Exercise 2"

print "Exercise 3"



file1 = open("../lab4/aula04_links.txt","r")
lines1 = file1.readlines()

dictionary2 = {}
for line in lines1:
    splits = line.split()
    doc = splits[0]
    dictionary2[doc] = []
    for i in xrange(1,len(splits)):
        dictionary2[doc].append(splits[i])
    
rank = PageRankAuto(dictionary2,0.15)


file3 = open("../lab3/aula03_queries.txt","r")
lines3 = file3.readlines()
average = {"Pr":0,"Re":0,"F1":0}

for i in range(0,len(lines3)/2):
    text = lines3[i*2+0];
    number_strings = lines3[i*2+1].split();
    expected = [int(el) for el in number_strings]
    result2 = searchL2R("../lab4/indexl4",text,20,rank,w)
  
    score2 = score(result2,expected)
    score2["query"]=text
    average["Pr"]+=score2["Pr"]
    average["Re"]+=score2["Re"]
    average["F1"]+=score2["F1"]
    print score2

















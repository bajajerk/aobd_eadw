import numpy as np
from numpy import linalg
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
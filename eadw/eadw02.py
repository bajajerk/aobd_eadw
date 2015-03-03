# -*- coding: UTF-8 -*-
from utils import InvertedIndex, Split, DocumentFrequency,\
    MinMaxDocumentFrequency

file = open("lab02_documents.txt","r")
lines = file.readlines()
index = InvertedIndex(lines,Split)
df = DocumentFrequency(lines,Split,*["with","the"])

print "Exercise 1"
print index

print "Exercise 2"
print "# documents = ", len(lines)

total_terms = 0
for word in index.keys():
    for doc in index[word].keys():
        total_terms += len(index[word][doc])

print "# terms = ", total_terms

print "# individual terms = ", len(index.keys())

print "df = ", df

print "min_max = ", MinMaxDocumentFrequency(df)
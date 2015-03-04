# -*- coding: UTF-8 -*-
from utils import InvertedIndex, Split, DocumentFrequency, \
    MinMaxDocumentFrequency, InverseDocumentFrequency


file = open("lab02_documents.txt","r")
lines = file.readlines()
file.close()
index = InvertedIndex(lines,Split)
df = DocumentFrequency(index,"with","the","lol","amorphous")
idf = InverseDocumentFrequency(index,len(lines),"with","the","lol","amorphous")

print "Exercise 1"
print index

print "Exercise 2"
print "# documents = ", len(lines)

total_terms = 0
for word in index.keys():
    for doc in index[word].keys():
        total_terms += index[word][doc]

print "# terms = ", total_terms

print "# individual terms = ", len(index.keys())

print "df = ", df

print "min_max = ", MinMaxDocumentFrequency(index,"with","the","lol","amorphous")

print "idf = ", idf

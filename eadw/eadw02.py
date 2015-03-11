# -*- coding: UTF-8 -*-
import sys

from utils import InvertedIndex, Split, DocumentFrequency, \
    MinMaxDocumentFrequency, InverseDocumentFrequency, DotProduct, SortByValue


args = sys.argv;
args.pop(0)
print "The arguments are: " , str(args)



file1 = open("lab02_documents.txt","r")
lines = file1.readlines()
file1.close()
index = InvertedIndex(lines,Split)
df = DocumentFrequency(index,*args)

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

print "min_max = ", MinMaxDocumentFrequency(index,*args)

for arg in args:
    print "idf("+arg+") = ", InverseDocumentFrequency(index,len(lines),arg)


print "Exercise 3"
dot = DotProduct(index,len(lines),*args)
print dot

print "Exercise 4"

while 1:
    word = raw_input("search: ")
    dot = DotProduct(index,len(lines),*Split(word))
    result = SortByValue(dot)
    result.reverse()
    print result



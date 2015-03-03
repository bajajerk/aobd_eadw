from utils import InvertedIndex, MySplitAscii

file1 = open("lab02_documents.txt","r")
lines1 = line = file1.readlines()

print "Exercise 1"
print InvertedIndex(lines1,MySplitAscii)


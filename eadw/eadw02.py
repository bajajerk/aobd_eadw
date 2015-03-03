from utils import InvertedIndex, SplitAscii

file1 = open("lab02_documents.txt","r")
lines1 = line = file1.readlines()

print "Exercise 1"
x = InvertedIndex(lines1,SplitAscii)
print x.keys()
print x['limited'].keys()

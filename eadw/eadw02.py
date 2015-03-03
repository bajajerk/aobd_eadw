# -*- coding: UTF-8 -*-
from utils import InvertedIndex, Split, StripSymbols

file1 = open("lab02_documents.txt","r")
lines1 = line = file1.readlines()

print "Exercise 1"
x = InvertedIndex(lines1,Split)
print x
print x.keys()
print x['we'].keys()
print x['we'][83]

print StripSymbols(u"olá, tudo fixe (porreiro)?,#fosga-se")


import json
print json.dumps(x,sort_keys=True, indent=4)
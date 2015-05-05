#!/usr/bin/python2.7
# -*- coding: utf8 -*-
import nltk



document = u"Python is a widely used general-purpose, high-level programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java. The language provides constructs intended to enable clear programs on both a small and large scale."

sentences = nltk.sent_tokenize(document)

for s in sentences:
    words = nltk.word_tokenize(s)
    print words
  
    tags = nltk.pos_tag(words) 
    print "\t",tags
    print nltk.ne_chunk(tags, binary=True)
    

print "Ex 2"

file = open("../lab3/aula03_cfc.txt","r")
lines = file.readlines()

for line in lines:
    partition = line.split(' ',1)
    id = int(partition[0])
    document = partition[1].replace('\n',' ').decode("UTF-8")
    sentences = nltk.sent_tokenize(document)
    entities = set()
    
    for s in sentences:
        words = nltk.word_tokenize(s)
        #print words
      
        tags = nltk.pos_tag(words)
        for tag in tags:
            if tag[1] == "NNP":
                entities.add(tag[0])
                
    print id,list(entities)

file.close()
#!/usr/bin/python2.7
# -*- coding: utf8 -*-
import nltk

stop_words = set({".",",",'"',"'","--","-",":","(",")","!","?"})
words = {}


file = open("common-english-words.txt","r")
lines = file.readlines()
for line in lines:
    tokens = line.split(',')
    for token in tokens:
        stop_words.add(token)

file = open("aula10_polarity.txt","r")
lines = file.readlines()



for line in lines:
    tokens = line.split()
    for i in range(1, len(tokens)):
        token = tokens[i]
        if token not in stop_words:
            if token not in words:
                words[token]=1
            else:
                words[token]+=1
            
file.close()



    
print "EX1"
print words
file.close()


print "EX2"
top_words = sorted(words.keys(), key=lambda entry: words[entry])
top_words.reverse()
top_words = set(top_words[:2000])

def featured(sentence):
    ret = {}
    for word in sentence.split():
        word = word.lower()
        ret[word]= word in top_words
        
    return ret

#print top_words

print featured("The quick brown fox jumps over the lazy dog")


print "EX3"
examples = []
for line in lines:
    tokens = line.split(' ',1)
    classif = True if tokens[0]=='+' else False 
    text = tokens[1]
    examples.append((featured(text),classif))
    
print examples
classifier = nltk.NaiveBayesClassifier.train(examples)


print classifier.classify(featured("the movie special effects was strange and didn't make any sense"))
print classifier.classify(featured("the movie special effects was outstanding although they didn't make any sense"))
print classifier.classify(featured("the movie special effects was outstanding and the actors were incredible"))
print classifier.classify(featured("the movie special effects was outstanding and the actors were incredibly stupid"))

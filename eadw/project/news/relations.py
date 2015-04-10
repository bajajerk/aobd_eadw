#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import nltk
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


stok = nltk.data.load('tokenizers/punkt/portuguese.pickle')

#nltk.download('all')

sentence = u"O Tribunal da Relação de Lisboa confirmou hoje a prisão preventiva de José Sócrates."

words = word_tokenize(sentence)
#tokens = nltk.word_tokenize(sentence)

#print stok.tokenize(sentence) 

tagged = pos_tag(words)   

chunks = ne_chunk(tagged)

chunks.draw()

ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words('english'))
NON_ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words()) - ENGLISH_STOPWORDS 
STOPWORDS_DICT = {lang: set(nltk.corpus.stopwords.words(lang)) for lang in nltk.corpus.stopwords.fileids()}


def get_language(text):
    words = set(nltk.wordpunct_tokenize(text.lower()))
    return max(((lang, len(words & stopwords)) for lang, stopwords in STOPWORDS_DICT.items()), key = lambda x: x[1])[0]
 

print get_language(sentence)

#stopwords = nltk.corpus.stopwords.words('portuguese')
#print stopwords
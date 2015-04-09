#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import nltk
from nltk.corpus import treebank

nltk.download('all')

sentence = "Hoje, José Sócrates foi ouvido no tribunal de Lisboa"

tokens = nltk.word_tokenize(sentence)

print tokens

t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
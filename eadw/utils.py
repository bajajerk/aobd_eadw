import unicodedata
import re
from math import log

def StripSymbols(text):
    if isinstance(text, unicode):
        text = unicodedata.normalize('NFKD',text).encode("ASCII","ignore")
    else:
        text = unicodedata.normalize('NFKD',unicode(text,"UTF-8")).encode("ASCII","ignore")
    
    res = []
    for c in text:
        if c.isalnum() or c.isspace() :
            res.append(c)
        else:
            res.append(' ')
            
            
    return re.sub(' +',' ',''.join(res))

def Split(text):
    return StripSymbols(text).lower().split()
    
def Count (tokens):
    result = {}
    for token in tokens:
        if token not in result:
            result[token] = 0
        result[token] += 1
    return result

def Intersection(tokens1,tokens2):
    return [val for val in tokens1 if val in tokens2]

def Quicksort(A):

    def QuicksortAux(A, low, high):
    
        def Partition(A , low, high):
            pivot = A[low]
            leftwall = low
            for i in range(low + 1, high) :
                if (A[i] < pivot) :
                    leftwall = leftwall + 1
                    A[i], A[leftwall]= A[leftwall],A[i]
            A[low],A[leftwall]=A[leftwall],A[low]
            return leftwall
        
        if (low < high):
            pivot_location = Partition(A,low,high)
            QuicksortAux(A,low, pivot_location - 1)
            QuicksortAux(A, pivot_location + 1, high)

    QuicksortAux(A, 0, len(A))
    return A


def SimpleInvertedIndex(lines,splitter):
    invertedIndex = {}
    for i in range(0, len(lines)):
        line = lines[i]
        tokens = splitter(line)
        for j in range(0,len(tokens)):
            word = tokens[j]  
            if word not in invertedIndex:
                invertedIndex[word] = []
            array =  invertedIndex[word]
            if i not in array:
                array.append(i)
    return invertedIndex

def InvertedIndex(lines,splitter):
    invertedIndex = {}
    for i in range(0, len(lines)):
        line = lines[i]
        tokens = splitter(line)
        for j in range(0,len(tokens)):
            word = tokens[j]  
            if word not in invertedIndex:
                invertedIndex[word] = {}
            obj =  invertedIndex[word]
            
            if i not in obj:
                obj[i]=0             

            obj[i] +=1;
            
    return invertedIndex

    
    

def DocumentFrequency(index,*words):
    result = {}    
    for word in words:
        result[word] = len(index[word]) if word in index.keys() else 0
            
    return result



def InverseDocumentFrequency(index,n,word):
    return log(float(n)/len(index[word])) if word in index.keys() else None

def MinMaxDocumentFrequency(index,*words):
    result = {}
    
    for word in words:
        result[word] = None
        
        if word in index.keys():
            for doc in index[word]:
                val = index[word][doc]
                if result[word] is None:
                    result[word] = [val,val]
                result[word][0] = min(result[word][0],val)
                result[word][1] = max(result[word][1],val)
            
    return result


def OverallFrequency(lines,words, splitter):
    result = {}

    for line in lines:
        for word in words:
            if word not in result:
                result[word] = 0
        
            tokens = splitter(line)    
            for token in tokens :
                if token == word : 
                    result[word] += 1
                            
    return result


def DotProduct(index,n,*terms):
    a = {}
    for term in terms:
        if term in index.keys():
            It = index[term]
            idft = InverseDocumentFrequency(index,n,term)
            print idft
            for pair in It:
                tfdt = It[pair]
                if pair not in a:
                    a[pair] = 0
                a[pair] += tfdt*idft
                    
            
    return a    
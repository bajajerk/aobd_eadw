import unicodedata

def StripSymbols(text):
    if isinstance(text, unicode):
        text = unicodedata.normalize('NFKD',text).encode("ASCII","ignore")
    else:
        text = unicodedata.normalize('NFKD',unicode(text,"UTF-8")).encode("ASCII","ignore")
    
    return ''.join(c for c in text if c.isalnum() or c.isspace());

def Split(text):
    return StripSymbols(text).lower().split()
    
def Count (tokens):
    count = {}
    for i in range(0, len(tokens)):
        key = tokens[i]
        if key not in count:
            count[key] = 0
        count[key] = count[key] +1
    return count

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
                obj[i]=[]                

            array = obj[i];
            array.append(j)
            
    return invertedIndex


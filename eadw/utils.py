def MySplit(text):
    return text.replace(',','').lower().split()
    
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


def newWord(x) :
    x = x[-1] + x[0 : -1]
    return x

def solution(A, B):
    if A == B :
        return 0
    
    for i in range(1, len(A) + 1) :        
        if newWord(A) == B :
            return i
        
        else :
            A = newWord(A)
            
    return -1
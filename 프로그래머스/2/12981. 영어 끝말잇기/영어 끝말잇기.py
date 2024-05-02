def solution(n, words):
    temp = []
    for i, j in enumerate(words) :
        if j not in temp : temp.append(j)
        else : 
            return [ i % n + 1, i // n + 1] 
        
        if i + 1 != len(words) :
            if j[-1] != words[i + 1][0] : 
                return [ (i + 1) % n + 1, (i + 1) // n + 1] 
            
    
    return [0, 0]
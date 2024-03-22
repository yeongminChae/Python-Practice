import math

def division_maker(m) :
    index = int(math.sqrt(m) )
    li = []
    
    for i in range(1, index + 1) :
        if m % i == 0 and i not in li :
            li.append(i)
            li.append(m // i)
    
    if len(li) < 3 :
        return False
    
    return True

def solution(n):
    answer = 0
    
    for i in range(1, n + 1) :
        if division_maker(i) :
            answer += 1
    
    return answer
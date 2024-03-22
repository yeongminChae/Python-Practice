import math

def solution(n):
    answer = []    
    temp = []
    
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0 :
            answer.append(i)
            
            if i != n // i :
                temp.append(n // i)
    answer.extend(reversed(temp))    
    
    return answer
import math

def solution(number, limit, power):
    answer = []
    
    for i in range(1, number + 1) :
        if makerFunc(i) <= limit : answer.append(makerFunc(i))
        else : answer.append(power)
            
    return sum(answer)

def makerFunc(i) :
    list1 = []
    for j in range(1, int(math.sqrt(i)) + 1) :
        if i % j == 0 : 
            list1.append(j)
            list1.append(i // j)
    return len(set(list1))
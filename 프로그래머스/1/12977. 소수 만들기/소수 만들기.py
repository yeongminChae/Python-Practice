from itertools import combinations 

def solution(nums):
    answer = 0
    for i in combinations(nums, 3) :
        if len(detector(sum(i))) == 2 : answer += 1
    
    return answer

def detector(m) :
    li1 = []
    for i in range(1, int(m ** 0.5) + 1) :
        if m % i != 0 : continue
        else : 
            li1.append(i)
            li1.append(m // i)
            
    return list(set(li1))
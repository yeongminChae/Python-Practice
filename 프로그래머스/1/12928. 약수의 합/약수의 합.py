import math

def solution(n):
    ans = []
    for i in range(1, math.ceil(math.sqrt(n)) + 1) :
        if n % i == 0 :
            ans.append(i)
            ans.append(n // i)
            
    return sum(set(ans))

# 1 2 4 8 16
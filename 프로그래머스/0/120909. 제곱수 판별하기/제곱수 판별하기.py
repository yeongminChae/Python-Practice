import math

def solution(n):
    num = int(math.sqrt(n))
    
    if n == num ** 2 :
        return 1
    
    return 2
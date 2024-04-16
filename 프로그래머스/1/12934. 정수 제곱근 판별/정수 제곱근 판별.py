import math

def solution(n):
    m = math.sqrt(n) 
    return -1 if n != int(m) ** 2 else (int(m) + 1) ** 2
import math

def solution(s):
    a = len(s)
    b = a // 2
    answer = s[math.ceil(b)] if a % 2 != 0 else s[b - 1 : b + 1]
    return answer

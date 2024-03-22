import math
# def factorial(n) :
#     if n == 1 :
#         return 1
#     return n * factorial(n - 1)

def combination(a, b) :
    return math.factorial(a) / (math.factorial(b) * math.factorial(a - b) )

def solution(balls, share):
    answer = combination(balls, share)
    return answer
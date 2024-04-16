def solution(n, m):
    answer = [func1(n, m), (n * m) // func1(n, m)]
    return answer

def func1(x, y) :
    while y : x, y = y, (x % y)
    return x


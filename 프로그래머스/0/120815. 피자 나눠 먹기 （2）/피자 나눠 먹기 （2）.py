def gcd(x, y) :
    while y :
        x, y = y, x % y
    return x

def solution(n):
    a = gcd(n, 6)
    b = (n * 6) // a
    return b // 6
    
from math import gcd

def solution(arr):
    a = arr[0]
    for i in arr[1 : ] :
        a = lcm(a, i)
    return a

def lcm(x, y):
    return x * y // gcd(x, y)
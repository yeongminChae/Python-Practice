import math

def solution(arr):
    while func1(len(arr)) == False :
        arr.append(0)
    return arr

def func1(n) :
    return n > 0 and (n & (n - 1)) == 0

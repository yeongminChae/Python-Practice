import sys

n = int(sys.stdin.readline())

def func(n) :
    a = 0
    length = len(str(n))
     
    for i in range(1, length):
        a += i * (10**i - 10**(i-1))
    
    a += length * (n - 10**(length-1) + 1)
    return a
    
print(func(n))    
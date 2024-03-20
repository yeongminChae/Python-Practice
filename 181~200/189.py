import sys

n = int(sys.stdin.readline())

def func(n) :
    a = map(int, sys.stdin.readline().split())
    a_sort = sorted(a)
    b = []
    
    for i in range(n) :
        b.append(a_sort[i] + b[i - 1] if i > 0 else a_sort[i])
    
    return sum(b)
    
print(func(n))    
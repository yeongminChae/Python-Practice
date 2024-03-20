import sys

n = int(sys.stdin.readline())

def func(n) :
    a = map(int, sys.stdin.readline().split())
    b = map(int, sys.stdin.readline().split())

    a_sort = sorted(a)
    b_sort = sorted(b, reverse=True)
    c = 0
    
    for i in range(len(a_sort)) :
        c += a_sort[i] * b_sort[i]
    
    return c        

print(func(n))

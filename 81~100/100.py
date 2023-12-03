import sys

def func() :
    a = 0
    b = 0
    
    for i in range(1, 6):    
        li1 = list(map(int, sys.stdin.readline().split()))
        
        if a < sum(li1) :
            a = sum(li1)
            b = i
        
    return b, a

c, d = func()
print(c, d)
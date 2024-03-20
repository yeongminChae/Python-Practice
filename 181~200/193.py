import sys

a, b = map(int, sys.stdin.readline().split())

def func(a, b):
    m = 0
    n = list(map(int, sys.stdin.readline().split()))
    
    for j, i in enumerate(n)  :
        m += i
        
        if m > b:
            print(j+1)
            break


func(a, b)
        
        
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

def func(n, k):
    q = [i for i in range(1, n+1)] 
    result = [] 
    index = 0 

    for _ in range(n):
        index += k-1 
        if index >= len(q): 
            index = index%len(q)
 
        result.append(str(q.pop(index)))
    return "<" + ", ".join(result) + ">"

    

print(func(n, m))

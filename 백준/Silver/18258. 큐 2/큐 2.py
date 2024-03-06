import sys
from collections import deque

n = int(sys.stdin.readline())

def func(n):
    dq = deque()
    for _ in range(n):
        a = deque(sys.stdin.readline().split())
        b = a[0]
        if b == 'push':
            dq.append(a[1])
        elif b == 'pop' :
            print(dq.popleft() if dq else -1)
        elif b == 'size' :
            print(len(dq))
        elif b == 'empty' :
            print(1 if len(dq) == 0 else 0)
        elif b == 'front' :
            print(dq[0] if dq else -1)
        elif b == 'back' :
            print(dq[-1] if dq else -1)
                        
    
    
func(n)        
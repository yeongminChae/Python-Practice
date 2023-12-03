import sys

def func() :
    li = []
    for _ in range(10) :
        n = int(sys.stdin.readline())
        li.append(n)
        
    a = max(li, key = li.count)
        
    print(sum(li) // len(li))
    print(a)

func()

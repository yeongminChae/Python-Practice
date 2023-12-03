import sys

n = int(sys.stdin.readline())

def func(n):
    for _ in range(n):
        a,b = sys.stdin.readline().split()
        li = []
        
        for i in b :
            li.append(i)
        
        li.pop(int(a) - 1)
        print(''.join(li))
        
func(n)

n = int(sys.stdin.readline())

def remove_typos(n):
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        typos = list(b)
        typos.pop(int(a) - 1)
        print(''.join(typos))

remove_typos(n)

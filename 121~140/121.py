import sys
n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        m = int(sys.stdin.readline())
        li = list(map(int, sys.stdin.readline().split()))
        print((max(li) - min(li)) * 2)


func(n)

import sys
n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        li = map(int, sys.stdin.readline().split())
        li2 = sorted(li, reverse=True)
        print(li2[2])


func(n)

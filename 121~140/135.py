import sys


def func():
    n, m = map(int, sys.stdin.readline().split())
    li_a = [sys.stdin.readline().split() for _ in range(n)]
    li_b = [sys.stdin.readline().split() for _ in range(m)]

    for i, j in zip(li_a, li_b):
        for a, b in zip(i, j):
            print(int(a) + int(b), end=" ")
        print()


func()

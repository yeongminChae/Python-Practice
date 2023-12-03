import sys

n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        a, b = map(int, input().split())
        print(a + b)


func(n)

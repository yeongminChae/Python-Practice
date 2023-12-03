import sys

n = int(sys.stdin.readline())


def func(n):
    a = 0
    for _ in range(n):
        a += int(sys.stdin.readline())
    return a - (n - 1)


print(func(n))

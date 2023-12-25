import sys


def func() -> str:
    n, m = map(int, sys.stdin.readline().split())
    a = str(n)
    b = ''
    while len(b) < m:
        b += a
    return b[:m]


print(func())

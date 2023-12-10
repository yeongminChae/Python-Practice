import sys


def func():
    a, b = sys.stdin.readline().split()
    c = int(a[::-1])
    d = int(b[::-1])
    m = str(c + d)

    return int(m[::-1])


print(func())

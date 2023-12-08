import sys


def func():
    n = sys.stdin.readline().split()
    li = sorted(map(int, n))

    return map(str, li)


a = func()
print(" ".join(a))

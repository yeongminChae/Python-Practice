import sys


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


def func():
    n, m = map(int, sys.stdin.readline().split())

    return factorial(n) // (factorial(m) * factorial(n - m))


print(func())

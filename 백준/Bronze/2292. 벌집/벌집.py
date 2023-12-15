import sys


def func():
    n = int(sys.stdin.readline())
    a = 1
    b = 1

    while n > a:
        a += (6 * b)
        b += 1

    return b


print(func())

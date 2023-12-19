import sys


def func():
    n = int(sys.stdin.readline())
    a = 0
    b = 665

    while a != n:
        b += 1
        if '666' in str(b):
            a += 1

    return b


print(func())

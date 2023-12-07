import sys


def func():
    li = ['a', 'e', 'i', 'o', 'u']
    a = sys.stdin.readline()
    b = 0

    for i in a:
        if i in li:
            b += 1

    return b


print(func())

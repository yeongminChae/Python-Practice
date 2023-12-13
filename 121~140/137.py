from itertools import zip_longest
import sys


def func():
    li = [list(map(str, sys.stdin.readline().strip())) for i in range(5)]
    a = ''
    b = 0

    for k in li:
        if len(k) > b:
            b = len(k)

    for i in range(b):
        for j in li:
            try:
                a += j[i]
            except IndexError:
                pass

    return a


# print(func())


def func2():
    li = [list(map(str, input().strip())) for i in range(5)]
    a = ''

    for chars in zip_longest(*li, fillvalue=''):
        a += ''.join(chars)

    return a


print(func2())

import sys


def func():
    a = sys.stdin.readline().split('-')
    b = ''

    for i in a:
        b += i[0]

    return b


print(func())

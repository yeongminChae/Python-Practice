import sys


def func():
    li = list(map(int, sys.stdin.readline().split()))
    li1 = sorted(li)
    li2 = sorted(li, reverse=True)

    if li == li1:
        return 'ascending'
    elif li == li2:
        return 'descending'
    else:
        return 'mixed'


print(func())

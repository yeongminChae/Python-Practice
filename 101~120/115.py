import sys


def func():
    li = []
    for _ in range(5):
        n = int(sys.stdin.readline())
        li.append(n)

    m = min(li[0:3])
    k = min(li[3:])

    return (m + k) - 50


print(func())

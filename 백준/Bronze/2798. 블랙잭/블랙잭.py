import sys
import itertools


def func():
    a, b = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    li2 = list(itertools.combinations(li, 3))
    li3 = [sum(i) for i in li2]
    li3 = list(filter(lambda x: x <= b, li3))

    return max(li3)


print(func())

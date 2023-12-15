import sys


def count(n):
    li = list(map(int, str(n)))
    return sum(li) + n


def func():
    n = int(sys.stdin.readline())
    a = len(str(n))

    for j in range(max(0, n - (a * 9)), n):
        if count(j) == n:
            return j
    return 0


print(func())

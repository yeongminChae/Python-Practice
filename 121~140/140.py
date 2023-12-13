import sys

n = int(sys.stdin.readline())


def func(n):
    a = 2

    for _ in range(1, n + 1):
        a = (2 * a) - 1

    return (a ** 2)


print(func(n))

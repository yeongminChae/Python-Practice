import sys
n = int(sys.stdin.readline())


def func(n):
    a = sys.stdin.readline().split()
    li = sorted(map(int, a))

    if n != 1:
        return li[0] * li[-1]
    else:
        return li[0] ** 2


print(func(n))

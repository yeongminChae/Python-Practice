import sys

n = int(sys.stdin.readline())


def func(n):
    li = []
    li2 = []
    a = 0

    for i in range(0, n+1):
        for j in range(i, n+1):
            li.append((i, j))

    for k in li:
        if k[0] != 0 or k[1] != 0:
            a += k[0] + k[1]
    return a


# print(func(n))


n = int(sys.stdin.readline())


def func2(n):
    return n * (n + 1) * (n + 2) // 2


print(func2(n))

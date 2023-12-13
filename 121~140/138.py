import sys
n = int(sys.stdin.readline())


def func(n):
    li1 = [[0] * 100 for _ in range(100)]

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                li1[i][j] = 1

    a = sum(li1, []).count(1)
    return a


print(func(n))

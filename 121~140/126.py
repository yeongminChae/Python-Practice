import sys


def func():
    a, b = map(int, sys.stdin.readline().split())
    li = [int(sys.stdin.readline()) for _ in range(a)]
    c = 0

    for i in range(a-1, -1, -1):
        if b == 0:
            break
        if li[i] > b:
            continue
        c += b // li[i]
        b %= li[i]

    print(c)


func()

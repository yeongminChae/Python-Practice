import sys


def func():
    li = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    a = 0
    b = 1
    c = 1

    for i in li:
        if a < max(i):
            a = max(i)
            b = li.index(i) + 1
            c = i.index(a) + 1

    print(a)
    print(' '.join(map(str, (b, c))))


func()

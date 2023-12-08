import sys
n = int(sys.stdin.readline())


def func(n):
    li = []
    for _ in range(n):
        n = int(sys.stdin.readline())
        li.append(n)

    li.sort()

    return li


for i in func(n):
    print(i)

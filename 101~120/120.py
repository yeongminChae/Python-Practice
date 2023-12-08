import sys
n = int(sys.stdin.readline())


def func(n):
    li = []
    for _ in range(n):
        a = int(sys.stdin.readline())
        if a == 0:
            li.pop()
        else:
            li.append(a)

    return li


print(sum(func(n)))

import sys

n = int(sys.stdin.readline())


def func(n):
    li = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        li.append((a, b))

    return sorted(li)


c = func(n)
for i in c:
    print(" ".join(map(str, i)))

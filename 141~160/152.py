import sys

n = int(sys.stdin.readline())


def func(n):
    li = []
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        li.append((a, b))

    return sorted(li, key=lambda x: int(x[0]))


a = func(n)
for i in a:
    print(" ".join(i))

import sys

n = int(sys.stdin.readline())


def func(n):
    li = []
    for _ in range(n):
        a = sys.stdin.readline().strip()
        li.append((len(a), a))

    li = set(li)
    return sorted(li)


b = func(n)

for i in b:
    print(i[1])

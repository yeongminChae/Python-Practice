import sys

n = int(sys.stdin.readline())


def func(m):
    li = []

    for _ in range(n):
        a = int(sys.stdin.readline())
        li.append(a)

    return sorted(li)


b = map(str, func(n))

print('\n'.join(b))

import sys

n = int(sys.stdin.readline())


def func(n):
    if n == 0:
        return 0

    li = list(int(sys.stdin.readline().strip()) for _ in range(n))
    li = sorted(li)
    a = round(n * 0.3)
    if a > n // 2:
        a = 0

    b = sum(li[a:-a or None])

    return round(b / len(li[a:-a]) if li[a:-a] else 0)


print(func(n))

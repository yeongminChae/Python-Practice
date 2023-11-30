import math

n, m = map(int, input().split())


def func(n):
    li = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            li.append(i)
            li.append(n // i)

    return sorted(set(li))


a = func(n)
if len(a) < m:
    print(0)
else:
    print(a[m - 1])

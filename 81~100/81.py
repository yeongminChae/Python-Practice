n, m = map(int, input().split())


def func2(a):
    if a == 1:
        return False
    if a == 2:
        return True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


def func(n, m):
    li = [i for i in range(n, m + 1) if func2(n)]

    return li


b = func(n, m)

if len(b) == 0:
    print(-1)
else:
    print(sum(b))
    print(min(b))

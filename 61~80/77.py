n, m = map(int, input().split())


def func(n, m):
    while (m):
        n, m = m, n % m

    return n


a = func(n, m)
print(a)
print(n * m // a)

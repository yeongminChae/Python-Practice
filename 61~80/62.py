n = int(input())


def func(n):
    l = 100
    m = 100

    for _ in range(n):

        a, b = map(int, input().split())

        if a > b:
            m -= a
        elif a < b:
            l -= b
        else:
            continue

    return l, m


c = func(n)
for i in c:
    print(i)

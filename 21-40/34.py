n = int(input())


def func(n):
    m = 0
    for _ in range(1, n + 1):
        a = input()

        if list(a) == sorted(a, key=a.find):
            m += 1

    return m


print(func(n))

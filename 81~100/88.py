n = int(input())


def func(n):
    i = 0
    for _ in range(n):
        a, b = map(int, input().split())

        i += b % a

    return i


print(func(n))

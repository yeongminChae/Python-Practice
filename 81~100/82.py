n = int(input())


def func(n):
    a = 1
    for i in range(1, n+1):
        a *= i

    return a


print(func(n))

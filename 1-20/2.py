n = int(input())


def func(n):
    a = n // 100
    b = (n % 100) // 10
    c = (n % 100) % 10
    print(a, b, c)


func(n)

n = int(input())


def func(n):
    a = "*"

    for i in range(1, 2 * n):
        print(f"{a * (n - abs(n - i))}")


func(n)

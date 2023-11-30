n = int(input())


def func(n):
    a = "*"
    b = " "

    for i in range(1, n + 1):
        print(f"{b * (i - 1)}{a * (2 * n - (i * 2 - 1))}")


func(n)

n = int(input())


def func(n):
    a = "*"
    b = " "

    for i in range(1, 2 * n):
        print(f"{b * abs(n - i)}{a * (n - abs(n - i))}")


func(n)

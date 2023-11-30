n = int(input())


def func(n):
    a = "*"
    b = " "

    for i in range(1, 2 * n):
        c = b * (n - (abs(i - n)) - 1)
        d = a * (2 * n - ((2 * (n - abs(n - i))) - 1))
        print(f"{c}{d}")


func(n)

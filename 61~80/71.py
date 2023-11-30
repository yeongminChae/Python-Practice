n = int(input())


def func(n):
    a = "*"
    b = " "

    for i in range(1, 2 * n):
        c = a * (n - abs(i - n))
        d = b * abs(n - i)
        print(f"{c}{d}{d}{c}")


func(n)

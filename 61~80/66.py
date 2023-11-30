n = int(input())


def func(n):
    a = "*"
    b = " "

    for i in range(n):
        print(f"{a * (n - i)}{b * i}")


func(n)

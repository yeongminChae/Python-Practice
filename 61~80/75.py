n = int(input())


def func(n):
    a = "* "
    b = " "

    for i in range(1, n+1):
        print(f"{b * (n - i)}{a * i}")


func(n)

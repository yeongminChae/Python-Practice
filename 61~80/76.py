n = int(input())


def func(n):
    a = "* "
    b = " "

    for i in range(1, n+1):
        if i % 2 != 0:
            print(a * n)
        else:
            print(f"{b}{a * n}")


func(n)

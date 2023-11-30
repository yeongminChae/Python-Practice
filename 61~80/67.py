n = int(input())


def func(n):
    a = "*"
    b = " "

    for i in range(n):
        print(f"{b * i}{a * (n - i)}")


func(n)

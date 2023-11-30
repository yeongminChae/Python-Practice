n = int(input())


def func(n):
    a = "*"
    b = " "

    for i in range(1, n * 2):
        print(f"{abs(i - n) * b}{(2 * (n -abs(i - n)) - 1) * a}")


func(n)

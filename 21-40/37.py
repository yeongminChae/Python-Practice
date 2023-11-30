a = int(input())
b = int(input())
c = int(input())


def func(a, b, c):
    n = a * b * c
    for i in range(0, 10):
        print(f"{str(n).count(str(i))}")


func(a, b, c)

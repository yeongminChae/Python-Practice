n = int(input())


def func(n):

    for _ in range(n):
        m = int(input())
        l = int(input())

        for _ in range(l):
            a, b = map(int, input().split())
            m += a * b

        print(m)


func(n)

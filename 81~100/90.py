T = int(input())


def func(T):
    for _ in range(T):
        li = []
        c = 0
        d = 0
        n = int(input())

        for _ in range(n):
            a, b = input().split()
            li.append((int(a), float(b)))

        for i in li:
            c += i[0]
            d += i[0] * i[1]

        print(c)
        print(round(d / c))


func(T)

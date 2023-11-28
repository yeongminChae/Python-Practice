n = int(input())


def func(n):

    for _ in range(n):
        a = input()
        b = 0
        c = 0

        for i in a:
            if i == "O":
                b += 1
                c += b
            else:
                b = 0

        print(c)


func(n)

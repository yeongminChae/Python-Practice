n = int(input())


def func(n):
    li = []
    for _ in range(1, n+1):
        a = input()
        b = 0
        c = 0

        for i in a:
            if i == "O":
                c += 1
                b += c
            else:
                c = 0

        li.append(b)
    return li


li2 = func(n)
for i in li2:
    print(li2)

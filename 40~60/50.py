a = input()


def func(a):
    n = 0
    m = 0
    k = 10

    for i in range(len(a)):
        if i + 1 == len(a):
            break
        if a[i] == a[i + 1]:
            n += 1
        else:
            m += 1

    a = k + n*5 + m*10
    return a


print(func(a))


def func(a):
    height = 10
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            height += 5
        else:
            height += 10
    return height


a = input()
print(func(a))

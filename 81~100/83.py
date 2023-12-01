n = int(input())


def func(n):
    li = [0, 1]
    for i in range(1, n+1):
        li.append(li[i] + li[(i - 1)])

    return li[n]


print(func(n))

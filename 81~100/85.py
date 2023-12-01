n = int(input())


def func(n):
    li = []
    for _ in range(9):
        li.append(int(input()))

    return n - sum(li)


print(func(n))

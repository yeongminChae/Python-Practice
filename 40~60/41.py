a, b, c = map(int, input().split())


def func(a, b, c):
    li = [a, b, c]
    li.sort()
    return (li[1])


print(func(a, b, c))

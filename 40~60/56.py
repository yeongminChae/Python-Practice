S = int(input())


def func(S):
    li = []
    i = 0
    n = 0
    m = ((S + 1) - i)

    while i != S // 2:
        n += i + m
        li.append(i)
        li.append(m)
        i += 1

    return len(li)


print(func(S))

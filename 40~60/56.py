S = int(input())


def func(S):
    a = 0
    for i in range(1, S+1):
        a += i

    return a


print(func(S))

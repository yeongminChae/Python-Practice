N = int(input())


def func(N):
    li = []
    for _ in range(N):
        li.append(int(input()))

    if li.count(1) > li.count(0):
        return "Junhee is cute!"
    else:
        return "Junhee is not cute!"


print(func(N))

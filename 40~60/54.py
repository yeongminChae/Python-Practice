N = int(input())


def func(N):
    li = []

    for _ in range(N):
        a, b, c = map(int, input().split())
        if a + c > b:
            li.append("do not advertise")
        elif a + c == b:
            li.append("does not matter")
        else:
            li.append("advertise")

    return li


print("\n".join(func(N)))

V = int(input())


def func(V):
    a = input()
    b = len(a) / 2

    for i in range(len(a)):
        if a.count(a[i]) > b:
            return a[i]
        elif a.count(a[i]) == b:
            return "Tie"
        else:
            if a[a.index(a[i])] != a[i]:
                return a[i]


print(func(V))

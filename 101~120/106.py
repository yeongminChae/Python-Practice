import sys


def func():
    li1 = []
    li2 = []

    for i in range(20):
        n = int(sys.stdin.readline())

        if i >= 10:
            li2.append(n)
        else:
            li1.append(n)

    li1.sort(reverse=True)
    li2.sort(reverse=True)

    a = sum(li1[:3])
    b = sum(li2[:3])

    return a, b


c = func()
print(c[0], c[1])

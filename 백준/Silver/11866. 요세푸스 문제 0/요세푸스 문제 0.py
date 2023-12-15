import sys


def func():
    a, b = map(int, sys.stdin.readline().split())
    li = [i for i in range(1, a + 1)]
    c = 0
    li2 = []

    while li:
        c = (c + b - 1) % len(li)
        li2.append(str(li.pop(c)))

    return li2


m = func()
print("<" + ", ".join(m) + ">")

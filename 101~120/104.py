import sys


def func():
    li = []
    li3 = []
    a = 0
    for i in range(8):
        n = int(sys.stdin.readline())
        li.append((n, i + 1))
    li2 = sorted(li, reverse=True)

    for i in range(5):
        a += li2[i][0]
        li3.append(li2[i][1])
    li3.sort()

    print(a)
    print(" ".join(map(str, li3)))


func()

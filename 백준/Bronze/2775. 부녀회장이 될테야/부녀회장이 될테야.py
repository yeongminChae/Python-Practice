import sys

n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        m = int(sys.stdin.readline())
        k = int(sys.stdin.readline())
        li = []

        for i in range(0, m + 1):
            if i == 0:
                li.append([j for j in range(1, k + 1)])
            else:
                li.append([sum(li[i - 1][0: k])
                          for k in range(1, len(li[i - 1]) + 1)])

        print(li[m][k - 1])


func(n)

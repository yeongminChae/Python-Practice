import sys
n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):

        li = map(int, sys.stdin.readline().split())
        li2 = sorted(li, reverse=True)

        if max(li2[1:4]) - min(li2[1:4]) >= 4:
            print("KIN")
        else:
            print(sum(li2[1:4]))


func(n)

import sys


def func():
    while True:
        li = list(map(int, sys.stdin.readline().split()))

        if li.count(0) != 0:
            break

        li2 = sorted(li)

        if (li2[0] ** 2) + (li2[1] ** 2) == (li2[2] ** 2):
            print('right')
        else:
            print('wrong')


func()

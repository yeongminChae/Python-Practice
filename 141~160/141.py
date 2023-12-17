import sys


def func():

    while True:
        n = sys.stdin.readline().strip()
        if n == '0':
            break

        if n[::-1] == n:
            print('yes')
        else:
            print('no')


func()

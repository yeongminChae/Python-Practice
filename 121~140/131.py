import sys


def func():
    while True:
        a = sys.stdin.readline().strip()
        if a == 'END':
            break
        else:
            print(a[::-1])


func()

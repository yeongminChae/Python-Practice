import sys


def func():
    a = sys.stdin.readline().strip()
    b = len(a) // 10

    for i in range(b + 1):
        print(a[i * 10: 10 + (i * 10)])


func()

import sys


def func():
    a = sys.stdin.readline().split(",")
    b = 0

    for i in a:
        try:
            int(i)
            b += 1
        except:
            print("error")

    return b


print(func())

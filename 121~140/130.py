import sys
n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        a = sys.stdin.readline().strip()
        b = a[0].upper() + a[1:]
        print(b)


func(n)

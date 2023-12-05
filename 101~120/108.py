import sys
n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        m = 0

        for i in range(a, b+1):
            m += str(i).count('0')

        print(m)


func(n)

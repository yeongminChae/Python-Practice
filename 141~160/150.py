import sys

n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        m = c % a if c % a != 0 else a
        k = (c - 1) // a + 1

        print(m * 100 + k)


func(n)

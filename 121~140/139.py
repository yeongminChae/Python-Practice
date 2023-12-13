import sys

n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        a = int(sys.stdin.readline())

        b = a // 25
        c = (a % 25) // 10
        d = ((a % 25) % 10) // 5
        e = ((a % 25) % 10) % 5

        print(' '.join(map(str, (b, c, d, e))))


func(n)

import sys

n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        n = int(sys.stdin.readline())
        m = [i for i in bin(n)[2:]]

        m.reverse()

        for i in range(0, len(m)):
            if m[i] == '1':
                print(i, end=' ')


func(n)

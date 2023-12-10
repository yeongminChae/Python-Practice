import sys
n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        li = list(map(int, sys.stdin.readline().split()))
        li2 = list(filter(lambda x: x % 2 == 0, li))

        print(" ".join(map(str, (sum(li2), min(li2)))))


func(n)

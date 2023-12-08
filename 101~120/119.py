import sys
n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        li = [int(sys.stdin.readline()) for _ in range(a)]
        print(a - len(set(li)))


func(n)


def func(n):
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        seats = [0]*b
        fail = 0
        for _ in range(a):
            seat = int(sys.stdin.readline())
            if seats[seat-1] == 0:
                seats[seat-1] = 1
            else:
                fail += 1
        print(fail)


n = int(sys.stdin.readline())
func(n)

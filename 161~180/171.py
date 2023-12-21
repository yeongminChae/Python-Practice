import sys
from collections import deque

a = int(sys.stdin.readline())


def func(a):
    dq = deque()
    for _ in range(a):
        n, m = map(int, sys.stdin.readline().split())
        dq.append((n, m))

    for i in range(a):
        m = 1
        for j in range(a):
            if dq[i][0] < dq[j][0] and dq[i][1] < dq[j][1]:
                m += 1
        print(m, end=' ')


func(a)

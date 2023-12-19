import sys
from collections import deque


def func():
    n = int(sys.stdin.readline())
    dq = deque()

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        dq.append((a, b))

    return sorted(dq, key=lambda x: (x[1], x[0]))


m = func()
for i in m:
    print(" ".join(map(str, i)))

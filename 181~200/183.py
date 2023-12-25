import sys
from collections import deque


def func() -> deque:
    n = int(sys.stdin.readline())
    dq1 = set(sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    dq2 = deque(sys.stdin.readline().split())

    return deque(1 if i in dq1 else 0 for i in dq2)


print(" ".join(map(str, func())))

import sys
from collections import deque


def func():
    n = int(sys.stdin.readline())
    dq = deque(range(1, n + 1))

    while len(dq) > 1:
        dq.popleft()
        dq.append(dq.popleft())

    return dq[0]


print(func())

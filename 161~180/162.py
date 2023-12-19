import sys
from collections import deque, Counter


def func():
    dq1 = deque()
    dq2 = deque()

    a = int(sys.stdin.readline())
    dq1 = deque(map(int, sys.stdin.readline().split()))

    b = int(sys.stdin.readline())
    dq2 = deque(map(int, sys.stdin.readline().split()))

    counter = Counter(dq1)

    for i in dq2:
        print(counter[i], end=' ')


func()

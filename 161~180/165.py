import sys
from collections import deque


def func():
    n = int(sys.stdin.readline())
    dq = deque(sys.stdin.readline().strip())
    a = 0

    for i, j in enumerate(dq):
        a += ((ord(j) - 96)*(31 ** i)) % 1234567891

    return a % 1234567891


print(func())

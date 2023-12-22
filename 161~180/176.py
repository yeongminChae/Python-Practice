import sys
from collections import deque


def func():
    n, m = map(int, sys.stdin.readline().split())
    dq1 = deque(int(sys.stdin.readline().strip()) for _ in range(n))

    left = 1
    right = max(dq1)
    max_mid = 0

    while left <= right:
        mid = (left + right) // 2
        dq2 = deque(i // mid for i in dq1)

        if sum(dq2) < m:
            right = mid - 1
        elif sum(dq2) >= m:
            max_mid = mid
            left = mid + 1

    return max_mid


print(func())

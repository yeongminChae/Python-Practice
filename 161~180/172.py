import sys
import math
from collections import deque


def func():
    a, b = map(int, sys.stdin.readline().split())
    dq = deque([i for i in range(a, b + 1) if i % 2 != 0 or i == 2])

    for i in dq:
        if i == 1:
            continue

        is_prime = True

        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            print(i)


func()

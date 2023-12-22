import sys
from collections import deque


def func():
    n = int(sys.stdin.readline().strip())
    dq1 = deque(int(sys.stdin.readline().strip()) for _ in range(n))
    dq2 = deque()
    dq3 = deque()
    m = 1

    for i in dq1:
        while m <= i:
            dq2.append(m)
            dq3.append('+')
            m += 1
        if dq2[-1] == i:
            dq2.pop()
            dq3.append('-')
        else:
            print('NO')
            exit(0)

    return '\n'.join(dq3)


print(func())

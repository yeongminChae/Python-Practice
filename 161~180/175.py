import sys
from collections import deque, Counter

n = int(sys.stdin.readline().strip())


def func(n):
    dq = deque(sorted(int(sys.stdin.readline()) for _ in range(n)))
    a = sorted(i for i, j in Counter(dq).items()
               if j == Counter(dq).most_common(1)[0][1])

    if len(a) > 1:
        b = a[1]
    else:
        b = a[0]

    print(round(sum(dq) / n))
    print(dq[n // 2])
    print(b)
    print(dq[-1] - dq[0])


func(n)

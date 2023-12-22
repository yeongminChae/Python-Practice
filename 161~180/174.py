import sys
from collections import deque

n = int(sys.stdin.readline().strip())


def func(n):
    for _ in range(n):
        n, m = map(int, sys.stdin.readline().split())
        dq1 = deque(sys.stdin.readline().split())
        dq2 = deque([(i, int(dq1[i])) for i in range(n)])

        k = 0
        while dq2:
            a = dq2.popleft()

            if any(a[1] < i[1] for i in dq2):
                dq2.append(a)
            else:
                k += 1
                if a[0] == m:
                    print(k)
                    break


func(n)


# any()는 파이썬의 내장 함수로, 주어진 반복 가능한(iterable) 자료형(예: 리스트, 튜플, 딕셔너리 등)에 대해 어느 하나라도 참(True)이면 True를 반환하는 함수입니다.

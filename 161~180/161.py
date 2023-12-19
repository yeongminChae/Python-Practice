import sys
from collections import deque

n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        a = sys.stdin.readline().strip()
        dq = deque()

        for i in a:
            if i == '(':
                dq.append(i)
            elif i == ')':
                if dq:
                    dq.pop()
                else:
                    print('NO')
                    break

        else:
            if dq:
                print('NO')
            else:
                print('YES')


func(n)

#  파이썬에서는 for문이나 while문에 대응하는 else문을 작성할 수 있습니다.
# for 또는 while문의 else문은 해당 반복문이 완전히 종료된 후
# (즉, 반복할 요소가 더 이상 없거나, 조건이 False가 된 후)에 실행됩니다.
# 다만, 만약 반복문이 break문에 의해 중간에 종료된다면, else문은 실행되지 않습니다.

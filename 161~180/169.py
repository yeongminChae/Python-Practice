import sys
from collections import deque


def func():
    while True:
        a = sys.stdin.readline()
        if a[0] == '.':
            break

        dq = deque()

        for i in a:
            if i == '(' or i == '[':
                dq.append(i)
            elif i == ')':
                if dq and dq[-1] == '(':
                    dq.pop()
                else:
                    print('no')
                    break

            elif i == ']':
                if dq and dq[-1] == '[':
                    dq.pop()
                else:
                    print('no')
                    break
        else:
            if len(dq) == 0:
                print('yes')
            else:
                print('no')


func()

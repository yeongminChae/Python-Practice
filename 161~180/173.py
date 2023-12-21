import sys
from collections import deque


def func() -> bool:
    a = sys.stdin.readline().split()
    b = ''

    for i in a:
        for j in i:
            if ord(j.lower()) >= 97 and ord(j.lower()) <= 123:
                b += j

    return True if b == b[::-1] else False


# print(func())


def isPallindrome(self, s: str) -> bool:
    strs = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def func2() -> bool:
    a = sys.stdin.readline().strip()
    dq = deque(
        i for i in a
        if i.isalnum()
        # 정규식 ([^a-z0-9])
        # if ord(i.lower()) >= 97 and ord(i.lower()) <= 123

    )

    b = "".join(dq)

    return True if b == b[::-1] else False


print(func2())

import sys
from collections import deque


def func():
    n = int(sys.stdin.readline())
    dq = deque(range(1, n + 1))

    while len(dq) > 1:
        dq.popleft()
        dq.append(dq.popleft())

    return dq[0]


print(func())


# 다음은 deque의 주요 메소드들입니다:

# append(x): 덱의 오른쪽 끝에 x를 추가합니다.
# appendleft(x): 덱의 왼쪽 끝에 x를 추가합니다.
# pop(): 덱의 오른쪽 끝 요소를 제거하고 반환합니다. 덱이 비어 있으면 IndexError를 일으킵니다.
# popleft(): 덱의 왼쪽 끝 요소를 제거하고 반환합니다. 덱이 비어 있으면 IndexError를 일으킵니다.
# extend(iterable): iterable의 요소를 덱의 오른쪽에 추가합니다.
# extendleft(iterable): iterable의 요소를 덱의 왼쪽에 추가합니다.
# remove(value): 덱에서 value를 찾아 제거합니다. value가 없으면 ValueError를 일으킵니다.
# rotate(n=1): 덱을 오른쪽으로 n 단계 회전합니다. 만약 n이 음수라면 왼쪽으로 회전합니다.

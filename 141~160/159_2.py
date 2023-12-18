import sys
from collections import deque


def push_front(dq, x):
    dq.appendleft(x)


def push_back(dq, x):
    dq.append(x)


def pop_front(dq):
    return dq.popleft() if dq else -1
    # 파이썬은 컬렉션이 비어있다면 객체를 false로 취급한다.


def pop_back(dq):
    return dq.pop() if dq else -1


def size(dq):
    return len(dq)


def is_empty(dq):
    return 0 if dq else 1


def front(dq):
    return dq[0] if dq else -1


def back(dq):
    return dq[-1] if dq else -1


def func():
    n = int(sys.stdin.readline())
    dq = deque()
    command = {
        "push_front": push_front,
        "push_back": push_back,
        "pop_front": pop_front,
        "pop_back": pop_back,
        "size": size,
        "empty": is_empty,
        "front": front,
        "back": back
    }

    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] in ("push_front", "push_back"):
            command[cmd[0]](dq, cmd[1])
        else:
            print(command[cmd[0]](dq))


if __name__ == "__main__":
    func()

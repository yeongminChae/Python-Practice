import sys
from collections import deque


def push(dq, x):
    dq.append(x)


def pop(dq):
    return dq.popleft() if dq else -1


def size(dq):
    return len(dq)


def empty(dq):
    return 0 if dq else 1


def front(dq):
    return dq[0] if dq else -1


def back(dq):
    return dq[-1] if dq else -1


def func():
    n = int(sys.stdin.readline())
    dq = deque()
    command = {
        'push': push,
        'pop': pop,
        'size': size,
        'empty': empty,
        'front': front,
        'back': back
    }

    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] in ('push'):
            command[cmd[0]](dq, cmd[1])
        else:
            print(command[cmd[0]](dq))


if __name__ == '__main__':
    func()

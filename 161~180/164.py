import sys
from collections import deque


def push(dq, x):
    dq.append(x)


def pop(dq):
    return dq.pop() if dq else -1


def size(dq):
    return len(dq)


def empty(dq):
    return 0 if dq else 1


def top(dq):
    return dq[-1] if dq else -1


def func():
    n = int(sys.stdin.readline())
    dq = deque()
    command = {
        "push": push,
        "pop": pop,
        "size": size,
        "empty": empty,
        "top": top
    }

    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] in ('push'):
            command[cmd[0]](dq, cmd[1])
        else:
            print(command[cmd[0]](dq))


if __name__ == '__main__':
    func()


# 스택(Stack)은 '나중에 들어온 데이터가 먼저 나가는' (Last-In-First-Out, LIFO) 특성을 가지고 있습니다.
# 따라서 스택에서는 데이터를 추가할 때는 append를 사용하고, 데이터를 빼낼 때는 pop을 사용합니다.
# 이렇게 하면 가장 마지막에 들어온 데이터가 가장 먼저 나가게 됩니다.

# 큐(Queue)는 '먼저 들어온 데이터가 먼저 나가는' (First-In-First-Out, FIFO) 특성을 가지고 있습니다.
# 따라서 큐에서는 데이터를 추가할 때는 append를 사용하고, 데이터를 빼낼 때는 popleft를 사용합니다.
# 이렇게 하면 가장 먼저 들어온 데이터가 가장 먼저 나가게 됩니다.

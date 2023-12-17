import sys


def func():
    a, b, v = map(int, sys.stdin.readline().split())

    return ((v - b - 1) // (a - b)) + 1


print(func())

# (v - b - 1) -> 낮에 총 올라가야 하는 값
# (a - b) -> 실제로 올라간 값

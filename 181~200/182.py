import sys
import math

p = int(sys.stdin.readline())


def func() -> int:
    a, b = map(int, sys.stdin.readline().split())

    n = math.factorial(a)
    m = math.factorial(b)
    o = math.factorial(b - a)

    return m // (n * o)


for _ in range(p):
    print(func())

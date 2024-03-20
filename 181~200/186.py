import sys


def func() -> str:
    n = int(sys.stdin.readline().strip())

    if n % 4 == 0:
        return "CY"
    else:
        return "SK"


print(func())

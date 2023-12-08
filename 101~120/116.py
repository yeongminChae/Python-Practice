import sys


def func():
    li = [int(sys.stdin.readline()) for _ in range(5)]
    return sorted(li)


a = func()
print(sum(a) // len(a))
print(a[len(a) // 2])

import sys


def func():
    li = []
    a = sys.stdin.readline()
    for i in a:
        li.append(i)

    return sorted(li[:-1], reverse=True)


a = func()
print("".join(a))


def func():
    a = sys.stdin.readline().strip()
    li = sorted(a, reverse=True)

    return "".join(li)


print(func())

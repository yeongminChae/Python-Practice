import sys


def func():
    a = sys.stdin.readline().strip()
    li1 = [ord(i) for i in a]
    li2 = []
    for i in range(97, 123):
        li2.append(li1.count(i))

    return map(str, li2)


b = func()
print(" ".join(b))

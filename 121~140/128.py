import sys


def func():
    a = sys.stdin.readline().strip()
    li = [ord(i) for i in a]
    li2 = []

    for i in li:
        if i >= 97 and i < 123:
            li2.append(chr(i - 32))
        else:
            li2.append(chr(i + 32))

    return li2


b = func()
print("".join(b))

import sys


def func():
    a = sys.stdin.readline().strip()
    b = ''

    for i in a:
        if i.isupper():
            b += chr((ord(i) - ord('A') + 13) % 26 + ord('A'))
        elif i.islower():
            b += chr((ord(i) - ord('a') + 13) % 26 + ord('a'))
        else:
            b += i

    return b


print(func())

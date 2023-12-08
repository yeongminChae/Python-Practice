import sys
import random


def func():
    li = []
    a = 0
    for _ in range(9):
        n = int(sys.stdin.readline())
        li.append(n)

    while True:
        random.shuffle(li)
        if sum(li[0:7]) == 100:
            return sorted(li[0:7])


a = map(str, func())
print("\n".join(a))


def find_dwarfs():
    dwarfs = [int(sys.stdin.readline()) for _ in range(9)]
    total = sum(dwarfs)

    for i in range(9):
        for j in range(i+1, 9):
            if total - dwarfs[i] - dwarfs[j] == 100:
                del dwarfs[j]
                del dwarfs[i]
                return sorted(dwarfs)


dwarfs = find_dwarfs()
for dwarf in dwarfs:
    print(dwarf)

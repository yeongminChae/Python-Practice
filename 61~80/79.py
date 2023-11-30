import math

n = int(input())
li = list(map(int, input().split()))


def func(li):
    a = 0

    for i in li:
        if i == 1:
            continue

        b = True
        for j in range(2, int(math.sqrt(int(i)))+1):
            if i % j == 0:
                b = False
                break

        if b:
            a += 1

    return a


print(func(li))

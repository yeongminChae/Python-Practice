import math

M = int(input())
N = int(input())


def func(M, N):
    li1 = []
    for i in range(M, N+1):
        li2 = []
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                li2.append(j)
                li2.append(i//j)
        if len(set(li2)) % 2 != 0:
            li1.append(i)

    return sorted(li1)


b = func(M, N)
if len(b) == 0:
    print(-1)
else:
    print(sum(b))
    print(min(b))

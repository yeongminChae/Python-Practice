N, M = map(int, input().split())


def func(N, M):
    li = list(range(1, N+1))

    for _ in range(1, M+1):
        i, j = map(int, input().split())
        li[i-1: j] = list(reversed(li[i-1: j]))

    return li


a = func(N, M)
print(" ".join(map(str, a)))

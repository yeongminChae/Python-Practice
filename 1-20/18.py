N = int(input())


def func(N):
    S = list(map(int, input().split()))
    if len(S) != N:
        return "Error"
    return sum(S)


print(func(N))

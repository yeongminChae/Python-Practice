A, B = map(int, input().split())


def func(A, B):
    A = int(str(A)[::-1])
    B = int(str(B)[::-1])

    return max(A, B)


print(func(A, B))

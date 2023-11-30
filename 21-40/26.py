n, m = map(int, input().split())


def func(n, m):
    li = ['0'] * n

    for _ in range(1, m+1):
        if len(li) > n:
            return

        i, j, k = map(int, input().split())
        li[i-1:j] = [str(k)] * len(li[i-1:j])

    return li


a = func(n, m)
print(" ".join(a))

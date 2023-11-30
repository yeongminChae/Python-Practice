n = list(map(int, input().split()))


def func(n):
    li = [1, 1, 2, 2, 2, 8]
    li2 = []
    for i in range(0, len(n)):
        if n[i] >= 0:
            li2.append(li[i] - n[i])
        else:
            li2.append(n[i] - li[i])
    return li2


print(' '.join(map(str, func(n))))


def func(n):
    li = [1, 1, 2, 2, 2, 8]
    # list comprehension을 이용하여 코드를 간단하게 만듭니다.
    li2 = [li[i] - n[i] for i in range(len(n))]
    return li2


print(' '.join(map(str, func(n))))

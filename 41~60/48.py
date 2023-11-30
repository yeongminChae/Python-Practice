N = int(input())


def func(N):
    li = []

    for _ in range(N):
        a, b, c = map(int, input().split())
        set = {a, b, c}

        if len(set) == 1:
            li.append(10000 + a*1000)
        elif len(set) == 2:
            if a == b:
                li.append(1000 + a*100)
            elif a == c:
                li.append(1000 + a*100)
            else:
                li.append(1000 + b*100)
        else:
            li.append(max(set)*100)

    return max(li)


print(func(N))

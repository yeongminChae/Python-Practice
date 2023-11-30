N, M = map(int, input().split())


def func(N, M):
    li = [] * N

    for k in range(1, N+1):
        li.append(str(k))

    for _ in range(1, M+1):
        i, j = map(int, input().split())
        a = li[i - 1]
        b = li[j - 1]
        if a != b:
            li.remove(a)
            li.insert(j - 1, a)
            li.remove(b)
            li.insert(i - 1, b)
        else:
            li.remove(a)
            li.insert(i - 1, a)
    return (li)


a = func(N, M)
print(" ".join(a))

N, M = map(int, input().split())


def func(N, M):
    # 1부터 N까지의 수를 가진 리스트 초기화
    li = list(range(1, N+1))

    for _ in range(M):    # M번 공을 교환한다.
        i, j = map(int, input().split())
        # i번째와 j번째 공을 서로 교환
        li[i-1], li[j-1] = li[j-1], li[i-1]

    return li


a = func(N, M)
print(" ".join(map(str, a)))    # 각 원소를 문자열로 변환 후 출력

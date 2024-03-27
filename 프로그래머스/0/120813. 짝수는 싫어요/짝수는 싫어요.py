def solution(n):
    new_li = [i for i in range(1, n + 1)]
    return list(filter(lambda x : x % 2 != 0, new_li))
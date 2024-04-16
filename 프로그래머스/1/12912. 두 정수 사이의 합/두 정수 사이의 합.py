def solution(a, b):
    n, m = min(a, b), max(a, b)
    answer = [i for i in range(n, m + 1)]
    return sum(answer)
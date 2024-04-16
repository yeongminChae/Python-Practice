def solution(n):
    answer = ['수' if i % 2 != 0 else '박' for i in range(1, n + 1)]
    return ('').join(answer)
def solution(n):
    answer, li = 0, [1, 2, 3, 5]
    if n <= 4 : return li[n - 1] % 1234567
    for i in range(4, n) : li.append(li[i - 1] + li[i - 2])
    return li[-1] % 1234567

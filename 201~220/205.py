from functools import reduce


def solution(n):
    ans = []
    for i in n:
        ans.append(multiple_arr(n, i))
    return ans


def multiple_arr(arr, num):
    return reduce(lambda x, y: x * y, (filter(lambda x: x != num, arr)))


arr1 = [1, 2, 3, 4]
print(solution(arr1))

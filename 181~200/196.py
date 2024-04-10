import math


def solution(array):
    new_arr = [(index + 1, value) for index, value in enumerate(array)]

    sorted_arr = sorted(new_arr, key=lambda x: x[1], reverse=True)

    answer = [index for index, value in sorted_arr]
    return answer


print(solution([30, 10, 23, 6, 100]))
# solution([30, 10, 23, 6, 100])


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# for i in range(65, 123):
    # print(ord(i), end=' ')

print(ord('a'))

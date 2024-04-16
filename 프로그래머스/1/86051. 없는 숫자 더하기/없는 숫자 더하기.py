def solution(numbers):
    li = [i for i in range(0, 10)]
    answer = sum(filter(lambda x: x not in numbers, li))
    return answer
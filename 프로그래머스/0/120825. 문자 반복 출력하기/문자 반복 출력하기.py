def solution(my_string, n):
    answer = ('').join(list(map(lambda x: x * n, my_string)))
    return answer
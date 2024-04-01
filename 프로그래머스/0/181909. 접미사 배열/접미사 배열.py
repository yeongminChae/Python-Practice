def solution(my_string):
    li = [my_string[::-1][0 : i] for i in range(1, len(my_string) + 1)]
    answer = [i[::-1] for i in li]
    return sorted(answer)
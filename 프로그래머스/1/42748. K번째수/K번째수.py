def solution(array, commands):
    answer = []
    for i in commands :
        sorted_li = sorted(array[i[0] - 1: i[1]])
        answer.append(sorted_li[i[2] - 1])
    return answer
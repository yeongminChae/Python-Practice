def solution(my_string, queries):
    answer = ''
    for i in queries :
        print(my_string[i[0]: i[1] + 1])
    return answer
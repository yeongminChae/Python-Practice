def solution(array):
    max_num = max(array)
    answer = [max_num]
    
    for i, j in enumerate(array) :
        if j == max_num :
            answer.append(i)
    
    return answer
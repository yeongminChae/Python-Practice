def solution(order):
    answer = 0
    for i in list(map(str, str(order))) :
        if i in '3' :
            answer += 1
        elif i in '6' :
            answer += 1
        elif i in '9' :
            answer += 1
            
    return answer
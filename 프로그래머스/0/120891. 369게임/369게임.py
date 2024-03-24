def solution(order):
    answer = 0
    new_li = str(order)
    
    for i in '369' :
        answer += new_li.count(i)
            
    return answer
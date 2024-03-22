def solution(s):
    answer = 0
    new_li = s.split(' ')
    
    for i, j in enumerate(new_li) :
        if j != 'Z' :
            answer += int(j)
        else :
            answer -= int(new_li[i - 1])
        
    return answer
def solution(code):
    i = 0
    answer = ''
    
    for k, j in enumerate(code) :
        if j == '1' :
            i = 0 if i == 1 else 1
        
        if i == 0 and k % 2 == 0 :
            answer += j
        elif i == 1 and k % 2 != 0 : 
            answer += j
            
    return answer.replace('1', '') if len(answer) != 0 else 'EMPTY'
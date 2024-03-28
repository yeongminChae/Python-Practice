def solution(n):
    answer = []
    m = 1

    while len(answer) != n :
        if m % 3 == 0 :
            pass
        elif '3' in str(m)  : 
            pass
        else :
            answer.append(m)
        
        m += 1
        
    return answer[-1]
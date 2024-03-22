def solution(n):
    answer = 1
    a = 1
    
    while True :
        if a < n :
            answer += 1
            a *= answer
        elif a >= n :
            break
        
    if a == n :
        return answer 
    else :
        return answer - 1

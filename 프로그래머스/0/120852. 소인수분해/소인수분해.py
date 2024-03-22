def solution(n):
    answer = []
    divisior = 2 
    
    while n > 1 :
        if n % divisior == 0 :
            if divisior not in answer: 
                answer.append(divisior)
            n //= divisior
        else :
            divisior += 1

    return answer
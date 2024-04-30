def solution(k, m, score):
    score = [i for i in sorted(score, reverse=True) if i <= k] 
    a, b, answer = len(score), 0, 0
    
    while a != 0 :
        if a < m or a == 0 : break
        answer += min(score[b : m + b]) * m
        a -= m
        b += m
    
    return answer


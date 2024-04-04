def solution(q, r, code):
    answer = ''
    for i, j in enumerate(code) :
        answer += j if i % q == r else ''
        
    return answer
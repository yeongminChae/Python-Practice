def solution(x, n):
    if x != 0 :
        answer = [i for i in range(x, (n * x), x)]
        answer.append(n * x)
    else :
        answer = [0] * n
        
    return answer
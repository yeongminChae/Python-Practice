def solution(a,b):
    answer = 0
    a, b = sorted(a, reverse=True), sorted(b)
    
    for i in range(0, len(a)) : answer += a[i] * b[i]
    return answer
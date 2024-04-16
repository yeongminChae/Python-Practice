def solution(t, p):
    answer = 0
    for i in range(len(t)) :
        n = t[i: i + len(p)]
        if int(n) <= int(p) and len(n) >= len(p): answer += 1 
    return answer
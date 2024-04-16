def solution(s):
    answer = []
    last_seen = {}

    for i, j in enumerate(s) :
        
        if j not in last_seen : answer.append(-1)
        else : answer.append(i - last_seen[j])
            
        last_seen[j] = i
    return answer
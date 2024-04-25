def solution(k, score):
    answer = []
    temp = []
    for i in score :
        temp.append(i)
        temp = sorted(temp, reverse=True)[ : k]
        answer.append(min(temp))
        
    return answer
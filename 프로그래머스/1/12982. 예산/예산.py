def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in d :
        if budget >= i :
            budget -= i
            answer += 1
        else : break

    return answer
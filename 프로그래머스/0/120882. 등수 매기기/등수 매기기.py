def solution(score):
    li = [sum(i) / len(i) for i in score]
    
    answer = [1] * len(score)
    
    for i in range(len(score)) :
        for j in range(len(score)) :
            if li[i] < li[j] :
                answer[i] += 1
            
    return answer
def solution(n):
    answer, temp = 0, 0
    for i in range(1, n + 1) :
        temp = 0
        for j in range(i, n + 1) :
            temp += j
            if temp == n : 
                answer += 1
                break
            elif temp > n :
                break
            
    return answer
def solution(num, total):
    answer = []
    middle = total // num
    m = int(num / 2)
    
    for j in range(middle - m, middle):
        answer.append(j)
    
    for i in range(middle, middle + m + 1) :
        answer.append(i)
    
    return answer if num % 2 != 0 else answer[1:]
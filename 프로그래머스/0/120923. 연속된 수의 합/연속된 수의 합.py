def solution(num, total):
    standard = (total * 2) // num
    answer = [standard // 2]
    
    if num % 2 != 0 :    
        a = 1
        while len(answer) != num :
            answer.append(standard // 2 - a)
            answer.append(standard // 2 + a)
            a += 1
            
    else :
        n = standard - (standard // 2)
        answer.append(n)
        b = 1
        while len(answer) != num :
            answer.append(n + b)
            answer.append(standard // 2 - b)
            b += 1
    
    return sorted(answer)
def solution(s):
    answer = []
    a = 0
    
    for i in s :
        if a % 2 == 0 : answer.append(i.upper())
        else : answer.append(i.lower())
        a += 1
        
        if i == ' ' : a = 0
    
    return ('').join(answer)
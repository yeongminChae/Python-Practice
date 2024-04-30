def solution(n):
    m = bin(n)[2:].count('1')
    
    while True :
        if m == bin(n + 1)[2:].count('1') :
            return n + 1         
        n += 1
    return answer
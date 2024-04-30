def solution(s):
    a, b = 0, s.count('0')
    
    while s != '1' :
        s = bin(len(list(filter(lambda x: x != '0' , s))))[2:]
        a += 1
        b += s.count('0')
    
    return a, b
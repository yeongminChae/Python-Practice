def solution(s):
    temp = 0
    if s[0] == ')' : return False
    
    for i in s :
        if i == '(' : temp += 1
        else : temp -= 1
        if temp < 0 : return False
    
    return True if temp == 0 else False
def solution(n, k):
    answer, num = 0, func(n, k) 
    for i in num.split('0') :
        if i == '' : continue
        if detector(int(i)) : answer += 1
    return answer

def func(n, q) :
    rev_num = ''
    
    while n > 0 :
        n, mod = divmod(n, q)
        rev_num += str(mod)
        
    return rev_num[::-1]

def detector(num) :
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True
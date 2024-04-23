def numbers(n, q) :
    rev_base = ''
    while n > 0 :
        n, mod = divmod(n, q)
        rev_base += str(mod)
    
    return rev_base[::-1]

def solution(n):
    answer = int(numbers(n, 3)[::-1], 3)
    return answer
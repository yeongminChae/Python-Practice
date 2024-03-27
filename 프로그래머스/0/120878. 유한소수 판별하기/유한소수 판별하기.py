def gcd(x, y) :
    while y :
        x, y = y, x % y     
    return x

def solution(a, b):
    while gcd(a, b) != 1 :
        gcd_save = gcd(a, b)
        a //= gcd_save
        b //= gcd_save

    while b % 2 == 0 :
        b //= 2
        
    while b % 5 == 0 :
        b //= 5
    
    if b == 1:
        return 1
    
    return 2
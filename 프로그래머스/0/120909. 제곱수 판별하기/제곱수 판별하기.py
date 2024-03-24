import math
import decimal

def solution(n):
    num = decimal.Decimal(math.sqrt(n))
    
    if n == num ** 2 :
        return 1
    
    return 2
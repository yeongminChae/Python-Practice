def count_digits(n):
    digits = 0
    length = len(str(n))
    
    for i in range(1, length):
        digits += i * (10**i - 10**(i-1))
    
    digits += length * (n - 10**(length-1) + 1)
    
    return digits

n = int(input())
print(count_digits(n))

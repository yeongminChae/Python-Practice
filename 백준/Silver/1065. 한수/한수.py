import sys

n = int(sys.stdin.readline())

def func(n) :
    a = 0
    
    if n < 100 :
        return n
    
    else:
        a = 99
        
        for i in range(100, n + 1) :
            nums = list(map(int, str(i)))
            
            if nums[0] - nums[1] == nums[1] - nums[2]:
                a += 1

    return a
    
    
print(func(n))

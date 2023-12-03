def func() :
    c = 0
    d = 0
    
    for _ in range(10) :
        a,b = map(int,input().split())
        
        c -= a
        c += b
        
        if c > d :
            d = c
            
    return d

print(func())
        
        
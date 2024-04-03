def solution(a, b, c, d):
    li = [a, b, c, d]
    n = len(set(li))
    if n == 1 :
        return 1111 * li[0]
    
    elif n == 4 :
        return min(li)
    
    elif n == 2 :
        for i in set(li) :
            return func_2(li, i)
                
    elif n == 3 :
        a = 1
        return func_3(a, li)

     
def func_3(a, arr) :
    for i in set(arr) :
        a *= i if arr.count(i) != 2 else 1
    return a

def func_2(arr, x) :
    p, q = 0, 0
    if arr.count(x) == 2 :
        return func_2_22(arr) 
    else :
        return func_2_31(arr, x)
        
def func_2_22(arr) :       
    new_li = list(set(arr))
    return (new_li[0] + new_li[1]) * abs(new_li[0] - new_li[1])

def func_2_31(arr, x) :
    p, q = 0, 0
    if arr.count(x) == 1 :
        q = x
        p = next(i for i in arr if i != x)
    elif arr.count(x) == 3 :
        p = x
        q = next(i for i in arr if i != x)
    return (10 * p + q) ** 2
            
        
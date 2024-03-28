def solution(polynomial):
    arr1 = []
    arr2 = []
    
    for i in polynomial.split(' + ') :
        if 'x' in i :
            arr1.append(int(i.split('x')[0]) if i.split('x')[0] != '' else 1)
        else :
            arr2.append(int(i))
            
    a = str(sum(arr1)) + 'x' if sum(arr1) != 1 else 'x'
    b = str(sum(arr2))
    
    if b != "0" and a != '0x':    
        return f'{a} + {b}'
    elif a == '0x' :
        return b
    else :
        return a 
           

def solution(arr):
    stk = []
    i = 0
    while len(arr) > i :
        if len(stk) == 0 :
            stk.append(arr[i])
            i += 1
            
        if arr[i] > stk[-1] :
            stk.append(arr[i])
            i += 1
        else :
            stk.pop()
        
    return stk
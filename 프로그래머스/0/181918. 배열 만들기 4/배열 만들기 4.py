def solution(arr):
    stk = []
    i = 0
    while len(arr) > i :
        if not stk or arr[i] > stk[-1]  :
            stk.append(arr[i])
            i += 1
            
        else :
            stk.pop()
        
    return stk
def solution(arr, n):
    if len(arr) % 2 != 0 :
        return list(map(lambda x : x[1] + n if x[0] % 2 == 0 else x[1] , enumerate(arr)))
    else :    
        return list(map(lambda x : x[1] + n if x[0] % 2 != 0 else x[1] , enumerate(arr)))       
    return answer
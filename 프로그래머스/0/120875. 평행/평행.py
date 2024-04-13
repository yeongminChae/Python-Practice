def solution(dots):    
    arr_12_34 = len(set([len_cal(dots, 0, 1), len_cal(dots, 2, 3)]))
    arr_13_24 = len(set([len_cal(dots, 0, 2), len_cal(dots, 1, 3)]))
    arr_14_23 = len(set([len_cal(dots, 0, 3), len_cal(dots, 1, 2)]))
    
    if arr_12_34 == 1 or arr_13_24 == 1 or arr_14_23 == 1 :
        return 1
    return 0

def len_cal(arr, a, b) :
    if arr[a][0] - arr[b][0] or arr[a][1] - arr[b][1] != 0 :
        return (arr[a][0] - arr[b][0]) / (arr[a][1] - arr[b][1])
    return 0
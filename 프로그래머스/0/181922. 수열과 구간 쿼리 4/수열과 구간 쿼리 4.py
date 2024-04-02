def solution(arr, queries):
    for k in queries :
        for i in range(len(arr)) :
            if k[0] <= i <= k[1] and i % k[2] == 0 :
                arr[i] += 1     
            
    return arr
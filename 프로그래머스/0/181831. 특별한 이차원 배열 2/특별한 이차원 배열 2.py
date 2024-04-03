def solution(arr):
    answer = all(arr[i][j] == arr[j][i] for i in range(len(arr)) for j in range(len(arr)))
    
    return int(answer)
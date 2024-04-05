def solution(arr):
    answer = [[]]
    for i in arr :
        while len(i) != len(arr) :
            if len(i) < len(arr) : i.append(0)
            else : arr.append([0 for _ in range(len(arr))])
    return arr
def solution(arr1, arr2):
    result = []
    for a, b in zip(arr1, arr2) :
        row = []
        for c, d in zip(a, b) : row.append(c + d)
        result.append(row)
        
    return result
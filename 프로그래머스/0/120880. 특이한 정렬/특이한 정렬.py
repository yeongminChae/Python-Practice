def solution(numlist, n):
    arr = [(i, abs(n - i)) for i in numlist]
    sorted_arr = sorted(arr, key = lambda x: (x[1], -x[0]))
    
    answer = []
    for i in sorted_arr :
        answer.append(i[0])
        
    return answer
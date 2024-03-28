def solution(numlist, n):
    sorted_arr = sorted(numlist, key = lambda x: (abs(n - x), -x))
        
    return sorted_arr
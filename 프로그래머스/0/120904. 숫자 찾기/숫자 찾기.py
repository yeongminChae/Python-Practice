def solution(num, k):
    new_li = list(map(int, str(num)))
    for i, j in enumerate(new_li) :
        if j == k :
            return i + 1
        
    return -1
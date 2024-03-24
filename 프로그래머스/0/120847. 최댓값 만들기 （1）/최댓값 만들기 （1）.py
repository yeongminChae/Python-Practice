def solution(numbers):
    new_li = sorted(numbers, reverse=True)
    answer = new_li[0] * new_li[1]
    
    return answer
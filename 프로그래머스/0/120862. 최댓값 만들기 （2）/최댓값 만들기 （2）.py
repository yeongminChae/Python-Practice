def solution(numbers):
    new_li = sorted(numbers, reverse=True)
                
                
    return max(new_li[0] * new_li[1] , new_li[-1] * new_li[-2])
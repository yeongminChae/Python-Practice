def solution(numbers, k):
    answer = 0
    index = 0
    length = len(numbers)
    
    for _ in range(1, k) :
        index = (index + 2) % length
    
    answer = numbers[index]
    
    return answer

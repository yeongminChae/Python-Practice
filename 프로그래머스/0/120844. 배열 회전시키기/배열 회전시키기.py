
def solution(numbers, direction):
    answer = []
    
    for i, j in enumerate(numbers) :
        if direction == 'right' :
            if i + 1 > len(numbers) - 1:
                answer.insert(0, j)    
            else :
                answer.insert(i + 1, j)
        else :
            if i - 1 < 0 :
                answer.insert(-1, j)    
            else :
                answer.insert(i - 1, j)
                
    return answer
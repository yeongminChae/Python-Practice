def solution(numbers):
    answer = []
    numbers = sorted(numbers)
    for i, j in enumerate(numbers) :
        for k in numbers[i + 1 : ] :
            answer.append(j + k)
            
    return sorted(list(set(answer)))
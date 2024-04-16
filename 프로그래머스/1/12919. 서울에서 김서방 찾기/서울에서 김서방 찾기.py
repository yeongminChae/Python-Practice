def solution(seoul):
    answer = ''
    for i, j in enumerate(seoul) :
        if j == 'Kim' : answer = f'김서방은 {i}에 있다'
        
    return answer
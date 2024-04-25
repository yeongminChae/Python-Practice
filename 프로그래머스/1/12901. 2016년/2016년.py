def solution(a, b):
    dict1 = {4: 'MON', 5: 'TUE', 6: 'WED', 0: 'THU', 1: 'FRI', 2: 'SAT', 3: 'SUN'}
    li = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    n = 0
    
    for i, j in enumerate(li) :
        if i + 1 < a : n += j
        elif i + 1 == 1 : n = 0
    
    return dict1[(n + b) % 7]
def solution(s):
    dict1 = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
6: 'six', 7: 'seven', 8: 'eight', 9: 'nine' }
    answer = s
    
    for i in dict1 :
        if dict1[i] in s : answer = answer.replace(dict1[i], str(i))

    return int(answer)
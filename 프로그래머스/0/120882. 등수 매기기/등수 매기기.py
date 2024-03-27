def solution(score):
    aver = [sum(j) for i, j in enumerate(score)]
    sorted_aver = sorted(aver, reverse=True)
    
    dict_avr = {}
    
    for i, j in enumerate(sorted_aver) :
        if j not in dict_avr:
            dict_avr[j] = i + 1 
    
    print(dict_avr)
    
    answer = [dict_avr[i] for i in aver]
    
    return answer
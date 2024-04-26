def solution(babbling):
    answer = []
    my_dict = { "aya": 0, "ye": 1, "woo": 2, "ma": 3 }
    
    for i in babbling :
        temp = i
        for j in my_dict :
            if j in temp and j * 2 not in temp:
                temp = temp.replace(j, ' ')
        
        answer.append(temp.replace(' ',''))
    return answer.count('')




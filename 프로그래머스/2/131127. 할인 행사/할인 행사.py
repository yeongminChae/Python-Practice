def solution(want, number, discount):
    dict1 = dict({j : number[i]  for i, j in enumerate(want)}.items())
    answer, temp = 0, 0
    
    while len(discount) - temp >= sum(number) :
        temp_dict = dict1.copy()
        for i in discount[temp : temp + 10] :
            try : temp_dict[i] = temp_dict[i] - 1
            except : continue
        temp += 1
        if list(temp_dict.values()).count(0) == len(want) : answer += 1
                
    return answer
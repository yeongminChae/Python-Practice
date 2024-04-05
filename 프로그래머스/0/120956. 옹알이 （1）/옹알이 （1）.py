def solution(babbling):
    answer = 0
    a = 0
    dict1 = { 0: "aya", 1: "ye", 2: "woo", 3: "ma" }
    
    while a < 4 :
        for j, i in enumerate(babbling) :
            if dict1[a] in i :  babbling[j] = i.replace(dict1[a], '-', 1)
        a += 1    
    
    for i in babbling :
        if len(list(set(i))) == 1 and ord(list(set(i))[0]) == 45 : answer += 1
    return answer
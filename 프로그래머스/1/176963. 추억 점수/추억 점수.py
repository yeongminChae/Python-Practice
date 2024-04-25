def solution(name, yearning, photo):
    answer = []
    dict1 = {}
    
    for i in range(len(name)):
        dict1[name[i]] = yearning[i]
        
    for i in photo :
        n = 0
        for j in i :
            if j in dict1 : n += dict1[j]
        answer.append(n)
    return answer
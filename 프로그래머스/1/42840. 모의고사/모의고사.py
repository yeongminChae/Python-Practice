def solution(answers):
    answer = []
    li1 = [i % 5 if i % 5 != 0 else 5 for i in range(1, len(answers) + 1)]
    li2 = li2_maker(answers)
    li3 = li3_maker(answers)
    dict1 = {'1': 0, '2': 0, '3': 0}
     
    for i, j in enumerate(answers) :
        if li1[i] == j : dict1['1'] += 1
        if li2[i] == j : dict1['2'] += 1
        if li3[i] == j : dict1['3'] += 1
    
    a = max(dict1.items(), key=lambda x : x[1])
    for i in dict1 :
        if dict1[i] == a[1] : answer.append(int(i))
    return answer

def li2_maker(list1) :
    li2 = [0] * (len(list1))
    a = 1
    for i, _ in enumerate(li2) :    
        if i % 2 == 0 : li2[i] = 2
        else :
            if a != 2 : li2[i] = a
            else :
                a += 1
                li2[i] = a
            a += 1
        if a > 5 : a = 1
    return li2

def li3_maker(li) :
    li3 = []
    a = 0
    for i, _ in enumerate(li) :
        if a < 1 :
            for _ in range(2) : li3.append(3)
        else :
            if a != 3 : 
                for _ in range(2) : li3.append(a)
        a += 1
        if a > 5 : a = 0
    return li3[:len(li)]
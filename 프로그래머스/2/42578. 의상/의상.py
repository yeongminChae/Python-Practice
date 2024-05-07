def solution(clothes):
    answer, dict1 = 1, dict_maker(clothes)
    for i in list(dict1.values()) :
        answer *= (len(i) + 1)
    return answer - 1

def dict_maker(clothes) :
    dict1 = {}
    for i in clothes :
        if i[1] in dict1 : dict1[i[1]].append(i[0])
        else : dict1[i[1]] = [i[0]]
    return dict1
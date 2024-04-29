def solution(dartResult):
    answer = []
    dict1 = {'S': 1, 'D': 2, 'T' : 3}
    n = ''

    for i in dartResult :
        if i.isdigit() :
            n += i
        elif i in dict1: 
            answer.append(int(n) ** int(dict1[i]))
            n = ''
        elif i == '*' :
            if len(answer) > 1 :
                answer[-2] *= 2
            answer[-1] *= 2
        elif i == '#' :
            answer[-1] *= (-1)
            
    return sum(answer)

def solution(s):
    answer, s = [], sorted(s[2:-2].replace('},{', ' ').split(' '), key=len)
    for i in s :
        if ',' not in i : answer.append(i)
        for j in i.split(',') :
            if j not in answer : answer.append(j)
            
    return list(map(int, answer))
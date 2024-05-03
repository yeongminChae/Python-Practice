def solution(s):
    answer, li1 = 0, maker(s)
    dict1 = {'(': ')', '{': '}', '[': ']'}
        
    for i in li1 :
        if i[0] in [')', '}', ']'] : continue
        temp = []
        for j in i :
            if j in dict1 :
                temp.append(j)
            else :
                if temp and dict1[temp[-1]] == j : temp.pop()
        if len(temp) == 0 : answer += 1
        
    return answer

def maker(s) :
    li1 = [s]
    for _ in range(len(s) - 1) :
        s = s[1:] + s[0]
        li1.append(s)
    return li1


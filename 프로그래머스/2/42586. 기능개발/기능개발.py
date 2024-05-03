import math

def solution(progresses, speeds):
    li1 = [math.ceil((100 - j) / speeds[i]) for i, j in enumerate(progresses)]
    ans, temp, idx = [], 0, li1[0]
    
    for i in li1 :
        if i <= idx : temp += 1
        else :
            ans.append(temp)
            idx = i
            temp = 1
    if temp != 0 : ans.append(temp)
        
    return ans
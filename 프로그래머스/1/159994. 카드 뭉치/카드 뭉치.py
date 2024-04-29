def solution(cards1, cards2, goal):
    temp1, temp2 = 0, 0
    
    for i in goal :
        if temp1 < len(cards1) and i == cards1[temp1] :
            temp1 += 1
        elif temp2 < len(cards2) and i == cards2[temp2] :
            temp2 += 1
        else :
            return 'No'
        
    return 'Yes'
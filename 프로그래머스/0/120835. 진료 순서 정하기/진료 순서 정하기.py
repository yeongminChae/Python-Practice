def solution(emergency):
    answer = []
    
    sorted_arr = sorted(emergency, reverse=True)
    
    for i in emergency :
        answer.append(sorted_arr.index(i) + 1)
         
    return answer
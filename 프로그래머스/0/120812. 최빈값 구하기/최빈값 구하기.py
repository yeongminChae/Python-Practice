def solution(array):
    set_arr = set(sorted(array))
    new_arr = []
    
    answer = 0
    temp = 0
    index = 0
    
    for i in set_arr :
        if array.count(i) >= temp :
            temp = array.count(i)
            index = i
            new_arr.append(array.count(i))
    
    if new_arr.count(max(new_arr)) > 1 :
        return -1
    
    return index
        
            
            
            
            
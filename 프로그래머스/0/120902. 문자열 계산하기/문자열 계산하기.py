def solution(my_string):
    new_li = my_string.split()
    answer = int(new_li[0])
    
    for i in range(1, len(new_li) - 1, 2):
        operator = new_li[i]
        new_num = int(new_li[i + 1])
                
        if operator == '+' :
            answer += new_num
        else :
            answer -= new_num        
        
    return answer
    
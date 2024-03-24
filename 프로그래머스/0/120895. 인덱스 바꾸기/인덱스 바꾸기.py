def solution(my_string, num1, num2):
    answer = ''
    new_li = list(map(str, my_string))
    str1 = new_li[num1]
    str2 = new_li[num2]
    
    for i, j in enumerate(new_li) :
        if i == num1 :
            j = str2
        elif i == num2 :
            j = str1
        
        answer += j
    return answer
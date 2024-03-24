def solution(my_string):
    answer = ''
    new_li = ['a','e','i','o','u']
    
    for i in my_string :
        if i not in  new_li:
            answer += i
            
    return answer
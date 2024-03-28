def all_multiple(li) :
    a = 1
    for i in li :
        a *= i 
    return a

def solution(num_list):
    a = sum(num_list) if len(num_list) >= 11 else all_multiple(num_list)
     
    return a
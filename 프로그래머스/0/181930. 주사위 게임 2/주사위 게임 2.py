def multiple_arr(li, n) :
    return sum(list(map(lambda x : x ** n, li)))

def solution(a, b, c):
    li = [a, b, c]
    
    if len(set(li)) == 3 :
        return sum(li)
    elif len(set(li)) == 2 :
        return sum(li) * multiple_arr(li, 2)
    else : 
        return sum(li) * multiple_arr(li, 2) * multiple_arr(li, 3)

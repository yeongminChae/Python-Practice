def solution(order):
    answer = []
    for i in order :
        if 'americano' in i or 'anything' == i : answer.append(4500)
        else : answer.append(5000)
    return sum(answer)
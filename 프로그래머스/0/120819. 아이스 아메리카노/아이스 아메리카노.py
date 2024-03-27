def solution(money):
    one_cup = 5500
    answer = [money // one_cup, money % one_cup]
    return answer
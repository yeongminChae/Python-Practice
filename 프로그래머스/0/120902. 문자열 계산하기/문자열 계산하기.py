def solution(my_string):
# ' + '와 '+'의 차이를 이해하는 것이 중요합니다. 전자는 공백을 포함한 분리 기준이고, 후자는 공백 없이 연산자만을 분리 기준으로 삼습니다

    new_li = my_string.replace(' - ', " + -").split(' + ')
    return sum(list(map(lambda x: int(x), new_li)))
    
def solution(picture, k):
    answer = []
    for i in picture :
        for _ in range(k) :
            answer.append(('').join(list(map(lambda x : x * k , i ))))
    return answer
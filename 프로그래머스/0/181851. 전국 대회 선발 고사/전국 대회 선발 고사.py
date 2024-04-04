def solution(rank, attendance):
    li = list(filter(lambda x: x[1] if attendance[x[0]] else 0, enumerate(rank)))
    li = sorted(li, key=lambda x: x[1])
    answer = [i[0] for i in li][0 : 3]
    return answer[0] * 10000 + answer[1] * 100 + answer[-1]
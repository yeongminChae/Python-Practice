def solution(strArr):
    answer = []
    li = sorted(strArr, key = lambda x: len(x))
    li2 = [len(i) for i in li]
    for i in set(li2) :
        answer.append(li2.count(i))
    return max(answer)
def solution(citations):
    answer, citations = 0, sorted(citations, reverse=True)
    for i, j in enumerate(citations) :
        if j >= i + 1: answer = i + 1
    return answer
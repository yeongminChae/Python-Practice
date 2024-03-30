def solution(a, d, included):
    li1 = [a + d*i for i in range(0, len(included))]
    return sum([li1[i] for i, j in enumerate(included) if j == True])


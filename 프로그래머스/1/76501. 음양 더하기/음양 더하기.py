def solution(absolutes, signs):
    answer = [absolutes[i] if j else absolutes[i] * -1 for i, j in enumerate(signs)]
    return sum(answer)
def solution(arr, idx):
    answer = [i for i, j in enumerate(arr) if i >= idx and j == 1]
    return -1 if len(answer) == 0 else answer[0]
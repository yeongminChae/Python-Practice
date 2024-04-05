def solution(board, k):
    answer = []
    for i, n in enumerate(board) :
        for j, m in enumerate(n) : 
            if (i + j) <= k : answer.append(board[i][j])
    return sum(answer)
def solution(keyinput, board):
    x = 0
    y = 0
    dict_x = {"left":-1, "right":1}
    dict_y = {"up":1, "down":-1}
    
    for i in keyinput :
        if i in dict_x.keys():
            next_x = x + dict_x[i]
            if abs(next_x) <= (board[0] // 2):
                x = next_x
            
        elif i in dict_y.keys():
            next_y = y + dict_y[i]
            if abs(next_y) <= (board[1] // 2):
                y = next_y
    
    answer = [x, y]
    return answer
def solution(board):
    danger_zone = set()  
    
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 1:
                for x in range(max(0, i-1), min(i+2, len(board))):
                    for y in range(max(0, j-1), min(j+2, len(board[0]))):
                        danger_zone.add((x, y))
    
    safe_area = (len(board) * len(board[0])) - len(danger_zone)
    
    return max(safe_area, 0)

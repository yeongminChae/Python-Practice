def solution(n):
    arr = [[0] * n for _ in range(n)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y = 0, 0
    num = 1  # 채울 숫자
    direction = 0  # 시작 방향은 오른쪽
    
    for i in range(n * n):
        arr[x][y] = num  # 현재 위치에 숫자를 채웁니다.
        num += 1  # 다음 숫자를 위해 1을 더합니다.
        
        # 다음 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 배열 범위를 벗어나지 않고, 다음 위치가 아직 채워지지 않았다면 이동합니다.
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            # 방향을 바꿉니다. (오른쪽 -> 아래 -> 왼쪽 -> 위 -> 오른쪽 ...)
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]
    
    return arr

def solution(dots): 
    x = max(dots)
    y = min(dots)
        
    return (x[0] - y[0]) * (x[1] - y[1])
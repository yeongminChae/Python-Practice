def solution(slice, n):
    x, y = divmod(n, slice)
    return x + int(y != 0) 
        
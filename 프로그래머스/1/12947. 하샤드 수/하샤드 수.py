def solution(x):
    n = sum(map(lambda x: int(x), str(x)))
    return True if x % n == 0 else False 
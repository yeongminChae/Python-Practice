def solution(n):
    return len([i for i in range(2, n + 1) if detector(i)])

def detector(x) :
    for i in range(2, int(x ** 0.5) + 1) :
        if x % i == 0 : return False
    return True
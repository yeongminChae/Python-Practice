def solution(x1, x2, x3, x4):
    a = False if x1 == False and x2 == False else True
    b = False if x3 == False and x4 == False else True
    return True if a == True and b == True else False
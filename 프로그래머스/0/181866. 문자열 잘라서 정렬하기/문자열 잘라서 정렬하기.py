def solution(myString):
    li = sorted(myString.split('x'))
    return [i for i in li if i != '']
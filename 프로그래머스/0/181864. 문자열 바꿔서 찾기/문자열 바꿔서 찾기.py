def solution(myString, pat):
    a = myString.replace('A','-').replace('B','A').replace('-','B')
    return 1 if pat in a else 0
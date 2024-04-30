def solution(s):
    a = ''
    for i in s.split(' ') :
        if i :  a += i[0].upper() + i[1:].lower() + ' '
        else : a += ' '
    return a[:-1]
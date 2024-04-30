def solution(s):
    s = [int(i) for i in s.split(' ')]
    
    return ' '.join(map(str, [min(s), max(s)]))
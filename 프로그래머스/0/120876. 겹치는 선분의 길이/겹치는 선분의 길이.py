def solution(lines):
    sets = [set(range(i[0], i[1])) for i in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
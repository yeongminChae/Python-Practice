def solution(sizes):
    sizes = [i if i[0] > i[1] else i[::-1] for i in sizes]
    a = max(sizes, key=lambda x: x[0])
    b = max(sizes, key=lambda x: x[1])
    
    return max(a) * min(b)
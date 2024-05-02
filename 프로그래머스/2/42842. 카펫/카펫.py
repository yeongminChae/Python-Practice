def solution(brown, yellow):
    total, idx = brown + yellow, 0
    li1 = maker(total)[::-1]
    for i in range(0, len(li1), 2) : 
        count = calc(li1[i], li1[i + 1])
        if count == brown and total - count == yellow : idx = i + 1

    return li1[idx - 1 : idx + 1]
    

def maker(total) :
    li1 = []
    for i in range(3, int(total ** 0.5) + 1) : 
        if total % i == 0 :
            li1.append(i)
            li1.append(total // i)
    return li1

def calc(a, b) :
    return a * 2 + (b - 2) * 2
 
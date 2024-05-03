def solution(elements):
    answer, elements, n = 0, elements * 2, len(elements)
    li1,set1 = [0], set()
    for i in elements : li1.append(li1[-1] + i)
    
    for i in range(1, n + 1) :
        for j in range(n) :
            temp = li1[i + j] - li1[i]
            set1.add(temp)
            
    return len(set1)
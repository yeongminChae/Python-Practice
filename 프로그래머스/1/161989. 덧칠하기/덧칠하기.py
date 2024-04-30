def solution(n, m, section):
    sect = sorted(section)
    answer, start = 0, sect[0]
    
    for i in range(0, len(sect)) :
        current = sect[i]
        if current - start >= m :
            start = current
            answer += 1
            
    return answer + 1
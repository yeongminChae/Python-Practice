from collections import Counter

def solution(k, tangerine):
    answer, temp, li1 = 0, 0, Counter(tangerine).most_common()
    while k > 0 :
        k -= li1[temp][1]
        answer += 1
        temp += 1
            
    return answer
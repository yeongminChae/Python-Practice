def solution(n,a,b):
    answer = 0
    while a != b :
        a = int((a - 1) / 2 + 1) 
        b = int((b - 1) / 2 + 1)
        answer += 1
        
    return answer

# 1,2 3,4 5,6
# 

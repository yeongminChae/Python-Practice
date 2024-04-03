from collections import deque

def solution(myString, pat):
    answer = 0
    li = deque(map(str, myString))
    while len(li) >= len(pat):
        str1 = ('').join(li)
        answer = answer + 1 if str1[0: len(pat)] == pat else answer
        li.popleft()
    
    return answer

# 8 : 3 3 2 -> 
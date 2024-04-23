def solution(s, n):
    answer = ''
    for i in s :
        if i.isalpha() :
            start = ord('A') if i.isupper() else ord('a')
            answer += chr((ord(i) - start + n) % 26 + start)
        else : answer += i
            
    return answer

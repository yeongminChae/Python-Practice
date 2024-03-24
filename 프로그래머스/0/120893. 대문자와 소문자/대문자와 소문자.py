def solution(my_string):
    answer = ''
    for i in my_string :
        if ord(i) >= 97 and ord(i) <= 123 :
            answer += i.upper()
        elif ord(i) >= 65 and ord(i) <= 91 :
            answer += i.lower()
            
    return answer
def solution(n):
    answer = []
    divisior = 2 
    
    while n > 1 :
        if n % divisior == 0 :
            if divisior not in answer: 
                answer.append(divisior)
            n //= divisior
        else :
            divisior += 1

    return answer

def solution2(n):
    answer = []  # 소인수를 담을 리스트
    divisor = 2  # 가장 작은 소수부터 시작
    
    while n > 1:
        if n % divisor == 0:
            answer.append(divisor)  # 현재 divisor(소인수)를 추가
            while n % divisor == 0:
                n //= divisor  # n을 divisor로 나눔, divisor로 더 이상 나누어지지 않을 때까지 반복
        divisor += 1  # 다음 수로 넘어감
    
    return answer    


# 1번 함수에서는 중복된 문자인지를 찾을 때, 모든 배열을 다 순환하기에 비효율 적일 수도 있음.
# 2번 풀이는 while문을 중첩해서, n이 더 이상 나누어지지 않을때까지 순환하고 그 다음 번호로 넘어감.     
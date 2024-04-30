def solution(n):
    answer = 0
# 등차수열: a = (n / k) - ((k - 1) * d) / 2, a = 초항, d = 공차, n = 주어진 합, k = 항의 갯수 
# is_integer() 정수인지 확인하는 함수    
    for k in range(1, n + 1) :
        a = (n / k) - ((k - 1) * 1) / 2
        if a.is_integer() and a > 0 : answer += 1
    return answer
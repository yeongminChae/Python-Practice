import math

# 최대공약수 구하기 방법 1. 내장 함수
def common_multiple(a, b) :
    n = math.gcd(a, b) # 최대공약수
    
    return (a * b) // n

# 최대공약수 구하기 방법 2. 유클리드 호제법
def common_multiple2(a, b) :
    while b > 0 :
        a, b = b, a % b
        return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    m = common_multiple(denom1, denom2) # 분모
    s = (m // denom1) * numer1 + (m // denom2)* numer2 # 분자
    
    y = math.gcd(s, m)
    
    answer.append(s // y)
    answer.append(m // y)
    
    return answer

# 1. 최소공배수 = 두 수의 곱 / 최대공약수 
# 2. 기약분수로 만들기 위해서는, 분모와 분자 각각을 분모,분자 최대공약수로 나누어 줘야 함.

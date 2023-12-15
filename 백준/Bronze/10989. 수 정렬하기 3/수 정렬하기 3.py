import sys

n = int(sys.stdin.readline())
count = [0] * 10001  # 0 ~ 10000 까지의 숫자를 저장하기 위한 리스트

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1  # 입력받은 숫자에 해당하는 인덱스의 값을 1 증가

for i in range(10001):  # 0 ~ 10000 까지의 숫자에 대해서
    if count[i] != 0:  # 만약 해당 숫자가 하나라도 있다면
        for _ in range(count[i]):  # 해당 숫자의 개수만큼
            print(i)  # 숫자를 출력

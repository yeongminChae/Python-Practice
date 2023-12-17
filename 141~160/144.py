import sys
import resource


def memory_usage():
    # 현재 프로세스의 메모리 사용량을 리턴
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss


n = int(sys.stdin.readline())
count = [0] * 10001  # 0 ~ 10000 까지의 숫자를 저장하기 위한 리스트

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1  # 입력받은 숫자에 해당하는 인덱스의 값을 1 증가

for i in range(10001):  # 0 ~ 10000 까지의 숫자에 대해서
    if count[i] != 0:  # 만약 해당 숫자가 하나라도 있다면
        for _ in range(count[i]):  # 해당 숫자의 개수만큼
            print(i)  # 숫자를 출력

# 이 문제를 해결하기 위해서는 계수 정렬(Counting Sort)라는 특별한 정렬 알고리즘을 사용해야 합니다.
# 계수 정렬은 각 숫자의 개수를 세어놓은 뒤, 이를 이용해 정렬을 수행하는 방법입니다.

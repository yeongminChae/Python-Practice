import sys

n = int(sys.stdin.readline())
set1 = set(map(int, sys.stdin.readline().split()))  # set으로 변환
m = int(sys.stdin.readline())
li2 = list(map(int, sys.stdin.readline().split()))

# 결과를 담을 리스트 생성
result = ['1' if i in set1 else '0' for i in li2]

print("\n".join(result))

import math

S = int(input())


def func(S):
    return int((-1 + math.sqrt(1 + (8*S))) // 2)


print(func(S))

# 45 n = 9 5*9 -> s = n*(n+1)/2 , 2s = n*(n+1) , n = sqrt(2s)
# 55 n = 10 5.5*10
# 66 n = 11 6*11

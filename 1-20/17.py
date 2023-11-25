T = int(input())


def func(T):
    li = []
    for _ in range(1, T+1):
        S = str(input())
        print(S[0] + S[-1])


func(T)

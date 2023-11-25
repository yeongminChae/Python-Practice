T = int(input())


def func(T):
    for _ in range(1, T+1):
        li = []
        R, S = map(str, input().split())
        R = int(R)
        for i in S:
            li.append(i*int(R))
        print("".join(li))


func(T)


def repeat_alphanumeric(T):
    for _ in range(T):
        R, S = input().split()
        R = int(R)

        result = ''
        for char in S:
            result += char * R

        print(result)


repeat_alphanumeric(T)

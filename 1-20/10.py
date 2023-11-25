n, m = map(int, input().split())


def func(n, m):
    a = max(n, m)
    b = min(n, m)
    c = len(str(a)) - 1
    d = len(str(b)) - 1

    if a % (10**c) < b % (10**d):
        return "받아내림 발생"
    else:
        return "받아내림 발생 안함"


print(func(n, m))

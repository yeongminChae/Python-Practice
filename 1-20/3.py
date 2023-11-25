n = int(input())
# 19980709


def func(n):
    a = 100
    b = a**2
    y = n // (b)
    m = (n % (b)) // 100
    d = (n % (b)) % 100
    print(f"{y}년 {m}월 {d}일")


func(n)


def func1(n):
    a = str(n)
    y = a[:4]
    m = a[4:6]
    d = a[6:]
    print(f"{int(y)}년 {int(m)}월 {int(d)}일")


func1(n)

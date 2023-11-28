n = int(input())


def func(n):
    for _ in range(1, n+1):
        li1 = []
        li2 = []
        li3 = []

        a, b = map(int, input().split())
        n = a * b

        for i in range(1, a+1):
            if a % i == 0:
                li1.append(i)
        for j in range(1, b+1):
            if b % j == 0:
                li2.append(j)
        for k in li1:
            if k in li2:
                li3.append(k)

        print(n // max(li3))


func(n)


def gcd(x, y):  # x: 6, y: 15
    while (y):
        x, y = y, x % y
        # 1: x: 6, y: 15
        # 2: x: 15, y: 6 % 15 = 6
        # 3: x: 6, y: 15 % 6 = 3
        # 4: x: 3, y: 6 % 3 = 0
    return x


def lcm(x, y):
    lcm = (x*y)//gcd(x, y)
    return lcm


T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(lcm(a, b))

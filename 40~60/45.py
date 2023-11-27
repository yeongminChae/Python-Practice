n = int(input())


def func(n):
    for _ in range(1, n+1):
        li1 = []
        li2 = []

        a, b = map(int, input().split())
        n = a * b

        for i in range(1, n+1):
            if n % i == 0:
                li1.append(i)

        for i in li1:
            if i % a == 0 and i % b == 0:
                li2.append(i)

        print(min(li2))


func(n)

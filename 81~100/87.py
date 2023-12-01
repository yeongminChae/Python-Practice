n = int(input())


def func(n):
    for _ in range(n):
        li1 = []
        m = int(input())

        for _ in range(1, m+1):
            a, b = input().split()
            li1.append((int(a), b))

        li1.sort(key=lambda x: x[0], reverse=True)
        print(li1[0][1])


func(n)

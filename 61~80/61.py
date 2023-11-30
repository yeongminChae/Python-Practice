n = int(input())


def func(n):
    for _ in range(n):
        li1 = []
        li2 = []
        for _ in range(9):
            a, b = map(int, input().split())
            li1.append(a)
            li2.append(b)

        if sum(li1) > sum(li2):
            print("Yonsei")
        elif sum(li1) < sum(li2):
            print("Korea")
        else:
            print("Draw")


func(n)

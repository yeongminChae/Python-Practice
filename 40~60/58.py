n = int(input())


def func(n):
    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q4 = 0
    AXIS = 0

    for _ in range(n):
        a, b = map(int, input().split())

        if a > 0 and b > 0:
            Q1 += 1
        elif a > 0 and b < 0:
            Q4 += 1
        elif a < 0 and b < 0:
            Q3 += 1
        elif a == 0 or b == 0:
            AXIS += 1
        else:
            Q2 += 1

    print(f"Q1: {Q1}")
    print(f"Q2: {Q2}")
    print(f"Q3: {Q3}")
    print(f"Q4: {Q4}")
    print(f"AXIS: {AXIS}")


func(n)

T = int(input())


def func(T):
    for _ in range(T):
        li = list(input().split())
        n = float(li[0])

        for i in li[1:]:
            if i == "@":
                n *= 3
            elif i == "%":
                n += 5
            elif i == "#":
                n -= 7

        print(f"{n:.2f}")


func(T)

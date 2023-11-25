n, m = map(int, input().split())


def func(n, m):
    if m >= 60 or m <= 0:
        return print("잘못된 입력입니다.")

    if m >= 30:
        return print(f"{n}시 {m - 30}분")
    else:
        if n - 1 < 0:
            return print(f"23시 {60 + (m - 30)}분")
        else:
            return print(f"{n - 1}시 {60 + (m - 30)}분")


func(n, m)

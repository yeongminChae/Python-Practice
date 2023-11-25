h, m = map(int, input().split())
n = int(input())


def func(h, m, n):
    if m >= 60 or m < 0:
        return "잘못된 입력입니다."

    a = n // 60
    b = n % 60
    c = h + a
    d = m + b

    if d < 60:
        return f"{c % 24}시 {d}분"
    else:
        return f"{(c + 1) % 24}시 {d - 60}분"


print(func(h, m, n))


def add_minutes(h, m, n):
    total_minutes = h * 60 + m + n  # 현재 시간을 분 단위로 바꾸고 n을 더함
    new_h = total_minutes // 60 % 24  # 총 분을 60으로 나누어 시간을 구하고, 24로 나눈 나머지를 새로운 시간으로 사용
    new_m = total_minutes % 60  # 총 분을 60으로 나눈 나머지를 새로운 분으로 사용
    return f"{new_h}시 {new_m}분"


print(add_minutes(h, m, n))

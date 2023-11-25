n = int(input())


def func(n):
    hour = n // 3600
    mins = (n % 3600) // 60
    sec = (n % 3600) % 60
    print(f"{hour}시간 {mins}분 {sec}초")


func(n)

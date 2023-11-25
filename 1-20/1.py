hour, mins, sec = map(int, input().split())


def func(hour, mins, sec) -> int:
    return hour*3600 + mins*60 + sec


print(func(hour, mins, sec))

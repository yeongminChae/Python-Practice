a = list(map(int, input().split(":")))
b = list(map(int, input().split(":")))


def func(a, b):
    n = a[0]*3600 + a[1]*60 + a[2]
    m = b[0]*3600 + b[1]*60 + b[2]

    c = 3600*24 + m - n if m < n else m - n
    d = c // 3600
    e = (c % 3600) // 60
    f = (c % 3600) % 60

    if e < 10:
        e = f"0{e}"
    if d < 10:
        d = f"0{d}"
    if f < 10:
        f = f"0{f}"

    return f"{d}:{e}:{f}"


print(func(a, b))

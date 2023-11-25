n = int(input())


def func(n) -> str:
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return ("윤년")
    else:
        return ("평년")


print(func(n))

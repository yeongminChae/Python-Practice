def solution(price, money, count):
    a = sum(i * price for i in range(1, count + 1))

    return 0 if money - a > 0 else a - money
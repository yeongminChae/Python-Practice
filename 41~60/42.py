n = int(input())


def func(n):
    li = []
    a = 2

    while n > 1:

        if n == 1:
            break
        else:
            if n % a != 0:
                a += 1

            else:
                li.append(str(a))
                n = n // a

    return li


print("\n".join(func(n)))


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


for factor in prime_factors(n):
    print(factor)

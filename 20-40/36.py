n = int(input())


def count(n):
    m = 0
    o = str(int(n) % 10) + str((int(n) // 10 + int(n) % 10) % 10)
    while o != str(n):
        o = str(int(o) % 10) + str((int(o) // 10 + int(o) % 10) % 10)
        m += 1

    return m + 1


def func(n):
    if len(str(n)) == 2:
        m = count(n)

    elif len(str(n)) == 1:
        n = "0" + str(n)
        m = count(n)

    return m


print(func(n))


def cycle_length(n):
    original_n = n
    cycle_count = 0

    while True:
        cycle_count += 1
        tens = n // 10
        ones = n % 10
        sum_of_digits = tens + ones
        n = (ones * 10) + (sum_of_digits % 10)

        if n == original_n:
            break

    return cycle_count


n = int(input())
print(cycle_length(n))

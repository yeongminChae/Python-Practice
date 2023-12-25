def d(n):
    return n + sum(map(int, str(n)))


self_numbers = set(range(1, 10001)) - {d(n) for n in range(1, 10001)}

for num in sorted(self_numbers):
    print(num)

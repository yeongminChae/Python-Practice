li = []


def func2(x):
    if x % 2 != 0:
        return True


for _ in range(7):
    n = int(input())
    li.append(n)

li2 = list(filter(func2, li))

if len(li2) == 0:
    print(-1)
else:
    print(sum(li2))
    print(min(li2))

# print(-1 if len(odd_numbers) == 0 else f"{sum(odd_numbers)}\n{min(odd_numbers)}")

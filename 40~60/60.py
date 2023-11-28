n = int(input())


def func(n):
    a = 0
    li1 = []
    li2 = []
    li3 = []

    while a != n:
        if a == n:
            break
        m = int(input())
        a += 1
        for _ in range(m):
            b, c = input().split()
            li1.append(int(c))
            li2.append(b)

        d = max(li1)
        li3.append(li2[li1.index(d)])

    return li3


print("\n".join(func(n)))

n = int(input())


def func():
    m = int(input())
    max_alcohol = 0
    max_school = ''

    for _ in range(m):
        school, alcohol = input().split()
        alcohol = int(alcohol)
        if alcohol > max_alcohol:
            max_alcohol = alcohol
            max_school = school

    return max_school


for _ in range(n):
    print(func())

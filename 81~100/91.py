def func():
    li = []
    c = 0
    for _ in range(4):
        a, b = map(int, input().split())

        c -= a
        li.append(c)
        c += b
        li.append(c)

    return max(li)


print(func())


def func():
    max_people = 0
    current_people = 0
    for _ in range(4):
        off, on = map(int, input().split())
        current_people = current_people - off + on
        max_people = max(max_people, current_people)
    return max_people


print(func())

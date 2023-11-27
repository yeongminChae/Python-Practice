def func():
    li = []
    for _ in range(1, 6):
        n = int(input())
        if n < 40:
            n = 40
        li.append(n)

    avg = sum(li) // len(li)

    return avg


print(func())

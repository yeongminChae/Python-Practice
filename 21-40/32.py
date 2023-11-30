a = input()


def func(a):
    b = a.upper()
    li = []
    li2 = []
    c = 0

    for i in set(b):
        li.append(b.count(i))
        li2.append(i)

    if li.count(max(li)) >= 2:
        return '?'
    else:
        c = max(li)
        d = li.index(c)
        return li2[d].upper()


print(func(a))

def func():
    li1 = []
    li2 = []
    a = ""
    b = ""

    for _ in range(3):
        a, b = map(int, input().split())
        li1.append(a)
        li2.append(b)

    for i in li1:
        if li1.count(i) == 1:
            a = str(i)

    for j in li2:
        if li2.count(j) == 1:
            b = str(j)

    return a, b


print(" ".join(func()))


def func2():
    x = y = 0
    for _ in range(3):
        a, b = map(int, input().split())
        # xor 연산은 동일한 값이 두 번 등장하면 그 결과가 0이 되는 특성을 이용하여 문제를 해결할 수 있습니다.
        x ^= a
        y ^= b
    return x, y


print(func2())

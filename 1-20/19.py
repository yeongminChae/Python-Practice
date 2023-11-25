S = str(input())


def func(S):
    li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    li2 = []

    for i in li:
        li2.append(str(S.find(i)))

    return li2


print(" ".join(func(S)))


def func2(S):
    for i in range(97, 123):  # 'a'부터 'z'까지의 아스키 코드
        print(S.find(chr(i)), end=' ')

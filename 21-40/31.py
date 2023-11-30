a = input()


def func(a):
    li = []
    for i in a:
        li.append(i)

    if (li == list(reversed(li))):
        return 1
    else:
        return 0


print(func(a))


def is_palindrome(a):
    # 리스트로 변환하는 과정 없이 바로 문자열을 뒤집어 비교
    if a == a[::-1]:    # [::-1]을 이용하면 문자열을 뒤집을 수 있습니다.
        return 1
    else:
        return 0


print(is_palindrome(a))

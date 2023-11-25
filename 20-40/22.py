a = str(input())


def func(a):
    b = 0
    for i in a:
        if i == ' ':
            b += 1
    return b + 1


print(func(a))


def count_words(a):
    words = a.split()   # 공백을 기준으로 문자열을 분리하여 리스트를 생성합니다.
    return len(words)   # 리스트의 길이를 반환합니다.


print(count_words(a))

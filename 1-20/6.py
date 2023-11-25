n, m = map(int, input().split())


def func(n, m) -> int:
    li = []
    li2 = []

    for i in str(n):
        li.append(i)

    for j in str(m):
        li2.append(j)

    if (len(li) > 3 or len(li2) > 3):
        print("세자리수를 입력해주세요")
        return

    a = "".join(list(reversed(li)))
    b = "".join(list(reversed(li2)))

    li3 = [int(a), int(b)]

    return max(li3)


c = func(n, m)
print(c)

n, m = map(int, input().split())


def reverse_and_compare(n, m):
    n = int(str(n)[::-1])  # 숫자를 문자열로 변환한 후 뒤집고, 다시 숫자로 변환
    m = int(str(m)[::-1])  # 숫자를 문자열로 변환한 후 뒤집고, 다시 숫자로 변환
    return max(n, m)  # 둘 중 큰 값을 반환


print(reverse_and_compare(n, m))

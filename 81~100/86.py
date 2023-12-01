import datetime

n = int(input())


def func(n):
    li1 = []
    li2 = []
    li3 = []
    for _ in range(n):
        a = input().split()
        li1.append(a[0])
        li2.append(a[1:])

    for i in li2:
        dt1 = datetime.datetime(int(i[2]), int(i[1]), int(i[0]))
        dt2 = datetime.datetime.now()
        li3.append(dt1 - dt2)

    b = li3.index(max(li3))
    c = li3.index(min(li3))

    print(li1[b])
    print(li1[c])


func(n)


n = int(input())


def func(n):
    students = []
    for _ in range(n):
        a = input().split()
        # 이름과 생년월일을 튜플로 저장
        students.append((a[0], datetime.datetime(
            int(a[3]), int(a[2]), int(a[1]))))

    # 생년월일 순으로 정렬
    students.sort(key=lambda x: x[1])

    # 가장 나이가 많은 사람 (즉, 생년월일이 가장 빠른 사람)의 이름 출력
    print(students[0][0])
    # 가장 나이가 적은 사람 (즉, 생년월일이 가장 늦은 사람)의 이름 출력
    print(students[-1][0])


func(n)

a = str(input())


def func(a):
    for i in range(48, 123):
        if chr(i) == a:
            print(i)


func(a)

T = int(input())


def func(T):
    a = 300
    b = 60
    c = 10

    n = T // a
    m = T % a
    k = m // b
    l = m % b // c
    o = m % b % c

    if o != 0:
        print(-1)
    else:
        print(n, k, l)


func(T)

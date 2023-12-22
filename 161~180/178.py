import sys


def func():
    n, m, b = map(int, sys.stdin.readline().strip().split())
    li = []

    for _ in range(n):
        li.append([int(i) for i in sys.stdin.readline().strip().split()])

    ans = int(1e9)
    glevel = 0

    for i in range(257):
        useBlock = 0
        takeBlock = 0

        for x in range(n):
            for y in range(m):
                if li[x][y] > i:
                    useBlock += li[x][y] - i
                else:
                    takeBlock += i - li[x][y]

        if useBlock > takeBlock + b:
            continue

        count = useBlock + takeBlock * 2

        if ans >= count:
            ans = count
            glevel = i

    print(ans, glevel)


func()

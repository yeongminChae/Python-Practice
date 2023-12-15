import sys


def count(li, x, y):
    count = [0, 0]

    for i in range(x, x + 8):

        for j in range(y, y + 8):
            if (i + j) % 2 == 0:
                if li[i][j] != 'B':
                    count[0] += 1
                if li[i][j] != 'W':
                    count[1] += 1
            else:
                if li[i][j] != 'W':
                    count[0] += 1
                if li[i][j] != 'B':
                    count[1] += 1
    return min(count)


def func():
    n, m = map(int, sys.stdin.readline().split())
    li = [list(sys.stdin.readline()) for _ in range(n)]

    min_repaint = float('inf')
    for i in range(n - 7):
        for j in range(m - 7):
            min_repaint = min(min_repaint, count(li, i, j))

    print(min_repaint)


func()

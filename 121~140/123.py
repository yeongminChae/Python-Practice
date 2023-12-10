import sys
n = int(sys.stdin.readline())


def func(n):

    for i in range(n):
        li = list(map(int, sys.stdin.readline().split()))
        li2 = sorted(li[1:])

        a = max(li2)
        b = min(li2)
        c = 0
        d = 0

        while c + 1 < len(li2):
            if d < li2[c + 1] - li2[c]:
                d = li2[c + 1] - li2[c]
                c += 1
            else:
                c += 1

        print(f"Class {i+1}")
        print(f"Max {a}, Min {b}, Largest gap {d}")


func(n)

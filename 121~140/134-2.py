import sys
n = int(sys.stdin.readline())


def func(n):
    for _ in range(n):
        li = []
        a, b = sys.stdin.readline().split()

        for i in zip(a, b):
            c = ord(i[0])
            d = ord(i[1])
            e = d - c
            if c > d:
                li.append(26 + e)
            else:
                li.append(e)

        print(f"Distances: {' '.join(list(map(str, li)))}")


func(n)

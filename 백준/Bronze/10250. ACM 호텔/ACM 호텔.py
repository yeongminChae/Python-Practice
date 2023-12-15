import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    floor = N % H if N % H != 0 else H
    room = (N-1) // H + 1
    print(floor * 100 + room)

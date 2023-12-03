from enum import Enum


class Play(Enum):
    도 = 1
    개 = 2
    걸 = 3
    윷 = 4
    모 = 0


def func(n):
    play = {
        Play.도: "A",
        Play.개: "B",
        Play.걸: "C",
        Play.윷: "D",
        Play.모: "E",
    }
    return play.get(n, "잘못된 입력입니다.")


def main():
    for _ in range(3):
        li = list(map(int, input().split()))
        a = li.count(0)

        print(func(Play(a)))


main()

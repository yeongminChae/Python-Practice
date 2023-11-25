from enum import Enum

n = int(input())


class Month(Enum):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12


def func(n):
    month = {
        Month.DEC: "겨울",
        Month.JAN: "겨울",
        Month.FEB: "겨울",
        Month.MAR: "봄",
        Month.APR: "봄",
        Month.MAY: "봄",
        Month.JUN: "여름",
        Month.JUL: "여름",
        Month.AUG: "여름",
        Month.SEP: "가을",
        Month.OCT: "가을",
        Month.NOV: "가을",
    }
    return month.get(n, "잘못된 입력입니다.")


a = func(Month(n))
print(f"{n}월은 {a}입니다.")

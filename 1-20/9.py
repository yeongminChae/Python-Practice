from enum import Enum

n = int(input())


class Week(Enum):
    MON = 6
    TUE = 0
    WED = 1
    THU = 2
    FRI = 3
    SAT = 4
    SUN = 5


def func(n):
    week = {
        Week.MON: "월요일",
        Week.TUE: "화요일",
        Week.WED: "수요일",
        Week.THU: "목요일",
        Week.FRI: "금요일",
        Week.SAT: "토요일",
        Week.SUN: "일요일",
    }
    return week.get(n, "잘못된 입력입니다.")


m = n % 7
a = func(Week(m))
print(f"{n}일후는 {a}입니다.")

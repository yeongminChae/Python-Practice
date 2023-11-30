from enum import Enum

a = input()


class Grade(Enum):
    APLUS = "A+"
    A = "A0"
    AMINUS = "A-"
    BPLUS = "B+"
    B = "B0"
    BMINUS = "B-"
    CPLUS = "C+"
    C = "C0"
    CMINUS = "C-"
    DPLUS = "D+"
    D = "D0"
    DMINUS = "D-"
    F = "F"


def func(a):
    grade = {
        Grade.APLUS: 4.3,
        Grade.A: 4.0,
        Grade.AMINUS: 3.7,
        Grade.BPLUS: 3.3,
        Grade.B: 3.0,
        Grade.BMINUS: 2.7,
        Grade.CPLUS: 2.3,
        Grade.C: 2.0,
        Grade.CMINUS: 1.7,
        Grade.DPLUS: 1.3,
        Grade.D: 1.0,
        Grade.DMINUS: 0.7,
        Grade.F: 0.0,
    }
    return grade.get(a, "잘못된 입력입니다.")


print(func(Grade(a)))

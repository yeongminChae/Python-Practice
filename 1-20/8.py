from enum import Enum

n = int(input())


class Cleaner(Enum):
    A = 1
    B = 2
    C = 3
    D = 0


def func(n):
    cleaner = {
        Cleaner.A: "A",
        Cleaner.B: "B",
        Cleaner.C: "C",
        Cleaner.D: "D",
    }
    return cleaner.get(n, "잘못된 입력입니다.")


m = n % 4

a = func(Cleaner(m))
print(f"{n}일째 당번은 {a}입니다.")

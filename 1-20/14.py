from enum import Enum

n = int(input())


class Cleaner(Enum):
    DAY1 = 1
    DAY2 = 2
    DAY3 = 3
    DAY4 = 4
    DAY5 = 5
    DAY6 = 6
    DAY7 = 7
    DAY8 = 8
    DAY9 = 9
    DAY10 = 10
    DAY11 = 11
    DAY12 = 0


def func(n):
    cleaner = {
        Cleaner.DAY1: "A",
        Cleaner.DAY2: "A",
        Cleaner.DAY3: "A",
        Cleaner.DAY4: "B",
        Cleaner.DAY5: "B",
        Cleaner.DAY6: "B",
        Cleaner.DAY7: "C",
        Cleaner.DAY8: "C",
        Cleaner.DAY9: "C",
        Cleaner.DAY10: "D",
        Cleaner.DAY11: "D",
        Cleaner.DAY12: "D",
    }
    return cleaner.get(n, "잘못된 입력입니다.")


m = n % 12
a = func(Cleaner(m))

print(f"{n}일째 당번은 {a}입니다.")

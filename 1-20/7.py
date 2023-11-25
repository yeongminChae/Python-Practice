from enum import Enum

n = int(input())


class Animal(Enum):
    자 = 4
    축 = 5
    인 = 6
    묘 = 7
    진 = 8
    사 = 9
    오 = 10
    미 = 11
    신 = 12
    유 = 1
    술 = 2
    해 = 3


def func(n):
    animal = {
        Animal.자: "쥐띠",
        Animal.축: "소띠",
        Animal.인: "호랑이띠",
        Animal.묘: "토끼띠",
        Animal.진: "용띠",
        Animal.사: "뱀띠",
        Animal.오: "말띠",
        Animal.미: "양띠",
        Animal.신: "원숭이띠",
        Animal.유: "닭띠",
        Animal.술: "개띠",
        Animal.해: "돼지띠",
    }
    return animal.get(n, "잘못된 입력입니다.")


m = n // (100**2)
a = m % 12
b = func(Animal(a))
print(f"{m}년은 {b}의 해입니다.")

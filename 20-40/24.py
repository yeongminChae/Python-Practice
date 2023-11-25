a = input()


def func(a):
    b = 0
    dial = {
        "A": 2,
        "B": 2,
        "C": 2,
        "D": 3,
        "E": 3,
        "F": 3,
        "G": 4,
        "H": 4,
        "I": 4,
        "J": 5,
        "K": 5,
        "L": 5,
        "M": 6,
        "N": 6,
        "O": 6,
        "P": 7,
        "Q": 7,
        "R": 7,
        "S": 7,
        "T": 8,
        "U": 8,
        "V": 8,
        "W": 9,
        "X": 9,
        "Y": 9,
        "Z": 9,
    }
    for i in a:
        if i in dial:
            b += dial.get(i) + 1

    return b


print(func(a))


def dial_time(word):
    dial = {
        "ABC": 2,
        "DEF": 3,
        "GHI": 4,
        "JKL": 5,
        "MNO": 6,
        "PQRS": 7,
        "TUV": 8,
        "WXYZ": 9,
    }

    time = 0
    for char in word:
        for key in dial.keys():
            if char in key:
                time += dial[key] + 1
                break

    return time


word = input()
print(dial_time(word))


def inputFunc():
    grade = {
        "A+": 4.5,
        "A0": 4.0,
        "B+": 3.5,
        "B0": 3.0,
        "C+": 2.5,
        "C0": 2.0,
        "D+": 1.5,
        "D0": 1.0,
        "F": 0.0,
        "P": 0.0
    }

    n = 0
    m = 0

    for _ in range(1, 21):
        a, b, c = map(str, input().split())

        if c != ("P"):
            n += (float(b) * float(grade.get(c)))
            m += float(b)

    return n % m


print(inputFunc())

li = ["c=",
      "c-",
      "dz=",
      "d-",
      "lj",
      "nj",
      "s=",
      "z=",]

a = input()


def func(a):
    b = 0
    for i in li:
        if a.count(i) >= 1:
            b += a.count(i)
            a = a.replace(i, "*")

    for j in a:
        if j != "*":
            b += 1

    return b


print(func(a))

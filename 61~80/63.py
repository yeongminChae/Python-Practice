def func():
    while True:
        n = int(input())
        li = []

        if n == -1:
            break

        for i in range(1, n):
            if n % i == 0:
                li.append(i)

        if sum(li) == n:
            c = []
            for i in li:
                c.append(str(i))

            d = " + ".join(c)
            print(f"{n} = {d} ")
        else:
            print(f"{n} is NOT perfect.")


func()

import sys

def func1() :
    s = int(sys.stdin.readline())
    a, b = ' ', '*'
    li = []
    for i in range(int(s // 2) + 1) :
        m = a * (int(s // 2) - (i)) + b * i
        li.append(m + '*' + m[::-1])
    return li

temp = func1()
new_li = temp + temp[::-1][1:]
for i in new_li : print(i)

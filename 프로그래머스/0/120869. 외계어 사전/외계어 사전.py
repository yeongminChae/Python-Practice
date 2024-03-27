def solution(spell, dic):
    a = ('').join(sorted(spell))
    print(a)
    
    for i in dic :
        b = ('').join(sorted(i))
        if b == a :
            return 1

    return 2
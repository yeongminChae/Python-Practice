def solution(myString, pat):
    a = ('').join([i.replace('A','-') for i in myString])
    b = ('').join([i.replace('B','A') for i in a])
    c = ('').join([i.replace('-','B') for i in b])
    return 1 if pat in c else 0
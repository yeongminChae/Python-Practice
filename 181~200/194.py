import sys
from collections import deque   

logs = deque(sys.stdin.readline().strip().split(','))

def func(logs: list[str]) -> list[str]:
    digits = []
    letters = []
        
    for i in logs :
        if i.split()[1].isdigit() :
            digits.append(i)
        else :
            letters.append(i)    
    
    letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
            
    return letters + digits
            
        

print(func(logs))


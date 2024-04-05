import re

def solution(myString, pat):
    a = 0
    for i, j in enumerate(myString) :
        if j in pat : a = i
    return myString[ : a + 1]
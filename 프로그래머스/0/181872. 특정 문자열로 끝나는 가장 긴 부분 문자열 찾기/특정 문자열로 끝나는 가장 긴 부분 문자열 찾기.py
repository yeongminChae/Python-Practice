import re

def solution(myString, pat):
    if len(pat) > 1 : a = myString.rindex(pat) + (len(pat) - 1)
    else : a = myString.rindex(pat)
    return myString[ : a + 1]
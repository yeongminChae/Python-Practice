import re
from collections import Counter

def solution(str1, str2):
    Counter1, Counter2 = converter(str1), converter(str2)
    intersection = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0: return 65536
    return int((len(intersection) / len(union)) * 65536)

def converter(text) :
    str1 = text.lower()
    li1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    return Counter(li1)


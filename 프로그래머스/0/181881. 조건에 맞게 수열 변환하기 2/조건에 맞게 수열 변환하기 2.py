from copy import deepcopy

def solution(arr):
    answer = 0
    while True :
        temp = deepcopy(arr)
        arr = func1(arr)
        if temp == arr : return answer
        answer += 1

def func1(arr) :
    for j, i in enumerate(arr) :
        if i % 2 == 0 and i >= 50 : arr[j] //= 2
        elif i % 2 != 0 and i < 50 : arr[j] = (i * 2) + 1
    return arr

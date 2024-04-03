def solution(arr, flag):
    answer = []
    for i, j in enumerate(flag) :
        func1(arr[i], answer) if int(j) == 1 else func2(arr[i], answer)
    return answer

def func1(i, arr) :
    arr.extend([i] * (i *2))
    return arr

def func2(i, arr) :
    [arr.pop() for _ in range(0, i)] if arr else arr
    return arr
def solution(n):
    temp = [0, 1]
    for i in range(1, n ) :
        temp.append(temp[i] + temp[i - 1])

    return temp[-1] % 1234567
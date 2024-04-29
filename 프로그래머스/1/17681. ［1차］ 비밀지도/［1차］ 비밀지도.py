def solution(n, arr1, arr2):
    answer = []

    for i in range(n) :
        a = binary_maker(bin(arr1[i])[2:], n)
        b = binary_maker(bin(arr2[i])[2:], n)
        
        temp = ''
        for j in range(n) :
            if a[j] == '0' and b[j] == '0' :
                temp += ' '
            else : temp += '#'
        answer.append(temp)
    return answer

def binary_maker(str1, n) :
    if len(str1) < n : str1 = '0' * (n - len(str1)) + str1
    return str1


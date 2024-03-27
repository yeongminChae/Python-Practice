def solution(bin1, bin2):
    answer = ''
    carry = 0
    max_num = max(len(bin1),len(bin2))
    a = list(bin1.zfill(max_num)[::-1])
    b = list(bin2.zfill(max_num)[::-1])

    
    for i in range(0, max_num) :
        if int(a[i]) + int(b[i]) + carry == 0 :
            answer += '0'
            carry = 0
        elif int(a[i]) + int(b[i]) + carry == 1 :
            answer += '1'
            carry = 0
        elif int(a[i]) + int(b[i]) + carry == 2 :
            answer += '0'
            carry = 1
        elif int(a[i]) + int(b[i]) + carry > 2 :
            answer += '1' 
    
    if carry == 1 :
        return (answer + str(carry))[::-1]
    
    return answer[::-1]

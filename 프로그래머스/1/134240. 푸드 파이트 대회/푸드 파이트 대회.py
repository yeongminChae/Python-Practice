def solution(food):
    li = [(i - 1) // 2 if i % 2 != 0 else i // 2 for i in food[1:]]
    ans = ''
    
    for i, j in enumerate(li) :
        ans += str(i + 1) * j
    
    return ans + '0' + ans[::-1]
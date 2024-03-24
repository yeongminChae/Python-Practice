def solution(my_string, num1, num2):
    new_li = list(map(str, my_string))
    new_li[num1], new_li[num2] = new_li[num2], new_li[num1]
    return ''.join(new_li)
def solution(str_list):
    n = ('').join(str_list).find('l')
    m = ('').join(str_list).find('r')

    if n == -1 and m == -1 : return []
    elif n != -1 and (n < m or m == -1) : return str_list[ : n] 
    elif m != -1 and (n > m or n == -1) : return str_list[m + 1 : ] 
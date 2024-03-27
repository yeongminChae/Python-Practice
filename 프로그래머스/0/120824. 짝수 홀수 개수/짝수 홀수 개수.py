def solution(num_list):
    even_arr = list(filter(lambda x: x % 2 == 0, num_list))
    answer = [len(even_arr), len(num_list) - len(even_arr)]
    return answer
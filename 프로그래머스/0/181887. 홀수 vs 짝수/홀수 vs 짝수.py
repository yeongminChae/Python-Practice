def solution(num_list):
    answer1 = sum([num_list[i] for i in range(1, len(num_list), 2)])
    answer2 = sum([num_list[i] for i in range(0, len(num_list), 2)])
    return answer1 if answer1 > answer2 else answer2
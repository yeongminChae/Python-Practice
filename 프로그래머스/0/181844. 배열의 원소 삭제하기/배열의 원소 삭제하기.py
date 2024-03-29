def solution(arr, delete_list):
    answer = []
    return list(filter(lambda x: x not in delete_list , arr))
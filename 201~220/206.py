def solution(arr):
    min_num, min_index = min(arr), arr.index(min(arr))
    right_arr = arr[min_index + 1:]

    return max(right_arr) - min_num


arr1 = [7, 1, 5, 3, 6, 4]
print(solution(arr1))

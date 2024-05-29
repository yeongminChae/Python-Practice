def solution(n):
    left, right, volume = 0, len(n) - 1, 0
    left_max, right_max = n[left], n[right]

    while left < right:
        left_max = max(left_max, n[left])
        right_max = max(right_max, n[right])

        if left_max < right_max:
            volume += left_max - n[left]
            left += 1
        else:
            volume += right_max - n[right]
            right -= 1

    return volume


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solution(arr))

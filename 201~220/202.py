def solution1(nums, t):
    ans = []
    for i, j in enumerate(nums):
        for k in range(i + 1, len(nums)):
            if j + nums[k] == t:
                ans.append([i, k])
    return ans


# print(solution1([2, 7, 11, 15], 9))

def solution2(nums, t):
    ans, dict1 = [], {}

    for i, j in enumerate(nums):
        temp = t - j
        if temp in dict1:
            ans.append([dict1[temp], i])
        dict1[j] = i

    return ans


# print(solution2([2, 7, 11, 15], 9))

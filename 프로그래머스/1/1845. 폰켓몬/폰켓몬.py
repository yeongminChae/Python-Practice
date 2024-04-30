def solution(nums):
    a = len(nums) // 2
    nums = set(sorted(nums))
    
    if len(nums) > a:
        return a
    elif len(nums) == a or len(nums) < a:
        return len(nums)
    
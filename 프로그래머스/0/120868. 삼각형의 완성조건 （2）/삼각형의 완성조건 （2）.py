def solution(sides):
    b = (sum(sides) - max(sides)) - 1
    return min(sides) + b 

# 3, 6 -> 3
# 11, 7 -> 7
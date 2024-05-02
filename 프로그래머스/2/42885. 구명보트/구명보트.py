def solution(people, limit):
    people = sorted(people)
    first, last, ans = 0, len(people) - 1, 0
    
    while first <= last :
        if people[first] + people[last] <= limit : first += 1
        last -= 1
        ans += 1
            
    return ans
            
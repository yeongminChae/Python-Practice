from collections import deque

def solution(cacheSize, cities):
    answer, dq, cities = 0, deque(), list(map(lambda x: x.lower(), cities))
    
    if cacheSize == 0 : return len(cities) * 5

    for i in cities: 
        if i not in dq and len(dq) < cacheSize: 
            answer = add_city(dq, i, answer, 5)
        elif i not in dq and len(dq) == cacheSize:
            dq.popleft()
            answer = add_city(dq, i, answer, 5) 
        else:
            dq.remove(i)
            answer = add_city(dq, i, answer, 1) 
    return answer

def add_city(dq, city, answer, cost):
    dq.append(city)
    return answer + cost

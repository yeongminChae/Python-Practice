def solution(priorities, location):
    answer, queue = 0, [(i, j) for i, j in enumerate(priorities)]
    while True :
        temp = queue.pop(0)
        if any(temp[1] < i[1] for i in queue) : queue.append(temp)
        else :
            answer += 1
            if location == temp[0] : return answer
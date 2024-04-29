def solution(N, stages):
    my_dict = {}
    stages = sorted(stages)
    a = 0

    for i in range(1, N + 1) :
        if i in stages :
            my_dict[i] = stages.count(i) / len(stages)
            stages = list(filter(lambda x : x > i , stages))
        else :
            my_dict[i] = 0
    
    new_arr = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in new_arr]
    return answer
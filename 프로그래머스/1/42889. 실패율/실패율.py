from collections import Counter

def solution(N, stages):
    my_dict = {}
    stage_counts = Counter(stages)
    stages = sorted(stages)
    players = len(stages)
    a = 0

    for i in range(1, N + 1) :
        if i in stages :
            my_dict[i] = stage_counts[i] / players
            players -= stage_counts[i]
        else :
            my_dict[i] = 0
    
    new_arr = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in new_arr]
    return answer
def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []
    
    for i, j in enumerate(answers) :
        if j == pattern1[i % len(pattern1)] :
            score[0] += 1
        if j == pattern2[i % len(pattern2)] :
            score[1] += 1
        if j == pattern3[i % len(pattern3)] :
            score[2] += 1
    
    for i, j in enumerate(score) :
        if j == max(score) :
            answer.append(i + 1)
            
    return answer
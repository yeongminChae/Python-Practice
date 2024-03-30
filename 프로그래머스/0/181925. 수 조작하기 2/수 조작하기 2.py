def solution(numLog):
    dict1 = {'1': 'w', '-1': 's', '10': 'd', '-10': 'a'}
    ans = []
    for i in range(0, len(numLog) -1) :
        ans.append(numLog[i + 1] - numLog[i])
    
    return ('').join([dict1[str(i)] for i in ans])
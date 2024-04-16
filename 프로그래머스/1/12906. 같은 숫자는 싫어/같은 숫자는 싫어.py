def solution(arr):
    ans = ['a']
    for i in arr :
        if i != ans[-1] : ans.append(i)
    return ans[1:]
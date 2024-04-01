def solution(my_strings, parts):
    answer = [my_strings[i][j[0] : j[1] + 1] for i, j in enumerate(parts)] 
    return ('').join(answer)
def solution(my_string, letter):
    answer = ('').join(list(filter(lambda x: x != letter, my_string)))
    return answer
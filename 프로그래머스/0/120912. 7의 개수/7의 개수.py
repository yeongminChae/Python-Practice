def solution(array):
    array = list(map( lambda x: str(x), array ))
    a = ('').join(array)
        
    return a.count('7')
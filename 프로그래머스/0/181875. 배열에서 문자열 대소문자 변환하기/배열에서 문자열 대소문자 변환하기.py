def solution(strArr):
    return list(map(lambda x : x[1].upper() if x[0] % 2 != 0 else x[1].lower(), enumerate(strArr)))
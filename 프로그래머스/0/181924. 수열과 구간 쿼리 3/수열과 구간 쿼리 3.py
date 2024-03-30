def solution(arr, queries):
    dict1 = {str(i): str(j) for i, j in enumerate(arr)}

    for i in queries :
        a = dict1[str(i[0])] 
        dict1[str(i[0])] = dict1[str(i[1])]
        dict1[str(i[1])] = a
        
    return [int(dict1[j]) for j in dict1]
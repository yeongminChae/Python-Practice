def solution(quiz):
    answer = []
    for i in quiz :
        if i.split()[1] == '+' and int(i.split()[0]) + int(i.split()[2]) == int(i.split()[-1]):
            answer.append('O')
        elif i.split()[1] == '+' and int(i.split()[0]) + int(i.split()[2]) != int(i.split()[-1]):
            answer.append('X')
        elif i.split()[1] == '-' and int(i.split()[0]) - int(i.split()[2]) == int(i.split()[-1]):
            answer.append('O')
        elif i.split()[1] == '-' and int(i.split()[0]) - int(i.split()[2]) != int(i.split()[-1]):
            answer.append('X') 
            
    return answer
def solution(numbers):
    answer = []
    letters = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    
    for i in letters :
        numbers = numbers.replace(i, str(letters[i]))
            
            
    return int(numbers)
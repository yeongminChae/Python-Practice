def solution(hp):
    five = hp // 5
    three = (hp % 5) // 3
    one = (hp % 5) % 3
    
    return five + three + one

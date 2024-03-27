def solution(chicken):
    answer = 0
    coupons = 0
    
    coupons += chicken
    
    while coupons >= 10 :
        service_chicken = coupons // 10
        answer += service_chicken
        
        coupons = coupons % 10 + service_chicken 
        
    return answer
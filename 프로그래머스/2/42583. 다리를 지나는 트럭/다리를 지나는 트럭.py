def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length  # 다리를 0으로 초기화
    current_weight = 0  # 현재 다리 위의 총 무게

    while truck_weights or current_weight:  # 대기 트럭이 있거나 다리 위에 트럭이 있을 때까지 반복
        time += 1
        current_weight -= bridge.pop(0)  # 다리를 건넌 트럭 무게 제거
        
        if truck_weights:  # 대기 트럭이 있는 경우
            if current_weight + truck_weights[0] <= weight:  # 다음 트럭이 다리에 올라갈 수 있는지 확인
                truck = truck_weights.pop(0)  # 대기열에서 트럭을 꺼냄
                bridge.append(truck)  # 다리에 트럭 추가
                current_weight += truck  # 현재 무게에 트럭 무게 추가
            else:
                bridge.append(0)  # 트럭이 다리에 올라갈 수 없는 경우, 0을 추가하여 시간을 맞춤
                
    return time
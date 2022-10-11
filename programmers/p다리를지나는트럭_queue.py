from collections import defaultdict, deque

def solution(bridge_length, weight, truck_weights):
    ans, rest_truck, bridge_sum = 0, len(truck_weights), 0
    bridge = deque([0]*bridge_length)

    while truck_weights or rest_truck:
        ans += 1
        if bridge[0]: rest_truck -= 1
        bridge_sum -= bridge.popleft()
        next_car = 0
        if truck_weights and bridge_sum + truck_weights[0] <= weight: 
            next_car = truck_weights[0]
            del truck_weights[0]
        bridge.append(next_car)
        bridge_sum += next_car

    return ans
# 배달

def solution(cap, n, deliveries, pickups):
    distance = 0
    total_deliveries = sum(deliveries)
    total_pickups = sum(pickups)

    farthest_delivery = n - 1
    farthest_pickup = n - 1

    while total_deliveries or total_pickups:
        truck_deliveries = cap if total_deliveries >= cap else total_deliveries
        truck_pickups = 0

        while deliveries[farthest_delivery] == 0 and farthest_delivery > 0:
            farthest_delivery -= 1
        while pickups[farthest_pickup] == 0 and farthest_pickup > 0:
            farthest_pickup -= 1

        farthest_node = max(farthest_delivery, farthest_pickup)
        distance += (1 + farthest_node) * 2

        total_deliveries -= truck_deliveries
        while truck_deliveries >= 0 and farthest_delivery >= 0:
            if deliveries[farthest_delivery] >= truck_deliveries:
                deliveries[farthest_delivery] -= truck_deliveries
                truck_deliveries = 0
                break
            else:
                truck_deliveries -= deliveries[farthest_delivery]
                deliveries[farthest_delivery] = 0
                farthest_delivery -= 1

        while cap - truck_pickups > 0 and farthest_pickup >= 0:  # 픽업 여유 공간이 있을 때
            if pickups[farthest_pickup] >= cap - truck_pickups:
                pickups[farthest_pickup] -= cap - truck_pickups
                truck_pickups = cap
                break
            else:
                truck_pickups += pickups[farthest_pickup]
                pickups[farthest_pickup] = 0  # 다 픽업함
                farthest_pickup -= 1
        total_pickups -= truck_pickups

    return distance

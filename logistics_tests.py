def can_allocate(item_weights, max_capacity, num_vehicles):
    sorted_weights = sorted(item_weights, reverse=True)
    vehicles = [0] * num_vehicles

    for weight in sorted_weights:
        if weight > max_capacity:
            return False
        
        min_remaining = float('inf')
        best_idx = -1
        for i in range(num_vehicles):
            remaining = max_capacity - vehicles[i]
            if remaining >= weight and remaining < min_remaining:
                min_remaining = remaining
                best_idx = i
        
        if best_idx == -1:
            return False
        
        vehicles[best_idx] += weight

    return True

def find_min_max_capacity():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    num_items = int(data[idx])
    idx += 1
    num_vehicles = int(data[idx])
    idx += 1
    weights = list(map(int, data[idx:idx + num_items]))

    lower_bound = max(weights)
    upper_bound = sum(weights)
    best_result = upper_bound

    while lower_bound <= upper_bound:
        mid_value = (lower_bound + upper_bound) // 2
        if can_allocate(weights, mid_value, num_vehicles):
            best_result = mid_value
            upper_bound = mid_value - 1
        else:
            lower_bound = mid_value + 1

    print(best_result)

if __name__ == "__main__":
    find_min_max_capacity()
def find_closest(arr, x):
    left, right = 0, len(arr) - 1
    closest_index = 0
    min_diff = float('inf')

    while left <= right:
        mid = (left + right) // 2
        current_diff = abs(arr[mid] - x)

        if current_diff < min_diff:
            min_diff = current_diff
            closest_index = mid
        elif current_diff == min_diff:
            if mid < closest_index:
                closest_index = mid

        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid  

    return closest_index

n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(find_closest(arr, x))
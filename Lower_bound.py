def lower_bound(arr, x):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(lower_bound(arr, x))
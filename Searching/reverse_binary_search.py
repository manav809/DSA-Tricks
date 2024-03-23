def reverse_order(arr, target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r)/2
        if arr[mid] > target: 
            l = mid + 1
        elif arr[mid] < target:
            r = mid - 1
        else:
            return mid
    return -1
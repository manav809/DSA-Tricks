def search(arr, target):
    # NOTE:Cannot use len()
    s = 0
    e = 1
    found = False
    while not found:
        if arr[e] < target:
            ran = (e - s  + 1) * 2
            s = e + 1
            e = e + ran + 1  
        else:
            found = True
    return binary_search(arr, s, e, target)
    
def binary_search(arr, s, r, target):
    while s <= r:
        mid = (s + r)//2
        if arr[mid] < target:
            s = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1


print(search([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170], 140))
    
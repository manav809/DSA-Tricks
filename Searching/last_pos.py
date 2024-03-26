def last_pos(arr, target):
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r)//2
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            #potential answer
            ans = mid
            l = mid + 1
    return ans

print(last_pos([1,2,7,7,7,7], 7))
print(last_pos([1,1,1,7,7,7], 1))
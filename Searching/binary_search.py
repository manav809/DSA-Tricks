def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r: 
        mid = l + ((r - l)//2)
        if nums[mid] < target: 
            l = mid
        elif nums[mid] > target: 
            r = mid
        else: 
            return mid
    return -1
            

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    l = 0
    r = l + 1
    while r < len(nums):
        if nums[l] == 0 and nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
            continue
        elif nums[l] == 0 and nums[r] == 0:
            r += 1
            continue
        l += 1
        r += 1
    return nums
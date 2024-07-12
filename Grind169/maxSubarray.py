def maxSubArray(nums):
    maximum = [nums[0]]

    for windowEnd in range(1, len(nums)):
        if maximum[-1] + nums[windowEnd] > nums[windowEnd]:
            maximum.append(maximum[-1] + nums[windowEnd])
        else:
            maximum.append(nums[windowEnd])
        
    return max(maximum)
            
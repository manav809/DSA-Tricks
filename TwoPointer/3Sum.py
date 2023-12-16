def threeSum(nums): 
    nums = sorted(nums)
    result = []
    for i in range(len(nums) - 2): 
        l = i + 1
        r = len(nums) - 1

        while l < r: 
            if nums[i] + nums[l] + nums[r] == 0: 
                if [nums[i], nums[l], nums[r]] not in result: 
                    result.append([nums[i], nums[l], nums[r]])
            elif nums[i] + nums[l] + nums[r] < 0:
                l += 1
                continue
            elif nums[i] + nums[l] + nums[r] > 0: 
                r -= 1
                continue
            l += 1
            r -= 1
    return result
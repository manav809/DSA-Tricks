def sortedSquares(nums):
    l = 0
    r = len(nums) - 1
    result = [0 for i in nums]
    idx = len(nums) - 1
    while l < r:
        squared_l = nums[l] ** 2
        squared_r = nums[r] ** 2

        if squared_l > squared_r: 
            result[idx] = squared_l
            l += 1
            idx -= 1
        elif squared_l < squared_r:
            result[idx] = squared_r
            r -= 1
            idx -= 1
        else:
            result[idx] = squared_l
            idx -= 1
            result[idx] = squared_r
            idx -= 1
            l += 1
            r -= 1
    if l == r:
        result[idx] = nums[l] ** 2
    return result
            




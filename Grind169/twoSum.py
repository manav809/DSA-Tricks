def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_map = {}
    for i in range(len(nums)):
        remainder = target - nums[i]
        if remainder not in hash_map:
            hash_map[nums[i]] = i
        else:
            return [hash_map[remainder], i]
    return [0, 0]
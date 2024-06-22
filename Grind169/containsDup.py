def containsDuplicate(nums):
    dupSet = set()
    for i in range(len(nums)):
        if nums[i] not in dupSet:
            dupSet.add(nums[i])
        else:
            return True
    return False
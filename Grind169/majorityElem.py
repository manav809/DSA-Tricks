def majorityElement(nums):
    count = 0
    element = 0
    for i in range(len(nums)):
        if count == 0:
            element = nums[i]
            count += 1
        elif element != nums[i]:
            count -= 1
        else:
            count += 1
    return element
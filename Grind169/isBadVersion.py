def isBadVersion(num):
    pass

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    l = 1
    r = n
    lowest = None
    while l <= r:
        mid = (l + r) // 2
        if isBadVersion(mid):
            lowest = mid
            r = mid - 1
        else:
            l = mid + 1
    return lowest